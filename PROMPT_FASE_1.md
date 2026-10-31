<!--
ISTRUZIONI PER VLAD (non copiare questo blocco)
1. Prima di aprire la sessione, prepara quanto elencato in «Cosa deve preparare Vlad» qui sotto.
2. Apri una nuova sessione di Claude Code sul repository murfivladi/casarusso (modello Opus, sforzo "high").
   La documentazione della Fase 0 è già nel repository: non serve allegare nulla.
   Se invece usi una chat senza repository, allega casarusso_fase0.zip.
3. Copia tutto il testo da "# PHASE 1 BRIEF" in giù e invialo.

COSA DEVE PREPARARE VLAD
A. Hosting (risposta a Q-04) — scrivilo nel primo messaggio:
   - Apache o Nginx? Accesso SSH o solo SFTP/FTP? Indirizzo e cartella dove va il sito (es. https://tuodominio.it/casarusso/).
   - Le credenziali NON vanno in chat: inseriscile come "secrets" del repository su GitHub
     (Settings → Secrets and variables → Actions): DEPLOY_HOST, DEPLOY_USER, DEPLOY_KEY (chiave SSH privata) o DEPLOY_PASSWORD, DEPLOY_PATH.
B. I tre asset della Fase 1 (guida: docs/RICHIESTE_ASSET/00_come_usare.md), caricati nel repository in assets_in/:
   - REQ-PRP-001 lapot' (immagini + modello 1,5 M)
   - REQ-CHR-010 babuška col cappotto (4 viste + modello 1,5 M)
   - REQ-CHR-070 Fomà (4 viste + modello 1,5 M)
C. Dati di Taormina per UNA cella di prova (il centro, Piazza IX Aprile):
   - OpenStreetMap: dal sito openstreetmap.org → «Esporta» → riquadro 15.2830–15.2900 E / 37.8500–37.8545 N → file .osm
   - TINITALY: la tessera che contiene Taormina (GeoTIFF)
   - DTM 1 m della Regione Siciliana: le tessere del centro di Taormina (se il geoportale le fornisce)
   Mettili in assets_in/dati/ (osm/, tinitaly/, sitr_dtm/).
D. Facoltativo: la risposta a Q-06 (chi rivede il russo) e a Q-12 (aspetto di Vera).
Se B o C non sono pronti, la sessione parte lo stesso: costruisce tutto il resto con modelli di prova
e si ferma solo sugli ultimi collaudi, dicendoti cosa manca.
-->

# PHASE 1 BRIEF — «Casa Russo — Il domovoj nella scarpa»

## 0. Who you are and what this session is
You are the combined **technical director, pipeline engineer and lead developer** of a private, non-commercial 3D first-person browser game based on the Italian children's book *Il domovoj nella scarpa*. The project owner is **Vlad**.
Phase 0 is done: the complete documentation is in `docs/` of this repository (start from `docs/README.md`). In this session you run **Phase 1 — "Pre-produzione tecnica e pipeline"** of `docs/FASI_DI_SVILUPPO.md`, as amended by `docs/REGISTRO_DECISIONI.md` §5.
Goal: **the assembly line**. One command must take an asset from Blender to the game in the browser, always the same way, with no manual steps — and with Vlad doing no Blender work at all (D-31).

## 1. Language and rules
- Everything you write for Vlad (messages, docs, code comments, commit messages) is in **Italian**. Image/voice prompts stay in English with an Italian «In breve».
- Read first, completely: `docs/README.md`, `docs/REGISTRO_DECISIONI.md`, `docs/TDD.md`, `docs/PIPELINE_ASSET.md`, `docs/LIVELLI.md` §1 and §10, `docs/DATI_TAORMINA.md`, `docs/ART_BIBLE.md` §5–§6 and §8–§11, `docs/DOMANDE_APERTE.md`.
- The decisions in `REGISTRO_DECISIONI.md` are binding. A new decision gets a new D-number there before it is used. Doubts: reasoned default + entry in `DOMANDE_APERTE.md`; ask Vlad only for things only he can provide (hosting, credentials, assets).
- The three project rules stay: everything at maximum (no permanent placeholders), Blender for all 3D, Babylon.js used to its full potential.
- Work on the branch given by the session; commit often with clear Italian messages; push.

## 2. Environment notes (verified at the end of Phase 0)
- `bpy` 5.2.3 (Blender 5.2 LTS as a Python module) installs from PyPI on Python 3.13 in this cloud sandbox: use it for headless Blender (`pip install bpy==5.2.3`). Cycles runs on CPU here; heavy bakes must be written so the same script runs later on a GPU machine (Q-21).
- npm and PyPI are reachable; arbitrary websites are not. Never work around a blocked site; ask Vlad to download and commit the file.
- Large binaries go through **Git LFS** (`.blend`, source textures, `assets_in/**`, audio). Watch GitHub LFS quotas: keep only what is needed.
- Chromium + Playwright are preinstalled (`require('playwright')` works; do not reinstall browsers).

## 3. Work to do
1. **Repository structure** exactly as `TDD.md` §1, Git LFS rules, `.gitattributes`, naming rules (`TDD.md` §8), `.gitignore`.
2. **Game project**: Vite + TypeScript + Babylon.js 9.x pinned per D-59 (latest patch published ≥ 14 days ago), Havok, Navigation Plugin V2, inkjs. Engine bootstrap with **WebGPU → WebGL2 fallback** (`TDD.md` §3, §7.1), presets and automatic preset selection (`TDD.md` §12.3–§12.4), the debug console skeleton `window.cr` with `vai`, `stato`, `perf`, `preset`, `teletrasporta`, `navmesh`, `celle` (`TDD.md` §11).
3. **Rendering decision (Q-10)**: build the test scene on Babylon 9 Frame Graph v1 and on the classic pipelines; measure; record the decision as a new D-number.
4. **Blender pipeline (headless Python)** per `PIPELINE_ASSET.md` §5:
   - characters: import high-poly → cleanup → QuadriFlow retopology to 40 000 tri + LODs → UV → Cycles bake (normal, AO, curvature, colour, roughness) → Rigify metarig fitted from landmarks → Mixamo-compatible skeleton → automatic weights + scripted cleanup → face blend shapes → retarget → materials → export;
   - props: import → cleanup → decimation → UV → bake → export;
   - lightmaps: UV2, Cycles bake for 4 reference hours, RGBD;
   - collisions `COL_`, points `CP_`, `FOT_`, `KNE_`, `CRC_`;
   - export `.glb` with **EXT_meshopt_compression** and **KTX2** (UASTC/ETC1S per `TDD.md` §8) via glTF-Transform.
5. **Review renders** (`PIPELINE_ASSET.md` §5.2) generated automatically for every asset; you inspect them yourself (read the PNGs) before accepting, and send Vlad a contact sheet for artistic approval.
6. **Asset validator** with the exact thresholds of `TDD.md` §10; it blocks the export and runs in CI.
7. **Taormina 1:1 pipeline**: DEM reprojection (GDAL) to EPSG:25833, terrain per 128 m cell, OSM buildings extruded on the terrain, stairways cut into the terrain, cell slicing with 3 LODs, manifest (`TDD.md` §6.1). Prepare also the viewshed script for Casa Russo (`DATI_TAORMINA.md` §6) even if it runs in Phase 4.
8. **Streaming**: manifest loader, load/unload by distance with hysteresis, distributed GPU upload, memory budgets, service worker cache (`TDD.md` §6.2).
9. **Hosting and deploy** to Vlad's own server (D-44, D-70, `TDD.md` §13): GitHub Actions job using the repository secrets, Apache `.htaccess` and Nginx config (MIME types for wasm/glb/ktx2, Brotli/gzip, immutable caching, `noindex`), HTTPS required.
10. **CI**: lint, typecheck, unit tests, validator, docs checks (`work/strumenti/autoverifica.py`, `verifica_libro.py`), build, Playwright smoke test, FPS measurement on the test scene.
11. **Update `docs/FASI_DI_SVILUPPO.md`** with every change listed in `REGISTRO_DECISIONI.md` §5, and keep all docs consistent with what you build.

## 4. Deliverables (Phase 1 exit criteria)
- The **lapot'** (REQ-PRP-001) and a **test room** (the Casa Russo kitchen from `LIVELLI.md` §3.3, procedural, with baked lightmaps) go Blender → validator → compressed `.glb` → Babylon → published site, **with one command**.
- The **babuška** (REQ-CHR-010) arrives in game rigged, with at least idle, walk, talk, nod, head-shake animations, passing all automatic checks and review renders.
- **Fomà fur prototype** (shell fur + beard bone chain) running within budget (`TDD.md` §12.2).
- One **real Taormina cell** (Piazza IX Aprile) loaded and unloaded by streaming.
- Pipeline repeatable with **no manual steps** for Vlad; CI green; site deployed.
- Test scene performance within budget on the reference PC class and on Vlad's iPad 11th gen (Vlad measures with `?perf=1` and sends the JSON).
- Updated docs: `TDD.md` (versions pinned, rendering decision), `PIPELINE_ASSET.md` (real script names), `DOMANDE_APERTE.md`, `README.md` (Phase 1 gate table).

If an asset or data file from Vlad is missing, build and test everything with a clearly named temporary test asset kept **only** in `tests/fixtures/` (never in `assets/`), list exactly what is missing, and finish the rest.

## 5. Delivery
At the end: send Vlad (with `SendUserFile`) the updated `docs/README.md`, the contact sheets of the review renders, and the link to the deployed site. Final message in Italian, short: what works, the Phase 1 gate status, what Vlad must do next (approve renders, measure on iPad, prepare Phase 2/3 assets), and the next step: Phase 2 (First Playable) in a new session.
