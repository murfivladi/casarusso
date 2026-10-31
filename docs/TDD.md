# TDD — Technical Design Document

Riferimenti: `FASI_DI_SVILUPPO.md` §16–§18, decisioni D-59…D-71, D-85, D-86. Versioni verificate il 31/10/2026 sui registri npm/PyPI; in Fase 1 si fissano con la regola di D-59 (ultima patch pubblicata da almeno 14 giorni).

| Componente | Versione oggi | Uso |
|---|---|---|
| Babylon.js (`@babylonjs/core`, `loaders`, `materials`, `addons`) | 9.33.1 | motore |
| `@babylonjs/havok` | 1.3.14 | fisica |
| `@recast-navigation/core` + `generators` (via Navigation Plugin V2 in `@babylonjs/addons`) | 0.44.0 | navmesh e crowd |
| inkjs | 2.4.0 | dialoghi |
| Vite | 8.3.5 | build |
| TypeScript | 7.0.2 | linguaggio |
| Playwright (`@playwright/test`) | 1.64.1 | test |
| glTF-Transform CLI | 4.5.1 | ottimizzazione glTF, meshopt, KTX2 |
| meshoptimizer | 1.3.0 | compressione geometria |
| KTX-Software (`toktx`) | 4.3.x (versione inclusa da glTF-Transform) | KTX2/Basis |
| Blender (headless) / `bpy` | 5.2 LTS / 5.2.3 | pipeline 3D (D-63) |

---

## 1. Architettura del repository

```
casarusso/
├── docs/                     documentazione (questa cartella)
├── work/                     testo del libro, indice, strumenti di verifica della Fase 0
├── game/
│   ├── index.html
│   ├── src/
│   │   ├── core/             bootstrap.ts, engine.ts, scene-manager.ts, streaming/, save/, time/, events.ts, debug/
│   │   ├── render/           pipeline.ts (frame graph), presets.ts, lightmaps.ts, sky.ts, weather.ts, vfx/ (nebbia, pelo, decal)
│   │   ├── systems/          controller/, interaction/, dialogue/, thoughts/, subtitles/, notebook/, phone/,
│   │   │                     missions/, softfail/, calendar/, house/, npc/, relations/, collections/, bar/,
│   │   │                     investigation/ (cap.4), tension/ (cap.8), footprints/ (cap.10), cleaning/ (cap.12), cannistri/ (cap.13)
│   │   ├── audio/            synth/ (worklet e generatori SYN-*), mixer.ts, spatial.ts, vox.ts
│   │   ├── chapters/         cap01/ … cap14/ (script di scena, trigger, checkpoint) + libero/
│   │   ├── ui/               title, pause, options, notebook-view, dialogue-box, subtitles, hud-touch, loading
│   │   └── data/             cataloghi generati (SFX, VOX, FOT, RUS, SEG, missioni) da `content/`
│   ├── content/
│   │   ├── ink/              cap01.ink … cap14.ink, libero.ink, comparse.ink (importati da docs/NARRATIVA)
│   │   ├── testi/            quaderno.json, obiettivi.json, pensieri.json (con marcatori LIBRO/NUOVO)
│   │   └── cataloghi/        sfx.json, vox.json, fot.json, rus.json, seg.json, missioni.json
│   └── public/               manifest, service worker, font
├── blender/
│   ├── scripts/              import/, retopo/, uv/, bake/, rig/, anim/, taormina/, kit/, export/, review/
│   └── sources/              .blend (Git LFS)
├── assets_in/                consegne di Vlad (Git LFS): immagini, modelli 3D, dati, audio
├── assets/                   output pronti per il gioco: .glb, .ktx2, .env, audio (generati dagli script)
├── tools/                    validator/, manifest/, ink-import/, taormina/, vox/, check-docs/
└── tests/                    e2e/ (Playwright), visual/ (screenshot di riferimento), perf/, fixtures/ (salvataggi)
```

### 1.1 Moduli e responsabilità
| Modulo | Responsabilità | Dipende da |
|---|---|---|
| `core/bootstrap` | rilevamento capacità, scelta del backend, preset, caricamento del nucleo, avvio del titolo | engine, presets |
| `core/engine` | crea `WebGPUEngine` o `Engine` (WebGL2), gestisce perdita di contesto, risoluzione dinamica | Babylon |
| `core/streaming` | manifesto, celle, LOD, priorità, memoria, cache | engine, scene-manager |
| `core/save` | stato di gioco, IndexedDB, migrazioni, export/import | tutti i sistemi (via interfaccia `Salvabile`) |
| `core/time` | calendario, ora, meteo, notti delle Donne | — |
| `core/events` | bus di eventi tipizzato | — |
| `core/debug` | console `window.cr`, pannello prestazioni | tutti |
| `render/*` | pipeline, effetti, lightmap, cielo, meteo, VFX | engine, presets |
| `systems/*` | sistemi SIS-01…27 del GDD | core |
| `audio/*` | sintesi, mix, spazializzazione, voci | core/time, systems |
| `chapters/*` | scene, trigger, checkpoint | systems |

## 2. Interfacce TypeScript (schizzi)

```ts
// core/engine.ts
export type Backend = 'webgpu' | 'webgl2';
export interface EngineHost {
  readonly backend: Backend;
  readonly engine: AbstractEngine;
  readonly preset: PresetId;
  setPreset(id: PresetId): Promise<void>;
  setRenderScale(s: number): void;          // 0.5–1.0
  onContextLost(cb: () => void): void;
}
export async function createEngine(canvas: HTMLCanvasElement): Promise<EngineHost>;

// core/streaming/streaming-manager.ts
export interface CellRef { id: string; bounds: [number, number, number, number]; lods: string[]; always?: boolean }
export interface StreamingManager {
  load(manifestUrl: string): Promise<void>;
  update(playerPos: Vector3, dtMs: number): void;       // chiamato ogni frame
  preload(cellIds: string[], reason: 'teleport' | 'scene'): Promise<void>;
  isReady(cellId: string, lod?: number): boolean;
  readonly stats: { loaded: number; loading: number; gpuMemMB: number; cpuMemMB: number };
}

// core/save/save-system.ts
export interface Salvabile<T> { readonly chiave: keyof StatoGioco; esporta(): T; importa(v: T): void }
export interface SaveSystem {
  salva(slot: SlotId): Promise<void>;
  carica(slot: SlotId): Promise<StatoGioco>;
  autosalva(motivo: 'checkpoint' | 'scena' | 'timer'): Promise<void>;
  esportaFile(): Promise<Blob>;
  importaFile(f: File): Promise<AnteprimaSalvataggio>;
  migra(stato: unknown): StatoGioco;                     // catena 1→2→3…
}

// systems/dialogue/dialogue-runner.ts
export interface RigaDialogo { id: string; pg: string; testo: string; lingua: 'it' | 'ru' | 'scn';
  sottotitolo?: string; traslitterazione?: string; vox?: string; tag: Record<string, string> }
export interface DialogueRunner {
  avvia(storia: string, nodo: string): Promise<void>;
  avanza(): void;
  scegli(indice: number): void;
  readonly stato: 'chiuso' | 'riga' | 'scelte';
  readonly rigaCorrente?: RigaDialogo;
  readonly scelte: { indice: number; testo: string }[];
  variabile<T = unknown>(nome: string): T;
  impostaVariabile(nome: string, v: unknown): void;
}

// systems/notebook/notebook.ts
export interface Notebook {
  sblocca(id: string): void;                  // IND-, RUS-, RIC-, FOT-, SEG-
  apri(sezione?: SezioneQuaderno): void;
  chiudi(): void;
  aggiungiFreccia(da: string, a: string): void;
  impostaObiettivo(id: string): void;
  readonly voci: VoceQuaderno[];
}

// systems/phone/phone.ts
export interface Phone {
  alza(modo: 'foto' | 'orologio'): void; abbassa(): void;
  scatta(): Promise<FotoScattata>;            // riconosce i soggetti FOT_
  torcia(on: boolean): void;
  readonly soggettoInquadrato?: string;
}

// systems/missions/mission-system.ts
export interface MissionSystem {
  avviaScena(id: string, opzioni?: { daCheckpoint?: string }): Promise<void>;
  completaPasso(missione: string, passo: number): void;
  checkpoint(id: string): Promise<void>;
  falliscoMorbido(motivo: string): Promise<void>;
  readonly scena: string; readonly obiettivo: string;
}

// core/time/calendar.ts
export interface Calendar {
  readonly data: string; readonly minuti: number; readonly meteo: Meteo;
  imposta(data: string, ora: string): void; scala(s: number): void;
  readonly notteDonne: boolean; posizioneSole(): { azimut: number; altezza: number };
}

// systems/house/house-state.ts
export interface HouseState { crepa: 0|1|2|3|4|5; luce: 0|1|2|3; acqua: 0|1|2|3; limone: 0|1|2|3|4; guarita: boolean;
  imposta(p: Partial<Omit<HouseState,'imposta'>>): void }

// systems/npc/npc-controller.ts
export interface NpcController {
  readonly id: string;
  vaiA(punto: Vector3 | string, velocita?: number): Promise<void>;
  guarda(target: TransformNode | null, peso?: number): void;   // sguardo testa/collo/occhi
  anima(clip: string, opzioni?: { loop?: boolean; blend?: number }): Promise<void>;
  routine(id: string): void;
  vedeSpiriti: false | 'traccia' | 'sente';                    // D-24
}

// audio/audio.ts
export interface AudioSystem {
  play(sfx: string, at?: Vector3 | TransformNode): AudioHandle;   // sottotitolo SFX automatico
  voce(vox: string, pg: string): Promise<void>;                  // duck degli ambienti
  ambiente(letto: string, fadeMs?: number): void;
  readonly volumi: Record<'master'|'voci'|'ambienti'|'effetti'|'ui', number>;
}

// core/debug/console.ts — vedi §11
export interface DebugConsole { [comando: string]: (...args: any[]) => unknown }
```

## 3. Avvio
1. `index.html` carica il nucleo (≤ 12 MB compressi: motore, codice, UI, font, Havok WASM, primo manifesto).
2. `bootstrap`: `navigator.gpu` + `WebGPUEngine.IsSupportedAsync` → WebGPU; altrimenti WebGL2 (`Engine` con `antialias:false`, MSAA gestito dal preset); altrimenti pagina d'aiuto.
3. Preset (§12.4), opzioni salvate, scena del titolo (cella `TITOLO` + Casa Russo esterna).
4. Service worker registrato al primo avvio (cache del nucleo e delle celle visitate).

## 4. Stato di gioco e salvataggi

### 4.1 Schema JSON (versione 1)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://casarusso.local/schema/salvataggio-v1.json",
  "title": "StatoGioco",
  "type": "object",
  "required": ["versione","versioneGioco","creato","aggiornato","storia","tempo","giocatore","ink","rapporti","flag","casa","val","quaderno","telefono","collezioni","missioni","mondo","statistiche"],
  "properties": {
    "versione": { "const": 1 },
    "versioneGioco": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
    "creato": { "type": "string", "format": "date-time" },
    "aggiornato": { "type": "string", "format": "date-time" },
    "storia": { "type": "object", "required": ["capitolo","scena","checkpoint","capitoliCompletati","modalita","puntoSicuro"],
      "properties": {
        "capitolo": { "type": "integer", "minimum": 1, "maximum": 14 },
        "scena": { "type": "string", "pattern": "^SCN-\\d{2}-\\d{2}$|^LIBERO$" },
        "checkpoint": { "type": "string", "pattern": "^CP-\\d{2}-[A-Z]$" },
        "capitoliCompletati": { "type": "array", "items": { "type": "integer" } },
        "modalita": { "enum": ["missione","libero"] },
        "puntoSicuro": { "type": "object", "properties": { "scena": {"type":"string"}, "pos": {"type":"array","items":{"type":"number"},"minItems":3,"maxItems":3}, "yaw": {"type":"number"} } },
        "aiuti": { "type": "object", "additionalProperties": { "type": "integer" } }
      } },
    "tempo": { "type": "object", "required": ["data","minuti","meteo","scala"],
      "properties": { "data": {"type":"string","format":"date"}, "minuti": {"type":"integer","minimum":0,"maximum":1439},
        "meteo": {"enum":["sereno","velato","ventoso","pioggia","temporale"]}, "scala": {"type":"number","minimum":0,"maximum":40} } },
    "giocatore": { "type": "object", "required": ["cella","pos","yaw","pitch","postura"],
      "properties": { "cella": {"type":"string"}, "pos": {"type":"array","items":{"type":"number"},"minItems":3,"maxItems":3},
        "yaw": {"type":"number"}, "pitch": {"type":"number"}, "postura": {"enum":["in_piedi","accovacciata","in_ginocchio","seduta"]} } },
    "ink": { "type": "object", "required": ["stato","cronologia"],
      "properties": { "stato": {"type":"string","description":"story.state.toJson()"},
        "cronologia": {"type":"array","maxItems":200,"items":{"type":"object","properties":{"id":{"type":"string"},"pg":{"type":"string"},"testo":{"type":"string"},"lingua":{"enum":["it","ru","scn"]}}}} } },
    "rapporti": { "type": "object", "propertyNames": {"pattern":"^rap_[a-z]+$"}, "additionalProperties": {"type":"integer","minimum":-3,"maximum":3} },
    "flag": { "type": "object", "propertyNames": {"pattern":"^flag_[a-z0-9_]+$"}, "additionalProperties": {"type":"boolean"} },
    "casa": { "type": "object", "required": ["casa_crepa","casa_luce","casa_acqua","casa_limone","casa_guarita"],
      "properties": { "casa_crepa": {"type":"integer","minimum":0,"maximum":5}, "casa_luce": {"type":"integer","minimum":0,"maximum":3},
        "casa_acqua": {"type":"integer","minimum":0,"maximum":3}, "casa_limone": {"type":"integer","minimum":0,"maximum":4}, "casa_guarita": {"type":"boolean"} } },
    "val": { "type": "object", "propertyNames": {"pattern":"^val_[a-z0-9_]+$"}, "additionalProperties": {"type":"integer"} },
    "quaderno": { "type": "object", "required": ["voci","obiettivo","sospettati","patto","paginaCasaRusso"],
      "properties": {
        "voci": {"type":"array","items":{"type":"object","required":["id","sbloccata","letta"],"properties":{"id":{"type":"string","pattern":"^(IND|RUS|RIC|FOT|SEG)-[A-Z0-9-]+$"},"sbloccata":{"type":"string"},"letta":{"type":"boolean"}}}},
        "obiettivo": {"type":"string","pattern":"^OBJ-\\d{2}-\\d{2}$|^$"},
        "sospettati": {"type":"object","properties":{"frecce":{"type":"array","items":{"type":"array","items":{"type":"string"},"minItems":2,"maxItems":2}}}},
        "patto": {"type":"boolean"}, "paginaCasaRusso": {"type":"boolean"},
        "ultimaPagina": {"type":"object","properties":{"sezione":{"type":"string"},"pagina":{"type":"integer"}}} } },
    "telefono": { "type": "object", "required": ["foto","torcia"],
      "properties": { "foto": {"type":"array","maxItems":120,"items":{"type":"object","required":["id","data","miniatura"],"properties":{"id":{"type":"string"},"soggetto":{"type":["string","null"]},"data":{"type":"string"},"miniatura":{"type":"string","description":"chiave IndexedDB (export: data URI)"}}}},
        "torcia": {"type":"boolean"} } },
    "collezioni": { "type": "object", "required": ["col_rus","col_ric","col_fot","col_seg"],
      "properties": { "col_rus": {"type":"array","items":{"type":"string"}}, "col_ric": {"type":"array","items":{"type":"string"}},
        "col_fot": {"type":"array","items":{"type":"string"}}, "col_seg": {"type":"array","items":{"type":"string"}} } },
    "missioni": { "type": "object", "required": ["attive","completate"],
      "properties": { "attive": {"type":"array","items":{"type":"object","properties":{"id":{"type":"string"},"passo":{"type":"integer"}}}},
        "completate": {"type":"array","items":{"type":"string"}} } },
    "bar": { "type": "object", "properties": { "turni": {"type":"integer"}, "ordiniServiti": {"type":"integer"}, "miglioreTurno": {"type":"integer"}, "clientiConosciuti": {"type":"array","items":{"type":"string"}} } },
    "npc": { "type": "object", "additionalProperties": { "type": "object", "properties": { "cella": {"type":"string"}, "pos": {"type":"array","items":{"type":"number"}}, "routine": {"type":"string"}, "passo": {"type":"integer"} } } },
    "mondo": { "type": "object", "properties": { "interagiti": {"type":"array","items":{"type":"string"}}, "oggetti": {"type":"object"},
        "pensieriVisti": {"type":"array","items":{"type":"string"}}, "cinematicheViste": {"type":"array","items":{"type":"string"}},
        "viaggio": {"type":"object","properties":{"t":{"type":"number"}}} } },
    "statistiche": { "type": "object", "properties": { "tempoGioco": {"type":"integer"}, "fallimentiMorbidi": {"type":"integer"} } }
  }
}
```

### 4.2 Archiviazione
- IndexedDB `casarusso` con store `salvataggi` (chiavi `auto`, `auto-bak`, `1`, `2`, `3`), `foto` (miniature JPEG 320×180), `opzioni`.
- Scrittura atomica: si scrive `auto-tmp`, si verifica lo schema, si rinomina in `auto` spostando il precedente in `auto-bak`.
- Export: un file `.casarusso.json` con lo stato e le miniature come data URI; import con validazione (ajv) e anteprima.

### 4.3 Migrazioni v1.0 → v2.0 → v3.0
- Ogni rilascio che cambia lo schema incrementa `versione` e aggiunge una funzione pura `migra_N_a_N+1(stato)`; la catena si applica in ordine al caricamento.
- **v1 → v2** (rilascio v2.0): aggiunge le variabili dei capp. 4–8 con i loro default; se `flag_v1_fine` è vero → `storia.scena = "SCN-04-01"`, `storia.modalita = "missione"`, `tempo = 2025-09-18 01:35`; nuove voci di collezione vuote; non tocca nulla di esistente.
- **v2 → v3** (rilascio v3.0): aggiunge variabili dei capp. 9–14 e `casa_guarita` se assente.
- I salvataggi di versioni **più nuove** del gioco non si caricano (messaggio chiaro).
- Test: `tests/fixtures/salvataggio_v1_*.json` (uno per checkpoint della v1.0) devono migrare e proseguire fino alla fine del cap. 14 nel giro automatico (FASI Fase 7).

## 5. Illuminazione
- **Base baked in Cycles** (Blender 5.2): per ogni cella e per 4 ore di riferimento (mattina 9:00, pomeriggio 15:30, tramonto, notte) lightmap HDR con rimbalzi e AO, su **secondo canale UV** non sovrapposto (padding 4 px a 1024, 8 px a 2048), codificata RGBD in KTX2 UASTC HDR dove supportato, altrimenti RGBD 8 bit.
- **Interpolazione oraria**: il gioco fonde le due lightmap più vicine all'ora corrente (shader di blend nel materiale; costo 1 campionamento in più), con la luce del sole dinamica che aggiunge le ombre dirette (CascadedShadowGenerator) e il colore del cielo.
- **Ambiente**: HDR per cella e ora renderizzati in Blender (equirettangolari 2K) → `.env` (prefiltered) con lo strumento IBL di Babylon in CI; sonde di riflessione locali (ReflectionProbe) negli interni chiave.
- **Personaggi e oggetti dinamici**: luce in tempo reale + IBL della cella + light probes sferiche (coefficienti SH baked in una griglia di 2 m negli interni, 8 m all'esterno).
- **Meteo**: pioggia = modificatori dei materiali (roughness, albedo, pozzanghere), cielo coperto (HDR alternativo baked), luce diffusa.
- **Clustered lighting** (Babylon 9) per gli interni con molte lampade.

## 6. Streaming
### 6.1 Manifesto (esempio)
```json
{
  "versione": 1, "release": "1.0.0", "crs": "EPSG:25833", "origine": [524000, 4187500], "cella": 128,
  "sempre": ["CR-INT","CR-EXT","TAO-SCA-01a","TAO-SCA-01b","TERRENO-LONTANO","CIELO"],
  "celle": [
    { "id": "TAO-c09-r15", "bounds": [525152, 4189420, 525280, 4189548],
      "lod": [ {"url":"celle/TAO-c09-r15_lod0.glb","bytes":5821440,"tri":182000},
               {"url":"celle/TAO-c09-r15_lod1.glb","bytes":1310720,"tri":41000},
               {"url":"celle/TAO-c09-r15_lod2.glb","bytes":262144,"tri":6000} ],
      "lightmap": { "mattina":"lm/TAO-c09-r15_0900.ktx2", "pomeriggio":"lm/TAO-c09-r15_1530.ktx2",
                    "tramonto":"lm/TAO-c09-r15_tram.ktx2", "notte":"lm/TAO-c09-r15_notte.ktx2" },
      "env": "env/TAO-c09-r15_1530.env", "navmesh": "nav/TAO-c09-r15.bin", "collisioni": "col/TAO-c09-r15.glb",
      "dipende": ["kit/facciate_v1.glb","tex/kit_atlas_v1.ktx2"], "audio": "corso", "release": "1.0" }
  ]
}
```
### 6.2 Regole
- Caricamento LOD0 entro 192 m, LOD1 192–448 m, LOD2 fino a 1,5 km; isteresi di scaricamento 64 m; massimo 3 richieste parallele (PC 6); priorità per distanza e direzione dello sguardo.
- Pre-caricamento della cella di destinazione durante le dissolvenze e sui percorsi delle scene (es. tutto il percorso delle impronte del cap. 10).
- Upload GPU distribuito su più frame (budget 3 ms/frame PC, 4 ms tablet) per evitare scatti.
- Navmesh per cella caricata con la geometria; gli NPC in celle scaricate passano a simulazione astratta.
- **Budget di memoria**: PC — texture ≤ 1,5 GB, geometria ≤ 600 MB; tablet — texture ≤ 450 MB, geometria ≤ 250 MB, pagina complessiva ≤ 1,3 GB (D-85); superata la soglia del 90% si scaricano le celle più lontane e si abbassa di un mip il kit.
- **Service worker**: cache-first per gli asset con hash nel nome (immutabili), network-first per il manifesto; quota stimata con `navigator.storage.estimate()`, limite 1,5 GB, rimozione LRU delle celle.

## 7. Rendering
### 7.1 Backend e browser (verificato)
| Browser / sistema | Backend | Note |
|---|---|---|
| Chrome / Edge (Windows, macOS, ChromeOS) | WebGPU | stabile |
| Chrome (Android 12+, GPU Qualcomm/ARM) | WebGPU | tablet Android; modalità compatibilità GLES 3.1 dal 2026 |
| Safari 26 (macOS, **iPadOS 26**) | WebGPU | attivo di default da Safari 26; tablet di riferimento (D-46) |
| Firefox (Windows 141+; macOS Apple Silicon 147+) | WebGPU | Firefox su Linux e Mac Intel → WebGL2 |
| Altri | WebGL2 | tutti gli effetti salvo quelli marcati «solo WebGPU» |

### 7.2 Effetti → funzioni di Babylon 9.x
| Effetto | Classe / funzione | WebGPU | WebGL2 | Preset minimo |
|---|---|---|---|---|
| PBR (clearcoat, sheen, subsurface, anisotropy) | `PBRMaterial` / `NodeMaterial` | ✓ | ✓ | Basso |
| Tone mapping ACES, LUT, grana, vignetta, aberrazione | `DefaultRenderingPipeline` / `ImageProcessingConfiguration` (o task equivalenti del frame graph) | ✓ | ✓ | Basso |
| Bloom | `DefaultRenderingPipeline.bloomEnabled` | ✓ | ✓ | Medio |
| Profondità di campo | `DefaultRenderingPipeline.depthOfField` | ✓ | ✓ | Medio (solo cinematiche) |
| FXAA / TAA | `fxaaEnabled` / `TAARenderingPipeline` | ✓ | ✓ | FXAA Basso–Medio, TAA Alto–Ultra |
| SSAO | `SSAO2RenderingPipeline` | ✓ | ✓ | Medio (mezza risoluzione) |
| SSR | `SSRRenderingPipeline` | ✓ | ✓ | Alto (Medio solo pavimenti dell'aeroporto e della stazione, mezza risoluzione) |
| Ombre a cascata | `CascadedShadowGenerator` | ✓ | ✓ | Basso (2 cascate) |
| Luce volumetrica | `FrameGraphVolumetricLightingTask` (Babylon 9) / ripiego `VolumetricLightScatteringPostProcess` | ✓ (compute) | ✓ (ripiego) | Alto (Medio solo scene degli spiriti) |
| Particelle | `GPUParticleSystem` (ripiego `ParticleSystem`) | ✓ | ✓ | Basso |
| Pelo di Fomà | gusci (`FurMaterial` della libreria materiali o Node Material a gusci con instancing) | ✓ | ✓ | Basso (6 gusci) |
| Molte luci | clustered lighting (Babylon 9) | ✓ | ✓ | Medio |
| Decal | `DecalMap`/decal proiettati | ✓ | ✓ | Basso |
| Fisica | `HavokPlugin` + `PhysicsCharacterController` | ✓ | ✓ | — |
| Navigazione | Navigation Plugin V2 (`CreateNavigationPluginAsync`) | ✓ | ✓ | — |
| Riflessi locali | `ReflectionProbe` | ✓ | ✓ | Alto |
| Risoluzione dinamica | `engine.setHardwareScalingLevel` + controllo del frame time | ✓ | ✓ | tablet sempre |
| FSR 1 (upscaling) | pipeline FSR 1 (Babylon 9.21+, WebGL2/Native) | — | ✓ | tablet WebGL2 |

**Frame Graph**: in Fase 1 si costruisce la pipeline sul Frame Graph v1 di Babylon 9 (task per GBuffer/geometria, SSAO2, SSR, TAA, volumetria, post); se un task manca per una funzione, si usa la pipeline classica equivalente per quella sola funzione. La scelta definitiva è un criterio d'uscita della Fase 1 (scena di prova che misura entrambe).

## 8. Formati, compressione e nomi
- **Geometria**: glTF 2.0 binario `.glb`, **EXT_meshopt_compression** + quantizzazione (D-60); motivazioni: decodifica più veloce di Draco, comprime anche animazioni e morph target, decoder WASM piccolo. Draco escluso.
- **Texture**: KTX2: **UASTC** (livello 4, RDO λ 2–4, Zstd 18) per normal map, ORM, maschere, volto dei personaggi e oggetti eroe; **ETC1S** (qualità 255) per albedo dell'architettura comune e decal; lightmap RGBD in UASTC; mipmap complete; dimensioni potenze di 2.
- **Ambienti**: `.env` (prefiltrati) 256–512 px.
- **Audio**: voci Opus in WebM (o AAC m4a per Safari se Opus non è supportato nel contenitore) a 96 kbps mono; i suoni sono sintetizzati.
- **Nomi**: minuscole, trattini, prefissi di classe: `chr_babuska_lod0.glb`, `prp_lapot.glb`, `env_aer_arrivi.glb`, `kit_facciata_a03.glb`, `cel_tao-c09-r15_lod1.glb`; mesh in Blender: `GEO_`, collisioni `COL_`, punti `CP_`, `FOT_`, `KNE_`, `CRC_`, NPC `NPC_`.
- **Cartelle**: `assets/chr/`, `assets/prp/`, `assets/env/`, `assets/kit/`, `assets/celle/`, `assets/lm/`, `assets/tex/`, `assets/vox/`.

## 9. Animazione
- Scheletro unico (D-64), clip retargettate in Blender (Mixamo con account gratuito, Rokoko Studio, Uthana: vedi PIPELINE §5), esportate come glTF animations; blending con `AnimationGroup` e pesi; IK piedi su scale (raycast + 2-bone IK).
- Labiale: visemi da analisi dell'audio (Rhubarb Lip Sync in pipeline → curve di blend shape per VOX); per le battute solo testo, labiale generico da lunghezza del testo.
- Sguardo: rig procedurale testa/collo/occhi con limiti (±70° yaw, ±35° pitch) e smorzamento.

## 10. Validatore degli asset (blocca l'export)
| Regola | Soglia |
|---|---|
| Triangoli personaggio principale | LOD0 ≤ 40 000 (Fomà ≤ 40 000 + gusci), LOD1 ≤ 15 000, LOD2 ≤ 5 000 |
| Triangoli comparsa | LOD0 ≤ 20 000, LOD1 ≤ 8 000 |
| Triangoli oggetto eroe / secondario | ≤ 15 000 / ≤ 3 000 |
| Triangoli cella | LOD0 ≤ 250 000 (tablet ≤ 90 000 visibili per cella), LOD1 ≤ 60 000, LOD2 ≤ 8 000 |
| Texture | lato ≤ 4096 (solo eroi su Ultra), altrimenti ≤ 2048; potenze di 2; KTX2 obbligatorio |
| Lightmap UV | secondo canale presente per le mesh statiche; nessuna sovrapposizione (test di rasterizzazione a 512 px, 0 pixel condivisi); padding ≥ 4 px a 1024 |
| Scala | 1 unità = 1 m; bounding box entro ±5% delle misure dichiarate nella scheda (es. Fomà 0,32 m, babuška 1,49 m) |
| Origine | personaggi ai piedi (0,0,0), oggetti al centro della base, celle all'angolo sud-ovest |
| Nomi | regex delle convenzioni §8; niente nomi di default («Cube.001») |
| Materiali | solo PBR metallic-roughness glTF + estensioni KHR ammesse (clearcoat, sheen, transmission, volume, ior, emissive_strength); ≤ 3 materiali per personaggio LOD0, ≤ 1 per LOD2 |
| Scheletro | nomi Mixamo-compatibili; ≤ 4 influenze per vertice; nessun peso < 0,01; somma pesi = 1 ± 0,001 |
| Animazioni | 30 fps campionati; nessuna traslazione della radice nelle clip «sul posto» |
| Normali | nessun NaN; tangenti generate (MikkTSpace) |
| Collisioni | `COL_` convessi ≤ 64 vertici o primitive |
| Dimensione file | personaggio ≤ 6 MB, cella LOD0 ≤ 8 MB (PC) |

## 11. Console di debug (`window.cr`, SIS-20)
| Comando | Effetto |
|---|---|
| `cr.vai(scena, {checkpoint?})` | salta alla scena SCN-CC-NN con lo stato coerente (variabili di default dei capitoli precedenti o di un fixture) |
| `cr.capitolo(n)` | inizio del capitolo n |
| `cr.data("AAAA-MM-GG","hh:mm")`, `cr.tempo(scala)` | calendario e scala del tempo |
| `cr.casa({crepa,luce,acqua,limone,guarita})` | stato della casa |
| `cr.var(nome[, valore])` | legge/scrive una variabile Ink/stato |
| `cr.stato()` | copia dello stato di gioco |
| `cr.salva(slot)`, `cr.carica(slot)`, `cr.esporta()`, `cr.importa(json)` | salvataggi |
| `cr.teletrasporta(LUO-o-[x,y,z])` | sposta Vera |
| `cr.input.premi(codice)`, `cr.input.tieni(codice, ms)`, `cr.input.muovi(x,y,ms)`, `cr.input.guarda(yaw,pitch)` | input simulato |
| `cr.guarda(id)`, `cr.interagisci(id)`, `cr.scegli(n)`, `cr.avanza()` | interazioni e dialoghi |
| `cr.attendi(eventoOId, timeoutMs)` | attende un evento (SFX, VOX, scena, checkpoint) |
| `cr.eventi()` | ultimi 500 eventi |
| `cr.ui()` | stato dell'interfaccia (dialogo, scelte, pensiero, sottotitoli suoni, marker, telefono, quaderno) |
| `cr.camera()`, `cr.render()` | dati di camera (altezza, FOV) e di rendering (effetti attivi, backend, preset) |
| `cr.perf()` | FPS, frame time GPU/CPU, draw call, triangoli, memoria texture/geometria |
| `cr.navmesh(on)`, `cr.collisioni(on)`, `cr.celle(on)` | visualizzazioni |
| `cr.preset(id)`, `cr.opzioni.set(chiave, valore)` | grafica e opzioni |
| `cr.fallisci()` | avvia il fallimento morbido |
| `cr.quaderno.apri(sezione)`, `cr.collezioni()` | quaderno e conteggi |
| `cr.bar.avviaTurno()`, `cr.bar.servi(ordine)` | bar |
| `cr.autoplay(capitolo, {velocita})` | giro automatico del capitolo (scelte di default o da file) |
| `cr.test.*` | helper di test (`scale`, `fotoContieneLayer`, `decalCrepaStadio`, `mattiaReagisce`, `impronte.completa`, `visibile`, `minigioco`, `cannistri.completa`, `unisci`, `missione`, `segreto`) |

## 12. Hardware di riferimento, preset e budget

### 12.1 Dispositivi (D-46)
| Ruolo | Dispositivo | Perché |
|---|---|---|
| **Tablet di riferimento** | iPad 11ª generazione (A16, 6 GB), iPadOS 26, Safari | è il dispositivo di Vlad; WebGPU attivo di default in Safari 26; GPU di fascia media tra i tablet in uso; limiti di memoria di Safari ben documentati → budget prudente |
| Tablet secondario | iPad Air M2 / Galaxy Tab S9 (Chrome) | preset Alto su tablet potenti |
| **PC medio** | Windows 11, GPU classe RTX 3060 / RTX 4060 (8–12 GB), CPU 6 core (Ryzen 5 5600 / Core i5-12400), 16 GB RAM, 1920×1080, Chrome/Edge | RTX 4060 e 3060 sono tra le 5 GPU più diffuse nel sondaggio Steam di settembre 2026 (la più diffusa è la RTX 5070, troppo alta per un «medio» di un gioco nel browser) |
| **Minimo** | iPad 10ª gen (A14, 4 GB); PC con Intel Iris Xe / GTX 1650, 8 GB, 1600×900 | sotto: avviso, il gioco parte comunque con preset Basso |

### 12.2 Budget di prestazioni (confermati o corretti)
| Voce | PC medio | Tablet di riferimento | Note |
|---|---|---|---|
| Frequenza | 60 FPS (frame ≤ 16,6 ms) | 30 FPS stabili (≤ 33,3 ms) | confermato |
| Risoluzione | nativa 1080p, scala 85–100% | dinamica 70–100% (FSR 1 su WebGL2) | confermato |
| Triangoli visibili | ≤ 3 M | ≤ 800 k | confermato |
| Draw call | ≤ 1 500 | ≤ 500 | confermato |
| Memoria texture | ≤ 1,5 GB | **≤ 450 MB** | corretto (D-85) |
| Memoria complessiva della pagina | ≤ 3 GB | **≤ 1,3 GB** | nuovo (D-85) |
| Personaggio | 40 000 tri | LOD 15 000 | confermato |
| Fomà | 40 000 + 16–24 gusci | 40 000 + 10 gusci | il «pelo» ridotto del piano = meno gusci, stessa tecnica |
| Scena con tre Donne | ≤ 3,5 ms GPU per i VFX | ≤ 6 ms | nuovo |
| Primo avvio fino al titolo | ≤ 30 s (connessione 30 Mbit/s) | ≤ 45 s | confermato |
| Cambio cella | nessuno scatto > 50 ms | nessuno scatto > 66 ms | misurato nel test perf |

### 12.3 Preset
| Impostazione | Basso | Medio (tablet rif.) | Alto (PC medio) | Ultra |
|---|---|---|---|---|
| Scala di risoluzione | 70% | 80% dinamica | 100% | 100% (o supersampling 120% opz.) |
| Antialiasing | FXAA | FXAA | TAA | TAA |
| Ombre | 2 cascate 1024 | 2 cascate 1536 | 4 cascate 2048 | 4 cascate 4096 + ombre di contatto |
| SSAO | no | mezza risoluzione | piena | piena, raggio maggiore |
| SSR | no | solo pavimenti lucidi, mezza ris. | sì | sì, più passi |
| Luce volumetrica | no | solo scene degli spiriti | sì | sì, alta risoluzione |
| Bloom / DOF | bloom basso / DOF solo cinematiche | sì / solo cinematiche | sì / sì | sì / sì |
| Particelle (moltiplicatore) | 0,25 | 0,4 | 1,0 | 1,5 |
| Texture | mip +1 (metà) | mip +1 salvo volti e lightmap | piene | piene + 4K eroi |
| Distanza LOD | ×0,6 | ×0,8 | ×1,0 | ×1,3 |
| Gusci del pelo di Fomà | 6 | 10 | 16 | 24 |
| Luci dinamiche con ombra | 1 | 2 | 4 | 6 |
| Agenti della folla | 8 | 12 | 20 | 28 |
| Riflessi locali (probe) | no | no | sì (statici) | sì (aggiornati) |
| Grana / aberrazione | no | grana | sì | sì |

### 12.4 Scelta automatica del preset
1. Classe del dispositivo: tablet (iPad o `pointer: coarse` + schermo ≥ 7") → massimo **Medio** (Alto solo con chip M, GPU Apple ≥ M1 da `GPUAdapterInfo`, o Android con Adreno 7xx/Mali-G7xx); PC → tutti.
2. Prova di 3 s sulla scena del titolo a preset Alto, misura del tempo GPU medio (timestamp query su WebGPU, `EXT_disjoint_timer_query_webgl2` su WebGL2, altrimenti frame time):
   - PC: < 7 ms → **Ultra**; < 11 ms → **Alto**; < 20 ms → **Medio**; altrimenti **Basso**.
   - Tablet: < 18 ms → **Medio**; altrimenti **Basso**; (Alto se consentito al punto 1 e < 12 ms).
3. `navigator.deviceMemory` ≤ 4 → al massimo Medio; WebGL2 senza timer → Medio su PC, Basso su tablet.
4. Durante il gioco: se per 10 s il frame time supera il budget del 15%, la scala di risoluzione scende di 5% (fino al minimo del preset); se resta sopra, notifica discreta «Vuoi passare a Basso?».

### 12.5 Misura delle prestazioni
Scena di prova (aeroporto + Corso + cucina con tre Donne) eseguita da Playwright su Chromium headless con GPU (PC di CI con GPU) e con prove manuali sull'iPad di Vlad con `?perf=1` (overlay che registra 60 s e mostra p50/p95/p99 del frame time e la memoria; esporta un JSON da inviare).

## 13. Build, CI, hosting, versioni
- **Build**: `vite build` → `dist/` con asset con hash; generazione di cataloghi e manifesto (`tools/manifest`), import Ink (`tools/ink-import`), compilazione Ink (inklecate).
- **CI (GitHub Actions)**: lint, typecheck, test unitari, validatore asset, verifica dei documenti (`tools/check-docs`: ID unici, citazioni [LIBRO] con `work/strumenti/verifica_libro.py`), build, Playwright (fumo + giri dei capitoli rilasciati), artefatti.
- **Pipeline Blender in CI**: `bpy` 5.2 su runner Linux per gli script veloci (validazione, export); bake Cycles pesanti eseguiti dallo stesso codice su una macchina con GPU (job manuale `bake`), output versionati con Git LFS.
- **Hosting** (D-44): hosting proprio di Vlad, sito statico senza protezione; deploy dal job `deploy` con `rsync` su SSH (o `lftp` su SFTP) usando segreti del repository (`DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`, `DEPLOY_PATH`); file di configurazione forniti per **Apache** (`.htaccess`) e **Nginx**: HTTPS obbligatorio, tipi MIME (`application/wasm`, `model/gltf-binary`, `image/ktx2`), compressione Brotli/gzip per JS/JSON/WASM, `Cache-Control: public, max-age=31536000, immutable` per gli asset con hash, `no-cache` per `index.html` e manifesto, intestazioni `Cross-Origin-Opener-Policy`/`Cross-Origin-Embedder-Policy` se servono thread WASM; `robots.txt` con `Disallow: /` e `<meta name="robots" content="noindex">`.
- **Versioni**: SemVer (`1.0.0`, `2.0.0`, `3.0.0`); tag git `v1.0.0`; ogni deploy scrive `version.json`; i salvataggi registrano `versioneGioco`.

## 14. Test
- **Playwright**: (1) fumo di avvio e preset; (2) giro automatico di ogni capitolo con `cr.autoplay` e verifica delle variabili attese a ogni checkpoint; (3) criteri di accettazione SIS-01…27 del GDD; (4) salva/carica deep-equal; (5) migrazioni dai fixture; (6) screenshot di riferimento delle inquadrature chiave (SCN-01-13 primo piano, SCN-02-08 Fomà, SCN-03-08 Donne, SCN-08-06, SCN-11-03, SCN-14-03) con soglia di differenza percettiva; (7) prestazioni sulla scena di prova; (8) testi: nessuna chiave mancante, controllo ortografico russo (lista RUS e battute VOX).
- **Prove manuali di Vlad**: ogni traguardo su iPad 11ª gen e su un PC.

## 15. Rischi (aggiornati)
| ID | Rischio | Impatto | Contromisura |
|---|---|---|---|
| R-01 | Taormina 1:1 è enorme | tempi, peso | kit di facciate, edifici da sagome OSM, solo i simboli fatti singolarmente; celle per rilascio |
| R-02 | Pelo e barba di Fomà nel browser | prestazioni | gusci + barba a ciocche su ossa; numero di gusci per preset; prototipo in Fase 1 |
| R-03 | Nebbia delle Donne costosa | cali di FPS | budget 3,5/6 ms, particelle e volumetria a mezza risoluzione su tablet; test sul tablet dalla Fase 2 |
| R-04 | Safari su iPad: memoria e reload della scheda | crash | budget 450 MB texture / 1,3 GB pagina; monitor della memoria; scaricamento aggressivo; test a ogni traguardo |
| R-05 | Modelli da Tripo/Hitem3D imprecisi (mani, vestiti) | deformazioni | pulizia dei pesi via script, pose di deformazione renderizzate e ispezionate da Claude con soglie numeriche (PIPELINE §5); se non passa: nuova scheda di richiesta con correzioni del prompt o della fascia poligoni |
| R-06 | Nessun lavoro manuale di Vlad in Blender (D-31) | qualità artistica | controlli automatici + render di revisione obbligatori + confronto con le immagini di riferimento; Vlad approva le immagini e i render, non modifica i modelli |
| R-07 | «Tutto giocabile in 3D» allunga i capitoli | durata | massimi dei raccordi; misura a ogni Beta |
| R-08 | Salvataggi tra versioni | perdita di progressi | schema versionato, migrazioni testate con fixture |
| R-09 | Licenze di dati e foto | uso non consentito | registro in CREDITI; ortofoto solo come riferimento finché non è verificata (Q-02) |
| R-10 | Budget voci (ElevenLabs gratuito) | voci mancanti | piano in AUDIO §4.3, Fish Audio come secondo strumento, priorità *must/should* |
| R-11 | Cambi di API di Babylon 9.x (Frame Graph, Navigation V2 in addons) | regressioni | versione fissata, aggiornamenti solo a inizio fase con test completi |
| R-12 | Hosting senza protezione | link condiviso per errore | `noindex`, URL non pubblicizzato; nessun dato personale nel gioco |
| R-13 | Pronuncia russa e siciliana delle voci sintetiche | resa poco credibile | revisione di madrelingua (Q-06, Q-07), accenti tonici segnati, 2 take |

## Fonti
- [@babylonjs/core su npm](https://www.npmjs.com/package/@babylonjs/core)
- [Annuncio Babylon.js 9.0](https://blogs.windows.com/windowsdeveloper/2026/03/26/announcing-babylon-js-9-0)
- [Babylon.js — Frame Graph: volumetric lighting](https://doc.babylonjs.com/features/featuresDeepDive/frameGraph/frameGraphExamples/frameGraphExampleVolumetricLighting)
- [Forum Babylon — Frame Graph v1.0](https://forum.babylonjs.com/t/frame-graph-v1-0-is-now-live/62163)
- [Babylon.js — Navigation Plugin V2](https://doc.babylonjs.com/features/featuresDeepDive/crowdNavigation/v2Intro)
- [Babylon.js 9.21.x (FSR 1 per WebGL2)](https://gamedev.net/news/5070-babylonjs-9210-released/)
- [WebKit — WebGPU in Safari 26](https://discuss.privacyguides.net/t/news-from-wwdc25-webkit-in-safari-26-beta/28226)
- [Firefox 141: WebGPU su Windows](https://www.gigazine.net/gsc_news/en/20250723-firefox-141) · [Firefox 147: WebGPU su Mac Apple Silicon](https://macmagazine.com.br/post/2026/01/13/firefox-147-inclui-suporte-a-webgpu-em-macs-com-apple-silicon-melhorias-no-pip-e-mais/)
- [Chrome — WebGPU su Android](https://developer.chrome.com/blog/new-in-webgpu-121)
- [Steam Hardware Survey settembre 2026](https://www.digitalcitizen.life/nvidia-rtx-5070-most-popular-gpu-steam-hardware-survey-september-2026/)
- [WebKit Bugzilla 300782](https://bugs.webkit.org/show_bug.cgi?id=300782) · [290623](https://bugs.webkit.org/show_bug.cgi?id=290623)
- [iPadOS 26 — dispositivi compatibili](https://everymac.com/systems/apple/ipad/ipad-faq/ipados-26-supported-devices-ipad-system-requirements.html)
- [glTF-Transform](https://gltf-transform.dev/) · [@gltf-transform/cli su npm](https://npmjs.com/package/@gltf-transform/cli)
- [bpy su PyPI](https://pypi.org/project/bpy/) · [Blender 5.2 LTS](https://gamefromscratch.com/blender-5-2-lts-released/)
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12)
