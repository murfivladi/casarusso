# Schede di richiesta — Oggetti del capitolo 1

Oggetti eroe e organici (classe A, immagine → 3D) e modelli dal web per gli oggetti generici (classe B). Gli oggetti geometrici semplici sono procedurali (classe C) e non hanno scheda: carrello portabagagli, transenne, tabellone arrivi, colonne, sedute metalliche dell'atrio, macchinine a gettoni, cassa automatica del parcheggio, pensiline fotovoltaiche, palme (Geometry Nodes), segnaletica stradale italiana, guard-rail e oleandri dell'A18.

## Riepilogo

| Scheda | Oggetto | Fascia | Fase |
|---|---|---|---|
| REQ-PRP-001 | Lapot' | 1,5 M | 1 + 3 |
| REQ-PRP-002 | Borsa a fiori | 1,0 M | 3 |
| REQ-PRP-003…005 | Tre valigie con lo spago | 1,0 M | 3 |
| REQ-PRP-006 | Cartello di Mattia | 0,5 M | 3 |
| REQ-PRP-007 | Telefono di Giulia | 0,5 M | 3 |
| REQ-PRP-008 | Telefono di Vera | 1,0 M | 2 |
| REQ-PRP-009 | Valigia a fiori del prete | 0,5 M | 3 |
| REQ-PRP-010 | Quaderno di scienze | 1,5 M | 2 |
| REQ-PRP-011 | Coniglio di pezza | 1,0 M | 3 |
| REQ-PRP-012 | Zainetto di Mattia | 0,5 M | 3 |
| REQ-PRP-013 | Monovolume grigia (esterno) | 1,0 M | 3 |
| REQ-PRP-014 | Auto generica di sfondo (taxi bianco e varianti) | 0,5 M | 3 |
| WEB-001…010 | Oggetti generici (Poly Haven, CC0) | — | 3 |

## Oggetti da immagine (classe A)


### REQ-PRP-001 — Il lapot' (scarpa di corteccia)
- **A cosa serve e in quali capitoli**: capp. 1–14: oggetto eroe (borsa, rito, dietro il frigo, stazione).
- **Priorità (fase in cui serve)**: Fase 1 (prova pipeline) e Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,5 M** — tenuto in mano e visto a 30–50 cm (cap. 11), fibre intrecciate da trasferire in normal map.
- **Prompt Nano Banana principale (EN)**:
  > An old Russian bast shoe (lapot) woven from strips of light-coloured linden bark, traditional criss-cross weave, low sides, a few bark cords at the heel, the toe visibly worn, darker and frayed, aged and slightly dusty, about 27 cm long. Seen from the side-front. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-001_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-001_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 15.000 tri; texture 2.048 (4.096 su Ultra).
- **Controlli automatici**: lunghezza 27 cm ±0,5; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Il lapot' (scarpa di corteccia). Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,5 M di facce.

### REQ-PRP-002 — La borsa a fiori
- **A cosa serve e in quali capitoli**: cap. 1 (sotto il braccio della babuška), cap. 2 (rito).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — vista a distanza di conversazione e da vicino nello starnuto.
- **Prompt Nano Banana principale (EN)**:
  > A soft cloth shopping tote bag with a dense floral print (red roses and small blue flowers on a dark background), two fabric handles, slightly worn, partly open at the top, with the worn toe of a bark shoe peeking out of the opening. Size about 40 × 35 cm. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-002_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-002_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 8.000 tri + simulazione di stoffa leggera.
- **Controlli automatici**: larghezza 40 cm ±1; il lapot' dentro viene sostituito da REQ-PRP-001 in Blender; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: La borsa a fiori. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-003 — Valigia grande con lo spago
- **A cosa serve e in quali capitoli**: cap. 1 (carrello), cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — in primo piano sul carrello all'arrivo.
- **Prompt Nano Banana principale (EN)**:
  > An old large hard-shell suitcase from the 1990s, faded brown with scuffed corners, tied around twice with thick natural hemp string knotted on top, 75 × 50 × 28 cm, lying flat. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-003_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-003_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 6.000 tri.
- **Controlli automatici**: 75 cm ±1; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Valigia grande con lo spago. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-004 — Valigia media con lo spago
- **A cosa serve e in quali capitoli**: cap. 1, cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — come sopra.
- **Prompt Nano Banana principale (EN)**:
  > An old medium soft fabric suitcase, dark green-grey with zip and side straps, tied once around with thick natural hemp string, 62 × 42 × 24 cm, lying flat. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-004_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-004_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 5.000 tri.
- **Controlli automatici**: 62 cm ±1; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Valigia media con lo spago. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-005 — Valigia piccola con lo spago (la terza, coi barattoli)
- **A cosa serve e in quali capitoli**: cap. 1, cap. 2 (escono i pirožki), MIS-S-03.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — si apre al cap. 2 e nella missione.
- **Prompt Nano Banana principale (EN)**:
  > An old small brown leather-look suitcase with two metal clasps and a worn handle, tied crosswise with thick natural hemp string, 50 × 35 × 20 cm, lying flat. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-005_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-005_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 5.000 tri (coperchio separato).
- **Controlli automatici**: 50 cm ±1; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Valigia piccola con lo spago (la terza, coi barattoli). Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-006 — Cartello di Mattia «BABUŠKA GALINA»
- **A cosa serve e in quali capitoli**: cap. 1 (in mano a Irina), SEG-16.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — oggetto piatto letto a 1–3 m.
- **Prompt Nano Banana principale (EN)**:
  > A hand-made cardboard sign, 50 × 35 cm, slightly bent, written in uneven children's block letters with a blue marker: BABUŠKA GALINA, and below a child's drawing of a bear that looks like a potato with ears, coloured with brown and yellow crayons. Front view, flat. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-006_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-006_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 200 tri + texture 2.048.
- **Controlli automatici**: testo leggibile «BABUŠKA GALINA»; Claude ridisegna la scritta in texture se Nano Banana sbaglia le lettere; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Cartello di Mattia «BABUŠKA GALINA». Foto dell'oggetto su fondo grigio, poi le viste per modifica; 0,5 M di facce.

### REQ-PRP-007 — Telefono di Giulia
- **A cosa serve e in quali capitoli**: cap. 1 (in mano), capp. 7, 10–11.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — piccolo, superfici lisce.
- **Prompt Nano Banana principale (EN)**:
  > A modern smartphone with no logo, black, in a translucent purple silicone case with small glitter, a slightly cracked screen protector corner, screen off. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-007_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-007_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 2.000 tri.
- **Controlli automatici**: dimensioni 15 × 7,2 cm; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Telefono di Giulia. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 0,5 M di facce.

### REQ-PRP-008 — Telefono di Vera (fotocamera, torcia, orologio)
- **A cosa serve e in quali capitoli**: tutto il gioco, in prima persona.
- **Priorità (fase in cui serve)**: Fase 2.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — sempre in mano davanti alla camera.
- **Prompt Nano Banana principale (EN)**:
  > A modern smartphone with no logo, in a matte navy-blue silicone case, slightly worn edges, screen off, back camera module with two lenses and a flash. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *lato*: «Using the attached image as the exact reference, show the SAME object from the side (90 degrees), same lighting and background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-008_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-008_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 4.000 tri + schermo come superficie di rendering.
- **Controlli automatici**: dimensioni 14,7 × 7,1 cm; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Telefono di Vera (fotocamera, torcia, orologio). Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-009 — Valigia a fiori del prete
- **A cosa serve e in quali capitoli**: cap. 1 (porta degli arrivi).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — passa a 2–4 m.
- **Prompt Nano Banana principale (EN)**:
  > A hard-shell wheeled cabin suitcase with a cheerful pink and white floral pattern, telescopic handle extended, 55 × 40 × 20 cm, standing upright. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-009_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-009_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 3.000 tri.
- **Controlli automatici**: 55 cm ±1; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Valigia a fiori del prete. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 0,5 M di facce.

### REQ-PRP-010 — Quaderno di scienze di Vera (chiuso)
- **A cosa serve e in quali capitoli**: tutto il gioco (quaderno in primo piano).
- **Priorità (fase in cui serve)**: Fase 2.
- **Fascia poligoni Tripo/Hitem3D**: **1,5 M** — sempre in primo piano a 38 cm; bordi delle pagine e copertina da vicino.
- **Prompt Nano Banana principale (EN)**:
  > A used A5 school notebook with a hard sage-green cover, slightly rounded and worn corners, a white rectangular label on the cover with handwritten blue-pen text «SCIENZE — Vera Russo — 1ªB», the pages' edges a bit wavy, closed, lying flat, seen from above at 30 degrees. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-010_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-010_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 6.000 tri + pagine procedurali.
- **Controlli automatici**: formato A5 (21 × 14,8 cm); triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Quaderno di scienze di Vera (chiuso). Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,5 M di facce.

### REQ-PRP-011 — Coniglio di pezza di Mattia
- **A cosa serve e in quali capitoli**: capp. 1 (nello zaino), 9, 10, 14.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — in braccio a Mattia in primi piani.
- **Prompt Nano Banana principale (EN)**:
  > An old floppy plush rabbit toy, faded light grey with a pink fabric inner ear, long ears, button eyes, one ear slightly torn and sewn back, sitting. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-011_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-011_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 4.000 tri.
- **Controlli automatici**: altezza 30 cm; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Coniglio di pezza di Mattia. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-012 — Zainetto di Mattia
- **A cosa serve e in quali capitoli**: cap. 1, cap. 10 (con il coniglio).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — a 1–2 m.
- **Prompt Nano Banana principale (EN)**:
  > A small children's backpack in red fabric with a front pocket and grey straps, partially open zip, no logo. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-012_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-012_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 2.500 tri.
- **Controlli automatici**: altezza 30 cm; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Zainetto di Mattia. Foto dell'oggetto su fondo grigio, poi le viste per modifica; 0,5 M di facce.

### REQ-PRP-013 — Monovolume grigia con l'ammaccatura (esterno)
- **A cosa serve e in quali capitoli**: cap. 1 (parcheggio), cap. 2 (arrivo in Via Circonvallazione).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — vista da vicino al parcheggio; interni procedurali separati.
- **Prompt Nano Banana principale (EN)**:
  > A generic seven-seat European minivan from about 2015, silver-grey metallic, no brand badges or logos, clean but used, a visible small dent on the rear right side door, side view. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. No text or logos unless described. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**:
  - *3/4*: «Using the attached image as the exact reference, show the SAME object rotated 45 degrees (three-quarter view from slightly above, 20 degrees), same lighting and plain light grey background, entire object visible. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME object from the back, same lighting and plain light grey background, entire object visible. Change nothing else.»
- **Formato e proporzioni**: PNG, lato ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D (immagine singola o multi-vista): risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Per oggetti rigidi è consigliato Tripo.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-013_fronte.png` (+ `_3q.png`, `_retro.png`, `_lato.png`); modello `assets_in/modelli/REQ-PRP-013_tripo.glb` (o `_hitem3d.glb`).
- **Cosa farà Claude dopo**: pulizia, decimazione con silhouette, UV, bake (normal, AO, curvatura, colore), materiali PBR, usura secondo ART_BIBLE, export GLB meshopt + KTX2, render di revisione.
- **Budget finale in gioco**: 35.000 tri (esterno) + interni procedurali 25.000.
- **Controlli automatici**: lunghezza 4,6 m ±5 cm; triangoli entro budget; validatore TDD §10; render di revisione.
- **Controlla l'immagine**: un solo oggetto intero; sfondo grigio uniforme; nessun marchio; materiali leggibili.
- **In breve**: Monovolume grigia con l'ammaccatura (esterno). Foto dell'oggetto su fondo grigio, poi le viste per modifica; 1,0 M di facce.

### REQ-PRP-014 — Auto generica di sfondo
- **A cosa serve e in quali capitoli**: taxi bianchi in fila al parcheggio (cap. 1), traffico in tangenziale e A18 (cap. 1), auto in Via Circonvallazione (capp. 2+); colori e varianti via script.
- **Priorità**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — vista a media/lunga distanza.
- **Prompt Nano Banana principale (EN)**:
  > A generic compact European five-door hatchback from about 2018, plain white paint, no brand badges, no logos, no number plates, clean, side view. Product photograph of a single object, centered with 10% margin, front view, camera at the object's mid height, 100mm lens. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no reflections of the studio, no depth of field, sharp focus everywhere, realistic photographic style, detailed materials. Nothing else in the frame. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**: *3/4*: «Using the attached image as the exact reference, show the SAME car rotated 45 degrees (three-quarter front view from slightly above), same lighting and background. Change nothing else.» · *retro*: «Using the attached image as the exact reference, show the SAME car from the back, same lighting and background. Change nothing else.»
- **Formato**: PNG ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Tripo H3.1, limite facce 500.000, texture PBR sì, quad no, GLB.
- **Nome file e cartella**: `assets_in/immagini/REQ-PRP-014_fronte.png` (+ `_3q.png`, `_retro.png`); `assets_in/modelli/REQ-PRP-014_tripo.glb`.
- **Cosa farà Claude dopo**: decimazione, separazione ruote e vetri, UV, bake, materiali (vernice con clearcoat, vetri), 6 varianti di colore e il taxi (insegna generica «TAXI»), LOD.
- **Budget finale in gioco**: LOD0 12.000, LOD1 3.000, LOD2 600 tri.
- **Controlli automatici**: lunghezza 4,1 m ±5 cm; validatore; render di revisione.
- **Controlla l'immagine**: nessun logo o stemma; ruote intere; sfondo uniforme.
- **In breve**: un'auto bianca qualsiasi, senza marchi, per il traffico e i taxi.

## Modelli dal web (classe B) — tutti Poly Haven, licenza CC0

Istruzioni per Vlad: aprire il link, scegliere **formato glTF** (o «Blend» se il glTF non c'è) e risoluzione **2K**, scaricare lo ZIP e scompattarlo in `assets_in/web/<ID>/`. Nessuna attribuzione obbligatoria (CC0); i crediti li riportiamo comunque in `CREDITI.md`.

| ID | Oggetto | Link | Uso nel cap. 1 | Rielaborazione di Claude |
|---|---|---|---|---|
| WEB-001 | Wet Floor Sign 01 | [polyhaven.com/a/WetFloorSign_01](https://polyhaven.com/a/WetFloorSign_01) | cartello «pavimento bagnato» nell'atrio | testo in italiano/inglese generico, usura |
| WEB-002 | Bar Chair Round 01 | [polyhaven.com/a/bar_chair_round_01](https://polyhaven.com/a/bar_chair_round_01) | sgabelli del bar degli arrivi | materiali acciaio spazzolato, LOD |
| WEB-003 | Cash Register 01 | [polyhaven.com/a/CashRegister_01](https://polyhaven.com/a/CashRegister_01) | cassa del bar (stile da rendere moderno) | rimodellazione del display via script, materiali |
| WEB-004 | Modular Street Seating | [polyhaven.com/a/modular_street_seating](https://polyhaven.com/a/modular_street_seating) | panche esterne davanti al terminal | colori della palette, UV2 |
| WEB-005 | Metal Trash Can | [polyhaven.com/a/metal_trash_can](https://polyhaven.com/a/metal_trash_can) | cestini (atrio e parcheggio) | differenziata con adesivi generici |
| WEB-006 | Security Camera 01 | [polyhaven.com/a/security_camera_01](https://polyhaven.com/a/security_camera_01) | telecamere sul soffitto dell'atrio | — |
| WEB-007 | Potted Plant 02 | [polyhaven.com/a/potted_plant_02](https://polyhaven.com/a/potted_plant_02) | piante in vaso dell'atrio | vaso ridisegnato |
| WEB-008 | Street Lamp 01 | [polyhaven.com/a/street_lamp_01](https://polyhaven.com/a/street_lamp_01) | lampioni del parcheggio | altezza 8 m, luce LED |
| WEB-009 | Concrete Road Barrier | [polyhaven.com/a/concrete_road_barrier](https://polyhaven.com/a/concrete_road_barrier) | barriere del parcheggio e dei cantieri | strisce bianche/rosse |
| WEB-010 | Croissant | [polyhaven.com/a/croissant](https://polyhaven.com/a/croissant) | cornetti nella vetrina del bar (anche bar di papà) | glassa e varianti |

## Fonti
- `PIPELINE_ASSET.md` §3–§6; `LIVELLI.md` §2.
- [Poly Haven — licenza CC0](https://polyhaven.com/license) · [Poly Haven API (elenco modelli)](https://api.polyhaven.com/assets?t=models)
- [Tripo H3.1](https://developers.tripo3d.com/en/models/v3-1)
