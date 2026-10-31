# GDD — Game Design Document

*Casa Russo — Il domovoj nella scarpa*. Gioco 3D in prima persona nel browser (PC e tablet), tratto dal libro 1 della serie *Casa Russo*. Uso privato.

Documenti collegati: `REGISTRO_DECISIONI.md` (ID D-NN), `NARRATIVA/` (scene SCN-, variabili), `TDD.md` (implementazione, console di debug `cr.*`), `LIVELLI.md` (luoghi LUO-), `PERSONAGGI.md` (PG-).

---

## 1. Visione, pilastri e tema

### 1.1 Visione
Il giocatore è **Vera Russo, 12 anni**, metà russa e metà siciliana, l'unica che vede tutti gli spiriti di casa. Vive il libro capitolo per capitolo, dall'aeroporto di Catania fino alla notte di pioggia del 4 novembre 2025, e tra un capitolo e l'altro gira per una Taormina ricostruita 1:1.

### 1.2 Tema: «Non ero divisa. Ero un ponte.» (14.028)
Ogni sistema serve il tema.

| Sistema | Come serve il tema |
|---|---|
| Dialoghi e rapporti | Due nonne, due tradizioni: le scelte di Vera avvicinano o allontanano le due metà, ma non c'è mai una scelta «giusta» che escluda una delle due |
| Lingua | Russo e italiano (e siciliano) convivono nelle voci; i sottotitoli fanno da ponte per il giocatore |
| Quaderno di scienze | Comincia diviso (scienze / indagine) e finisce con la pagina «CASA RUSSO» che mette tutti nello stesso elenco |
| Stato della casa | La casa si ammala quando le due metà litigano e guarisce col patto: il mondo rende fisico il conflitto |
| Chi vede cosa | Vera vede tutti *perché* è tutte e due le cose (08.045): la percezione è la meccanica centrale |
| Collezioni | Parole russe e foto di Taormina: si colleziona l'una e l'altra metà |
| Ditale e cucchiaio | Ultimo gesto del giocatore: unire a mano i due oggetti dei nonni |

### 1.3 Pilastri
1. **Fedeltà al libro**: eventi, battute e tono del libro restano quelli (D-06). Il testo nuovo è sempre marcato [NUOVO] e scritto con la voce del libro.
2. **Vedere ciò che gli altri non vedono**: la meraviglia e l'ironia nascono dal contrasto tra ciò che vede Vera e ciò che spiegano gli adulti.
3. **Un luogo vero**: Taormina 1:1, luce e meteo del calendario reale del 2025.
4. **Gentilezza**: niente morte, niente punizioni; fallimento morbido (D-07); niente musica, solo il suono del mondo.

### 1.4 Pubblico e tono
- Pubblico 10–14 anni; leggibilità dei testi pensata per la scuola media; nessun contenuto spaventoso oltre il «mistero».
- **Curva del tono**: ironico (capp. 1–3) → misterioso e affettuoso (4–6) → teso (7–9: casa malata, febbre, litigio) → avventuroso (10–11) → caldo e risolto (12–14), con l'aggancio finale ironico-misterioso (la scopa sul tetto).

### 1.5 Cosa il gioco non è
Non è un horror, non è un gioco d'azione o di combattimento, non ha nemici, non ha punteggi competitivi, non ha acquisti, non è online, non è per telefono, non cambia il finale del libro, non ha musica.

---

## 2. Struttura

### 2.1 Capitoli come missioni e Taormina libera
- Ogni capitolo è una **missione** composta da scene `SCN-CC-NN` (tipi: libera, guidata, dialogo, cinematica, minigioco, raccordo).
- Tra i capitoli, nei **vuoti del calendario** di almeno mezza giornata, si apre la **Taormina libera** (D-66).
- Il passaggio al capitolo successivo avviene sempre per scelta del giocatore: obiettivo del quaderno «Quando sei pronta: vai a dormire» (o l'azione che apre il capitolo: es. «Vai a scuola»).

### 2.2 Come funziona una giornata
| Fascia | Ore di gioco | Durata reale in libero (scala 1×) | Cosa succede |
|---|---|---|---|
| Mattina | 07:00–13:30 | 9 min | Colazione, Concetta alle 7:30 con la moka; giorni di scuola: scuola 8:00–13:30 (scena di raccordo) |
| Pomeriggio | 13:30–19:00 | 12 min | Compiti al bar di papà, scalinate, Corso, missioni secondarie |
| Sera | 19:00–23:00 | 8 min | Cena in famiglia (scena breve), casa |
| Notte | 23:00–07:00 | 6 min o salto | Martedì, giovedì e sabato: le Donne di Fora (dal cap. 3 in poi); altre notti: si dorme (salto con dissolvenza) |

Il tempo scorre a **scala 40×** in mondo libero (1 minuto reale = 40 minuti di gioco) e a 1× nelle scene; la scala è sospesa in dialogo, quaderno e menu. Dormire salta alla mattina successiva.

### 2.3 Vuoti del calendario e mondo libero (v1.0–v3.0)

| Vuoto | Giornate giocabili | Apre dopo | Chiude con | Rilascio |
|---|---|---|---|---|
| Dom 14/9 | domenica intera | SCN-02-10 | «Vai a dormire» → SCN-03-01 | v1.0 |
| Pomeriggi 15–18/9 | 4 pomeriggi brevi (dentro il cap. 3, D-08) | SCN-03-01… | sera di ogni giorno | v1.0 |
| Dopo il cap. 3 (solo v1.0) | domenica 14/9 ripetibile (D-82) | fine v1.0 | — (con v2.0 → SCN-04-01) | v1.0 |
| Sab 27/9 – ven 3/10 | 3 giornate: sab 27, mer 1/10, ven 3/10 | SCN-04-11 | SCN-05-01 | v2.0 |
| Lun 6 – lun 13/10 | 2 giornate: mer 8, sab 11 | SCN-05-06 | SCN-06-01 | v2.0 |
| Dentro il cap. 7 (15–21/10) | giornate brevi della casa malata | SCN-07-02… | SCN-07-07 | v2.0 |
| Mer 29 – ven 31/10 | 2 giornate: mer 29, ven 31 | SCN-12-08 | SCN-13-01 | v3.0 |
| Dom 2 pomeriggio – lun 3/11 | 1 giornata: lun 3 | SCN-13-09 | SCN-14-01 | v3.0 |
| Dopo il finale | calendario fermo ai primi di novembre, casa guarita | SCN-14-06 | — | v3.0 |

### 2.4 Cosa cambia nel mondo dopo ogni capitolo
| Dopo | Cambiamenti persistenti |
|---|---|
| Cap. 1 | Valigie della babuška in casa; lapot' dietro il frigo dal cap. 2 |
| Cap. 2 | Pane e sale dietro il frigo ogni sera; brontolii notturni udibili in cucina (solo Vera e, sottovoce, Mattia) |
| Cap. 3 | Le Donne arrivano martedì, giovedì e sabato notte; Vera può incontrarle (dialoghi brevi) |
| Cap. 4 | Moka di Concetta di nuovo sul fornello; dispetti «residui» casuali in libero (calze spaiate, tazzine storte) finché `casa_guarita` è falso |
| Cap. 5 | Quaderno da investigatrice (pagina Sospettati); Concetta a pranzo la domenica |
| Cap. 6 | Candela del Pokrov in cucina (oggetto consumato a metà) |
| Cap. 7 | Casa malata attiva: crepa, luce, acqua, limone (D-15); casse d'acqua da portare su |
| Cap. 8 | Le Donne restano rigide nell'ingresso; Fomà non risponde |
| Cap. 9 | Lapot' assente; babuška a letto con la febbre (stanza accessibile in punta di piedi) |
| Cap. 11 | Fomà tornato; Giulia più gentile (battute nuove); Mattia «sente» più spesso |
| Cap. 12 | Regola delle pulizie: martedì, giovedì e sabato la casa deve essere in ordine (minigiochi ripetibili in libero) |
| Cap. 13 | Casa guarita (`casa_guarita = true`), fiore del limone, ditale+cucchiaio sulla mensola di Vera |
| Cap. 14 | Lettera di Mattia sulla finestra; rumori di scopa sui tetti in alcune notti di pioggia (aggancio al libro 2) |

---

## 3. Sistemi

Template fisso: **Scopo · Input · Regole · Stati e transizioni · Dati salvati · Interfaccia e feedback · Accessibilità · Casi limite · Dipendenze · Criteri di accettazione**. I campi dei dati salvati si riferiscono allo schema `TDD.md` §4 (radice = oggetto di salvataggio). I criteri usano la console di debug `cr.*` (TDD §11) e sono scritti per Playwright.

### SIS-01 Controller in prima persona
- **Scopo**: muovere Vera con il corpo e lo sguardo di una dodicenne.
- **Input**: *Tastiera e mouse*: W A S D, mouse per guardare, Maiusc corsa (tenere; opzione «corsa a interruttore»), C accovacciarsi (interruttore), Ctrl alternativa per accovacciarsi. *Gamepad*: levetta sinistra muove, destra guarda, pressione levetta sinistra (L3) corsa, B/○ accovacciarsi. *Touch*: joystick virtuale a sinistra, trascinamento a destra per guardare, corsa spingendo il joystick oltre l'85% del raggio, pulsante «Accovacciati».
- **Regole**: altezza di Vera 152 cm, occhi a **1,41 m** (D-55); accovacciata 0,95 m; in ginocchio 0,70 m (solo a punti di interesse, es. dietro il frigo, impronte); seduta in auto 1,08 m. Velocità: camminata 1,30 m/s, corsa 3,40 m/s, accovacciata 0,65 m/s, scale ×0,85. Accelerazione 8 m/s², decelerazione 10 m/s². Gradino massimo superabile 0,22 m; pendenza massima 38°. Capsula di collisione Havok raggio 0,22 m, altezza 1,52/1,00 m. Sguardo verticale ±80°. Oscillazione della camera (head bob) ampiezza 1,2 cm a 1,9 Hz in camminata, disattivabile. Niente corsa dentro casa di notte (camminata automatica lenta, «a piedi nudi»). Il 9° gradino scricchiola se calpestato (SFX-012), saltabile con il tasto Salta-gradino contestuale (E) quando è evidenziato (segreto SEG-01).
- **Stati e transizioni**: `in_piedi` ↔ `accovacciata` (C); `in_piedi/accovacciata` → `in_ginocchio` (E su punto «inginocchiati»), ritorno con E o muovendosi; `seduta` (scene auto, tavolo, panchina) entrata/uscita solo da script; `bloccata` durante cinematiche.
- **Dati salvati**: `giocatore.cella`, `giocatore.pos[3]`, `giocatore.yaw`, `giocatore.pitch`, `giocatore.postura`.
- **Interfaccia e feedback**: nessun HUD fisso; piccolo punto centrale (mirino) opzionale; passi diversi per superficie (pietra, marmo, legno, piastrelle, asfalto, bagnato).
- **Accessibilità**: sensibilità 0,1–3,0; inversione asse Y; head bob on/off; FOV 60–90° (predefinito 72° su PC, 70° su tablet); corsa a interruttore; riduzione movimento (dissolvenze al posto di movimenti di camera forzati).
- **Casi limite**: incastro tra oggetti → dopo 2 s senza progresso con input attivo, spinta di 5 cm verso l'ultimo punto navigabile; uscita dai limiti della cella → riposizionamento all'ultimo punto valido; tablet con tastiera fisica → entrambi gli input attivi.
- **Dipendenze**: Havok (SIS-ENG), streaming (TDD §6), audio passi (AUDIO).
- **Criteri di accettazione**:
  1. `cr.vai("SCN-01-02")`; `cr.stato().giocatore.postura === "in_piedi"`; altezza camera dal suolo = 1,41 ± 0,01 m (`cr.camera().altezza`).
  2. Dopo `cr.input.tieni("KeyW",2000)` la distanza percorsa è 2,6 ± 0,2 m; con Maiusc 6,8 ± 0,4 m.
  3. `cr.input.premi("KeyC")` → postura `accovacciata`, altezza camera 0,95 ± 0,01 m.
  4. Salire 10 gradini da 18 cm in Casa Russo senza blocchi (`cr.test.scale("LUO-CR-SCL")` restituisce `ok`).
  5. Con head bob disattivato l'oscillazione verticale della camera in camminata è < 1 mm.

### SIS-02 Interazione ed evidenziazione
- **Scopo**: capire cosa si può usare e usarlo.
- **Input**: E / clic sinistro (opzione) · A/✕ · tocco sull'oggetto o pulsante «Azione».
- **Regole**: raggio dal centro dello schermo, distanza massima 2,2 m (oggetti) e 3,0 m (persone); cono di tolleranza 4°. Un oggetto interattivo mostra un **contorno caldo sottile** (2 px, colore `#F2D49B`, opacità 0,7) e un'etichetta di una parola («Guarda», «Parla», «Prendi», «Fotografa», «Siediti», «Inginocchiati», «Ascolta»). Le persone girano la testa verso Vera entro 3 m (SIS-13). Gli spiriti non sono evidenziati prima della loro prima apparizione.
- **Stati**: `nessuno` → `puntato` (contorno) → `in uso` (azione) → `usato` (alcuni oggetti tornano `puntato`, altri si disattivano).
- **Dati salvati**: `mondo.interagiti[]` (ID oggetti già usati che cambiano stato), `mondo.oggetti{id:{stato}}`.
- **Interfaccia**: contorno + etichetta in basso al centro (stile UI §7 dell'ART_BIBLE); su tablet l'oggetto puntato si può anche toccare direttamente.
- **Accessibilità**: contorno più spesso (4 px) e colore ad alto contrasto in opzione; «evidenzia tutti gli interattivi vicini» tenendo premuto Tab / LB per 1 s.
- **Casi limite**: due oggetti sovrapposti → vince il più vicino al centro; oggetto dietro vetro → non interattivo salvo eccezioni marcate (vetrinetta del cap. 4).
- **Dipendenze**: SIS-01, raycast Babylon, SIS-03.
- **Criteri**: (1) puntando `OBJ-01-TABELLONE` a 2 m `cr.ui().etichetta === "Guarda"`; (2) a 2,5 m nessuna etichetta; (3) `cr.interagisci("OBJ-01-CARTELLO")` mostra il pensiero `PEN-01-03` in `cr.ui().pensiero` e non aggiunge foto (le foto si fanno solo con il telefono, SIS-07).

### SIS-03 Dialoghi (Ink)
- **Scopo**: parlare con le persone e con gli spiriti come nel libro.
- **Input**: avanzare/saltare la scrittura: Spazio, E, clic · A/✕ · tocco. Scelte: 1–4 o frecce + Invio · croce direzionale + A · tocco. Cronologia: H · View/Share · pulsante nel menu del dialogo.
- **Regole**: storie Ink compilate (inkjs 2.4). Testo che si scrive a **42 caratteri/s** (opzione 20–80 o istantaneo); il primo tocco completa la riga, il secondo avanza. **1–4 scelte**; nessun timer sulle scelte (eccezione: nessuna). Durante il dialogo il personaggio si gira verso Vera (rotazione max 120°/s), la guarda (SIS-13), riproduce animazioni di parlato e gesti (tag Ink `#anim:annuisce`). Le battute doppiate seguono l'audio (avanzamento automatico opzionale). Le battute in russo mostrano il **sottotitolo italiano** e, se l'opzione è attiva, la traslitterazione sotto in corsivo piccolo. Tag Ink supportati: `#parla:PG-ID`, `#vox:VOX-ID`, `#sfx:SFX-ID`, `#anim:nome`, `#cam:nome`, `#pensiero`, `#quaderno:ID`, `#foto:soggetto`, `#rap:nome:+1`, `#lingua:ru|it|scn`, `#attesa:ms`.
- **Stati**: `chiuso` → `apertura` (0,3 s, la camera si stabilizza) → `riga` (scrittura) → `scelte` → `riga`… → `chiusura`.
- **Dati salvati**: `ink.stato` (JSON di `story.state.toJson()`), `ink.cronologia[]` (ultime 200 righe: `{id, pg, testo, lingua}`); variabili specchiate in `rapporti`, `flag`, `casa`, `val`.
- **Interfaccia**: riquadro in basso, 3 righe max, nome del personaggio in maiuscoletto; scelte numerate a destra; colore del nome per personaggio (ART_BIBLE §7).
- **Accessibilità**: dimensione testo S/M/L/XL; sfondo del riquadro opacità 0–100%; avanzamento automatico; lettura dei sottotitoli con contrasto AA.
- **Casi limite**: dialogo interrotto da caricamento → si riprende dall'ultimo nodo stabile (`ink.stato`); scelta già fatta in altri slot → nessun effetto incrociato; dialogo con personaggio che cammina → si ferma.
- **Dipendenze**: inkjs, SIS-13, AUDIO, SIS-06 (quaderno).
- **Criteri**: (1) `cr.vai("SCN-01-05")`, `cr.interagisci("PG-GIULIA")`, `cr.ui().dialogo.scelte.length === 3`; (2) `cr.scegli(2)` imposta `cr.var("flag_giulia_ginevra") === true` e `rap_giulia === 2`; (3) dopo `cr.salva("1")` e `cr.carica("1")` la cronologia contiene la stessa ultima riga; (4) una riga `#lingua:ru` mostra il sottotitolo italiano esatto previsto dalla scena.

### SIS-04 Pensieri di Vera
- **Scopo**: dare la voce ironica di Vera senza fermare il gioco.
- **Input**: nessuno (automatici); ripetibile l'ultimo con H (cronologia).
- **Regole**: sottotitoli in **corsivo**, centrati in alto (25% dall'alto) per non coprire i dialoghi; 3,5 s + 0,06 s per carattere; non più di uno alla volta; i pensieri `[LIBRO]` sono frasi di Vera narratrice; i pensieri `[NUOVO]` hanno la stessa voce. Trigger: guardare un oggetto, entrare in un'area, eventi.
- **Stati**: coda FIFO max 3; i pensieri di bassa priorità vengono scartati se la coda è piena.
- **Dati salvati**: `mondo.pensieriVisti[]` (per non ripetere).
- **Interfaccia**: corsivo bianco caldo con ombra leggera, stessa dimensione dei sottotitoli.
- **Accessibilità**: opzione «pensieri sempre in pausa» (attende un tasto); lettore di schermo.
- **Casi limite**: pensiero durante un dialogo → ritardato alla chiusura.
- **Dipendenze**: SIS-03 (cronologia), trigger di area/sguardo, testi in Ink (knot `pensieri`).
- **Criteri**: `cr.vai("SCN-01-07")`; guardare `OBJ-01-POSTER-ETNA` per 1 s → `cr.ui().pensiero.testo` uguale a `PEN-01-07` e `cr.ui().pensiero.corsivo === true`.

### SIS-05 Sottotitoli dei suoni
- **Scopo**: rendere accessibili i suoni importanti (D-28).
- **Regole**: ogni suono importante ha un ID `SFX-` con testo tra parentesi quadre (es. «[starnuto]», «[la crepa scricchiola]») e **direzione**: freccia ai bordi dello schermo (sinistra/destra/dietro/sopra/sotto) calcolata dalla posizione 3D; se la sorgente è a schermo, nessuna freccia. Un sottotitolo per sorgente; durata = suono + 0,5 s. I suoni che solo Vera sente (spiriti) usano il colore «spiriti» (`#BFD7E8`).
- **Dati salvati**: nessuno (opzioni a parte).
- **Accessibilità**: opzione on/off (predefinito on), dimensione, mostra direzione.
- **Input**: nessuno.
- **Stati**: `nascosto` → `visibile(durata)` → `nascosto`; max 3 sottotitoli contemporanei, impilati.
- **Interfaccia**: testo tra parentesi quadre sotto i dialoghi, freccia direzionale al bordo; colore spiriti `#BFD7E8`, altri suoni bianco caldo.
- **Casi limite**: suono ripetuto (russare) → un solo sottotitolo che resta finché dura il suono; sorgente dietro un muro → direzione comunque calcolata.
- **Dipendenze**: AUDIO (catalogo SFX con posizione), SIS-19.
- **Criteri**: `cr.vai("SCN-01-12")`, `cr.attendi("SFX-001")` → `cr.ui().sottotitoliSuoni[0]` = `{testo:"[starnuto]", direzione:"davanti-sinistra"}` con la borsa a sinistra del centro.

### SIS-06 Quaderno di scienze
- **Scopo**: il diario di Vera (D-25): indizi, parole russe, ricordi, foto, obiettivo, sospettati, il patto, la pagina CASA RUSSO.
- **Input**: J / Tab · Y/△ · pulsante «Quaderno» in alto a destra. Pagine: A/D, frecce, Q/E · LB/RB · trascinare l'angolo della pagina. Chiudere: J, Esc · B/○ · tocco fuori dal quaderno.
- **Regole**: libro 3D in primo piano (mani di Vera visibili) su sfondo sfocato; il gioco è in pausa. Sezioni con linguette: **Obiettivo** (prima pagina aperta sempre) · **Indizi** (IND-) · **Parole russe** (RUS-) · **Ricordi** (RIC-) · **Foto** (FOT-, album Luoghi/Gatti/Persone/Capitoli) · **Sospettati e frecce** (dal cap. 5; le frecce si tracciano trascinando da un sospettato a un indizio) · **Il Patto** (cap. 13) · **CASA RUSSO** (cap. 14). Le prime pagine sono di scienze (cellule e fotosintesi, disegni a biro blu e matita, D-41). Le nuove voci si **scrivono a matita/biro animata** (2 s) con il suono SFX-090 la prima volta che si apre il quaderno dopo lo sblocco; una piccola orecchia segna le sezioni con novità. Nel cap. 4 ogni giorno di indagine ha una pagina con lo spazio per la prova (SIS-21).
- **Stati**: `chiuso` → `aperto(sezione,pagina)` → `scrittura` (animazione) → `aperto`.
- **Dati salvati**: `quaderno.voci[] {id, sbloccata (data di gioco ISO), letta}`, `quaderno.obiettivo` (ID OBJ-), `quaderno.sospettati.frecce[] [da, a]`, `quaderno.patto` (bool), `quaderno.paginaCasaRusso` (bool), `quaderno.ultimaPagina {sezione, pagina}`.
- **Interfaccia**: carta a quadretti 5 mm, margine rosso, testo a mano (font ART_BIBLE §7); il testo delle voci è anche disponibile in versione stampatello ad alta leggibilità (opzione).
- **Accessibilità**: «testo leggibile» sostituisce la grafia con font chiaro; lettura con lettore di schermo del testo delle pagine (ARIA live region).
- **Casi limite**: sblocco di più voci insieme → si scrivono in sequenza; quaderno aperto durante un evento a tempo → impossibile (le scene a tempo lo disabilitano con icona grigia).
- **Dipendenze**: SIS-03, SIS-07, SIS-09.
- **Criteri**: (1) `cr.vai("SCN-01-16")` con tutte le voci del cap. 1 → `cr.stato().quaderno.voci` contiene `IND-01-01…IND-01-07`, `RUS-01…RUS-08`, `RIC-01`, `RIC-02`; (2) `cr.quaderno.apri("sospettati")` prima del cap. 5 restituisce `bloccata`; (3) trascinare `SOS-FOMA` su `IND-04-03` aggiunge la freccia allo stato.

### SIS-07 Telefono di Vera
- **Scopo**: fotocamera, torcia, orologio e data (D-26).
- **Input**: F (alza il telefono in modalità foto; F o clic sinistro scatta; Esc/F di nuovo abbassa) · X/□ (alza), RT (scatta) · pulsante «Telefono» poi «Foto» e pulsante di scatto a schermo. Torcia: T · LB/L1 · interruttore nel telefono. Orologio/data: Q · RB/R1 · pulsante «Telefono».
- **Regole**: il telefono è un oggetto 3D nelle mani di Vera (cover blu con adesivo di un dinosauro regalato da Nicolò dal cap. 3 [NUOVO]). **Foto**: zoom 1×–3× (rotella, levette, pizzico); un **soggetto fotografabile** (`FOT-…`) è riconosciuto se è inquadrato per almeno il 12% dell'area, entro la sua distanza massima e non coperto oltre il 40%; la foto si salva comunque (album «Altre», max 60) anche senza soggetto. Gli **spiriti non compaiono nelle foto** (rendering escluso dal layer foto): la foto mostra il lapot', la nebbia leggera o niente, con pensiero di Vera (PEN-FOT-SPIRITI). **Torcia**: cono 35°, 12 m, ombra dinamica; durata illimitata. **Orologio**: mostra ora, data e giorno della storia, notte delle Donne con un'icona di ventaglio (dal cap. 3).
- **Stati**: `in_tasca` → `alzato_foto` → `scatto` → `alzato_foto`; `torcia on/off` indipendente; `schermata_orologio`.
- **Dati salvati**: `telefono.foto[] {id, soggetto|null, data, miniatura (chiave IndexedDB)}`, `telefono.torcia` (bool).
- **Interfaccia**: schermo del telefono con interfaccia semplice (senza marchi), griglia dei terzi opzionale, cornice gialla attorno al soggetto riconosciuto.
- **Accessibilità**: scatto assistito (aggancia il soggetto più vicino al centro con 1 s di mira); scatto su rilascio per il touch.
- **Casi limite**: foto durante il dialogo → non consentita; memoria di foto libere piena → si sostituisce la più vecchia dopo conferma.
- **Dipendenze**: SIS-06, render-to-texture, IndexedDB.
- **Criteri**: (1) `cr.vai("SCN-01-07")`, puntare `FOT-01-01` (tabellone) a 6 m e `cr.input.premi("KeyF")` due volte → `cr.stato().telefono.foto` contiene un elemento con `soggetto:"FOT-01-01"`; (2) foto di Fomà al cap. 2 → nessun pixel del layer «spiriti» nella miniatura (`cr.test.fotoContieneLayer("spiriti") === false`); (3) `cr.data("2025-09-16","22:00")` → `cr.ui().telefono.data === "martedì 16 settembre"` e icona Donne attiva dal cap. 3.

### SIS-08 Missioni, obiettivi e marker discreto
- **Scopo**: guidare senza togliere autonomia (D-16).
- **Input**: nessuno diretto; il marker si mostra/nasconde dalle opzioni o tenendo premuto J per 0,6 s.
- **Regole**: missione = capitolo (`MIS-CC`) o secondaria (`MIS-S-NN`). Ogni scena ha un **obiettivo** (`OBJ-CC-NN`) scritto a mano nella prima pagina del quaderno, con la voce di Vera (es. «Parlare con la famiglia. Almeno con tre. Mattia conta doppio, perché scappa.»). **Marker discreto**: piccolo cerchio caldo con punto (14 px) proiettato sull'obiettivo, visibile solo se l'obiettivo è fuori vista per più di 20 s o se il giocatore resta fermo 30 s; scompare entro 8 m. Disattivabile (D-16). Eventi a script attivati da: area, interazione, tempo, variabile.
- **Stati della missione**: `bloccata` → `attiva` → `completata`; secondarie anche `fallita_morbida` (si riprova).
- **Dati salvati**: `storia.capitolo`, `storia.scena`, `storia.checkpoint`, `storia.capitoliCompletati[]`, `missioni.attive[] {id, passo}`, `missioni.completate[]`, `quaderno.obiettivo`.
- **Interfaccia**: notifica in alto a sinistra «Nuovo obiettivo» con l'icona della matita per 3 s.
- **Accessibilità**: marker sempre visibile (opzione), testo obiettivo letto ad alta voce dal lettore di schermo.
- **Casi limite**: obiettivo in un'altra cella non caricata → il marker indica la direzione dell'uscita più vicina.
- **Dipendenze**: SIS-06, SIS-11, streaming (TDD §6), testi OBJ- in NARRATIVA.
- **Criteri**: `cr.vai("SCN-01-02")` → `cr.stato().quaderno.obiettivo === "OBJ-01-02"`; con marker attivo e giocatore fermo 30 s `cr.ui().marker.visibile === true`; con opzione disattivata mai visibile.

### SIS-09 Fallimento morbido
- **Scopo**: nessuna punizione (D-07).
- **Regole**: una condizione di fallimento (Mattia perso, rumore troppo forte in una scena silenziosa, impronta persa, minigioco sbagliato tre volte) avvia una **scenetta buffa di 4–8 s** ([NUOVO], specifica per capitolo) e riporta Vera all'**ultimo punto sicuro** (`storia.puntoSicuro`, aggiornato ogni volta che si completa un passo). Nulla si perde: quaderno, foto, collezioni, variabili restano. Dopo 2 fallimenti nello stesso punto compare un **aiuto** (es. il marker si accende, Mattia indica più a lungo). Nessuna schermata «Hai perso».
- **Stati**: `normale` → `scena_buffa` → `ripartenza`.
- **Dati salvati**: `storia.puntoSicuro {scena, pos, yaw}`, `statistiche.fallimentiMorbidi`, `storia.aiuti{scena:int}`.
- **Input**: nessuno; la scenetta si salta con Azione dopo 1 s.
- **Interfaccia**: nessun testo di sconfitta; dissolvenza breve con la pagina del quaderno «Riproviamo».
- **Accessibilità**: opzione «aiuti immediati» (l'aiuto compare già al primo fallimento).
- **Casi limite**: fallimento durante un salvataggio → il salvataggio viene completato prima della ripartenza; fallimento ripetuto 5 volte → il passo si completa da solo con un pensiero di Vera.
- **Dipendenze**: SIS-08, SIS-10, scene buffe per capitolo (NARRATIVA).
- **Criteri**: `cr.vai("SCN-01-14")`, `cr.fallisci()` → entro 9 s `cr.stato().giocatore.pos` = `puntoSicuro.pos` (± 0,1 m) e `quaderno.voci` invariato.

### SIS-10 Salvataggi
- **Scopo**: non perdere mai nulla, anche tra versioni (D-68).
- **Input**: menu Pausa → Salva/Carica; titolo → Continua.
- **Regole**: autosalvataggio a ogni checkpoint `CP-`, alla fine di ogni scena e ogni 120 s in mondo libero (mai durante un dialogo aperto: si salva il nodo stabile precedente). 3 slot manuali + 1 auto + copia di sicurezza della penultima versione. Stato JSON con `versione` (schema, intero, oggi **1**) e `versioneGioco`. Migrazioni in catena `1→2→3…` (TDD §4.3). **Esporta** (file `.casarusso.json`) e **Importa** (con validazione dello schema e anteprima: capitolo, data di gioco, tempo di gioco). Le miniature delle foto stanno in un archivio IndexedDB separato e si esportano incluse in base64 nel file.
- **Stati**: `idle` → `scrittura` (icona di matita in basso a destra, mai bloccante) → `idle` / `errore` (riprova 3 volte, poi avviso).
- **Dati salvati**: tutto lo schema TDD §4.
- **Interfaccia**: elenco slot con capitolo, scena, data della storia, tempo di gioco, miniatura dell'ultima inquadratura.
- **Accessibilità**: conferma per sovrascrivere con testo chiaro.
- **Dipendenze**: IndexedDB, TDD §4 (schema e migrazioni), SIS-07 (miniature).
- **Casi limite**: spazio IndexedDB esaurito → avviso e suggerimento di esportare; salvataggio di una versione più nuova del gioco → non caricabile, messaggio chiaro; file corrotto → si usa la copia di sicurezza.
- **Criteri**: (1) `cr.salva("1")`, ricarica pagina, `cr.carica("1")`, deep-equal dello stato (esclusi `aggiornato`); (2) import di `tests/fixtures/salvataggio_v1_cap3.json` in v2.0 → `cr.stato().versione === 2` e `storia.capitolo === 4` pronto; (3) export → import → stato identico.

### SIS-11 Calendario, tempo, meteo, notti delle Donne
- **Scopo**: il calendario reale del 2025 (D-20, D-54).
- **Regole**: data e minuti del giorno; scala tempo (SIS §2.2). **Sole**: posizione calcolata (algoritmo NOAA) per 37,852° N, 15,287° E, fuso Europe/Rome; luce dinamica sopra la base baked (TDD §5). **Meteo per data** da tabella (ART_BIBLE §2): settembre sereno; ottobre sereno/velato; 4 novembre pioggia. **Notti delle Donne**: martedì, giovedì, sabato dalle 23:30 alle 04:00 dal cap. 3 in poi; in mondo libero, se Vera è sveglia in casa in quelle ore, la nebbia entra dal buco della serratura (incontro breve, dialogo variabile secondo `rap_rosalia`, `rap_nina`, `rap_tina` e capitolo).
- **Stati**: `giorno`/`notte`, `meteo` (sereno, velato, ventoso, pioggia, temporale), `notteDonne` (bool).
- **Dati salvati**: `tempo.data` (AAAA-MM-GG), `tempo.minuti` (0–1439), `tempo.meteo`, `tempo.scala`.
- **Interfaccia**: nessun orologio a schermo; si legge sul telefono (SIS-07).
- **Input**: telefono per leggere l'ora (SIS-07); debug `cr.data`.
- **Accessibilità**: opzione «ferma il tempo in libero» (scala 0) per chi gioca lentamente.
- **Casi limite**: cambio di giorno durante una missione secondaria → la missione resta attiva se la finestra lo consente; notte delle Donne durante una scena di trama → la scena ha la precedenza.
- **Dipendenze**: TDD §5 (luce dinamica), ART_BIBLE §2 (palette per ora e mese), SIS-12, SIS-13.
- **Criteri**: `cr.data("2025-09-16","23:45")` dopo il cap. 3 → `cr.stato().tempo` e `cr.ui().notteDonne === true`; `cr.data("2025-09-17","23:45")` → false; il 4/11 `tempo.meteo === "pioggia"`.

### SIS-12 Stato della casa (crepa, luce, acqua, limone)
- **Scopo**: rendere visibile la casa malata, anche in libero (D-15).
- **Regole**: quattro variabili intere: `casa_crepa` 0–5 (0 nessuna; 1 una mano; 2 due mani; 3 tre mani; 4 fino al soffitto con intonaco caduto; 5 ramo verso la camera dei genitori), `casa_luce` 0–3 (frequenza dei salti: 0 mai, 1 ogni 60 min di gioco, 2 ogni 20, 3 ogni 8), `casa_acqua` 0–3 (0 limpida, 1 sa di ferro, 2 ferro + ruggine, 3 marrone), `casa_limone` 0–4 (0 sano, 1 foglie gialle, 2 metà foglie, 3 limoni verdi caduti, 4 rami nudi «come dita»), `casa_guarita` bool. Valori impostati dalle scene (cap. 7, 8, 9, 12, 13) e, in libero, dall'avanzare dei giorni del cap. 7 (+1 crepa al giorno fino a 3). Collegamenti: crepa = decal con maschera di crescita su 6 stadi; luce = eventi di blackout (tutte le luci della casa spente, SFX-040, papà scende al quadro elettrico se presente); acqua = colore del flusso del rubinetto e pensiero di Vera; limone = mesh con foglie per stadio + particelle di foglie che cadono; suoni della casa (scricchiolii, tosse dei muri SFX-044 di notte a `casa_crepa ≥ 3`). Con `casa_guarita` tutto torna a 0 e compare il fiore del limone.
- **Dati salvati**: `casa.casa_crepa`, `casa.casa_luce`, `casa.casa_acqua`, `casa.casa_limone`, `casa.casa_guarita`.
- **Input**: nessuno diretto; si osserva e si interagisce con rubinetto, quadro elettrico, limone, crepa.
- **Stati**: `sana` → `malata(livelli)` → `guarita`; i livelli salgono solo per script e per i giorni del cap. 7; da `guarita` non si torna indietro.
- **Interfaccia**: nessun indicatore: crepa, luci, acqua, foglie e suoni sono il feedback; il quaderno ha una pagina «La casa» con lo schizzo della crepa che si aggiorna.
- **Accessibilità**: i blackout hanno sempre il sottotitolo SFX-040 e una luce minima di sicurezza (luna, lampione) per non lasciare lo schermo nero; opzione «niente lampeggi».
- **Casi limite**: blackout durante il quaderno o un dialogo → rimandato; caricamento di un salvataggio vecchio senza campi `casa` → migrazione con valori del capitolo.
- **Dipendenze**: SIS-10, SIS-11, ART_BIBLE (materiali e decal), AUDIO.
- **Criteri**: `cr.casa({crepa:3,luce:2,acqua:1,limone:2})` → `cr.test.decalCrepaStadio() === 3`; entro 25 min di gioco a scala 40× avviene un blackout (`cr.eventi()` contiene `BLACKOUT`); `cr.casa({guarita:true})` → tutte le variabili a 0 e `OBJ-CR-FIORE-LIMONE` visibile.

### SIS-13 Personaggi non giocanti
- **Scopo**: persone credibili e il «chi vede cosa» (D-24).
- **Regole**: routine orarie per personaggio (PERSONAGGI §routine, `LIVELLI` posizioni) eseguite su navmesh per cella (Navigation Plugin V2, D-62) con crowd per le comparse (max 24 agenti attivi su PC, 12 su tablet). **Sguardo**: rotazione testa/collo verso Vera entro 3 m e 100° dal davanti, smorzata (0,25 s), con ammiccamenti casuali. **Attraverso gli spiriti**: gli adulti hanno un «filtro» — se lo sguardo incrocerebbe uno spirito, la testa punta 15 cm oltre (attraverso), e le loro battute ambiente offrono spiegazioni normali (formiche, vento, topi, umidità). **Mattia** reagisce ai suoni degli spiriti girando la testa verso la sorgente e indicando le tracce (impronte, briciole); **Giulia** dal cap. 11 ha un piccolo ritardo nello sguardo «come se avesse sentito qualcosa». **Le nonne** non vedono ma *sanno*: in presenza di uno spirito fanno il segno della croce (Concetta da sinistra a destra, babuška da destra a sinistra) o si stringono la vestaglia (13.038).
- **Stati**: `routine` → `attenzione` (Vera vicina) → `dialogo` → `routine`; `scena` (controllato da script).
- **Dati salvati**: solo per i PNG legati a missioni attive: `npc{PG-ID:{cella, pos, routine, passo}}`.
- **Input**: nessuno (interazione via SIS-02).
- **Interfaccia**: nessuna; il nome compare solo in dialogo.
- **Accessibilità**: opzione «persone più lente» (velocità di camminata ×0,8) per seguire i personaggi.
- **Casi limite**: PNG bloccato → dopo 3 s teletrasporto fuori vista sul punto successivo della routine; PNG che dovrebbe essere in una cella non caricata → simulazione astratta della routine (solo posizione logica).
- **Dipendenze**: Navigation Plugin V2, animazioni (PIPELINE_ASSET), PERSONAGGI routine, SIS-11.
- **Criteri**: (1) con `cr.vai("SCN-03-09")` il raggio di sguardo di Irina (se presente in scena di test) non interseca il bounding box di Fomà; (2) `cr.test.mattiaReagisce("SFX-020")` → testa di Mattia orientata verso la sorgente entro 0,6 s.

### SIS-14 Rapporti
- **Scopo**: le scelte cambiano rapporti e battute (D-06).
- **Regole**: variabili `rap_*` intere da −3 a +3 (default 0; Giulia default −1: «nata senza la parte del cervello che si stupisce»). Soglie: ≤ −2 freddo, −1…+1 normale, ≥ +2 caldo. Gli effetti cambiano battute, piccole azioni (es. Giulia che copre Vera) e alcune scene alternative elencate in `NARRATIVA/00_struttura.md`. Nessuna schermata di punteggio: si vede solo nel comportamento e in una frase del quaderno nella pagina «Persone» (dal cap. 5).
- **Dati salvati**: `rapporti{rap_*}`.
- **Input**: scelte di dialogo (SIS-03) e alcune azioni (aiutare, fotografare con permesso).
- **Stati**: valore intero per personaggio; nessuna transizione a soglia irreversibile.
- **Interfaccia**: nessun numero visibile; pagina «Persone» del quaderno con una frase per personaggio che cambia con la fascia.
- **Accessibilità**: —
- **Casi limite**: valori fuori intervallo → limitati a −3/+3; salvataggi vecchi senza un `rap_` nuovo → default.
- **Dipendenze**: SIS-03, NARRATIVA/00_struttura (dizionario delle variabili).
- **Criteri**: `cr.var("rap_giulia",2)`; `cr.vai("SCN-01-15")` → la scena usa il ramo `giulia_alleata` (`cr.ui().dialogo` contiene la riga `DLG-01-GIULIA-20`).

### SIS-15 Collezioni
- **Scopo**: raccogliere le due metà di Vera (D-69).
- **Regole**: insiemi e conteggi in §4. Ogni voce sbloccata appare nel quaderno; completare un insieme per rilascio dà una pagina speciale del quaderno e un effetto nel mondo (§4).
- **Dati salvati**: `collezioni.col_rus[]`, `collezioni.col_ric[]`, `collezioni.col_fot[]`, `collezioni.col_seg[]`.
- **Input**: foto (SIS-07), dialoghi (SIS-03), interazioni (SIS-02).
- **Stati**: voce `bloccata` → `sbloccata` → `letta`.
- **Interfaccia**: notifica «+1 Parole russe» con la parola in cirillico e traslitterazione per 3 s; contatori nelle linguette del quaderno («12/17»).
- **Accessibilità**: elenco testuale delle voci mancanti per zona (opzione «aiuto collezioni»).
- **Casi limite**: voce sbloccata due volte → ignorata; voce di un rilascio futuro → non esiste nel catalogo.
- **Dipendenze**: SIS-06, cataloghi in NARRATIVA.
- **Criteri**: `cr.collezioni()` restituisce i conteggi per insieme e rilascio coerenti con §4.

### SIS-16 Bar di papà
- **Scopo**: attività ricorrente nel mondo libero (D-19).
- **Input**: interazione con banco, macchina del caffè, vetrina, clienti.
- **Regole**: turno di 6 minuti reali (pomeriggio). I clienti chiedono una cosa a voce (testo + parole chiave): caffè, macchiato, cappuccino (solo la mattina: se un turista lo chiede al pomeriggio, papà fa una faccia), granita al limone/mandorla/caffè con brioche, cornetto, arancino (dalla vetrina), acqua. Vera prepara con 2–4 passi (prendi tazzina, macchina, servi; granita: coppa, gusto, brioche). Ordini sbagliati: il cliente ride, papà corregge (nessuna penalità). Clienti con battute ([NUOVO], `mondo_libero.md`), che cambiano con capitolo e stagione (turisti in pantaloncini a ottobre; solo paesani dopo il 4 novembre, 14.001). Compiti al tavolino in fondo vicino al bagno (06.001): sedersi fa passare 1 ora e dà a volte un pensiero.
- **Dati salvati**: `bar.turni`, `bar.ordiniServiti`, `bar.miglioreTurno`, `bar.clientiConosciuti[]`.
- **Stati**: `fuori turno` → `turno` (ordini in coda, max 3) → `fine turno` (papà commenta).
- **Interfaccia**: il blocchetto delle comande di papà appare in basso a sinistra con gli ordini scritti a mano.
- **Accessibilità**: opzione «ordini con figure» (icone accanto alle parole).
- **Casi limite**: turno interrotto dalla sera → si chiude con il commento di papà; capitolo in cui il bar è chiuso (sera del cap. 14) → interazione disabilitata con pensiero.
- **Dipendenze**: SIS-13 (clienti), mondo_libero (battute), LIVELLI (bar).
- **Criteri**: `cr.bar.avviaTurno()`; `cr.bar.servi("caffè")` corretto → `bar.ordiniServiti +1`; errore → nessuna variazione negativa di variabili.

### SIS-17 Missioni secondarie
- **Regole**: 12 missioni (`MIS-S-01…12`) definite in `mondo_libero.md`, con datore, passi, ricompensa e finestra di calendario. Una alla volta per datore; più missioni attive insieme (max 4).
- **Dati salvati**: `missioni.attive`, `missioni.completate`.
- **Scopo**: storie piccole di Taormina tra i capitoli (D-19).
- **Input**: dialogo con il datore, interazioni.
- **Stati**: `disponibile` → `attiva(passo)` → `completata`; `fuori finestra` quando il calendario esce dalla finestra (resta nel quaderno come «da finire» e si riprende alla finestra successiva, se prevista).
- **Interfaccia**: pagina «Commissioni» nel quaderno con elenco puntato a biro.
- **Accessibilità**: marker sempre attivo per le secondarie (opzione).
- **Casi limite**: missione attiva quando inizia un capitolo → sospesa e ripresa dopo.
- **Dipendenze**: SIS-08, SIS-11, mondo_libero.
- **Criteri**: ogni missione ha un test `cr.test.missione("MIS-S-NN")` che la completa via debug e verifica la ricompensa.

### SIS-18 Segreti di casa
- **Regole**: 16 segreti (`SEG-01…16`) in Casa Russo e casa di Concetta (elenco in `mondo_libero.md`); ogni segreto richiede un'azione (inginocchiarsi, guardare dal buco della serratura, saltare il 9° gradino, aprire un cassetto a una certa ora…) e sblocca una voce SEG nel quaderno.
- **Dati salvati**: `collezioni.col_seg[]`.
- **Scopo**: premiare chi esplora la casa a fondo.
- **Input**: interazioni contestuali (E), postura (in ginocchio, accovacciata), ora del giorno.
- **Stati**: `nascosto` → `scoperto`.
- **Interfaccia**: voce SEG con schizzo nel quaderno; suono SFX-091 «[fruscio di pagina]».
- **Accessibilità**: opzione «aiuto collezioni» mostra un indizio testuale per segreto.
- **Casi limite**: segreto legato a uno stato della casa (es. crepa) → disponibile solo in quella finestra; se mancato, si sblocca nella versione «ricordo» dopo il finale.
- **Dipendenze**: SIS-12, SIS-11, LIVELLI.
- **Criteri**: `cr.test.segreto("SEG-01")` (saltare il 9° gradino di notte) aggiunge `SEG-01` a `collezioni.col_seg`.

### SIS-19 Menu e opzioni
- **Regole**: Titolo (Continua, Nuova partita, Carica, Opzioni, Crediti); Pausa (Riprendi, Quaderno, Salva, Carica, Opzioni, Comandi, Torna al titolo). **Opzioni**: *Grafica* (preset Basso/Medio/Alto/Ultra/Automatico, scala risoluzione 50–100%, FPS max 30/60/illimitato, singole voci del preset), *Controlli* (sensibilità, inverti Y, corsa a interruttore, rimappatura, vibrazione gamepad), *Audio* (generale, ambienti, voci, effetti, mono, riduzione dinamica), *Sottotitoli* (dimensione S/M/L/XL, sfondo, suoni on/off, direzione, traslitterazione russa), *Gioco* (marker discreto, velocità del testo, avanzamento automatico, head bob, FOV, riduzione movimento, evidenziazione forte, testo leggibile del quaderno). Opzioni salvate a parte (`localStorage` con copia in IndexedDB) e non nel salvataggio di gioco.
- **Scopo**: avviare, mettere in pausa e regolare il gioco.
- **Input**: mouse/tastiera, gamepad (croce + A/B), touch.
- **Stati**: `titolo` → `gioco` ↔ `pausa` → `opzioni`/`salva`/`carica`.
- **Dati salvati**: opzioni fuori dal salvataggio: chiave `casarusso.opzioni.v1`.
- **Interfaccia**: menu in stile quaderno (carta, biro), voce selezionata sottolineata a matita.
- **Accessibilità**: navigazione completa da tastiera e gamepad, focus visibile, contrasto AA, dimensione UI 90–130%.
- **Casi limite**: cambio preset con memoria insufficiente → avviso e ritorno al preset precedente.
- **Dipendenze**: TDD §12 (preset), SIS-10.
- **Criteri**: `cr.opzioni.set("sottotitoli.dimensione","XL")` → altezza del font dei sottotitoli ≥ 36 px a 1080p; preset cambia senza ricaricare la pagina.

### SIS-20 Console di debug
- **Scopo**: sviluppo e test automatici. Specifica completa in `TDD.md` §11.
- **Regole**: attiva con `?debug=1` o tasto `\` tre volte; oggetto globale `window.cr`. Disattivata nelle build di rilascio salvo parametro.
- **Input**: console del browser; tastiera `\` ×3.
- **Stati**: disattivata / attiva (pannello prestazioni opzionale).
- **Dati salvati**: nessuno (i comandi agiscono sullo stato normale).
- **Interfaccia**: pannello trasparente con FPS, draw call, triangoli, memoria texture, cella corrente, scena e checkpoint.
- **Accessibilità**: —
- **Casi limite**: comando con ID inesistente → errore leggibile, nessuna modifica.
- **Dipendenze**: tutti i sistemi espongono un'interfaccia di debug.
- **Criteri**: ogni comando elencato nel TDD ha un test Playwright di fumo.

### SIS-21 Indagine giorno per giorno (cap. 4)
- **Scopo**: la «guerra delle tazzine» come gioco (D-10).
- **Regole**: 7 giorni (ven 19 → ven 26 settembre, salto sab–dom 20–21 con una giornata breve) con un dispetto al giorno (moka, kefir, lenzuola, calze, tazzine, pane, moka col sale). Ogni giorno: (1) scoperta del dispetto (scena), (2) **ricerca di una prova** nella casa (1–3 punti di interesse; es. luccichio di alluminio dietro il frigo, un capello di nebbia sul bordo della vetrinetta, briciole di pane nero, odore di rosmarino sulle lenzuola, una frase sentita di notte), (3) **annotazione nel quaderno**: trascinare la prova sulla pagina del giorno e scegliere tra due colpevoli («le Donne» / «Fomà»); se si sceglie «le nonne», Vera scrive e cancella (PEN-04-NONNE) — prepara il cap. 5. Non si può sbagliare in modo bloccante: una scelta sbagliata è corretta il giorno dopo da un nuovo indizio.
- **Dati salvati**: `val.val_prove_cap4` (0–7), `flag.flag_prova_moka`, `flag.flag_prova_kefir`, `flag.flag_prova_lenzuola`, `flag.flag_prova_calze`, `flag.flag_prova_tazzine`, `flag.flag_prova_pane`, `flag.flag_prova_sale`, `quaderno.voci`.
- **Input**: come SIS-02 e SIS-06 (trascinare la prova sulla pagina).
- **Stati**: per giorno: `dispetto` → `ricerca` → `annotazione` → `fatto`.
- **Interfaccia**: pagina del giorno nel quaderno con il disegno del dispetto e una cornice vuota per la prova.
- **Accessibilità**: la prova si può annotare anche con un tasto (Azione) invece del trascinamento.
- **Casi limite**: giocatore che dorme senza cercare la prova → la prova viene annotata da sola il giorno dopo con «L'ho capito dopo» (nessun blocco).
- **Dipendenze**: SIS-06, SIS-11, cap04.
- **Criteri**: completare via debug i 7 giorni → `val_prove_cap4 === 7`, `IND-04-01…07` presenti; con 4 prove su 7 il capitolo si chiude ugualmente (le prove mancanti si annotano da sole con frase «L'ho capito dopo»).

### SIS-22 Barra della tensione della casa (cap. 8)
- **Scopo**: D-11.
- **Regole**: `val.val_tensione_casa` 0–100, parte da 40. Le risposte di Vera durante il consiglio alzano (+5…+15) o abbassano (−5…−10) la tensione; anche il tempo senza risposta la alza (+1 ogni 4 s). Soglie: 50 ante dei pensili, 60 frigo più forte, 70 lampadina, 80 crepa (crac). **Qualsiasi percorso arriva a 100** (il libro arriva all'urlo): le risposte cambiano *quanto in fretta* e *quali battute* (ramificazioni in cap08). A 100 → cinematica «BASTA! Di chi sono io?» (SCN-08-06). La barra **non è un HUD**: si legge nella casa (vibrazione delle stoviglie, tremolio della luce, cuore di Vera nel suono) e, se l'opzione accessibilità è attiva, come sottile cornice rossa ai bordi.
- **Dati salvati**: `val.val_tensione_casa`, `flag.flag_consiglio_calma` (se Vera ha provato almeno due risposte calme).
- **Input**: scelte di dialogo (SIS-03).
- **Stati**: `calma` (<50) → `scricchiolii` (50–79) → `crepa` (80–99) → `urlo` (100).
- **Interfaccia**: nessuna barra a schermo salvo opzione accessibilità (cornice rossa sottile).
- **Accessibilità**: opzione «niente lampeggi» sostituisce il lampeggio della lampadina con un affievolimento lento.
- **Casi limite**: pausa durante il consiglio → tensione congelata; caricamento a metà → riparte da SCN-08-04 con valore salvato.
- **Dipendenze**: SIS-03, SIS-12, AUDIO (cuore, stoviglie).
- **Criteri**: `cr.vai("SCN-08-04")`, nessun input per 60 s → tensione 55 ± 2; serie di risposte calme → tensione minima 25 e poi comunque l'evento a 100 entro 4 minuti.

### SIS-23 Impronte di farina con Mattia (cap. 10)
- **Scopo**: D-12.
- **Regole**: Mattia cammina avanti di 3–6 m, si ferma, «annusa» (animazione) e indica un'area (cerchio di 1,5 m sul terreno); Vera deve **inginocchiarsi** (E) dentro l'area e guardare: la torcia del telefono o il sole radente rendono visibile un puntino bianco (decal con maschera di visibilità angolare: visibile solo da < 1,2 m e con camera < 1,0 m dal suolo). 18 impronte dalla porta di casa alla funivia; poi 6 da Mazzarò alla strada lungo il mare. Se Vera ignora Mattia per più di 40 s o si allontana oltre 25 m → fallimento morbido (Mattia si siede sul gradino con il coniglio: «Allora non vieni?»). Il bar di papà va superato senza farsi vedere (SCN-10-04): cono di vista di papà attraverso la vetrina, passare quando serve un cliente.
- **Dati salvati**: `val.val_impronte_trovate`, `flag.flag_bar_evitato`.
- **Input**: E per inginocchiarsi; torcia (T) per vedere meglio all'ombra.
- **Stati**: per impronta: `nascosta` → `indicata da Mattia` → `trovata`.
- **Interfaccia**: nessun indicatore oltre al dito di Mattia e al cerchio di sole sul terreno; contatore solo nel quaderno.
- **Accessibilità**: opzione «impronte più evidenti» (visibili da 2 m).
- **Casi limite**: folla di turisti sul Corso → l'area indicata è sempre sgombrata dagli agenti della crowd.
- **Dipendenze**: SIS-01, SIS-13, decal con visibilità angolare (TDD §7).
- **Criteri**: `cr.test.impronte.completa()` → `val_impronte_trovate === 24`; impronta invisibile a camera alta 1,41 m (`cr.test.visibile("IMP-10-05") === false`) e visibile in ginocchio vicino.

### SIS-24 Pulizie a minigiochi (cap. 12)
- **Scopo**: D-13.
- **Regole**: 4 minigiochi da 45–90 s, rigiocabili in libero il martedì/giovedì/sabato: **Lenzuola dritte** (tirare gli angoli: trascinare 4 maniglie finché la tensione è uniforme, tolleranza 6°), **Mollette uguali** (abbinare 12 mollette di 4 colori sul filo, coppie dello stesso colore per ogni lenzuolo), **Scale** (strofinare i 18 gradini col panno: tenere premuto e muovere; macchie che si riducono; il 9° scricchiola e ha una macchia più ostinata), **Rosmarino sul piattino** (raccogliere un rametto dal vaso del balcone e posarlo senza bruciarlo, 12.022). Nessun tempo limite duro: valutazione in tre «stelline di pulito» che cambiano una battuta di Donna Rosalia; mai bloccante.
- **Dati salvati**: `val.val_pulizie_punteggio` (0–12), `flag.flag_pulizie_complete`.
- **Input**: trascinamento con mouse/touch; levette e grilletti sul gamepad.
- **Stati**: per minigioco: `pronto` → `in corso` → `valutato`.
- **Interfaccia**: inquadratura ravvicinata sulle mani di Vera; stelline di «pulito» disegnate a matita.
- **Accessibilità**: modalità «senza fretta»: nessuna valutazione, solo completamento.
- **Casi limite**: uscita a metà → il minigioco riparte da capo senza perdite.
- **Dipendenze**: SIS-12 (regola delle pulizie), cap12.
- **Criteri**: ogni minigioco ha `cr.test.minigioco(id,"perfetto")` → +3 stelline; il capitolo prosegue anche con 4/12.

### SIS-25 Caccia ai cannistri e ditale + cucchiaio (cap. 13)
- **Scopo**: D-14.
- **Regole**: mattina del 2 novembre: tre cesti nascosti (Vera, Mattia, Giulia) nei punti dove Concetta è salita la notte (D-49: armadio del corridoio, sotto il letto di Mattia, dietro la tenda della camera di Giulia) più 5 dolci sparsi (frutta martorana, pupo di zucchero…). Mattia e Giulia cercano i loro con battute; Vera trova il suo per ultimo. Nel suo cesto, sotto i tetù, **il ditale** e **il cucchiaio**: interazione a due mani (mouse: trascinare il ditale sul manico; gamepad: levette sinistra e destra; touch: due dita) fino all'incastro (feedback tattile/vibrazione e SFX-069 «[clic leggero: ditale nel cucchiaio]»).
- **Dati salvati**: `val.val_cannistri_trovati` (0–3), `val.val_dolci_trovati` (0–5), `flag.flag_ditale_cucchiaio_uniti`.
- **Input**: ricerca libera; unione con due mani (mouse, levette, due dita).
- **Stati**: `notte` → `mattina caccia` → `trovati` → `uniti`.
- **Interfaccia**: nessun indicatore; Mattia e Giulia commentano «acqua, fuochino, fuoco» se Vera è vicina a un cesto (Giulia solo con `rap_giulia ≥ 1`).
- **Accessibilità**: unione eseguibile anche con un solo tasto tenuto per 2 s.
- **Casi limite**: cesto di Mattia trovato da Vera → Vera lo lascia dov'è e chiama Mattia (battuta [NUOVO]).
- **Dipendenze**: SIS-02, SIS-13, cap13.
- **Criteri**: `cr.test.cannistri.completa()` → `val_cannistri_trovati === 3`; `cr.test.unisci()` → `flag_ditale_cucchiaio_uniti === true` e oggetto `OBJ-13-DITALE-CUCCHIAIO` sulla mensola di Vera nel mondo libero.

### SIS-26 Scene guidate e cinematiche
- **Regole**: *guidata* = il giocatore controlla lo sguardo (e a volte il passo) ma il percorso è vincolato (cap. 2 seguire la babuška: muro invisibile morbido a 1 m dal percorso; nessun rischio di essere scoperti, D-09); *cinematica* = camera animata (primi piani, DOF), saltabile solo se già vista (tenere premuto Esc/B 1 s). Le camere delle cinematiche simulano sempre lo sguardo di Vera (prima persona) salvo i neri con narrazione.
- **Scopo**: raccontare i momenti chiave con regia.
- **Input**: sguardo libero (guidate); tenere premuto Esc/B 1 s per saltare le cinematiche già viste.
- **Stati**: `guidata(percorso)` / `cinematica(timeline)`.
- **Dati salvati**: `mondo.cinematicheViste[]`.
- **Interfaccia**: bande nere 2,39:1 solo nelle cinematiche; nessuna nelle guidate.
- **Accessibilità**: riduzione movimento: le camere a mano diventano fisse; sottotitoli sempre attivi in cinematica.
- **Casi limite**: caricamento a metà cinematica → si riparte dall'inizio della cinematica.
- **Dipendenze**: timeline di animazione (TDD), AUDIO, SIS-03.
- **Criteri**: `cr.vai("SCN-01-13")` → durata 7,0 ± 0,2 s; DOF attivo (`cr.render().dof === true`).

### SIS-27 Viaggio in auto (cap. 1) e funivia (cap. 10)
- **Regole**: Vera seduta (dietro la babuška); può guardare liberamente (yaw ±150°, pitch −40°/+55°), parlare con chi è in auto (Mattia accanto, Giulia dietro), fotografare dal finestrino. Il paesaggio è una cella di streaming «percorso A18» con LOD aggressivi e skybox con l'Etna; la durata reale del viaggio è compressa a 4 minuti (tempo di gioco 18:15 → 19:15). Funivia: cabina con turisti, 2 minuti reali.
- **Scopo**: far vivere i viaggi del libro senza tagli.
- **Input**: sguardo, interazione, foto (il movimento è disattivato).
- **Stati**: `seduta` per tutta la durata; eventi a tempo lungo il percorso.
- **Dati salvati**: `storia.scena`, progresso del viaggio `mondo.viaggio.t` (0–1).
- **Interfaccia**: nessuna; finestrino con riflessi leggeri.
- **Accessibilità**: riduzione movimento: niente sobbalzi della camera.
- **Casi limite**: foto all'Etna fuori finestra temporale → foto salvata in «Altre» con pensiero «Troppo presto, la luce non è ancora quella».
- **Dipendenze**: streaming del percorso, SIS-07, SIS-03.
- **Criteri**: durante SCN-01-15 il frame time resta entro budget (TDD §12) e la foto `FOT-01-06` (Etna) è riconosciuta solo tra 19:00 e 19:15.

---

## 4. Progressione e collezioni

Conteggi esatti per insieme, capitolo e zona. Elenchi completi: `NARRATIVA/parole_russe.md` (RUS), `NARRATIVA/mondo_libero.md` (RIC liberi, FOT, SEG), capitoli (voci di trama).

| Insieme | Cap.1 | Cap.2 | Cap.3 | Libero v1.0 | **Tot. v1.0** | Capp.4–8 | Libero v2.0 | **Tot. v2.0** | Capp.9–14 | Libero v3.0 | **Tot. v3.0** | **Totale** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Parole russe (RUS) | 8 | 6 | 1 | 2 | **17** | 11 | 2 | **13** | 6 | 1 | **7** | **37** |
| Ricordi (RIC) | 2 | 2 | 0 | 1 | **5** | 4 | 0 | **4** | 4 | 0 | **4** | **13** |
| Foto di trama (FOT capitoli) | 6 | 2 | 2 | — | **10** | 8 | — | **8** | 8 | — | **8** | **26** |
| Foto Luoghi | — | — | — | 10 | **10** | — | 10 | **10** | — | 8 | **8** | **28** |
| Foto Gatti | — | 1 | — | 7 | **8** | — | 8 | **8** | 1 | 5 | **6** | **22** |
| Foto Persone | — | — | — | 7 | **7** | — | 3 | **3** | — | 2 | **2** | **12** |
| Segreti di casa (SEG) | — | — | — | 6 | **6** | — | 6 | **6** | — | 4 | **4** | **16** |
| Indizi (IND, di trama) | 7 | 6 | 6 | — | 19 | 30 | — | 30 | 28 | — | 28 | 77 |

Zone delle collezioni libere: v1.0 = Casa Russo, scalinate, casa di Concetta, Corso Umberto (Porta Catania → Porta Messina, Piazza IX Aprile, Piazza Duomo), scuola; v2.0 = Teatro Antico, Villa Comunale, belvedere, Via Pirandello, resto del centro monumentale; v3.0 = funivia, Mazzarò, Isola Bella, lungomare, stazione.

**Ricompense** (nessuna influisce sulla trama):
| Completamento | Ricompensa |
|---|---|
| Tutte le RUS di un rilascio | Pagina «Dizionario di Casa Russo» nel quaderno (riprende l'appendice del libro) + la babuška dice a Vera una frase intera in russo ([NUOVO], VOX) |
| Tutti i RIC | Pagina doppia «I due nonni» (Kolja e Turi disegnati affiancati) |
| Foto Gatti | Il gatto rosso del quarto gradino segue Vera fino al portone e dorme sul suo letto nelle notti senza Donne |
| Foto Luoghi | Cartolina di Taormina «scritta» da Vera alla cugina di San Pietroburgo nel quaderno |
| Foto Persone | Foto di famiglia al balcone (v3.0: con la babuška e Concetta insieme) appesa in cucina |
| Segreti | Pagina «Mappa segreta di Casa Russo» nel quaderno |

---

## 5. Budget di tempo

### 5.1 Durata dei capitoli (sola trama, giocatore medio, senza mondo libero)

| Cap. | Titolo | Durata obiettivo | Di cui raccordi | Rilascio |
|---|---|---|---|---|
| 1 | La scarpa | 17 min | 0 | v1.0 |
| 2 | Il vecchietto dietro il frigorifero | 14 min | 3 (salita della scalinata, serata in casa) | v1.0 |
| 3 | Le signore di fuori | 22 min | 9 (quattro giornate) | v1.0 |
| 4 | La guerra delle tazzine | 25 min | 8 (giornate d'indagine) | v2.0 |
| 5 | Due nonne che non sanno niente | 15 min | 2 | v2.0 |
| 6 | Pokrov | 12 min | 2 | v2.0 |
| 7 | La casa tossisce | 16 min | 5 (giorni della casa malata, casse d'acqua) | v2.0 |
| 8 | Il consiglio di mezzanotte | 15 min | 1 | v2.0 |
| 9 | La scarpa vuota | 14 min | 3 | v3.0 |
| 10 | Il fratello che quasi vede | 18 min | 4 | v3.0 |
| 11 | Il treno per il nord | 12 min | 2 (ritorno) | v3.0 |
| 12 | Donne di fuori | 18 min | 5 (lunedì, pulizie) | v3.0 |
| 13 | La notte dei Morti | 18 min | 2 | v3.0 |
| 14 | Solo per un po' | 11 min | 2 | v3.0 |
| | **Totale** | **227 min (3 h 47 min)** | 48 min | |

Totale v1.0: 53 min · v2.0: 83 min · v3.0: 91 min. Verifica a ogni Beta: un giocatore di test (Vlad) e il giro automatico misurano la durata; scarto ammesso ±15% per capitolo, totale dentro 180–240 min.

### 5.2 Durata massima dei raccordi
Ogni raccordo ha una durata massima; oltre il massimo il gioco «spinge» con un pensiero di Vera e, dopo altri 60 s, il marker si accende anche se disattivato (solo per i raccordi). Elenco completo con massimi in `NARRATIVA/raccordi.md` (somma dei massimi: 71 min).

### 5.3 Mondo libero atteso
| Rilascio | Contenuto libero | Tempo atteso per completare tutto |
|---|---|---|
| v1.0 | domenica 14/9 + pomeriggi 15–18/9: bar, 4 missioni secondarie, 6 segreti, collezioni v1.0 | 60–90 min |
| v2.0 | 7 giornate libere: bar, 5 missioni, 6 segreti, collezioni v2.0 | 120–150 min |
| v3.0 | 3 giornate + dopo il finale: 3 missioni, 4 segreti, collezioni v3.0 | 90–120 min |

---

## 6. Flussi UX

### 6.1 Primo avvio
1. Pagina di caricamento (sfondo nero, scritta a mano «Casa Russo» che si disegna, barra sottile): scarica il nucleo (≤ 12 MB) e il manifesto.
2. **Rilevamento**: WebGPU → altrimenti WebGL2; se nessuno dei due, pagina che spiega quali browser usare. Su telefono (schermo < 7" o `pointer: coarse` e diagonale < 7"): avviso «Questo gioco è pensato per PC e tablet» con possibilità di continuare.
3. **Preset automatico** (TDD §12.4): prova di 3 s sulla scena del titolo; mostra «Qualità scelta: Medio» con «Cambia».
4. **Lingua**: solo italiano (D-67) → nessuna scelta; schermata unica «Sottotitoli»: dimensione (anteprima con la frase «Mi chiamo Vera Russo, ho dodici anni…»), suoni sottotitolati sì/no, traslitterazione russa sì/no.
5. **Cuffie consigliate** (una riga) e volume di prova (ronzio del frigorifero).
6. Titolo.

### 6.2 Titolo
Scena 3D: il balcone di Casa Russo al tramonto di settembre, il mare tra due tetti, l'Etna; il lapot' sul gradino. Titolo «Casa Russo», sottotitolo «Il domovoj nella scarpa» (D-40). Voci: **Continua** (se esiste un salvataggio: mostra capitolo e data della storia) · **Nuova partita** (conferma se esiste un salvataggio: «Il salvataggio automatico verrà sovrascritto. Gli slot manuali restano.») · **Carica** · **Opzioni** · **Crediti**.

### 6.3 Pausa
Esc · Start/Options · pulsante in alto a sinistra: il mondo si ferma e si sfoca; menu a sinistra; a destra la data della storia, il capitolo, l'obiettivo e il tempo di gioco.

### 6.4 Fine capitolo
Schermo nero con la frase finale (narrata da Vera 13–14 anni quando prevista) → **scheda di fine capitolo** nello stile del quaderno: titolo del capitolo, data, «Cosa ho scoperto» (gli indizi del capitolo come elenco a biro), parole russe nuove, foto scattate (3 miniature), ricordi, una frase di Vera sul capitolo ([NUOVO]), pulsanti «Continua» e «Torna al titolo». Salvataggio automatico.

### 6.5 Caricamento tra zone lontane
Tra celle non adiacenti (es. Casa Russo ↔ stazione, aeroporto ↔ auto ↔ Taormina): dissolvenza in nero con **pagina del quaderno** con un disegno della destinazione e una frase di Vera; durata minima 1,2 s, barra a matita; tra celle adiacenti caricamento invisibile (TDD §6).

### 6.6 Comandi rimappabili
Menu Opzioni → Controlli: ogni azione ha due assegnazioni per tastiera/mouse e una per gamepad; conflitti segnalati e risolti scambiando; «Ripristina predefiniti». Le azioni di sistema (Esc/Start per la pausa) non sono rimappabili. Sul touch si possono spostare e ridimensionare i pulsanti (modalità «Modifica disposizione», griglia 8 px, dimensione 70–140%).

---

## 7. Mappature dei comandi

### 7.1 PC (predefinite)
| Azione | Principale | Alternativa |
|---|---|---|
| Muovi | W A S D | Frecce |
| Guarda | Mouse | — |
| Corri (tenere) | Maiusc sinistro | — |
| Accovacciati (interruttore) | C | Ctrl sinistro |
| Interagisci / avanza dialogo | E | Clic sinistro (opzione) |
| Salta la scrittura / avanza | Spazio | Invio |
| Scelte di dialogo | 1 2 3 4 | Frecce + Invio |
| Telefono: foto | F | — |
| Scatta (con telefono alzato) | Clic sinistro | F |
| Zoom fotocamera | Rotella | + / − |
| Torcia | T | — |
| Orologio e data | Q | — |
| Quaderno | J | Tab |
| Pagina precedente/successiva | A / D | Q / E nel quaderno |
| Cronologia dialoghi | H | — |
| Evidenzia interattivi vicini (tenere 1 s) | Alt sinistro | — |
| Pausa | Esc | — |

### 7.2 Gamepad
| Azione | Xbox | PlayStation |
|---|---|---|
| Muovi / Guarda | Levetta sinistra / destra | Levetta sinistra / destra |
| Corri | L3 (pressione) | L3 |
| Accovacciati | B | ○ |
| Interagisci / avanza | A | ✕ |
| Telefono: foto (alza/abbassa) | X | □ |
| Scatta | RT | R2 |
| Zoom | LT tenuto + levetta destra | L2 + levetta destra |
| Torcia | LB | L1 |
| Orologio e data | RB | R1 |
| Quaderno | Y | △ |
| Pagine del quaderno | LB / RB | L1 / R1 |
| Scelte | Croce direzionale ↑↓ + A | Croce direzionale + ✕ |
| Cronologia | View | Share/Create |
| Evidenzia interattivi | Croce ↓ tenuta 1 s | Croce ↓ tenuta |
| Pausa | Menu | Options |

Vibrazione leggera: starnuto del cap. 1, crac della crepa, incastro ditale-cucchiaio (disattivabile).

### 7.3 Tablet touch (orientamento orizzontale; misure a 1180×820 pt, iPad 11")
| Elemento | Posizione | Dimensione |
|---|---|---|
| Joystick virtuale | compare dove il pollice tocca nel 40% sinistro dello schermo, sotto la metà; base fissa opzionale a 140 pt dal bordo sinistro e 150 pt dal basso | raggio 70 pt, pomello 32 pt |
| Area sguardo | 60% destro dello schermo, trascinamento | sensibilità separata dal mouse |
| Azione | in basso a destra, 48 pt dai bordi | cerchio 96 pt |
| Accovacciati | a sinistra di Azione, 24 pt di spazio | 64 pt |
| Telefono (apre foto/torcia/orologio a ventaglio) | sopra Azione | 64 pt |
| Quaderno | in alto a destra, 24 pt dai bordi | 56 pt |
| Pausa | in alto a sinistra, 24 pt dai bordi | 48 pt |
| Scelte di dialogo | elenco a destra, righe alte 56 pt | toccabili |
| Tocco diretto | toccare un oggetto evidenziato lo usa; doppio tocco sull'area di sguardo = Azione (opzione) | — |
| Pizzico | zoom della fotocamera; nel quaderno ingrandisce la pagina | — |

Con tastiera fisica collegata al tablet valgono anche i comandi PC; con gamepad collegato i pulsanti a schermo si nascondono.

### 7.4 Regole di rimappatura
Due tasti per azione su tastiera/mouse, uno su gamepad; nessun tasto può servire due azioni dello stesso contesto (movimento, dialogo, quaderno, telefono); le assegnazioni si salvano nelle opzioni; i suggerimenti a schermo usano sempre l'assegnazione corrente e le icone del dispositivo usato per ultimo (tastiera, Xbox, PlayStation, touch).

---

## Fonti

- `FASI_DI_SVILUPPO.md` (§2, §14–§17) e documento di gioco (§3–§5).
- Manoscritto, ID dei paragrafi in `work/libro.txt`.
- [Babylon.js — Navigation Plugin V2](https://doc.babylonjs.com/features/featuresDeepDive/crowdNavigation/v2Intro)
- [inkjs (npm)](https://www.npmjs.com/package/inkjs)
- [Regione Siciliana — calendario scolastico 2025/26](https://www.regione.sicilia.it/la-regione-informa/anno-scolastico-202526-sicilia-campanella-inizio-lezioni-15-settembre)
- [NOAA Solar Calculator (algoritmo della posizione del sole)](https://gml.noaa.gov/grad/solcalc/)
