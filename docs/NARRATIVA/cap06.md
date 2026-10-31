# Capitolo 6 — Pokrov

| Voce | Valore |
|---|---|
| Data e giorno | martedì 14 ottobre 2025 (notte delle Donne) |
| Arco orario | 15:30–17:50 bar · 18:00–18:40 balcone (tramonto 18:28) · 00:30–01:20 cucina |
| Luce | bar: luce di metà pomeriggio dal Corso; balcone: tramonto, il mare grigio, l'Etna viola poi nera (06.006, 06.017); notte: cucina col lampione, poi la candela del Pokrov come unica luce calda |
| Meteo | 26 °C (lo dice la radio del bar, 06.001), sereno |
| Luoghi | LUO-BAR (tavolino in fondo vicino al bagno) · LUO-COR · LUO-SCA-01 · LUO-CR-BAL · LUO-CR-CUC |
| Durata obiettivo | 12 minuti (raccordi 2) |
| Checkpoint | CP-06-A bar · CP-06-B balcone · CP-06-C notte |
| Personaggi | Vera, Salvo, clienti del bar, babuška, Fomà, (un filo di nebbia delle Donne) |
| Libro | §06.001–06.042 (pp. 29–33) |

## Sinossi
Il 14 ottobre a Taormina ci sono ventisei gradi e i turisti ordinano granite come ad agosto. Tornando a casa Vera trova la babuška sul balcone col cappotto verde: è il Pokrov, il velo della Madonna, il giorno in cui al villaggio l'inverno copriva la terra con la prima neve, il giorno in cui Kolja accendeva la stufetta «per il domovoj». Di notte Fomà, seduto sul bordo del lavandino, confessa la sua nostalgia: niente stufa, niente neve, niente Kolja. Vera accende una candela davanti al frigo: «Non è una stufa. Ma è un fuoco.» «Brava, Veročka.»

## Scene

### SCN-06-01 — Compiti al bar di papà (raccordo + bar) · CP-06-A
- **Tipo**: raccordo (massimo 5 min).
- **Trigger**: martedì 14, dopo la scuola.
- **Beat**: B-06-01.
- **Obiettivo** OBJ-06-01 [NUOVO]: «Fare i compiti al bar. Tavolino in fondo, vicino al bagno.»
- PEN-06-01 [LIBRO §06.001]: «Il quattordici ottobre, a Taormina, c'erano ventisei gradi. Lo so perché lo disse la radio del bar di papà, dove andavo il pomeriggio dopo la scuola a fare i compiti al tavolino in fondo, quello vicino al bagno, che nessun turista vuole.»
- RADIO DEL BAR [NUOVO] (SFX-038 «[radio del bar]» con testo): «…e oggi a Taormina ventisei gradi, cielo sereno, mare calmo. L'estate non ne vuole sapere di andarsene…»
- PEN-06-02 [LIBRO §06.001]: «I turisti, a metà ottobre, giravano ancora in pantaloncini e infradito, e ordinavano granite al limone come se fosse agosto. Papà diceva che l'estate a Taormina finisce quando lo decide lei, e quest'anno non aveva ancora deciso.»
- SALVO [LIBRO §06.001, battuta riferita in discorso diretto: NUOVO] (se Vera parla con lui): «L'estate a Taormina finisce quando lo decide lei. Quest'anno non ha ancora deciso.» · se `flag_bar_cap3`: [NUOVO] «E tu, barista, mi servi due granite al tavolo sei?» → mini-turno di 2 ordini.
- Compiti: sedersi al tavolino in fondo → quaderno di scienze (pagina fotosintesi) → passa un'ora → «Torna a casa» alle 17:50.

### SCN-06-02 — Il Pokrov (dialogo sul balcone) · CP-06-B
- **Trigger**: arrivo a casa alle 18:00; la babuška è sul balcone col cappotto verde.
- **Beat**: B-06-02.
- **Testo del libro**: [LIBRO §06.002–06.017] — dialogo completo: «Babuška. Non hai caldo?» / «Oggi è il Pokrov»; Vera si siede sul gradino del balcone (da lì un pezzo di mare tra due tetti e un pezzo di Etna che diventa viola); «Che cos'è il Pokrov?»; il racconto (velo, mantello, Costantinopoli, il 14 ottobre); «Come la Madonna della Lettera a Messina?» «Più o meno.»; la prima neve, il detto delle ragazze; «E nevicava davvero?»; l'aria fina che sa di ferro, le betulle, la stufa, la carta alle finestre, i valenki, la casa piccola e calda; Kolja e la stufetta di ghisa «per il domovoj», «Io gli dicevo che era un vecchio scemo»; Vera le prende la mano.
- **Lingua** (D-48): la babuška parla a Vera **in russo**; il racconto è lungo e importante: è doppiato in russo con sottotitoli [LIBRO]. Vera risponde in italiano tranne una battuta: alla domanda «Che cos'è il Pokrov?» il giocatore può scegliere:
  - `*` (1) «Che cos'è il Pokrov?» (italiano) [LIBRO §06.007]
  - `*` (2) «Что такое Покров?» · *Čto takoe Pokrov?* · sottotitolo «Che cos'è il Pokrov?» → rap_babuska +1; la babuška sorride (ANI) e risponde uguale.
- Doppiato (russo, battute principali): §06.005 [VOX-06-01] «Сегодня Покров.» · *Segodnja Pokrov.*; §06.009 [VOX-06-02] (racconto del velo); §06.011 [VOX-06-03] (il villaggio e il detto: «Батюшка Покров, покрой землю снежком, а меня женишком.» · *Batjuška Pokrov, pokroj zemlju snežkom, a menja ženichom.* · sottotitolo [LIBRO] «Pokrov, Pokrov, copri la terra di neve, e me di un fidanzato.»); §06.014 [VOX-06-04] (la stufa, i valenki, la casa piccola e calda); §06.016 [VOX-06-05] (Kolja e la stufetta). I testi russi completi sono in `AUDIO.md` §4 (righe VOX-06-01…05) e in `parole_russe.md`.
- **Regia**: la luce scende durante il racconto (accelerazione del tempo: 18:00 → 18:40 in 3 minuti); il mare diventa grigio, l'Etna nera; l'ultima immagine: la mano di Vera prende quella della babuška (ANI-VER), «fredda nonostante il caldo».
- PEN-06-03 [LIBRO §06.017]: «Non disse altro. Guardò il mare, che diventava grigio, e l'Etna, che diventava nera. E io le presi la mano, che era fredda nonostante il caldo, e rimanemmo lì.»
- Se `flag_irina_kolja`: PEN-06-04 [NUOVO]: «Il dedushka barava a scacchi e accendeva le stufe per i domovoj. Cominciavo a capire chi era.»
- **Voci del quaderno**: RUS-25 Pokrov · RUS-26 valenki · RUS-27 pečka · RUS-28 il detto del Pokrov · RIC-06 [LIBRO §06.016 + NUOVO] «Il dedushka Kolja accendeva la stufetta di ghisa il giorno del Pokrov. Diceva che era per il domovoj. La babuška gli diceva che era un vecchio scemo.» · RIC-09 [LIBRO §06.011–06.014 + NUOVO] «Il villaggio della nonna della babuška: il 14 ottobre la prima neve, le betulle gialle, la carta alle finestre, i valenki. La casa diventava piccola e calda.» · IND-06-01 [NUOVO] «14 ottobre: il Pokrov. Il velo della Madonna che protegge. La babuška col cappotto, con 26 gradi. Le manca la neve.»
- **Fotografabile**: FOT-06-01 l'Etna viola dal balcone, con la babuška di spalle.

### SCN-06-03 — Fomà sul lavandino (dialogo) · CP-06-C
- **Trigger**: notte (00:30), Vera non dorme e scende in cucina.
- **Beat**: B-06-03.
- **Testo del libro**: [LIBRO §06.018–06.032] — Fomà sul bordo del lavandino coi piedi a penzoloni, guarda fuori; «Fomà»; il sobbalzo; «Tu! Sempre tu. Non dormi mai, tu?» «Non ci riesco.» «Nemmeno io. In questo paese fa troppo caldo per dormire.»; Vera sulla sedia accanto; il cortile, il limone nero, il lampione; «Oggi era il Pokrov»; lo sbuffo; il racconto di Fomà (duecento anni di Pokrov, la stufa, l'angolo caldo, le frittelle, la neve; «Kolja la accendeva per me, la stufetta»); «Quest'anno niente stufa. Niente neve. Niente Kolja.»; «Ti manca?»; «Il domovoj non ha nostalgia… Il domovoj sta dove sta la famiglia. È la regola… Ma la famiglia è lì, e la casa era là. E adesso io non so più dove sto.»
- Doppiato: FOMÀ §06.021 [VOX-06-06], §06.027 [VOX-06-07], §06.029 [VOX-06-08], §06.032 [VOX-06-09].
- **Scelte di Vera** (dove il libro fa parlare Vera, la battuta è del libro; il giocatore sceglie il *come* o un'aggiunta [NUOVO] dopo):
  - dopo «Quest'anno niente stufa. Niente neve. Niente Kolja.»: il libro dice «Io non sapevo cosa dire» (06.030). Scelta: `*` (1) stare zitta (PEN-06-05 [LIBRO §06.030] «Guardai il vecchietto seduto sul bordo del lavandino, con la barba lunga fino ai piedi e i pugni stretti sulle ginocchia, e per la prima volta non mi sembrò buffo. Mi sembrò solo vecchio, e lontano da casa.») · `*` (2) avvicinare la sedia di un passo (stesso pensiero; rap_foma +1).
  - poi VERA [LIBRO §06.031]: «Ti manca?»
- **Voci del quaderno**: IND-06-02 [NUOVO] «Fomà ha nostalgia. Dice di no ("il domovoj non ha nostalgia"), ma dice anche: "Non so più dove sto." Kolja accendeva la stufetta per LUI.»

### SCN-06-04 — La candela del Pokrov (interazione rituale)
- **Beat**: B-06-04.
- **Obiettivo** OBJ-06-04 [NUOVO]: «Fare un fuoco per il Pokrov. Senza bruciare la casa.»
- **Svolgimento** (il giocatore compie i gesti del libro, 06.033–06.034):
  1. aprire il cassetto delle candele «per quando salta la luce» → prendere una candela bianca normale;
  2. metterla in un bicchiere;
  3. prendere un piattino → pane → sale;
  4. accendere la candela con l'accendino del gas (SFX-036 «[accendino del gas]»);
  5. posarla sul pavimento davanti al frigorifero (punto evidenziato).
  - VERA [LIBRO §06.035]: «Non è una stufa. Ma è un fuoco. Per il Pokrov.»
- **Regia**: Fomà guarda la candela (2 s), scende piano dal lavandino, si siede a gambe incrociate davanti alla fiamma, allunga le manine pelose verso il fuoco (ANI-FOM-12). Luce: la candela diventa la luce principale della scena (luce puntiforme calda 1800 K con sfarfallio, ombre morbide).
  - PEN-06-06 [LIBRO §06.036]: «Fomà mi guardò. Guardò la candela. Per un momento pensai che si sarebbe arrabbiato, che avrebbe detto che era una cosa da niente, una candela da quattro soldi.»
  - FOMÀ [LIBRO §06.038] [VOCE VOX-06-10] (dopo un po', senza guardarla): «Brava. Brava, Veročka.»
  - PEN-06-07 [LIBRO §06.039]: «Era la prima volta che mi chiamava per nome.»
- **Effetti**: rap_foma +1 (minimo 1 da qui in poi); oggetto PRP-CANDELA-POKROV (consumata a metà) resta in cucina e servirà al cap. 8.
- **Voci del quaderno**: IND-06-03 [NUOVO] «Ho acceso una candela davanti al frigo, con pane e sale. Per il Pokrov. Fomà si è seduto davanti al fuoco come davanti a un camino. Mi ha chiamata Veročka.»

### SCN-06-05 — Avevano solo freddo (cinematica breve, fine)
- **Beat**: B-06-05.
- PEN-06-08 [LIBRO §06.040–06.041]: «Pensai che anche lei, come Fomà, non sapeva più dove stava.» · «Non erano cattivi. Non volevano la guerra. Avevano solo freddo, in un posto dove faceva caldo.»
- **Regia**: dal vetro, il limone nel cortile si muove appena senza vento (shader della chioma, 1 s); poi verso l'ingresso: dal buco della serratura **un filo di nebbia bianca** esce, «guarda dentro», si ritira (è martedì: le Donne passano ma non entrano) — SFX-020 a volume basso.
- VOX-06-11 [LIBRO §06.042] [VOCE narratrice]: «E dal buco della serratura dell'ingresso, mi sembrò, per un attimo, di vedere uscire un filo di nebbia bianca, che guardava dentro, e poi si ritirava.»
- **Voci del quaderno**: IND-06-04 [NUOVO] «La babuška e Fomà: tutti e due non sanno più dove stanno. Non sono cattivi. Hanno solo freddo, in un posto dove fa caldo.» · IND-06-05 [NUOVO] «Martedì notte: un filo di nebbia dal buco della serratura ha guardato dentro. Ha visto la candela?»
- **Fine**: scheda con frase [NUOVO]: «Una candela da quattro soldi. E per la prima volta mi ha chiamata per nome.»
- **Cosa cambia nel mondo**: candela del Pokrov in cucina; Fomà risponde a Vera dal frigo in libero (battute in `mondo_libero.md` §4); prima giornata del cap. 7 il giorno dopo.

## Voci del quaderno del capitolo

| ID | Testo |
|---|---|
| IND-06-01 | 14 ottobre: il Pokrov. Il velo della Madonna che protegge. La babuška col cappotto, con 26 gradi. Le manca la neve. |
| IND-06-02 | Fomà ha nostalgia. Dice di no ("il domovoj non ha nostalgia"), ma dice anche: "Non so più dove sto." Kolja accendeva la stufetta per LUI. |
| IND-06-03 | Ho acceso una candela davanti al frigo, con pane e sale. Per il Pokrov. Fomà si è seduto davanti al fuoco come davanti a un camino. Mi ha chiamata Veročka. |
| IND-06-04 | La babuška e Fomà: tutti e due non sanno più dove stanno. Non sono cattivi. Hanno solo freddo, in un posto dove fa caldo. |
| IND-06-05 | Martedì notte: un filo di nebbia dal buco della serratura ha guardato dentro. Ha visto la candela? |
| RIC-06 | Il dedushka Kolja accendeva la stufetta di ghisa il giorno del Pokrov. Diceva che era per il domovoj. La babuška gli diceva che era un vecchio scemo. |
| RIC-09 | Il villaggio della nonna della babuška: il 14 ottobre la prima neve, le betulle gialle, la carta alle finestre, i valenki. La casa diventava piccola e calda. |
| RUS-25…28 | Pokrov · valenki · pečka · «Batjuška Pokrov, pokroj zemlju snežkom, a menja ženichom» |
| FOT-06-01 | L'Etna viola dal balcone, e la babuška di spalle. |

## Fonti
- Manoscritto §06.001–06.042; appendice («Il Pokrov (14 ottobre) è una festa della Chiesa ortodossa…»).
- [Pokrov — Wikipedia (Protezione della Madre di Dio)](https://it.wikipedia.org/wiki/Protezione_della_Madre_di_Dio)
