# Come usare le schede di richiesta (guida per Vlad)

Le schede ti dicono **esattamente** cosa generare. Tu produci immagini e modelli 3D; io (Claude) faccio tutto il resto in Blender con gli script: ritopologia, UV, texture, scheletro, animazioni, luci, export (D-31). Non devi aprire Blender.

## Passo 1 — Scegli la scheda
- Apri `personaggi_v1.md` o `oggetti_cap01.md`.
- Segui l'ordine della colonna **Fase**: prima le schede della **Fase 1** (lapot' REQ-PRP-001, babuška REQ-CHR-010, Fomà REQ-CHR-070: servono a collaudare la pipeline), poi **Fase 2** (telefono di Vera, quaderno), poi **Fase 3** (tutto il capitolo 1), poi **Fase 4**.

## Passo 2 — Genera l'immagine principale con Nano Banana (Gemini)
1. Apri una **nuova conversazione** in Gemini con il modello di immagini (Nano Banana / Nano Banana Pro).
2. Se la scheda lo dice (abiti successivi di un personaggio), **allega prima** l'immagine frontale della scheda indicata e scrivi all'inizio: «Same person as the reference image, same face and hair.»
3. Copia **tutto** il testo del «Prompt Nano Banana principale» (dal `>` in poi) e invialo.
4. Se l'immagine non va bene, rigenera nella stessa conversazione (non cambiare il prompt, chiedi solo «Generate again»).

## Passo 3 — Controlla l'immagine con la lista della scheda
Spunta ogni voce di «Controlla l'immagine». Gli errori più comuni e come correggerli (sempre nella stessa conversazione, in inglese):
| Problema | Cosa scrivere |
|---|---|
| Braccia attaccate al corpo | «Same image, but arms held 35 degrees away from the body, hands open and empty.» |
| Piedi tagliati | «Same image, zoomed out so the whole body including the feet is visible.» |
| Ombre forti / sfondo non uniforme | «Same image with plain uniform light grey background and soft even lighting, no shadows.» |
| Logo o scritta sui vestiti | «Same image, remove any logo or text from the clothes.» |
| Oggetto in mano | «Same image, hands empty.» |

## Passo 4 — Genera le altre viste (stessa conversazione!)
Copia uno alla volta i «Prompt di modifica» (lato sinistro, lato destro, retro, 3/4) **nella stessa conversazione**, così Nano Banana usa la prima immagine come riferimento. Controlla che vestiti e capelli siano uguali in tutte le viste.

## Passo 5 — Salva le immagini
Salva in `assets_in/immagini/` con i nomi della scheda, ad esempio:
`REQ-CHR-010_fronte.png`, `REQ-CHR-010_lato_sx.png`, `REQ-CHR-010_lato_dx.png`, `REQ-CHR-010_retro.png`.

## Passo 6 — Genera il modello 3D
**Hitem3D** (consigliato per i personaggi):
1. Scegli «Multi-view to 3D» (multi-vista).
2. Carica: **fronte** (obbligatoria), **retro**, **sinistra**, **destra**.
3. Imposta la **risoluzione** e il **numero di facce** indicati nella scheda: 1,5 M → risoluzione 1536 e 1.500.000 facce; 1,0 M → 1536 e 1.000.000; 0,5 M → 1024 e 500.000.
4. **Texture PBR: sì**.
5. Scarica in **GLB**.

**Tripo** (consigliato per gli oggetti rigidi: valigie, telefoni, auto):
1. Modello H3.1 (o il più recente «detailed»), immagine singola o multi-vista.
2. Qualità geometria **Detailed**, **limite facce** come la scheda (1.500.000 / 1.000.000 / 500.000; se c'è solo un menu di valori, scegli il primo uguale o superiore).
3. **Texture PBR: sì**, **Quad: no**.
4. Scarica in **GLB**.

Se lo strumento non permette il valore esatto, usa il più vicino **superiore** e scrivilo in un file `NOTE.txt` accanto al modello.

## Passo 7 — Salva il modello
In `assets_in/modelli/` con il nome della scheda: `REQ-CHR-010_hitem3d.glb` oppure `REQ-PRP-001_tripo.glb`.

## Passo 8 — Modelli dal web
Per le righe **WEB-…** di `oggetti_cap01.md`: apri il link, scegli formato **glTF** e risoluzione **2K**, scarica lo ZIP e scompattalo in `assets_in/web/WEB-001/` (ecc.).

## Passo 9 — Dimmi che è pronto
Scrivimi l'elenco delle schede fatte. Io controllo i file, eseguo la pipeline e ti mando i **render di revisione** (giro a 360°, pose, primi piani) per l'approvazione. Se un modello non passa i controlli, ti mando la scheda corretta (di solito una modifica al prompt o alla fascia di facce).

## Cartelle (riepilogo)
```
assets_in/immagini/   le immagini Nano Banana
assets_in/modelli/    i GLB di Hitem3D o Tripo (+ NOTE.txt)
assets_in/web/        i modelli scaricati dai link WEB-…
assets_in/dati/       mappe e altimetrie (vedi DATI_TAORMINA.md)
assets_in/concept/    le immagini di concept (vedi CONCEPT/prompt_concept.md)
assets_in/audio/      le voci (vedi AUDIO.md §5)
```

## Fonti
- `PIPELINE_ASSET.md` §3–§7.
- [Hitem3D — risoluzioni e facce](https://www.hitem3d.ai/de/ai-faq/how-to-choose-the-model-resolution-for-hitem3d)
- [Hitem3D — multi-vista (fronte obbligatoria, retro e lati facoltativi)](https://blog.hitem3d.ai/blog/Hitem-3D-The-New-Epoch/)
- [Tripo H3.1](https://developers.tripo3d.com/en/models/v3-1)
