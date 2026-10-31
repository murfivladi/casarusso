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
