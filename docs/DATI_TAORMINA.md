# Dati per la ricostruzione 1:1 di Taormina

Obiettivo (D-18): Taormina riconoscibile metro per metro da chi la conosce, con licenze pulite. La sandbox di Claude **non può scaricare** da questi siti: ogni fonte ha i passi che deve fare Vlad. I file scaricati vanno in `assets_in/dati/<fonte>/` (struttura in `PIPELINE_ASSET.md` §7).

## 1. Fonti

| ID | Fonte | Cosa fornisce | Risoluzione / precisione | Copertura | Licenza | Testo di attribuzione | Come ottenerla (passi per Vlad) | Come entra in Blender |
|---|---|---|---|---|---|---|---|---|
| DAT-01 | **OpenStreetMap** | sagome degli edifici, strade, scalinate (`highway=steps`), sentieri, muri, alberi singoli, punti di interesse, nomi | precisione delle sagome ~1–3 m nel centro (mappato dal catasto e da ortofoto) | completa | **ODbL 1.0** (database; il gioco è un «lavoro prodotto», D-74) | «Dati cartografici © OpenStreetMap contributors, ODbL» | 1) aprire [download.geofabrik.de/europe/italy/isole.html](https://download.geofabrik.de/europe/italy/isole.html); 2) scaricare `isole-latest.osm.pbf`; 3) salvare in `assets_in/dati/osm/`. (In alternativa, export dal sito OSM del riquadro 15,27–15,31 E / 37,83–37,86 N.) | script `blender/scripts/taormina/osm_import.py` (pyosmium → GeoJSON → mesh estruse su DEM; altezze da `building:levels` × 3,1 m + tetto) |
| DAT-02 | **TINITALY 1.1** (INGV) | modello digitale di elevazione | celle 10 m, errore verticale tipico ~3–4 m | Italia | **CC BY 4.0** | «TINITALY/1.1 DEM, Tarquini S. et al., INGV (2023), doi:10.13127/tinitaly/1.1, CC BY 4.0» | 1) aprire [tinitaly.pi.ingv.it/Download_Area1_1.html](https://tinitaly.pi.ingv.it/Download_Area1_1.html); 2) cliccare sulla tessera che contiene Taormina (Sicilia nord-orientale) e quella con l'Etna e Catania; 3) salvare i GeoTIFF in `assets_in/dati/tinitaly/` | riproiezione da UTM 32N a ETRS89/UTM 33N (GDAL in CI); terreno di base e paesaggio intermedio |
| DAT-03 | **DTM LiDAR 1 m — Regione Siciliana** (SITR, ATA 2012–2013) | terreno nudo ad alta risoluzione | 1 m | Sicilia (verificare la tessera di Taormina) | **CC BY 4.0** (metadato INSPIRE) | «DTM LiDAR 1 m © Regione Siciliana — SITR, CC BY 4.0» | 1) aprire il [Geoportale SITR](https://www.sitr.regione.sicilia.it/geoportale/); 2) cercare «DTM 1 metro» e il quadro d'unione del Comune di Taormina; 3) scaricare le tessere che coprono il centro, la costa da Mazzarò alla stazione e la Via Circonvallazione; 4) salvare in `assets_in/dati/sitr_dtm/` | terreno di dettaglio delle celle di gioco (ricampionato a 0,5 m nelle scalinate) |
| DAT-04 | **Ortofoto SITR** (volo ATA 2012–2013, 0,25 m) | riferimento visivo per posizioni, tetti, cortili | 25 cm | Sicilia | **da verificare** (Q-02); uso solo come riferimento di posizione, **non** come texture finché la licenza non è confermata | — | come DAT-03 (cercare «Ortofoto 2012-2013») | solo layer di riferimento in Blender, mai esportato |
| DAT-05 | **Copernicus DEM GLO-30** | rilievo lontano: Etna, Peloritani, costa | 30 m | mondiale | licenza Copernicus DEM (uso libero con avviso) | «Produced using Copernicus WorldDEM-30 © DLR e.V. 2010–2014 and © Airbus Defence and Space GmbH 2014–2018, provided under COPERNICUS by the European Union and ESA» | 1) aprire [OpenTopography — Copernicus GLO-30](https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.3); 2) selezionare il riquadro 14,8–15,5 E / 37,4–38,0 N; 3) scaricare GeoTIFF; 4) salvare in `assets_in/dati/copernicus/` | mesh lontana (skyline) e orizzonte per il bake del cielo |
| DAT-06 | **Wikimedia Commons** | foto di riferimento dei luoghi | — | — | per file (CC0, CC BY, CC BY-SA, PD) | per file (in `CONCEPT/riferimenti_luoghi.md` e `CREDITI.md`) | link diretti in `CONCEPT/riferimenti_luoghi.md` | solo riferimento (D-75) |
| DAT-07 | **Mapillary** | foto stradali a livello occhi | — | buona sul Corso, parziale nelle scalinate | CC BY-SA 4.0 | «Immagini © Mapillary contributors, CC BY-SA» | consultazione online su [mapillary.com](https://www.mapillary.com/app/?lat=37.852&lng=15.287&z=16); niente download necessario | solo riferimento (D-75) |
| DAT-08 | **Foto proprie di Vlad** (facoltative) | facciate, portoni, scalinate, interni della stazione | — | dove Vlad vuole | proprietà di Vlad | — | foto col telefono, di giorno, senza persone riconoscibili in primo piano; salvare in `assets_in/dati/foto_vlad/<luogo>/` | riferimento e texture (fotogrammetria facoltativa di dettagli: portali, edicole) |

## 2. Fonti vietate
- **Google Maps, Google Street View, Google Earth** (immagini, modelli 3D, tracciamenti): i termini d'uso non consentono l'estrazione.
- **Apple Maps / Look Around, Bing Maps (immagini)**: stesso motivo.
- Foto prese da siti, blog, social, agenzie senza licenza aperta esplicita.
- Foto di persone private riconoscibili come riferimento di personaggi.
- Modelli 3D commerciali o con licenza NC/ND/SA (D-33) senza segnalazione.
- Dati del catasto non pubblicati con licenza aperta.

## 3. Elenco dei luoghi simbolo per rilascio (modellati singolarmente)

| Rilascio | Luogo | Riferimenti principali |
|---|---|---|
| v1.0 | Porta Catania, Duomo (esterno) e fontana di Piazza Duomo, Torre dell'Orologio, Piazza IX Aprile (Sant'Agostino, San Giuseppe, belvedere), Porta Messina, Palazzo Corvaja (facciata), Corso Umberto (tutte le facciate), scalinate del lato monte, Via Circonvallazione, scuola di Via Dietro Cappuccini (esterni); aeroporto di Catania (atrio arrivi, facciata, parcheggio) | `CONCEPT/riferimenti_luoghi.md` §1–§6 |
| v2.0 | Teatro Antico, Villa Comunale con le follie di Florence Trevelyan, Badia Vecchia, Naumachie, Odeon, Palazzo Corvaja (cortile), Duomo (interno), Via Pirandello e belvedere, terminal bus | §7–§10 |
| v3.0 | Funivia (stazioni e cabine), Mazzarò, Isola Bella, SS114, stazione di Taormina-Giardini (fabbricato, pensilina, binari) | §11–§14 |

## 4. Obiettivi di precisione

| Elemento | Obiettivo | Tolleranza |
|---|---|---|
| Rete di strade, scalinate e piazze del centro | posizione e andamento come OSM + DTM 1 m | ±1 m in pianta, ±0,3 m in quota |
| Sagome degli edifici | OSM | ±1,5 m; altezze ±1 piano |
| Edifici simbolo | proporzioni dalle foto (almeno 8 foto per edificio) | ±3% sulle misure principali |
| Facciate comuni | kit modulare coerente con lo stile del quartiere (aperture, balconi, persiane, colori) | non riproduzione esatta di ogni finestra; numero di piani esatto |
| Terreno lontano | DEM 10 m / 30 m | ±5 m |
| Profilo dell'Etna e della costa visti da Taormina | esatto (DEM) | errore angolare < 0,2° |
| Linee di vista chiave (§6) | verificate con script | obbligatorie |
| Interni (Casa Russo, bar, scuola, casa di Concetta) | inventati (D-87) | — |
| Aeroporto | riconoscibile dalle foto | ±15% sulle dimensioni (nessuna pianta pubblica) |

## 5. Pipeline (sintesi; dettaglio in `PIPELINE_ASSET.md` §4)
1. GDAL: riproiezione dei DEM in EPSG:25833, ritaglio sulle celle, fusione DTM 1 m dentro TINITALY con raccordo.
2. Terreno per cella (128 m) in Blender: griglia adattiva (0,5 m nelle scalinate, 2 m nei giardini, 8 m fuori dal centro).
3. OSM → edifici estrusi sul terreno, strade e scalinate tagliate nel terreno (gradini generati con alzata/pedata misurate per scalinata), muri, alberi.
4. Kit modulare di facciate assegnato per regole (età, piano, larghezza del fronte).
5. Edifici simbolo modellati da script + foto (procedurale guidato) e controllati con i render di revisione.
6. Bake delle lightmap per cella e ora; export, validatore, manifesto.

## 6. Casa Russo nella Taormina reale (D-45, D-89)
Casa Russo è **inventata** (appendice del libro) e si inserisce come «edificio fittizio» sostituendo il volume di un edificio OSM della stessa taglia, senza riprodurre il civico né l'aspetto reale di quella casa.
**Criteri** per lo script `tools/taormina/scegli_casa_russo.py` (Fase 4), che cerca tra gli edifici a 2 piani affacciati su `highway=steps` del settore ovest (tra Porta Catania e Piazza IX Aprile, lato monte del Corso):
1. a ≤ 25 m a piedi da un tratto carrabile di Via Circonvallazione (l'auto si ferma in cima, D-89);
2. dal balcone (quota primo piano + 1,2 m, facciata sud ±40°): **mare visibile in uno spiraglio tra due tetti** (apertura angolare 3°–12°) a sud-est e **cima dell'Etna visibile** a sud-ovest (viewshed su DTM + edifici OSM);
3. una seconda scalinata parallela più a monte raggiungibile in 3–5 minuti (casa di Concetta, «due scalinate più su»);
4. dalla porta di casa al Corso: discesa ≤ 120 m; dalla casa a Porta Messina passando davanti al bar: ≤ 900 m;
5. cortile posteriore possibile (spazio libero ≥ 3 × 2 m nel lotto OSM).
**Default** se nessun lotto soddisfa tutto: si sceglie il lotto con il punteggio massimo e si sposta di poco il volume (±2 m) per ottenere lo spiraglio sul mare; la scelta finale si registra in `DOMANDE_APERTE.md` (Q-01) con uno screenshot della vista dal balcone.

## Fonti
- [OpenStreetMap — Copyright e licenza](https://www.openstreetmap.org/copyright)
- [Geofabrik — estratti Italia isole](https://download.geofabrik.de/europe/italy/isole.html)
- [TINITALY 1.1 — area download](https://tinitaly.pi.ingv.it/Download_Area1_1.html)
- [DTM LiDAR 1 m Regione Sicilia — INSPIRE Geoportal (CC BY 4.0)](https://inspire-geoportal.ec.europa.eu/srv/api/records/m_amte:299FN3:8740c0d0-8f32-4e85-9856-42f8b88853da)
- [SITR — relazione volo ATA 2012–2013](https://www.sitr.regione.sicilia.it/wp-content/uploads/Documenti/Download-Documenti/ATA_2012_2013/ATA1213_20120723_Realzione_pianificazione_volo.pdf)
- [Licenza Copernicus DEM GLO-30](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/DEM/resources/license/License-COPDEM-30.pdf)
- [Google Maps — Termini di servizio aggiuntivi](https://maps.google.com/help/terms_maps/)
- [Mapillary — licenza delle immagini](https://help.mapillary.com/hc/en-us/articles/115001770409-Licenses)
