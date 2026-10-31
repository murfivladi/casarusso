# Schede di richiesta — Personaggi della v1.0 (capitoli 1–3)

Protocollo D-32 (immagine Nano Banana → Tripo/Hitem3D → Blender automatico). Regole delle immagini: `PIPELINE_ASSET.md` §4. Istruzioni passo passo: `00_come_usare.md`.
Per decisione D-39 **tutti** i personaggi si rigenerano, compresi i cinque modelli «pronti» del vecchio documento di gioco.
I personaggi con più abiti hanno una scheda per abito: la **prima** scheda di ogni personaggio fissa il viso; le successive allegano la sua immagine frontale come riferimento.
Vera serve per i riflessi, le foto e le braccia in prima persona.

## Riepilogo

| Scheda | Personaggio | Fascia | Fase |
|---|---|---|---|
| REQ-CHR-001…003 | Vera (cap. 1, pigiama, scuola) | 1,0 M | 3 / 4 / 4 |
| REQ-CHR-010…012 | Babuška (cappotto, casa, camicia da notte) | 1,5 M / 1,0 M / 1,0 M | 1+3 / 4 / 4 |
| REQ-CHR-020…021 | Irina | 1,0 M | 3 / 4 |
| REQ-CHR-030…031 | Salvo | 1,0 M | 3 / 4 |
| REQ-CHR-040…041 | Giulia | 1,0 M | 3 / 4 |
| REQ-CHR-050…051 | Mattia | 1,0 M | 3 / 4 |
| REQ-CHR-060 | Nonna Concetta | 1,0 M | 4 |
| REQ-CHR-070 | Fomà | 1,5 M | 1+4 |
| REQ-CHR-080…082 | Donna Rosalia, Donna Nina, Donna Tina | 1,0 M | 4 |
| REQ-CHR-090…092 | Nicolò, prof.ssa di matematica, prof. di musica | 1,0 M / 0,5 M / 0,5 M | 4 |
| REQ-CHR-100…110 | comparse dell'aeroporto | 0,5 M | 3 |
| REQ-CHR-120…125 | comparse di scalinata, scuola, bar, Corso | 0,5 M | 4 |
| REQ-CHR-130…132 | gatti | 0,5 M | 4 |


### REQ-CHR-001 — Vera Russo — abiti del cap. 1
- **A cosa serve e in quali capitoli**: riflessi (finestrini, specchi), foto di famiglia, mani in prima persona (si ricavano dal modello); cap. 1.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — non si vede quasi mai da vicino in viso, ma le mani e gli avambracci sono sempre in campo: servono buon dettaglio a distanza di conversazione.
- **Prompt Nano Banana principale (EN)**:
  > A 12-year-old Italian-Russian girl, slim, 152 cm tall, light-brown hair to the shoulder blades in a low ponytail with a blue elastic and loose strands, grey eyes, light olive skin with a few freckles, short nails. She wears a white T-shirt with thin blue stripes, short denim overalls, white sneakers, a red-and-blue string bracelet on her left wrist. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-001_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-001_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri (LOD 15.000 / 5.000); braccia in prima persona come mesh separata da 12.000 tri.
- **Controlli automatici**: altezza 152 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 152 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Vera Russo — abiti del cap. 1. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-002 — Vera Russo — pigiama (notte)
- **A cosa serve e in quali capitoli**: scene notturne dei capp. 2–3 (riflessi, piedi nudi, mani).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — stesso motivo della scheda 001.
- **Prompt Nano Banana principale (EN)**:
  > The same 12-year-old girl (light-brown hair in a loose low ponytail, grey eyes), wearing light-blue cotton pyjamas with a small star print, long trousers, barefoot, red-and-blue string bracelet. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare a Nano Banana l'immagine frontale di REQ-CHR-001 come riferimento del viso e scrivere prima del prompt: «Same girl as the reference image, same face and hair.»
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-002_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-002_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 152 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 152 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Vera Russo — pigiama (notte). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-003 — Vera Russo — scuola e casa (settembre)
- **A cosa serve e in quali capitoli**: riflessi e foto nei capp. 3 e mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — stesso motivo.
- **Prompt Nano Banana principale (EN)**:
  > The same 12-year-old girl, wearing an open navy-blue zip hoodie over a plain white T-shirt, blue jeans, white sneakers, red-and-blue string bracelet. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-001 come riferimento del viso (come sopra).
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-003_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-003_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 152 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 152 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Vera Russo — scuola e casa (settembre). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-010 — Babuška Galina — cappotto verde (cap. 1)
- **A cosa serve e in quali capitoli**: cap. 1 (arrivo, abbraccio, primo piano lento sugli occhi SCN-01-13), cap. 2 (arrivo).
- **Priorità (fase in cui serve)**: Fase 1 (prova pipeline) e Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,5 M** — primo piano lento sugli occhi e sulle rughe: servono pori, pieghe intorno agli occhi e trama della lana.
- **Prompt Nano Banana principale (EN)**:
  > A small 74-year-old Russian grandmother from Saint Petersburg, 149 cm, slightly rounded shoulders, round face with high cheekbones, pale skin with fine wrinkles, very light grey eyes with many wrinkles around them, silver hair in a low bun. She wears a knee-length dark bottle-green wool coat, 1980s cut with large buttons, buttoned, a cream wool headscarf with small red and blue flowers tied under the chin, a grey skirt below the knee, skin-colour tights, low black shoes. Strong, knotty hands, a worn rose-gold wedding band on the right ring finger. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-010_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-010_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri; testa 4.096 px su Ultra.
- **Controlli automatici**: altezza 149 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 149 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Babuška Galina — cappotto verde (cap. 1). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,5 M di facce.

### REQ-CHR-011 — Babuška Galina — vestito di casa e grembiule
- **A cosa serve e in quali capitoli**: capp. 2–3 a cena e in casa; mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione a tavola, nessun primo piano estremo.
- **Prompt Nano Banana principale (EN)**:
  > The same grandmother (same face, silver bun, no headscarf), wearing a simple cotton dress with tiny dark-blue flowers, sleeves to the elbow, and a faded linen apron, beige slippers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-010 come riferimento del viso.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-011_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-011_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 149 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 149 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Babuška Galina — vestito di casa e grembiule. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-012 — Babuška Galina — camicia da notte (cap. 2)
- **A cosa serve e in quali capitoli**: cap. 2, il rito (scalza, con la borsa a fiori in mano: la borsa è un oggetto separato).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — scena guidata a 3–4 m, luce del lampione.
- **Prompt Nano Banana principale (EN)**:
  > The same grandmother (same face), silver hair loose in a thin braid over one shoulder, wearing a long white cotton nightgown with long sleeves, barefoot. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-010 come riferimento del viso.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-012_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-012_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 149 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 149 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Babuška Galina — camicia da notte (cap. 2). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-020 — Irina Russo — cap. 1
- **A cosa serve e in quali capitoli**: cap. 1 (cartello, corre incontro alla madre), cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > A 41-year-old Russian woman living in Sicily, 168 cm, slender, oval face with high cheekbones, blue-grey eyes, ash-blond shoulder-length hair held back with a claw clip, no make-up except mascara. She wears a white linen shirt with rolled sleeves, navy straight trousers, flat sandals, a thin watch, a small crossbody bag. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: La borsa a tracolla resta sul modello (non è un oggetto di scena).
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-020_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-020_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 168 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 168 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Irina Russo — cap. 1. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-021 — Irina Russo — casa (sera)
- **A cosa serve e in quali capitoli**: capp. 2–3, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > The same woman (same face and hair), wearing a soft grey knit sweater, dark leggings, home slippers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-020 come riferimento.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-021_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-021_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 168 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 168 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Irina Russo — casa (sera). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-030 — Salvo Russo — cap. 1
- **A cosa serve e in quali capitoli**: cap. 1 (cammina nervoso, guida), cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > A 44-year-old Sicilian man, 178 cm, sturdy with a slight belly, dark brown eyes, short curly black hair with grey temples, two-day stubble, tanned. He wears a dark-blue polo shirt, jeans, brown loafers, a steel watch. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-030_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-030_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 178 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 178 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Salvo Russo — cap. 1. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-031 — Salvo Russo — al bar
- **A cosa serve e in quali capitoli**: cap. 3 (bar), mondo libero (bar).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione e bancone.
- **Prompt Nano Banana principale (EN)**:
  > The same man (same face), wearing a white shirt with sleeves rolled up and a long black waist apron without any writing, black trousers, black shoes. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-030.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-031_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-031_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 178 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 178 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Salvo Russo — al bar. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-040 — Giulia Russo — cap. 1
- **A cosa serve e in quali capitoli**: cap. 1 (colonna, telefono), cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione; il telefono è un oggetto separato (REQ-PRP-007).
- **Prompt Nano Banana principale (EN)**:
  > A 16-year-old Sicilian girl, 165 cm, slim, brown eyes, long straight dark hair with a centre parting, thin eyeliner, chipped navy nail polish. She wears an oversized grey hoodie, denim shorts, black high-top sneakers, large black over-ear headphones around her neck. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-040_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-040_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 165 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 165 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Giulia Russo — cap. 1. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-041 — Giulia Russo — casa
- **A cosa serve e in quali capitoli**: capp. 2–3, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > The same teenage girl (same face and hair), wearing a loose black T-shirt and grey sweatpants, white socks. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-040.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-041_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-041_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 165 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 165 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Giulia Russo — casa. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-050 — Mattia Russo — cap. 1
- **A cosa serve e in quali capitoli**: cap. 1 (saltella, il signore, il parcheggio), cap. 2.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione con camera abbassata; personaggio molto animato.
- **Prompt Nano Banana principale (EN)**:
  > An imaginary 6-year-old boy, 116 cm, skinny with scraped knees, grey eyes, messy light-brown hair with a cowlick, one missing front baby tooth (mouth closed so it is not visible). He wears a green T-shirt with a printed cartoon dinosaur (generic, no brand), shorts, velcro sandals, a crooked blue baseball cap. A small backpack is NOT included (separate object). Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-050_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-050_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 116 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 116 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Mattia Russo — cap. 1. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-051 — Mattia Russo — pigiama
- **A cosa serve e in quali capitoli**: capp. 2–3 (dorme), 9, 14.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > The same boy (same face), no cap, wearing striped cotton pyjamas (white and light blue), barefoot. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Allegare REQ-CHR-050.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-051_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-051_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 116 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 116 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Mattia Russo — pigiama. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-060 — Nonna Concetta — giorno
- **A cosa serve e in quali capitoli**: cap. 2 (arancini al portone), cap. 4–5, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione.
- **Prompt Nano Banana principale (EN)**:
  > A 71-year-old Sicilian grandmother, 146 cm plus teased bouffant hair (total 150 cm), round and energetic, lively black eyes, coppery-brown dyed teased hair, coral earrings, a few rings. She wears a dark floral dress below the knee with a navy cardigan, low-heeled black shoes. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-060_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-060_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 150 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 150 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Nonna Concetta — giorno. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-070 — Fomà, il domovoj
- **A cosa serve e in quali capitoli**: capp. 2–3 (e tutto il gioco); cap. 1 solo occhi.
- **Priorità (fase in cui serve)**: Fase 1 (prova pelo) e Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,5 M** — creatura eroe vista da vicino, pelo e barba con dettaglio fine da trasferire in normal map e mappe del pelo.
- **Prompt Nano Banana principale (EN)**:
  > A tiny ancient Russian house spirit (domovoi), only 32 cm tall like a 1.5-litre water bottle, an old man with an almost cat-like face: big round red shiny nose, furry cheeks, small shiny jet-black eyes, wild messy grey hair, a very long grey beard reaching the floor and trailing behind like a train, the whole body covered in soft grey tabby fur like an old cat, small furry hands with long yellowish nails, bare furry feet. He wears a rough brick-red linen peasant shirt with white embroidery at the collar, belted with a simple rope. Photographed as a realistic creature (not a cartoon), standing upright in A-pose. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Il prompt dice «32 cm»; nell'immagine non c'è nulla per la scala, va bene. Se la barba copre i piedi nella vista frontale, chiedere in modifica: «Same character, beard tucked to one side so both feet are visible».
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-070_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-070_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri + gusci di pelo; barba a ciocche su 8 ossa.
- **Controlli automatici**: altezza 32 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 32 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Fomà, il domovoj. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,5 M di facce.

### REQ-CHR-080 — Donna Rosalia (Donne di Fora)
- **A cosa serve e in quali capitoli**: cap. 3 (e capp. 4, 8, 12, 13, notti libere).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione notturna; il vestito sarà reso semitrasparente e la gonna sotto il ginocchio diventa nebbia.
- **Prompt Nano Banana principale (EN)**:
  > A tall elegant Sicilian noblewoman of indeterminate age (looks 45), 178 cm, beautiful severe face like the statues of saints in Sicilian processions, black shiny eyes, dark hair gathered high with a tortoiseshell comb, thin gold bracelets on both wrists. She wears a long wine-red (#6E2433) late-19th-century gown with a fitted bodice and narrow waist. Arms in A-pose, hands empty (the lace fan is a separate object). Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Il ventaglio è REQ-PRP-020 (scheda futura nella Fase 4).
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-080_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-080_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 178 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 178 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Donna Rosalia (Donne di Fora). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-081 — Donna Nina (Donne di Fora)
- **A cosa serve e in quali capitoli**: cap. 3 e seguenti.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — come Rosalia.
- **Prompt Nano Banana principale (EN)**:
  > A shorter plump Sicilian lady spirit (looks 55), 158 cm, round face, lively mouth, grey curls held in a hair net, a three-strand pearl necklace, a black lace shawl on her shoulders. She wears a long forest-green (#2F5A3A) late-19th-century dress. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-081_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-081_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 158 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 158 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Donna Nina (Donne di Fora). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-082 — Donna Tina (Donne di Fora)
- **A cosa serve e in quali capitoli**: cap. 3 e seguenti.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — come Rosalia.
- **Prompt Nano Banana principale (EN)**:
  > A young Sicilian woman spirit, almost a girl (looks 19), 163 cm, gentle face with wide curious eyes, long loose wavy light-brown hair. She wears a long pale sky-blue (#A9C9E2) late-19th-century dress. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-082_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-082_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 163 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 163 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Donna Tina (Donne di Fora). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-090 — Nicolò
- **A cosa serve e in quali capitoli**: cap. 3 (banco, carte), cap. 12, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **1,0 M** — conversazione ravvicinata al banco.
- **Prompt Nano Banana principale (EN)**:
  > An imaginary 11-year-old Sicilian boy, 148 cm, thin, short black hair in a buzz cut, glasses with blue frames, wearing a grey T-shirt with a generic T-rex print (no brand), dark jeans, sneakers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1536, numero di facce 1.000.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: geometria Detailed, limite facce 1.000.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-090_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-090_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 40.000 tri.
- **Controlli automatici**: altezza 148 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 148 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Nicolò. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 1,0 M di facce.

### REQ-CHR-091 — La professoressa di matematica
- **A cosa serve e in quali capitoli**: cap. 3, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — vista in aula a 3–6 m.
- **Prompt Nano Banana principale (EN)**:
  > A 50-year-old Italian female maths teacher, 165 cm, short grey hair, reading glasses on a chain around the neck, wearing a beige blouse, a long dark skirt, low shoes. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-091_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-091_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 165 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 165 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: La professoressa di matematica. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-092 — Il professore di musica
- **A cosa serve e in quali capitoli**: cap. 3, mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — vista in aula.
- **Prompt Nano Banana principale (EN)**:
  > A 60-year-old Sicilian male music teacher, 175 cm, long white hair at the back, theatrical air, wearing a brown corduroy jacket, a silk foulard, beige trousers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-092_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-092_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 175 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 175 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Il professore di musica. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-100 — Il signore dell'aeroporto
- **A cosa serve e in quali capitoli**: cap. 1 (Mattia gli spiega la babuška).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa con battute a 2–4 m.
- **Prompt Nano Banana principale (EN)**:
  > A 60-year-old good-natured Sicilian man, 175 cm, light panama hat, short-sleeved light-blue shirt, beige trousers, a folded newspaper is NOT included. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-100_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-100_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 175 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 175 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Il signore dell'aeroporto. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-101 — Il prete con la valigia a fiori
- **A cosa serve e in quali capitoli**: cap. 1 (porta degli arrivi).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa a 2–4 m; la valigia è REQ-PRP-009.
- **Prompt Nano Banana principale (EN)**:
  > A 55-year-old Italian priest, 172 cm, black clergy shirt with white collar, black trousers, black shoes, kind face, glasses. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-101_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-101_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 172 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 172 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Il prete con la valigia a fiori. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-102 — Turista tedesco (uomo)
- **A cosa serve e in quali capitoli**: cap. 1, cap. 10 (funivia), mondo libero.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa; varianti di colore via script.
- **Prompt Nano Banana principale (EN)**:
  > A 50-year-old German male tourist, 180 cm, sunburnt pink skin, wearing a sun hat, a short-sleeved checked shirt, khaki shorts, sandals with white socks, a small backpack strapped on. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-102_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-102_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 180 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 180 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Turista tedesco (uomo). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-103 — Turista tedesca (donna)
- **A cosa serve e in quali capitoli**: cap. 1, cap. 10, mondo libero.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — come sopra.
- **Prompt Nano Banana principale (EN)**:
  > A 48-year-old German female tourist, 170 cm, sunburnt, short blond hair, sunglasses on her head, wearing a light floral blouse, beige linen trousers, trekking sandals. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-103_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-103_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 170 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 170 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Turista tedesca (donna). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-104 — Pallavolista
- **A cosa serve e in quali capitoli**: cap. 1 (squadra di pallavolo, 8 copie con varianti).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparse in gruppo.
- **Prompt Nano Banana principale (EN)**:
  > A 20-year-old female volleyball player, 182 cm, athletic, hair in a high ponytail, wearing a plain blue-and-white team tracksuit without any logo or text, white sports shoes, a sports bag is NOT included. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Varianti (capelli, carnagione, altezza ±6 cm) generate via script dalla stessa base.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-104_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-104_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 182 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 182 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Pallavolista. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-105 — Barista dell'aeroporto
- **A cosa serve e in quali capitoli**: cap. 1 (bar degli arrivi).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — dietro il banco.
- **Prompt Nano Banana principale (EN)**:
  > A 30-year-old Sicilian male barista, 176 cm, short dark hair, neat beard, black shirt, black apron without writing, black trousers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-105_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-105_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 176 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 176 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Barista dell'aeroporto. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-106 — Addetto al parcheggio
- **A cosa serve e in quali capitoli**: cap. 1 (fallimento morbido del parcheggio).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa.
- **Prompt Nano Banana principale (EN)**:
  > A 40-year-old Sicilian man, 174 cm, wearing a high-visibility yellow vest over a white T-shirt, dark work trousers, work shoes, a cap. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-106_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-106_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 174 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 174 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Addetto al parcheggio. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-107 — Viaggiatrice in attesa (signora col cartello)
- **A cosa serve e in quali capitoli**: cap. 1.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa; il cartello è procedurale.
- **Prompt Nano Banana principale (EN)**:
  > A 65-year-old Italian woman from Bergamo, 160 cm, short grey hair, wearing a light cardigan over a summer dress, comfortable shoes. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-107_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-107_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 160 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 160 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Viaggiatrice in attesa (signora col cartello). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-108 — Ragazzo con i fiori
- **A cosa serve e in quali capitoli**: cap. 1.
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa; il mazzo è un oggetto procedurale.
- **Prompt Nano Banana principale (EN)**:
  > A 25-year-old Italian young man, 180 cm, nervous, wearing a white shirt, dark chinos, sneakers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-108_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-108_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 180 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 180 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Ragazzo con i fiori. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-109 — Viaggiatore generico A (uomo d'affari)
- **A cosa serve e in quali capitoli**: cap. 1 (flussi di passeggeri).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — folla.
- **Prompt Nano Banana principale (EN)**:
  > A 45-year-old businessman, 178 cm, navy suit without tie, white shirt, black shoes. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-109_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-109_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 178 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 178 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Viaggiatore generico A (uomo d'affari). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-110 — Viaggiatrice generica B (studentessa)
- **A cosa serve e in quali capitoli**: cap. 1 (folla), Corso (folla).
- **Priorità (fase in cui serve)**: Fase 3.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — folla.
- **Prompt Nano Banana principale (EN)**:
  > A 22-year-old student, 166 cm, curly hair, wearing a yellow T-shirt, wide jeans, canvas sneakers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-110_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-110_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 166 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 166 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Viaggiatrice generica B (studentessa). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-120 — Signora Agata dei gerani
- **A cosa serve e in quali capitoli**: scalinate (capp. 2–14), MIS-S-01, MIS-S-08.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa ricorrente.
- **Prompt Nano Banana principale (EN)**:
  > A 78-year-old Sicilian woman, 152 cm, white hair in a bun, black dress with a small white pattern, an old-fashioned apron, slippers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-120_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-120_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 152 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 152 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Signora Agata dei gerani. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-121 — Vicino dei gelsomini
- **A cosa serve e in quali capitoli**: scalinate.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa.
- **Prompt Nano Banana principale (EN)**:
  > A 70-year-old Sicilian man, 170 cm, bald, white vest top, grey trousers with braces, slippers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-121_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-121_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 170 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 170 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Vicino dei gelsomini. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-122 — Marta, compagna di classe
- **A cosa serve e in quali capitoli**: scuola (capp. 3, 12), mondo libero.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa con battute.
- **Prompt Nano Banana principale (EN)**:
  > An imaginary 11-year-old Sicilian girl, 147 cm, dark curly hair in two braids, pink T-shirt, jeans, sneakers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-122_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-122_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 147 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 147 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Marta, compagna di classe. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-123 — Compagno di classe (base per 8 varianti)
- **A cosa serve e in quali capitoli**: scuola.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — folla dell'aula.
- **Prompt Nano Banana principale (EN)**:
  > An imaginary 12-year-old Sicilian boy, 150 cm, short brown hair, plain dark-green sweatshirt, jeans, sneakers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Nota**: Varianti via script.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-123_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-123_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 150 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 150 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Compagno di classe (base per 8 varianti). Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-124 — Signor Sciacca, il tabaccaio
- **A cosa serve e in quali capitoli**: bar di papà (mondo libero).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — cliente ricorrente.
- **Prompt Nano Banana principale (EN)**:
  > A 66-year-old Sicilian man, 168 cm, grey moustache, flat cap, beige short-sleeved shirt, brown trousers. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-124_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-124_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 168 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 168 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Signor Sciacca, il tabaccaio. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-125 — Vigile urbano
- **A cosa serve e in quali capitoli**: Corso Umberto.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — comparsa.
- **Prompt Nano Banana principale (EN)**:
  > A 45-year-old Italian municipal police officer, 178 cm, white peaked cap and white summer uniform shirt with dark trousers, without any real insignia or text. Full-body photograph, front view, straight-on camera at chest height, 85mm lens. The person stands in a relaxed A-pose: arms held 35 degrees away from the body, hands open and empty with fingers slightly apart, feet visible and parallel at shoulder width, neutral expression, mouth closed, looking straight at the camera. Plain seamless light grey background (#D9D9D9), no floor line, soft even studio lighting, no harsh shadows, no rim light, no depth of field, sharp focus from head to toe, realistic photographic style with detailed readable fabric textures, natural skin. No text, no logos, no brands, no props, nothing in the hands. Vertical 2:3.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME person from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *lato destro*: «Using the attached image as the exact reference, show the SAME person from their right side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME person seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
  - *3/4*: «Using the attached image as the exact reference, show the SAME person rotated 45 degrees to their right (three-quarter view), same A-pose, same clothes, same lighting and plain light grey background, full body. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 2:3 verticale.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-125_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-125_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro Rigify con nomi Mixamo adattato con MediaPipe, pesi automatici e pulizia, 32 blend shapes del volto, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 20.000 tri.
- **Controlli automatici**: altezza 178 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: una sola persona, figura intera, piedi visibili; braccia staccate dal corpo (A-pose), mani aperte e vuote; sfondo grigio uniforme, nessuna ombra forte; nessun logo o scritta sui vestiti; proporzioni credibili per l'età (altezza in gioco 178 cm); le viste laterali e posteriore mostrano gli stessi vestiti e la stessa acconciatura.
- **In breve**: Vigile urbano. Genera la figura intera in A-pose e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

## Animali

### REQ-CHR-130 — Il gatto rosso del quarto gradino
- **A cosa serve e in quali capitoli**: scalinata (cap. 2 e tutto il gioco), FOT-GAT-01.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — animale visto a 1–3 m.
- **Prompt Nano Banana principale (EN)**:
  > A big red tabby European shorthair cat, male, sturdy, one ear with a small notch, amber eyes. Full-body photograph, front view, straight-on at the animal's eye level, the animal standing still and symmetric, all four paws visible, tail visible, neutral pose. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no depth of field, realistic photographic style, detailed fur. No text, no props. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME animal from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME animal seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-130_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-130_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro quadrupede da template, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 12.000 tri + gusci di pelo (6–10).
- **Controlli automatici**: altezza 30 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: un solo animale, intero, quattro zampe e coda visibili; sfondo grigio uniforme; pelo nitido, nessuna sfocatura.
- **In breve**: Il gatto rosso del quarto gradino. Genera la figura intera (animale) e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-131 — Gatto nero
- **A cosa serve e in quali capitoli**: scalinate e Corso (varianti).
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — animale.
- **Prompt Nano Banana principale (EN)**:
  > A slender black European shorthair cat, green eyes. Full-body photograph, front view, straight-on at the animal's eye level, the animal standing still and symmetric, all four paws visible, tail visible, neutral pose. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no depth of field, realistic photographic style, detailed fur. No text, no props. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME animal from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME animal seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-131_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-131_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro quadrupede da template, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 12.000 tri.
- **Controlli automatici**: altezza 25 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: un solo animale, intero, quattro zampe e coda visibili; sfondo grigio uniforme; pelo nitido, nessuna sfocatura.
- **In breve**: Gatto nero. Genera la figura intera (animale) e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

### REQ-CHR-132 — Garibaldi, il gatto di nonna Concetta
- **A cosa serve e in quali capitoli**: casa di Concetta, scalinata.
- **Priorità (fase in cui serve)**: Fase 4.
- **Fascia poligoni Tripo/Hitem3D**: **0,5 M** — animale.
- **Prompt Nano Banana principale (EN)**:
  > A red-and-white bicolour European shorthair cat, plump, white chest and paws. Full-body photograph, front view, straight-on at the animal's eye level, the animal standing still and symmetric, all four paws visible, tail visible, neutral pose. Plain seamless light grey background (#D9D9D9), soft even studio lighting, no harsh shadows, no depth of field, realistic photographic style, detailed fur. No text, no props. 1:1 square.
- **Prompt di modifica per le altre viste (EN)**, sempre nella stessa conversazione con la prima immagine come riferimento:
  - *lato sinistro*: «Using the attached image as the exact reference, show the SAME animal from their left side, a 90-degree profile, in exactly the same A-pose, same clothes, same proportions, same hair, same lighting and plain light grey background, full body visible from head to feet. Change nothing else.»
  - *retro*: «Using the attached image as the exact reference, show the SAME animal seen from directly behind, same A-pose, same clothes and hairstyle seen from the back, same lighting and plain light grey background, full body from head to feet. Change nothing else.»
- **Formato e proporzioni**: PNG, lato lungo ≥ 2048 px, 1:1.
- **Impostazioni Tripo / Hitem3D**: Hitem3D multi-vista: risoluzione 1024, numero di facce 500.000, texture PBR sì, formato GLB. Alternativa Tripo H3.1: limite facce 500.000, texture PBR sì, quad no, GLB. Viste da caricare in Hitem3D: fronte, retro, sinistra, destra.
- **Nome file e cartella**: immagini `assets_in/immagini/REQ-CHR-132_fronte.png`, `_lato_sx.png`, `_lato_dx.png`, `_retro.png`; modello `assets_in/modelli/REQ-CHR-132_hitem3d.glb` (o `_tripo.glb`).
- **Cosa farà Claude dopo**: pulizia, ritopologia QuadriFlow e LOD, UV, bake (normal, AO, curvatura, colore, rugosità), scheletro quadrupede da template, materiali PBR, retarget delle animazioni, export GLB meshopt + KTX2 (PIPELINE §5).
- **Budget finale in gioco**: 12.000 tri.
- **Controlli automatici**: altezza 28 cm ±1; triangoli entro budget; Hausdorff ≤ 4 mm (volto ≤ 1,5 mm); pesi normalizzati ≤ 4 influenze; pose di deformazione senza compenetrazioni > 2 mm; validatore TDD §10; render di revisione (PIPELINE §5.2).
- **Controlla l'immagine**: un solo animale, intero, quattro zampe e coda visibili; sfondo grigio uniforme; pelo nitido, nessuna sfocatura.
- **In breve**: Garibaldi, il gatto di nonna Concetta. Genera la figura intera (animale) e le altre viste modificando la prima immagine; in Hitem3D scegli 0,5 M di facce.

## Fonti
- `PIPELINE_ASSET.md` §2–§5; `PERSONAGGI.md`.
- [Nano Banana — riferimenti multipli e coerenza (Runway)](https://help.runwayml.com/hc/en-us/articles/50317213804435-Creating-images-with-Nano-Banana)
- [Hitem3D — risoluzioni](https://www.hitem3d.ai/de/ai-faq/how-to-choose-the-model-resolution-for-hitem3d)
