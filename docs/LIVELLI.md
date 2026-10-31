# Level Design Document

Luoghi con ID `LUO-`. Misure in metri, scala reale (1 unità Blender = 1 m). Coordinate di Taormina in **ETRS89 / UTM 33N (EPSG:25833)**; i valori indicati qui sono approssimati a ±30 m e vengono fissati in Fase 1–4 dai dati di `DATI_TAORMINA.md`. Le piante sono schemi quotati in testo (le piante vettoriali si producono in Fase 3–4 da Blender).

Legenda delle piante: `█` muro portante · `│ ─` tramezzo · `▯` porta · `≡` finestra · `▒` scala (gradini numerati) · `F` frigorifero · `L` limone · `*` punto interattivo · `C` checkpoint · `@` posizione di Vera all'inizio della scena.

---

## 1. Regole comuni

| Voce | Regola |
|---|---|
| Collisioni | forme semplici esportate da Blender con prefisso `COL_` (box, capsule, convex hull ≤ 64 vertici); niente collisione per mesh sotto i 5 cm; gradini con rampa di collisione invisibile inclinata (il controller sale dolcemente) salvo il 9° gradino (gradino reale per l'evento sonoro) |
| Spazi per accovacciarsi | ogni nascondiglio ha un volume `CRC_` (altezza libera ≥ 1,0 m) e, se serve inginocchiarsi, un punto `KNE_` |
| Navmesh | per cella, generata dal Navigation Plugin V2 con agente raggio 0,25 m, altezza 1,8 m (adulti), 1,2 m (bambini), gradino 0,22 m, pendenza 38° |
| Illuminazione | lightmap baked in Cycles per ogni ora di riferimento della cella (TDD §5); luce dinamica (sole, luna, lampade) sopra |
| Soggetti fotografabili | volume `FOT_` con ID e distanza massima |
| Punti di checkpoint | empty `CP_` con orientamento |
| Riferimenti visivi | l'Etna e il mare sono i due punti cardinali della giocatrice: da ogni luogo aperto di Taormina almeno uno dei due è visibile entro 30 s di cammino |

---

## 2. Capitolo 1 — Aeroporto e strada (v1.0)

### 2.1 LUO-AER-ARR — Atrio arrivi, Catania-Fontanarossa (Terminal A, piano terra)
- **Scopo**: SCN-01-02 … SCN-01-13.
- **Fedeltà**: riconoscibile dalle foto di riferimento (`CONCEPT/riferimenti_luoghi.md` §1); nessuna pianta ufficiale pubblica: dimensioni ricostruite dalle foto con tolleranza ±15%. Marchi di negozi e compagnie sostituiti da insegne generiche.
- **Dimensioni**: sala 62 × 26 m, soffitto 7,2 m (controsoffitto a lamelle con lucernari lineari), vetrata sul fronte città lunga 62 m (sole basso da ovest alle 17:00–18:00: lame di luce sul pavimento di granito lucido, SSR).
- **Pianta** (quote in m):
```
   0        10        20        30        40        50       62
   ┌───────────────────────────≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡┐  ← vetrata e uscite verso parcheggio (nord-ovest)
   │  BAR (8×6)   │ tabellone*     colonna1   colonna2 (Giulia)│
   │  banco*      │ (FOT-01-01)                              │ 26
   │  vetrina*    │      P3 Salvo↔  ··· percorso ···        │
   │──────────────┘                                          │
   │  poster Etna*     @Vera        P2 Irina (transenna)      │
   │                    C CP-01-A                            │
   │ ═══════ transenna (14 m) ═══════   P1 punto d'incontro  │
   │        ▯▯ PORTA SCORREVOLE* (larghezza 4 m) ▯▯          │
   └────────────────────────▯▯───────────────────────────────┘  ← dietro: corridoio dal ritiro bagagli (non giocabile)
```
- **Aree**: bar degli arrivi (LUO-AER-BAR, 8 × 6 m, banco 5 m, 6 tavolini alti); zona attesa davanti alla porta; transenna metallica a 4 m dalla porta; colonne rivestite (4, sezione 0,9 m); tabellone arrivi (3 × 1,6 m) a 3,2 m d'altezza; poster (Etna, Teatro Antico); sedute in metallo (2 file da 8); fontanella; servizi (porta chiusa).
- **Percorsi**: Vera libera in tutta la sala tranne oltre la transenna (muro invisibile morbido) e fuori dalle uscite prima di SCN-01-14.
- **Posizioni NPC** (inizio SCN-01-02): Irina P2 (alla transenna, 6 m dalla porta); Salvo percorso avanti-indietro tra tabellone e colonna 1 (14 m, 1 giro ogni 22 s); Giulia appoggiata alla colonna 2; Mattia percorso a otto bar ↔ sedute (velocità 1,6 m/s, si ferma 4 s ogni 10); il signore accanto al poster del Teatro; comparse: 12 in attesa, flussi casuali dalle uscite.
- **Checkpoint**: CP-01-A (punto @), CP-01-B (P1 davanti alla porta).
- **Fotografabili**: FOT-01-01 tabellone (≤ 12 m), FOT-01-02 cartello (≤ 5 m), FOT-01-03 porta aperta (≤ 15 m), FOT-01-04 babuška (≤ 8 m).
- **Luce**: 17:05–17:45; sole a ovest radente (altezza 18° → 10°), interni 4000 K da lucernari + lamelle; pavimento granito grigio lucido (roughness 0,12).
- **Cella di streaming**: `AER-01` (sala + bar), `AER-02` (facciata e marciapiede).

### 2.2 LUO-AER-BAR — Bar degli arrivi
Vedi sopra. Interazioni: banco (barista), vetrina arancini, frigo bibite; bancone in acciaio spazzolato e marmo.

### 2.3 LUO-AER-PRK — Parcheggio
- **Dimensioni giocabili**: 120 × 70 m davanti al terminal (strada di accesso, attraversamento pedonale, parcheggio all'aperto con pensiline fotovoltaiche); la monovolume al posto **P-214**, 85 m dall'uscita.
- **Elementi**: fila di carrelli (bersaglio di Mattia, D-72), cassa automatica, palme, aiuole secche, taxi bianchi in fila, autobus navetta blu, vista sull'Etna a ovest-nord-ovest oltre i tetti.
- **Fallimento morbido**: Mattia esce dalla vista 25 s o distanza > 35 m (SIS-09); punto sicuro all'uscita del terminal.
- **Celle**: `AER-03`, `AER-04`.

### 2.4 LUO-AUT — Interno della monovolume grigia
- **Veicolo**: monovolume generica 7 posti (D-88): 4,6 × 1,85 × 1,75 m; interni grigio antracite, tessuto; ammaccatura sulla portiera posteriore destra.
- **Posti**: Salvo guida (sx anteriore); babuška (dx anteriore) con la borsa sulle ginocchia; **Vera dietro la babuška** (seconda fila dx); Mattia seconda fila centro (seggiolino); Irina seconda fila sx; Giulia terza fila; valigie: due nel bagagliaio, una tra i piedi della terza fila.
- **Camera**: occhi di Vera a 1,08 m dal pianale; sguardo ±150° / −40°…+55°; finestrini con riflessi (riflesso di Vera sul vetro laterale al tramonto).

### 2.5 LUO-A18 — Strada Catania → Taormina
- **Percorso reale**: aeroporto → asse dei servizi/tangenziale di Catania → A18 Catania–Messina → uscita Taormina → SS114/salita a Taormina → Via Circonvallazione (LUO-CIR) fino alla testa della scalinata di Casa Russo.
- **Compressione**: 55 km reali in 4 minuti di gioco: il veicolo non percorre la strada a velocità reale; la cella `A18-SEQ` è un **corridoio di streaming** di 12 segmenti (6 km ciascuno nella realtà, ognuno rappresentato da 600 m di geometria dettagliata ai lati + panorama lontano reale da DEM) con dissolvenze invisibili sotto i cavalcavia e le gallerie.
- **Momenti**: traffico in tangenziale (0:00–1:10); Etna a sinistra in controluce con pennacchio (1:30–3:00, ora di gioco 19:00–19:12, FOT-01-06); mare a destra dopo Acireale; uscita e salita con Taormina illuminata sulla roccia (3:30–4:00).
- **Fedeltà**: profilo dell'Etna e della costa dal DEM (esatto); bordo strada generico mediterraneo (oleandri, guard-rail, cartelli autostradali italiani senza marchi).

---

## 3. Casa Russo (v1.0)

### 3.1 Collocazione
Zona fissata da D-45 e D-89: scalinata sul lato monte del Corso Umberto, settore ovest; la casa è a 4 gradini dalla Via Circonvallazione (l'auto si ferma in cima). Il punto esatto lo sceglie in Fase 4 lo script di visibilità (`DATI_TAORMINA.md` §6). Orientamento di progetto: facciata principale verso **sud** (balcone a sud: mare a sud-est tra due tetti, Etna a sud-ovest).

### 3.2 Volumi
Casa stretta a due piani, persiane verdi, intonaco giallo paglierino scolorito; ingombro 6,4 × 10,5 m; altezza interpiano 3,20 m; corpo basso della cucina (un piano) sul retro con **terrazzo sopra** (14.013) affacciato sul cortile; tetto a falde in coppi; cortiletto 3,0 × 2,0 m («grande come un tavolo da ping-pong») con il limone, chiuso da un muro alto 2,2 m sopra il quale passa la luce del lampione della scalinata.

### 3.3 Piano terra
```
          0     1     2     3     4     5     6.4
     0  ┌─████████████▯▯████████████████████┐   ← PORTONE* (sud-est, sulla scalinata, 4 gradini sotto la strada)
        │ INGRESSO 2,4×3,0  │  SOGGIORNO 4,0×3,8 │
        │ mobile*  specchio │  vetrinetta* (D-50)│≡ finestra sulla scalinata
        │ scarpiera*        │  divano  tv        │
     3  │──▯──────────▒▒▒▒▒▯   cassetto tovaglie*│
        │ SOTTOSCALA  ▒ scala 18 gradini         │
        │ quadro el.* ▒ (9° gradino*, crepa      │
        │ lavatrice*  ▒  sul muro a dx)          │
     6  │─────────────▒──────────────────▯───────│
        │  CUCINA 6,4×3,6 (corpo basso)          │
        │  F* frigo + intercapedine 12 cm (KNE_)  │
        │  fornello a gas  lavandino≡  lavastov. │
        │  tavolo 1,6×0,9 (6 sedie)  dispensa*   │
   9.6  │──────────▯ porta sul cortile───────────│
        │  CORTILE 3,0×2,0   L* limone  filo*    │
  11.6  └────────────────────────────────────────┘
```
- **Ingresso** (LUO-CR-ING): portone di legno a due ante (1,3 × 2,4 m), **serratura antica con buco della chiave grande come un dito** (foro 9 × 18 mm visibile, punto SEG-03; origine della nebbia delle Donne); pavimento in graniglia fredda (03.048); mobile dell'ingresso (dito di Rosalia, 03.026).
- **Scala** (LUO-CR-SCL): rettilinea, 18 alzate da 17,8 cm, pedata 27 cm, larghezza 0,9 m, corrimano a destra in salita; **9° gradino** scricchiolante (SFX-012) e con la crepa sul muro di destra all'altezza del 9° gradino (decal a 6 stadi, SIS-12); il gradino in cima è il posto di Vera per ascoltare il litigio (07.021).
- **Cucina** (LUO-CR-CUC): finestra sul cortile sopra il lavandino (luce del lampione di notte, 02.016; Fomà seduto sul bordo del lavandino, 06.018); **frigorifero** a due porte bianco anni 2000 (1,75 × 0,7 × 0,65 m) contro il muro est con **intercapedine di 12 cm** e griglia nera sul retro (02.030): volume `KNE_` per inginocchiarsi e guardare con la torcia (capp. 3, 4, 9); tavolo da 6 con 6 sedie (posti a cena: capotavola nord Salvo, poi Irina, babuška, Concetta / Giulia, Vera, Mattia); dispensa a muro (pane nero, sacco della farina della babuška accanto al frigo: origine delle impronte, 10.007); cassetto delle candele «per quando salta la luce» (06.033); pensili (ante che sbattono, 08.037); lampadina sopra il tavolo; forno elettrico (13.012).
- **Soggiorno** (LUO-CR-SOG): vetrinetta con il servizio buono di Concetta (tazzine col bordo d'oro), chiave sotto il centrino (SEG-07).
- **Sottoscala**: quadro elettrico (SFX-041, SEG-09), lavatrice (09.005).
- **Cortile** (LUO-CR-COR): limone alto 3,2 m (chioma 2,4 m) con foglie per stadio (SIS-12), filo per il bucato dal limone alla finestra del bagno al primo piano (04.030), mattonella smossa (SEG-08).

### 3.4 Primo piano
```
          0     1     2     3     4     5     6.4
     0  ┌──────────────≡≡≡ BALCONE 3,0×1,1 (sud) ──┐   gradino del balcone* (06.006)
        │ CAMERA GENITORI│▯ │ CAMERA DI GIULIA     │
        │ 3,6×3,2        │  │ 3,0×3,0  (di fronte  │
        │                │  │  a quella di Vera)   │
     3.2│────────▯───────┘  └──▯───────────────────│
        │ ▒ arrivo scala   CORRIDOIO 1,1 m         │
        │────────▯──────────┬──▯───────┬──▯───────│
        │ CAMERA DI VERA    │ STANZA    │ CAMERA DI│
        │ 3,0×2,9  @letto   │ BABUŠKA   │ MATTIA   │
        │ scrivania*        │ (ex studio)│ 2,6×2,6 │
     6.3│───────────────────┴───────────┴──────────│
        │ BAGNO 2,2×2,0 ≡(sul cortile)  │ porta sul TERRAZZO* sopra la cucina (6,4×3,6) │
        └────────────────────────────────────────┘
```
- **Camera di Vera** (LUO-CR-VER): accanto alla stanza della babuška (02.011), di fronte a quella di Giulia (02.013): porta con fessura (02.015, maschera di inquadratura); letto, scrivania col quaderno, mensola (ditale+cucchiaio dal cap. 13), finestra sulla scalinata (gelsomini del vicino).
- **Stanza della babuška** (LUO-CR-SBA): letto, armadio, sedia (02.011); cassetto del comodino (SEG-16); valigie fino al cap. 2 (MIS-S-03).
- **Balcone** (LUO-CR-BAL): 3,0 × 1,1 m, ringhiera in ferro battuto, gradino della porta-finestra dove ci si siede (06.006, 09.033, 14.019); vista: **mare tra due tetti** a sud-est e **pezzo di Etna** a sud-ovest (verifica con script, `DATI_TAORMINA.md` §6); SEG-10.
- **Terrazzo** sopra la cucina: 6,4 × 3,6 m, parapetto basso, accesso dal corridoio; futura stanza (14.013, MIS-S-12); dal cap. 14 ci si sale (SEG-15).

### 3.5 Percorsi, nascondigli e punti di scena
| Scena | Punti |
|---|---|
| SCN-02-06/07 | fessura della porta di Vera → corridoio → scala → stipite della porta della cucina (vista su tutta la cucina, babuška al centro, frigo a 3,2 m) |
| SCN-03-07…11 | camera → scala (9° evidenziato) → stipite tra scala e ingresso (vista su ingresso e cucina); serratura a 2,5 m |
| SCN-05-04 | ingresso → stipite della cucina (candela davanti al frigo) |
| SCN-06-03/04 | sedia accanto al lavandino; cassetto candele; punto davanti al frigo |
| SCN-07-07 | ultimo gradino in alto, seduta |
| SCN-08-* | capotavola sud (Vera), lato ovest (Donne), lato est (Fomà sul tavolo) |
| SCN-12-06 | ingresso, seduta con la schiena al muro di fronte al portone |
| SCN-13-04/05 | letto di Vera → stipite della cucina |
| Nascondigli `CRC_` | dietro lo stipite della cucina; sotto il tavolo; dietro la porta della camera; sul pianerottolo di Concetta dietro il vaso grande dei gerani |

### 3.6 Punti di ricerca del cap. 9
Dietro il frigo · sotto il lavandino · forno · dispensa · cesto della biancheria (bagno) · scarpiera · sotto i letti (4) · dietro la lavatrice · cortile sotto il limone.

### 3.7 Luce
| Momento | Luci |
|---|---|
| Giorno | sole dalle finestre sud; cucina in luce indiretta dal cortile (diffusa, 6500 K) |
| Sera | lampade 2700 K (lampadario a goccia in cucina, abat-jour), TV blu in soggiorno |
| Notte | lampione della scalinata 2200 K (sodio) dalla finestra della cucina e dal lucernario sopra il portone; luna secondo calendario; torcia del telefono |
| Blackout | tutte le lampade spente in 80 ms con sfarfallio; resta il lampione esterno |

**Celle**: `CR-INT` (interni, sempre in memoria quando Vera è entro 150 m), `CR-EXT` (facciata, cortile, terrazzo).

---

## 4. Scalinate e casa di nonna Concetta (v1.0)

### 4.1 LUO-SCA-01 — Scalinata di Casa Russo
- Scalinata pubblica in pietra (gradini consumati, alzata 14–17 cm, pedate lunghe irregolari 0,6–1,4 m), larghezza 2,2–3,0 m, dislivello ~22 m fino al Corso con 4 rampe e 3 pianerottoli; vasi di gerani ai lati, muri a secco intonacati, portoni, edicola votiva; lampioni a mensola (sodio 2200 K).
- **Gatto rosso del quarto gradino** (contando dalla Via Circonvallazione): sempre lì di giorno (02.008), sposta la routine con MIS-S-01.
- **Celle**: `TAO-SCA-01a/b`.

### 4.2 LUO-SCA-02 e LUO-CON — Scalinata e casa di nonna Concetta
- **Due scalinate più su** (D-45, C-08): oltre la Via Circonvallazione, nella scalinata parallela che sale verso il monte; 3 minuti a piedi (90 s di gioco in SCN-05-02).
- **Casa di Concetta**: piano terra con pianerottolo esterno, **vaso grande dei gerani** (nascondiglio di SCN-05-03), portone più vecchio con serratura più grande (05.008), finestra della cucina sul pianerottolo (Vera ci guarda dentro), interni: ingresso, cucina con tavolo e tovaglia bianca, soggiorno con pizzi, centrini, santi, **credenza con la foto di nonno Turi e il lumino** (cella `TAO-CON`).
- **Punti di ricerca del cap. 9 fuori casa**: vasi dei gerani della scalinata · sotto il portone di Concetta · edicola votiva · gradini sotto il lampione · muretto del cortile · bidone della spazzatura in fondo alla discesa (09.031).

---

## 5. Corso Umberto, bar di papà, scuola (v1.0)

### 5.1 LUO-COR — Corso Umberto 1:1
- Da **Porta Catania** (E 524 897, N 4 189 310) a **Porta Messina** (E 525 450, N 4 189 611), ~800 m; larghezza 4–7 m; pavimentazione in basole di pietra lavica e pietra chiara; facciate dal kit modulare (TDD/PIPELINE) sulle sagome OSM, edifici simbolo modellati singolarmente: Porta Catania, Duomo e fontana di Piazza Duomo, Palazzo Corvaja (facciata, interno in v2.0), Torre dell'Orologio, Piazza IX Aprile con chiesa di Sant'Agostino e San Giuseppe, belvedere della piazza, Porta Messina.
- **Folla**: 20 agenti (PC) / 10 (tablet) + figure lontane impostor; densità per stagione (pieno a set–ott, rado il 4/11).
- **Landmark**: dal belvedere di Piazza IX Aprile si vedono l'Etna, la baia di Naxos e la costa.
- **Celle**: `TAO-c07-r14` … `TAO-c11-r16` (§10).

### 5.2 LUO-BAR — Bar di papà
- Sul Corso, tra Piazza IX Aprile e Porta Messina (necessario per il percorso del cap. 10), lato monte; **insegna generica senza marchi** («Bar Russo — dal 1978» [NUOVO]); vetrina sul Corso (cono di vista di Salvo, SIS-23), 3 tavolini fuori.
- **Interno** 5,5 × 11 m: banco 4 m con macchina del caffè a due gruppi, vetrina refrigerata delle granite, vetrina calda, cassa, 6 tavolini, radio sulla mensola, **tavolino in fondo vicino al bagno** (06.001) dove Vera fa i compiti.
- **Cella**: `TAO-BAR` (interno caricato quando Vera è a < 40 m dalla porta).

### 5.3 LUO-SCU — Scuola media
- Complesso reale della scuola secondaria di primo grado di Via Dietro Cappuccini (D-87), esterni 1:1, nome e marchi non riprodotti («Scuola media di Taormina»); interni inventati: atrio, corridoio, aula 1ªB (7 × 6,5 m, 22 banchi, lavagna di ardesia — la prof. usa il gesso), aula di musica (pianoforte verticale), cortile con muretto e vista sul mare.
- Percorso casa–scuola: scalinata → Corso → Via Teatro Greco/Via Pirandello → Via Dietro Cappuccini (circa 9 minuti reali a piedi; nel raccordo 70 s con transizioni).
- **Celle**: `TAO-SCU`, `TAO-SCU-INT`.

---

## 6. v2.0 — Taormina monumentale (livello di pianificazione)

| Luogo | Scopo per capitolo | Dimensioni e aree | Note |
|---|---|---|---|
| LUO-TEA Teatro Antico | libero v2.0; Irina con i turisti (MIS-S-06); cap. 9 citato | cavea Ø 109 m, scena, portici; vista sull'Etna e sulla baia | edificio simbolo modellato dalle foto + DEM; orari di apertura rispettati in libero (chiuso di notte) |
| LUO-VIL Villa Comunale | libero; MIS-S-06, MIS-S-07; cap. 10 (bugia) | giardino ~3 ha a terrazze, «follie» di Florence Trevelyan, viali, belvedere | vegetazione da libreria CC0 rielaborata |
| LUO-BEL belvedere di Via Pirandello | libero; FOT-LUO-13 | terrazza 40 m | vista su Isola Bella |
| LUO-PIR Via Pirandello, terminal bus, negozio di prodotti dell'Est | MIS-S-05; cap. 10 (stazione a monte della funivia) | 600 m di strada | negozio fittizio (D-52) |
| Duomo (interno), Palazzo Corvaja (cortile), Badia Vecchia, Naumachie, Odeon | libero, foto | — | interni solo dove previsto |

---

## 7. v3.0 — La costa (livello di pianificazione)

| Luogo | Scopo | Dimensioni e aree | Note |
|---|---|---|---|
| LUO-FUN-M / LUO-FUN / LUO-FUN-V Funivia Taormina–Mazzarò | cap. 10 (andata), cap. 11 (ritorno), libero | linea ~ 750 m, dislivello ~ 170 m; stazione a monte su Via Pirandello, stazione a valle a Mazzarò; cabina rossa (D-12; il libro: «cabina rossa», 10.018) | viaggio di 2 minuti (SIS-27); cavi e piloni da foto |
| LUO-MAZ Mazzarò | cap. 10 | piazzale della funivia, spiaggia, lungomare | impronte finali (6) |
| LUO-ISB Isola Bella | libero | isolotto, spiaggia di ciottoli, passaggio a guado | riserva naturale: solo esterni |
| LUO-LUN strada lungo il mare (SS114) | cap. 10 | 1,6 km da Mazzarò alla curva sopra la stazione (compressi in 2 min di cammino con dissolvenza a metà) | traffico, marciapiede |
| LUO-STA Stazione di Taormina-Giardini 1:1 | cap. 11 | fabbricato viaggiatori (tetto spiovente, finestre ad arco, pareti color crema), atrio con pavimenti di marmo, panchine di legno, colonnine di ferro verdi, lampioni, primo binario, pensilina, il mare oltre i binari; cartellone orari (17:42 per Messina) | edificio simbolo; il «fondo del binario dove finisce la pensilina e comincia il sole» (11.004) è il punto di scena di Fomà, orientato a nord |

---

## 8. Fotografabili e checkpoint (riepilogo)
Gli ID FOT di trama sono nei capitoli; quelli liberi in `NARRATIVA/mondo_libero.md` §6. Ogni checkpoint `CP-CC-X` ha un empty con lo stesso nome nella cella indicata dal capitolo.

## 9. Linee di vista
| Da | Si vede | Uso |
|---|---|---|
| Balcone di Casa Russo | mare tra due tetti (SE), Etna (SO) | capp. 6, 9, 14, titolo |
| Belvedere di Piazza IX Aprile | Etna, baia di Naxos | orientamento sul Corso |
| Cabina della funivia | Isola Bella, Mazzarò, mare | cap. 10 |
| Fondo del binario | nord (Messina), montagna con Taormina «appesa alla roccia» (11.034) | cap. 11 |
| A18 al tramonto | Etna in controluce | cap. 1 |

---

## 10. Griglia di streaming di Taormina

- **Sistema**: ETRS89/UTM 33N. **Origine della griglia**: E 524 000, N 4 187 500. **Cella**: 128 × 128 m. ID: `TAO-cCC-rRR` (colonna verso est, riga verso nord). Ogni cella ha: `.glb` geometria (3 LOD), lightmap per ora di riferimento (mattina, pomeriggio, tramonto, notte), navmesh, collisioni, manifesto (TDD §6).
- **Sempre in memoria**: Casa Russo (`CR-INT`, `CR-EXT`), scalinata `TAO-SCA-01a/b`, terreno lontano (DEM 10 m semplificato + skyline dell'Etna e della costa da Copernicus GLO-30, 1 mesh), cielo e acqua.
- **Raggio di caricamento**: celle entro 192 m caricate a LOD0, 192–448 m a LOD1, oltre come impostor/LOD2 fino a 1,5 km; scaricamento con isteresi di 64 m.

| Rilascio | Celle (indicative, da confermare con i dati in Fase 4) | Contenuto |
|---|---|---|
| v1.0 | colonne 06–12 × righe 13–18 (42 celle) | Corso intero, scalinate del lato monte, Via Circonvallazione, casa di Concetta, scuola di Via Dietro Cappuccini |
| v2.0 | + colonne 10–15 × righe 11–17 (24 celle nuove) | Teatro Antico, Villa Comunale, Via Pirandello, belvedere, Badia Vecchia, Naumachie |
| v3.0 | + corridoio funivia e costa: colonne 07–20 × righe 03–18 (40 celle nuove, solo quelle con contenuto) | stazione a valle, Mazzarò, Isola Bella, SS114, stazione di Taormina-Giardini |
| Fuori griglia | `AER-01…04`, `A18-SEQ` (corridoio), interni (`TAO-BAR`, `TAO-SCU-INT`, `TAO-CON`) | caricamenti con schermata (GDD §6.5) |

**Schermate di caricamento** (GDD §6.5): aeroporto ↔ auto ↔ Taormina; Casa Russo ↔ stazione (se non a piedi); qualsiasi interno ↔ esterno lontano. Tra celle adiacenti nessuna schermata.

## Fonti
- Manoscritto (ID in `work/libro.txt`); `FASI_DI_SVILUPPO.md` Fase 3–7.
- [OpenStreetMap — Taormina](https://www.openstreetmap.org/#map=16/37.8520/15.2870)
- [Wikimedia Commons — Category:Taormina](https://commons.wikimedia.org/wiki/Category:Taormina)
- [Wikimedia Commons — Category:Catania–Fontanarossa Airport](https://commons.wikimedia.org/wiki/Category:Catania%E2%80%93Fontanarossa_Airport)
- [Funivia Taormina–Mazzarò (cronaca locale)](https://www.lasicilia.it/tag/funivia)
