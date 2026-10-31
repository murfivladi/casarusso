# Pipeline degli asset

Come si produce ogni asset del gioco, secondo D-31 (Claude fa tutto in Blender con script headless, nessun lavoro manuale di Vlad in Blender), D-32 (immagine → 3D con richieste a Vlad), D-33 (modelli dal web CC0/CC-BY). Formati e soglie del validatore: `TDD.md` §8 e §10. Stile: `ART_BIBLE.md`.

## 1. Classi di asset e percorso

| Classe | Percorso | Esempi |
|---|---|---|
| **A — Immagine → 3D** | Nano Banana (Vlad) → Tripo o Hitem3D (Vlad) → `assets_in/` → Blender automatico (Claude) | tutti i personaggi, Fomà, le Donne (corpo e vestito), oggetti artigianali ed eroi: lapot', borsa a fiori, valigie con lo spago, cartello di Mattia, telefoni, ditale, cucchiaio, moka, vetrinetta con tazzine, quaderno (copertina), coniglio di pezza |
| **B — Modelli dal web** (CC0/CC-BY) | Claude cerca e verifica la licenza → scheda per Vlad → Vlad scarica in `assets_in/web/` → Blender (rielaborazione allo stile) | arredi generici, sedie e panchine dell'aeroporto, carrelli, segnaletica, alberi e piante, auto di sfondo, base della monovolume se adatta |
| **C — Procedurale in Blender** | script Python | architettura (Casa Russo, aeroporto, stazione), terreno da DEM, edifici da OSM, kit modulare delle facciate, scalinate, ringhiere, persiane, oggetti semplici (stoviglie, bottiglie, casse d'acqua) |
| **D — Texture PBR** | librerie CC0 (Poly Haven, ambientCG) o materiali procedurali baked in Blender | intonaci, pietre, maioliche (motivi originali), legni, metalli, tessuti |

Regola: si sceglie la classe A solo dove serve una forma organica o un'identità precisa; tutto ciò che è geometrico è classe C (più controllabile, nessuna attesa).

## 2. Fasce di poligoni per Tripo/Hitem3D (sorgente high-poly)

| Fascia | Quando | Esempi |
|---|---|---|
| **1,5 M** | primi piani lenti o oggetti tenuti a lungo davanti alla camera; dettagli fini da trasferire in normal map | babuška (primo piano sugli occhi SCN-01-13), Fomà, lapot' (fibre di corteccia), quaderno di scienze (copertina e bordo pagine), ditale e cucchiaio (cap. 13, tenuti in mano) |
| **1,0 M** | personaggi principali e oggetti importanti visti a distanza di conversazione (0,8–2 m) | Irina, Salvo, Giulia, Mattia, nonna Concetta, le tre Donne, Nicolò, borsa a fiori, valigie con lo spago, telefono di Vera, moka, coniglio di Mattia |
| **0,5 M** | comparse, oggetti secondari, oggetti visti a media/lunga distanza | turisti, squadra di pallavolo, prete, signore dell'aeroporto, dottore, professori, gatti, cartello di Mattia, valigia a fiori del prete, telefono di Giulia, casse |

Regole di affinamento: (1) un personaggio che ha **un** primo piano narrativo sale di fascia; (2) per gli oggetti piccoli la fascia dipende dalla distanza di visione, non dalla dimensione: un ditale tenuto a 30 cm vale 1,5 M; (3) superfici molto lisce (telefoni) possono scendere di fascia senza perdita, ma restano alla fascia indicata nella scheda per avere bordi puliti nel bake.

## 3. Modello della scheda di richiesta (usato in `RICHIESTE_ASSET/`)

```
### REQ-XXX-NNN — Nome
- A cosa serve e in quali capitoli:
- Priorità (fase in cui serve):
- Fascia poligoni Tripo/Hitem3D: 1,5 M / 1,0 M / 0,5 M — motivo:
- Prompt Nano Banana principale (EN):
- Prompt di modifica per le altre viste (EN): vista laterale · vista posteriore · vista 3/4 (usando la prima immagine come riferimento)
- Formato e proporzioni dell'immagine:
- Impostazioni Tripo / Hitem3D:
- Nome file e cartella (assets_in/…):
- Cosa farà Claude dopo:
- Budget finale in gioco:
- Controlli automatici da superare:
- Controlla l'immagine (lista per Vlad):
- In breve (IT):
```

### 3.1 Impostazioni standard dei generatori 3D
| Strumento | Impostazioni (personaggi) | Impostazioni (oggetti) |
|---|---|---|
| **Hitem3D** (consigliato per i personaggi) | modalità **multi-vista** (fronte obbligatorio + retro + sinistra + destra, tutte dalla stessa sessione di modifica di Nano Banana); risoluzione **1536** per 1,5 M e 1,0 M (impostare il numero di facce: 1.500.000 o 1.000.000), **1024** per 0,5 M (500.000); texture **PBR sì**; formato **GLB** (o FBX se GLB non disponibile) | immagine singola se l'oggetto è simmetrico, altrimenti fronte + 3/4; stesse regole di risoluzione e facce |
| **Tripo** (alternativa; consigliato per oggetti duri) | modello **H3.1** o successivo, qualità geometria **Detailed**, limite facce come la fascia (1,5 M / 1,0 M / 0,5 M; se l'interfaccia offre solo preset, scegliere il primo uguale o superiore), **texture PBR sì**, **quad no** (il quad di Tripo è limitato a poche decine di migliaia di facce: la ritopologia la fa Claude), esportazione **GLB** | idem |

Se uno strumento non permette esattamente la fascia indicata, si sceglie il valore più vicino **superiore** e lo si scrive nel file `NOTE.txt` accanto al modello.

## 4. Regole per le immagini Nano Banana destinate al 3D
1. **Un soggetto per immagine**; nessun altro oggetto o persona.
2. **Personaggi a figura intera in A-pose**: braccia staccate dal corpo di 30–45°, mani aperte e vuote con le dita leggermente separate, piedi visibili e paralleli alla larghezza delle spalle, espressione neutra, bocca chiusa, sguardo dritto in camera.
3. **Vista frontale** il più possibile dritta (camera all'altezza del petto, ottica 85 mm equivalente, nessuna prospettiva esagerata).
4. **Sfondo grigio chiaro uniforme e senza cuciture** (#D9D9D9 circa), nessun pavimento visibile né ombra a terra marcata.
5. **Luce da studio morbida e uniforme**: niente ombre forti, niente luce di contorno, niente profondità di campo né mosso.
6. **Stile fotografico realistico** con tessuti leggibili (trama, cuciture, pieghe naturali ma non esagerate).
7. **Niente testo, loghi, marchi**, salvo che il testo sia il soggetto (cartello di Mattia, etichetta del quaderno).
8. **Oggetti staccabili in schede separate** (telefono di Giulia, borsa a fiori, valigie, ventaglio): il personaggio non li tiene in mano.
9. **Oggetti** su sfondo neutro in vista frontale e 3/4, inquadrati interi con un margine del 10%.
10. **Coerenza tra le viste**: le viste laterali e posteriore si ottengono **modificando la prima immagine** con i prompt di modifica della scheda (stessa sessione, la prima immagine come riferimento), mai con generazioni separate da zero.
11. Risoluzione: la più alta offerta (almeno 2048 px sul lato lungo); formato 2:3 verticale per i personaggi, 1:1 per gli oggetti.
12. **Bambini**: solo personaggi immaginari generati; nessuna foto di bambini reali come riferimento.

## 5. Pipeline Blender automatica (D-31)

### 5.1 Personaggi (classe A)
| Passo | Script | Cosa fa | Controllo automatico |
|---|---|---|---|
| 1 Import | `import/import_hipoly.py` | importa il GLB high-poly, applica scala da altezza dichiarata (es. babuška 1,49 m), orienta a −Y, origine ai piedi | altezza ±1 cm; nessuna mesh staccata > 2% |
| 2 Pulizia | `retopo/clean.py` | fusione vertici, rimozione isole minuscole, chiusura buchi, separazione occhi/denti se presenti | non-manifold = 0 (dopo la chiusura) |
| 3 Ritopologia | `retopo/quadriflow.py` | QuadriFlow a 20 000 quad (40 000 tri) con densità guidata da maschere (volto ×2, mani ×1,6, piedi ×0,6), simmetria X; anelli di bordo per bocca/occhi da template | conteggio tri ≤ 40 000; distanza di Hausdorff dal high-poly ≤ 4 mm (corpo), ≤ 1,5 mm (volto) |
| 4 LOD | `retopo/lod.py` | LOD1 15 000, LOD2 5 000 (decimazione con preservazione dei bordi UV) | soglie TDD §10 |
| 5 UV | `uv/unwrap_char.py` | cuciture da template per regione (testa, busto, braccia, gambe, abiti), unwrap conformal, packing per texel density (ART §6); UV2 non serve ai personaggi | stiramento medio < 0,08; nessuna sovrapposizione |
| 6 Bake | `bake/bake_char.py` | Cycles: normal (tangent), AO, curvatura, colore (dal high-poly texturizzato), rugosità/metallicità dalle mappe PBR del generatore; correzione colore verso la palette | mappe senza buchi (pixel vuoti < 0,1%); range di roughness come ART §5 |
| 7 Scheletro | `rig/fit_metarig.py` | render frontale e laterale → rilevamento punti chiave (MediaPipe Pose + mani) → adattamento del meta-rig Rigify → generazione dello scheletro di deformazione con nomi Mixamo (D-64) | lunghezze ossa entro ±10% dalle proporzioni attese per età |
| 8 Pesi | `rig/weights.py` | pesi automatici (bone heat) + correzioni: mani rigide per falange, smoothing sui vestiti, limite 4 influenze, normalizzazione, gonne/cappotto con ossa ausiliarie | somma = 1; nessun vertice senza peso; test di deformazione (sotto) |
| 9 Volto | `rig/face.py` | 32 blend shapes (FACS ridotti) trasferite da un volto template con surface deform; visemi | nessuna intersezione labbra/denti nelle pose |
| 10 Animazioni | `anim/retarget.py` | retarget delle clip (Mixamo, Rokoko, Uthana) e delle clip specifiche (ANI-*) sullo scheletro | piedi senza scivolamento > 2 cm nelle clip sul posto |
| 11 Materiali | `export/materials.py` | PBR glTF (pelle con subsurface tramite estensioni supportate o parametri del materiale lato motore), sheen per tessuti | ≤ 3 materiali |
| 12 Export | `export/export_glb.py` + glTF-Transform | GLB, meshopt, KTX2 | validatore (TDD §10) |

### 5.2 Render di revisione (al posto del lavoro manuale)
Ogni asset genera in `review/<asset>/` immagini PNG che Claude **ispeziona visivamente** (lettura delle immagini) prima di accettarlo; Vlad le riceve come foglio di contatto per approvazione artistica, senza dover aprire Blender.
| Render | Asset | Cosa si guarda |
|---|---|---|
| Giro a 8 viste (turntable) con la luce di riferimento | tutti | forma, proporzioni, materiali, coerenza con l'immagine di partenza |
| Wireframe sovrapposto | tutti | densità, anelli del volto, poligoni degeneri |
| UV checker (scacchiera) | tutti | stiramenti e cuciture visibili |
| **Pose di deformazione** (A, T, braccia in alto, squat, seduta, torsione del busto 45°, pugno chiuso, mano aperta, corsa) | personaggi | gomiti, spalle, ginocchia, vestiti che si compenetrano |
| Primo piano delle mani (6 pose) | personaggi | dita, unghie, pollice |
| Primo piano alla distanza della camera di gioco (0,6 / 1,2 / 3 m) e con la luce della scena | tutti | dettaglio percepito, normal map, texel density |
| Volto con 8 espressioni | personaggi principali | blend shapes, rughe (babuška, Concetta) |
| Confronto affiancato con l'immagine Nano Banana | classe A | somiglianza |
Soglie numeriche automatiche aggiuntive: compenetrazioni nelle pose di deformazione < 2 mm su 99% dei vertici; volume delle articolazioni conservato ±8%. Se un asset non supera i controlli: correzione via script (parametri) fino a 3 tentativi; poi nuova scheda per Vlad con le modifiche al prompt o alla fascia.

### 5.3 Fomà e Donne
- **Fomà**: come §5.1 a 32 cm; in più `rig/beard_chain.py` (8 ossa con molle), `bake/fur_maps.py` (genera curve di pelo con Geometry Nodes guidate dalla normal del high-poly, poi baka mappe di densità, lunghezza, direzione e colore per i gusci), naso con parametro di rossore.
- **Donne**: corpo e vestito come §5.1; la **gonna sotto il ginocchio** è sostituita da una mesh di nebbia (procedurale) e il materiale ha maschere di dissolvenza dal basso (ART §11).

### 5.4 Oggetti (classe A)
Import → pulizia → decimazione a budget (15 000 eroe / 3 000 secondario) con preservazione della silhouette → UV + bake (normal, AO, curvatura, colore) → materiali → export → render di revisione (giro, wireframe, UV checker, primo piano alla distanza d'uso).

### 5.5 Architettura e Taormina (classe C)
| Passo | Script | Note |
|---|---|---|
| DEM | `taormina/dem.py` | GDAL → mesh adattiva per cella |
| OSM | `taormina/osm_import.py` | edifici estrusi, tetti per tipo, strade e scalinate scavate, muri |
| Kit facciate | `kit/build_kit.py` | moduli (pianoterra con portone, piano con finestra/balcone, cornicione, angolo, gronda) in 6 stili; regole di assegnazione |
| Edifici simbolo | `taormina/landmarks/*.py` | uno script per edificio con misure dalle foto (es. `porta_messina.py`) |
| Interni | `env/casarusso.py`, `env/aeroporto.py`, `env/bar.py`, `env/scuola.py`, `env/stazione.py` | piante di `LIVELLI.md` |
| UV2 + lightmap | `bake/lightmap.py` | UV2 automatiche (packing), bake Cycles 4 ore, denoise OIDN |
| Collisioni, navmesh sorgente | `export/collisions.py` | primitive `COL_` |
| Celle | `export/cells.py` | taglio per griglia, LOD, manifesto |
Render di revisione per cella: vista dall'alto, 4 viste a livello occhi dai punti di interesse, vista notturna, mappa delle lightmap.

### 5.6 Animazioni
Fonti in ordine di preferenza: (1) **Mixamo** (account Adobe gratuito; uso consentito nei progetti); (2) **Rokoko** (libreria gratuita con licenza indicata per clip); (3) **Uthana** (generazione da testo, verificare il piano gratuito); (4) animazione procedurale da script (sguardi, gesti piccoli, Fomà). Le clip specifiche dei personaggi (ANI-*) si ottengono combinando (1)–(4) e correggendo via script. Tutte le fonti in `CREDITI.md`.

## 6. Modelli dal web (classe B)
1. **Ricerca** (Claude): Poly Haven (CC0), ambientCG (CC0), Sketchfab con filtro «Downloadable» + licenza CC0 o CC BY, Fab (solo asset gratuiti con licenza compatibile: CC0/CC BY; la licenza standard di Fab non è CC e va segnalata).
2. **Verifica della licenza** sulla pagina del modello (screenshot non necessario: si registra licenza, autore, URL, data).
3. **Scheda per Vlad** (in `RICHIESTE_ASSET/`): titolo · autore · URL · licenza · formato da scaricare (GLB o FBX; se c'è, «Original format» per avere le texture) · dove salvarlo (`assets_in/web/<id>/`) · testo di attribuzione.
4. **Voce in `CREDITI.md`**.
5. **Rielaborazione** in Blender allo stile (materiali dalla libreria ART §5, usura, scala reale, UV2 per lightmap, LOD, validatore).
Esclusi: NC, ND, SA, «editorial use only», licenze sconosciute (D-33).

## 7. Cartella di consegna `assets_in/`
```
assets_in/
├── immagini/            REQ-CHR-xxx_fronte.png, _lato_sx.png, _lato_dx.png, _retro.png, _3q.png
├── modelli/             REQ-CHR-xxx_hitem3d.glb (o _tripo.glb), REQ-PRP-xxx_tripo.glb, NOTE.txt facoltativo
├── web/                 WEB-xxx/ (file scaricati, come sono)
├── dati/                osm/, tinitaly/, sitr_dtm/, copernicus/, foto_vlad/
├── concept/             CON-xxx_v1.png (immagini di concept da rivedere)
└── audio/               vox/VOX-CC-NN_take1.wav, voci.json
```
Regole dei nomi: l'ID della scheda all'inizio del nome, nessuno spazio, minuscole per i suffissi. Claude controlla la cartella a ogni sessione e risponde con l'esito (accettato, da rifare con motivo).

## Fonti
- [Hitem3D — scelta della risoluzione](https://www.hitem3d.ai/de/ai-faq/how-to-choose-the-model-resolution-for-hitem3d)
- [Hi3D multi-view to 3D (fal.ai) — conteggio facce 100k–2M](https://fal.ai/models/hitem3d/hi3d/multi-view-to-3d/llms.txt)
- [Hitem3D 3.0 — note d'uso (Scenario)](https://help.scenario.com/articles/6895221001-hitem3d-3-0-the-essentials)
- [Tripo — modello H3.1 (sviluppatori)](https://developers.tripo3d.com/en/models/v3-1)
- [Tripo — nodo di ritopologia (limiti quad)](https://docs.comfy.org/built-in-nodes/TripoRetopologyNode)
- [Nano Banana — guida al prompting e riferimenti multipli (Runway)](https://help.runwayml.com/hc/en-us/articles/50317213804435-Creating-images-with-Nano-Banana)
- [Blender — Rigify](https://docs.blender.org/manual/en/latest/addons/rigging/rigify/introduction.html)
- [Blender — QuadriFlow remesh](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html)
- [glTF-Transform](https://gltf-transform.dev/)
- [Poly Haven — licenza](https://polyhaven.com/license) · [ambientCG](https://ambientcg.com/) · [Sketchfab — licenze](https://sketchfab.com/licenses)
- [Mixamo — FAQ licenza](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)
