# Capitolo 2 — Il vecchietto dietro il frigorifero

| Voce | Valore |
|---|---|
| Data e giorno | sabato 13 settembre 2025 |
| Arco orario | 19:35 (arrivo) → 00:15 |
| Luce | crepuscolo blu sulla scalinata (tramonto alle 19:13), lampioni accesi; cucina illuminata a cena; di notte cucina buia con la luce arancio del lampione del cortile dalla finestra |
| Meteo | sera tiepida (24 °C), finestre aperte, odore di gelsomini del vicino |
| Luoghi | LUO-CIR Via Circonvallazione (sosta dell'auto) · LUO-SCA-01 scalinata di Casa Russo · LUO-CR-ING · LUO-CR-CUC · LUO-CR-SCL · LUO-CR-COR (corridoio) · LUO-CR-SBA · LUO-CR-VER |
| Durata obiettivo | 14 minuti (raccordi 3) |
| Checkpoint | CP-02-A scalinata · CP-02-B cena · CP-02-C notte (inizio SCN-02-05) · CP-02-D fine |
| Personaggi | Vera, babuška, Irina, Salvo, Giulia, Mattia, nonna Concetta, Fomà, gatto rosso del quarto gradino |
| Libro | §02.001–02.040 (pp. 9–13) |

## Sinossi
La monovolume si ferma in cima alla scalinata. Davanti al portone c'è nonna Concetta con un vassoio di arancini «per la signora che viene da lontano»; la babuška risponde con un barattolo di pirožki. A cena le due nonne si dicono «complimenti» come si dice «ti ho visto, sai». Quasi a mezzanotte Vera non dorme, sente la porta della babuška e la segue in cucina: la babuška posa il lapot' sul pavimento, chiama il «nonnino» in russo tre volte, gli lascia pane nero e sale. La scarpa si muove. Ne esce un vecchietto alto come una bottiglia, barbuto, con la camicia rossa: cerca la stufa, non la trova, e sceglie il posto caldo dietro il frigorifero che ronza. Si chiama Fomà.

## Scene

### SCN-02-01 — In cima alla scalinata (raccordo) · CP-02-A
- **Tipo**: raccordo (massimo 3 min).
- **Trigger**: dissolvenza dal cap. 1; l'auto si ferma in Via Circonvallazione, accanto alla testa della scalinata (D-89).
- **Obiettivo** OBJ-02-01 [NUOVO]: «Portare a casa le valigie. Sono quattro gradini. Tre valigie. Fate voi il conto.»
- **Beat**: B-02-01.
- PEN-02-01 [LIBRO §02.001] (mentre Vera scende dall'auto e guarda giù): «Casa nostra è in una scalinata. Non sopra, non accanto: proprio dentro. A Taormina le strade che salgono dal Corso Umberto verso la montagna a un certo punto si stancano di essere strade e diventano scale, con i gradini di pietra consumati, i vasi di gerani sui lati e i gatti che dormono esattamente dove devi mettere il piede.»
- PEN-02-02 [LIBRO §02.001] (guardando il portone e il limone oltre il muretto): «La nostra è una casa vecchia a due piani, stretta, con le persiane verdi e un cortiletto grande come un tavolo da ping-pong, dove c'è un limone che era lì prima di tutti noi. Mio padre dice che il limone è il vero padrone di casa, e noi siamo in affitto.»
- **Interazione facoltativa**: prendere una valigia dal bagagliaio (la più piccola) → flag_valigia_aiutata = true; SALVO [NUOVO]: «Brava. Quella è la più leggera. Cosa ci sarà dentro, i cuscini?» → la babuška [NUOVO, italiano con accento]: «Barattoli.»
- **Fotografabile**: FOT-02-01 la scalinata al crepuscolo vista dall'alto.

### SCN-02-02 — Arancini e pirožki (dialogo osservato)
- **Trigger**: avvicinarsi al portone (3 m).
- **Beat**: B-02-02, B-02-03.
- PEN-02-03 [LIBRO §02.002]: «Davanti al portone, quel sabato sera, c'era nonna Concetta.»
- PEN-02-04 [LIBRO §02.003]: «Nonna Concetta è la mamma di mio padre. Abita due scalinate più in là, ha settantun anni, è alta un metro e cinquanta compresi i capelli cotonati, e ha una voce che si sente fino a Giardini Naxos.»
- CONCETTA [LIBRO §02.004] [VOCE VOX-02-01]: «Arancini. Al ragù e al burro. Per la signora che viene da lontano, che avrà fame.»
- PEN-02-05 [LIBRO §02.005]: «La babuška scese dalla macchina, si sistemò il fazzoletto e guardò nonna Concetta dall'alto in basso, il che era difficile, perché erano alte uguali.»
- BABUŠKA [LIBRO §02.006] [VOCE VOX-02-02] (in italiano, «con la erre lunga lunga»): «Grazie. Ho portato i pirožki.»
- (dalla terza valigia, quella legata con lo spago, tira fuori un barattolo di latta pieno di fagottini dorati — ANI-BAB, oggetto PRP-BARATTOLO)
- PEN-02-06 [LIBRO §02.008]: «Le due nonne si guardarono. Per un momento, nella scalinata, si fece silenzio. Anche il gatto rosso sul quarto gradino aprì un occhio.»
- **Gatto rosso**: il gatto sul quarto gradino apre un occhio (ANI-GAT-02); fotografabile → FOT-GAT-01 (album Gatti).
- **Scelta di Vera** (2 s di silenzio, poi):
  - `*` (1) «Nonna, i tuoi arancini sono i più buoni di Taormina.» → rap_concetta +1 → CONCETTA [NUOVO]: «Di Taormina? Della provincia, picciridda.»
  - `*` (2) «Babuška, cosa c'è dentro i pirožki?» → rap_babuska +1 → BABUŠKA [NUOVO] [RU] «С капустой. И с яблоками.» · *S kapustoj. I s jablokami.* · sottotitolo «Cavolo. E mele.»
  - `*` (3) (stare zitta) → nessun effetto
- Poi in ogni ramo:
  - SALVO [LIBRO §02.009] [VOCE VOX-02-03]: «Che bello. Mangiamo tutto. Insieme. Tutti contenti.»
- **Voci del quaderno**: RUS-09 pirožki.

### SCN-02-03 — La cena dei «complimenti» (dialogo, seduti) · CP-02-B
- **Trigger**: ingresso in cucina; tutti a tavola (posti in `LIVELLI.md` §3.4: Vera tra Mattia e Giulia, di fronte alle due nonne).
- **Beat**: B-02-04.
- PEN-02-07 [LIBRO §02.010]: «Nessuno era contento. Ma mangiammo tutto lo stesso, intorno al tavolo della cucina, e devo dire che sia gli arancini sia i pirožki erano buonissimi, e che le due nonne passarono la cena a dirsi «complimenti» con la stessa voce con cui si dice «ti ho visto, sai».»
- **Interazione**: Vera sceglie cosa assaggiare per primo (piatto 3D davanti a lei):
  - `*` (1) un arancino → flag_arancino_primo = true → la babuška guarda Vera per 1 s (camera), CONCETTA [NUOVO]: «Brava. Prima le cose di casa.»
  - `*` (2) un pirožok → flag_arancino_primo = false → Concetta guarda Vera per 1 s, BABUŠKA [NUOVO] [RU] «Кушай, кушай.» · *Kušaj, kušaj.* · sottotitolo «Mangia, mangia.»
  - Poi Vera assaggia anche l'altro (automatico): PEN-02-08 [NUOVO]: «Buonissimi tutti e due. Era un problema.»
- **Complimenti** (scambio fisso, [NUOVO] costruito sul libro):
  - CONCETTA [NUOVO]: «Complimenti per questi… pirožki.»
  - BABUŠKA [NUOVO]: «Complimenti per arancini.»
  - CONCETTA [NUOVO]: «Complimenti.»
  - BABUŠKA [NUOVO]: «Complimenti.»
- **Giulia alleata** (`flag_giulia_ginevra or rap_giulia >= 2`, D-58): GIULIA [NUOVO] sottovoce a Vera: «Al quarto "complimenti" chiamo i caschi blu.» → PEN-02-09 [NUOVO]: «Giulia faceva le battute con me. Era la serata delle cose strane.» → rap_giulia +1. Ramo normale: GIULIA [NUOVO] (al telefono, sotto il tavolo): «Posso alzarmi?» IRINA [NUOVO]: «No.»
- **Mattia**: MATTIA [NUOVO]: «Io mangio un arancino e un pirožok insieme. Così nessuno piange.»
- **Fotografabile**: FOT-02-02 il tavolo con arancini e pirožki (prima che finiscano).
- **Voci del quaderno**: IND-02-01 [NUOVO] «Nonna Concetta e la babuška si dicono "complimenti". Vuol dire "ti ho visto, sai". Da tenere d'occhio.»

### SCN-02-04 — La stanza della babuška (raccordo libero in casa)
- **Tipo**: raccordo (massimo 4 min). Ora 21:40.
- **Trigger**: fine cena.
- **Obiettivo** OBJ-02-04 [NUOVO]: «Andare a letto. Ufficialmente.»
- **Beat**: B-02-05.
- **Interazioni**:
  | Punto | Pensiero / effetto |
  |---|---|
  | Porta della stanza della babuška (ex studio) | PEN-02-10 [LIBRO §02.011]: «La babuška dormiva nella stanza che prima era lo studio di papà, accanto alla mia. Papà aveva portato via il computer e i libri e ci aveva messo un letto, un armadio e una sedia.» |
  | Tavolo della cucina con i conti del bar | PEN-02-11 [LIBRO §02.011]: «Lo studio era diventato «la stanza della babuška», e papà, adesso, i conti del bar li faceva sul tavolo della cucina, sospirando.» (Salvo seduto sospira: SFX non sottotitolato) |
  | Lavello (Irina lava i piatti) | sblocca **RIC-04** (vedi sotto) |
  | Frigorifero | PEN-02-12 [NUOVO]: «Il frigorifero ronza. Ha sempre ronzato. Stasera mi sembrava che ronzasse più contento.» |
  | Camera di Vera, scrivania | quaderno di scienze sulla scrivania: tutorial «Scrivi le cose strane» (apre la pagina Indizi) |
  | Porta di Giulia | risate soffocate dei video (SFX non sottotitolato) |
- RIC-04 [LIBRO §01.014 + NUOVO]: Irina che lava i piatti in silenzio fa ricordare a Vera: «Ha pianto la sera dopo, mentre lavava i piatti, e io ho fatto finta di non vedere.» [LIBRO §01.014] — titolo della voce [NUOVO]: «La telefonata di aprile.»
- **Dopo**: entrare nel letto → SCN-02-05.

### SCN-02-05 — Non riesco a dormire (guidata, a letto) · CP-02-C
- **Trigger**: Vera si sdraia; ora 23:50.
- **Beat**: B-02-06.
- **Regia**: Vera a letto, sguardo libero (soffitto, finestra aperta, porta socchiusa). Ambiente: grilli, motorino lontano, ronzio del frigo dal piano di sotto, risate di Giulia attraverso il muro, Mattia che dorme a bocca aperta dal corridoio.
- PEN-02-13 [LIBRO §02.012–02.013]: «Io non riuscivo a dormire. Era quasi mezzanotte. Dalla finestra entrava l'aria tiepida e l'odore dei gelsomini del vicino.»
- PEN-02-14 [LIBRO §02.013]: «Giulia, nella stanza di fronte, guardava video con le cuffie e rideva da sola. Mattia dormiva con la bocca aperta, si sentiva dal corridoio.»
- Dopo 20 s (o quando Vera guarda la porta): SFX-081 «[una porta che si apre piano]» (sinistra) — è la porta della babuška.
  - PEN-02-15 [LIBRO §02.014]: «E poi sentii la porta della babuška aprirsi.»

### SCN-02-06 — Seguire la babuška (guidata, D-09)
- **Trigger**: fine SCN-02-05.
- **Obiettivo** OBJ-02-06 [NUOVO]: «Seguire la babuška. Senza farsi vedere. (Non ti vede comunque: è concentrata.)»
- **Beat**: B-02-07.
- **Svolgimento**:
  1. Vera si alza (automatico) e mette l'occhio alla fessura della porta: inquadratura stretta (maschera della fessura) — la babuška passa nel corridoio **in camicia da notte, scalza, con la borsa a fiori in mano**.
     - PEN-02-16 [LIBRO §02.015]: «La babuška passò nel corridoio in camicia da notte, scalza, con la borsa a fiori in mano. Scese le scale, piano, un gradino alla volta, tenendosi al corrimano.»
  2. **Contare fino a dieci**: tenere premuto Azione; i numeri da 1 a 10 si scrivono a biro al centro (1 al secondo). PEN-02-17 [LIBRO §02.015]: «Contai fino a dieci e la seguii.»
  3. Corridoio e scale: camminata lenta a piedi nudi; muro morbido a 1 m dal percorso; nessun rischio di essere scoperti. Se Vera pesta il **9° gradino**: SFX-012 «[il nono gradino scricchiola]», la babuška non si volta, PEN-02-18 [NUOVO]: «Il nono gradino scricchiola. Da ricordare.» (Da qui in poi il 9° gradino è evidenziato quando ci si avvicina di notte; SEG-01 si sblocca la prima volta che lo si salta, vedi `mondo_libero.md`.)
  4. Fermarsi dietro lo stipite della porta della cucina (punto indicato da un'ombra sul pavimento). Postura automatica: in piedi, mezza nascosta (camera spostata di 25 cm a destra).
- Se `flag_starnuto_detto = false`: PEN-02-19 [NUOVO] (sulle scale): «All'aeroporto non le avevo detto niente subito. Stavolta non le avrei detto niente per niente.»

### SCN-02-07 — Il rito (guidata, sguardo libero da dietro lo stipite)
- **Beat**: B-02-08, B-02-09.
- PEN-02-20 [LIBRO §02.016]: «In cucina la luce era spenta. Ma dalla finestra sul cortile entrava la luce del lampione, e vidi la babuška in piedi in mezzo alla stanza, con il lapot' in mano. Lo teneva davanti a sé, con tutte e due le mani, come si tiene una tazza troppo piena.»
- PEN-02-21 [LIBRO §02.017]: «Poi parlò. In russo, a voce bassa, quasi cantando:»
- BABUŠKA [LIBRO §02.018] [VOCE VOX-02-04] [RU] (tre volte, quasi cantando; la seconda e la terza più piano):
  «Дедушка, дедушка, пойдём с нами. Это новый дом. Пойдём жить с нами.»
  · *Dedushka, dedushka, pojdëm s nami. Èto novyj dom. Pojdëm žit' s nami.*
  · sottotitolo «Nonnino, nonnino, vieni con noi. Questa è la casa nuova. Vieni a vivere con noi.»
- PEN-02-22 [LIBRO §02.019]: «Lo ripeté tre volte. Poi si inginocchiò, piano, perché le facevano male le ginocchia, e posò il lapot' sul pavimento. Accanto mise un pezzetto di pane nero e un pizzico di sale su un tovagliolo. Si fece il segno della croce, al contrario di come lo fa nonna Concetta, da destra a sinistra. E rimase lì, ad aspettare.»
- PEN-02-23 [LIBRO §02.020–02.021]: «Io trattenevo il fiato dietro lo stipite della porta. Per un po' non successe niente. Il frigorifero ronzava. Un motorino passò giù sul Corso.»
- **Suoni**: SFX-010 «[frigorifero che ronza]», SFX-011 «[motorino lontano]» (in basso, lontano).
- **Opzione «trattenere il fiato»** [NUOVO, facoltativa]: tenendo premuto Azione l'ambiente si attenua (filtro passa-basso sul mix, battito del cuore) — solo atmosfera.
- **Voci del quaderno**: RUS-11 il rito «Dedushka, dedushka, pojdëm s nami…» · IND-02-02 [NUOVO] «Di notte la babuška è scesa in cucina con la borsa a fiori. Scalza.» · IND-02-03 [NUOVO] «Ha chiamato la scarpa "nonnino", tre volte, in russo. Poi pane nero e sale su un tovagliolo. E la croce al contrario.»

### SCN-02-08 — La scarpa si muove (cinematica in prima persona)
- **Beat**: B-02-10, B-02-11.
- **Camera**: resta sugli occhi di Vera (prima persona); lenta messa a fuoco sul lapot' (DOF f/2,4); la luce del lampione disegna una striscia arancione sul pavimento.
- PEN-02-24 [LIBRO §02.022–02.023]: «Poi la scarpa si mosse. Si mosse da sola. Ondeggiò, come una barchetta, e da dentro uscì una mano. Una manina piccola, pelosa, con le unghie lunghe e gialle come quelle di un vecchio.»
- SFX-014 «[la scarpa ondeggia]» · ANI-FOM-01 la mano tasta, afferra il pane, sparisce · SFX-013 «[masticare]» · la mano torna e prende il sale.
- PEN-02-25 [LIBRO §02.023]: «La mano tastò il pavimento, trovò il pane, lo afferrò e sparì dentro la scarpa. Si sentì masticare. Poi la mano uscì di nuovo, prese il sale e sparì anche il sale.»
- PEN-02-26 [LIBRO §02.024]: «Poi uscì lui.» (ANI-FOM-02)
- PEN-02-27 [LIBRO §02.025]: «Era alto come una bottiglia d'acqua da un litro e mezzo. Aveva una barba grigia lunghissima che gli arrivava ai piedi e che si portava dietro come uno strascico, e i capelli grigi tutti arruffati, e il corpo coperto di peli morbidi, come un gatto vecchio.»
- PEN-02-28 [LIBRO §02.025]: «Aveva una camicia rossa con la cintura di corda, e niente scarpe: o meglio, la sua scarpa era quella da cui era uscito. Aveva un naso grosso e rosso, e due occhietti neri e lucidi che si guardavano intorno con un'aria offesissima.»
- **Voci del quaderno**: IND-02-04 [NUOVO] «Dalla scarpa è uscita una manina pelosa, con le unghie gialle. Ha preso il pane. Poi il sale.» · IND-02-05 [LIBRO §02.025 + NUOVO] «Lui: alto come una bottiglia da un litro e mezzo. Barba fino ai piedi. Camicia rossa, cintura di corda. Naso rosso. Occhietti neri. Peloso come un gatto vecchio.»

### SCN-02-09 — Fomà (cinematica osservata, sguardo libero)
- **Beat**: B-02-12, B-02-13, B-02-14.
- FOMÀ [LIBRO §02.026] [VOCE VOX-02-05]: «Fu.»
- FOMÀ (borbottio senza traduzione) [VOCE VOX-02-06] [RU] — sottotitolo «[parole in russo che la babuška non vorrà tradurre]».
- PEN-02-29 [LIBRO §02.026]: «Poi una serie di parole in russo che non conoscevo, e che più tardi la babuška si rifiutò di tradurmi. Poi, in un italiano strano, impastato, con tutte le erre sbagliate:»
- FOMÀ [LIBRO §02.026] [VOCE VOX-02-07]: «E la stufa? Dov'è la stufa? Che casa è una casa senza stufa?»
- BABUŠKA [LIBRO §02.027] [VOCE VOX-02-08] [RU] (sussurrando) «Здесь нет печки, дедушка. Здесь тепло. Не нужно.» · *Zdes' net pečki, dedushka. Zdes' teplo. Ne nužno.* · sottotitolo «Non c'è la stufa, nonnino. Qui fa caldo. Non serve.»
- FOMÀ [LIBRO §02.028] [VOCE VOX-02-09] (alza le braccia, ANI-FOM-03): «Non serve! Non serve, dice! E io dove dormo? Sul pavimento, come un cane? In una scarpa, come un ciabattino?»
- PEN-02-30 [LIBRO §02.029]: «Si guardò intorno. Guardò il fornello a gas, il lavandino, la lavastoviglie. Annusò l'aria. Fece il giro della cucina strisciando la barba sul pavimento. E alla fine si fermò davanti al frigorifero, che ronzava.» (ANI-FOM-04, ANI-FOM-05; la barba lascia una scia nella polvere: decal temporaneo)
- PEN-02-31 [LIBRO §02.030]: «Mise la mano sul fianco del frigorifero. Poi infilò la testa nello spazio stretto tra il frigorifero e il muro, dove c'è la griglia nera sul retro. Ne uscì dopo un po', con la barba piena di polvere e un'aria soddisfatta.» (ANI-FOM-06)
- FOMÀ [LIBRO §02.031] [VOCE VOX-02-10]: «Qui. Qui dietro è caldo. Ronza. Mi piace. Mi metto qui.»
- (spinge il lapot' nello spazio dietro il frigorifero, ci salta dentro e sparisce: ANI-FOM-07)
- PEN-02-32 [LIBRO §02.033]: «La babuška rimase in ginocchio un altro po'. Poi si alzò, si spolverò la camicia da notte e disse, verso il frigorifero:»
- BABUŠKA [LIBRO §02.034] [VOCE VOX-02-11] [RU] «Спокойной ночи, Фома.» · *Spokojnoj noči, Fomà.* · sottotitolo «Buona notte, Fomà.»
- FOMÀ [LIBRO §02.035] [VOCE VOX-02-12] (da dietro il frigo): «Buona notte, buona notte. Senza stufa. Ma si può.»
- **Foto**: se Vera prova a fotografare Fomà (F è attivo in questa scena), la foto mostra il pavimento e il lapot' vuoto → PEN-FOT-SPIRITI [NUOVO]: «Nella foto c'era la scarpa. Solo la scarpa. Il resto non si fa fotografare.» (insegna la regola di SIS-07).
- **Voci del quaderno**: RUS-12 «Fu!» · RUS-13 «Spokojnoj noči» · IND-02-06 [NUOVO] «Cercava la stufa. Non c'è. Ha scelto il posto dietro il frigorifero, perché "è caldo e ronza". La babuška lo ha chiamato FOMÀ.»
- **Effetti**: rap_foma resta 0 (non sa ancora di Vera).

### SCN-02-10 — Il cuore come un tamburo (guidata breve → fine) · CP-02-D
- **Trigger**: la babuška si volta verso la porta (Vera torna di corsa su; la camera corre da sola, 2 s, poi controllo).
- **Beat**: B-02-15.
- PEN-02-33 [LIBRO §02.036]: «Io tornai di sopra di corsa, senza far rumore, e mi infilai nel letto con il cuore che batteva come un tamburo.»
- PEN-02-34 [LIBRO §02.037]: «Avevo appena visto un vecchietto alto come una bottiglia uscire da una scarpa e andare a vivere dietro il nostro frigorifero.»
- PEN-02-35 [LIBRO §02.038]: «La babuška lo aveva chiamato nonnino, e poi Fomà. Ero quasi sicura di sapere che cosa fosse, perché me ne aveva parlato la mamma quando ero piccola, prima di dormire, insieme a Baba Jaga e all'uccello di fuoco. Un domovoj. Lo spirito della casa.»
- PEN-02-36 [LIBRO §02.038]: «Quello che vive dietro la stufa, che protegge la famiglia, che si offende se non gli dai il pane.»
- PEN-02-37 [LIBRO §02.039]: «Io avevo sempre pensato che fosse una favola.»
- RIC-03 [LIBRO §02.038 + NUOVO] «Le favole della mamma: Baba Jaga, l'uccello di fuoco e il domovoj, lo spirito della casa. Le raccontava prima di dormire.» · RUS-10 domovoj · RUS-14 Baba Jaga.
- Finale: schermo che si scurisce lentamente sul soffitto; SFX-010 ronzio dal basso; poi SFX-015 «[russare, lontano, dal piano di sotto]».
  - VOX-02-13 [LIBRO §02.040] [VOCE narratrice]: «Restai sveglia a lungo, a guardare il soffitto. Da giù, ogni tanto, arrivava il ronzio del frigorifero. E una volta, una volta sola, mi sembrò di sentire qualcuno che russava.»
- Scheda di fine capitolo: frase di Vera [NUOVO]: «Dietro il nostro frigorifero abita un domovoj. Domani lo dico a qualcuno. Forse. No.»
- **Cosa cambia nel mondo**: da qui la babuška lascia pane e sale dietro il frigo ogni sera; brontolii notturni udibili in cucina (SFX-016, solo Vera); si apre la **domenica 14 settembre** in mondo libero (`mondo_libero.md` §2, `raccordi.md` RAC-02).

## Voci del quaderno del capitolo

| ID | Sezione | Testo |
|---|---|---|
| IND-02-01 | Indizi | Nonna Concetta e la babuška si dicono "complimenti". Vuol dire "ti ho visto, sai". Da tenere d'occhio. |
| IND-02-02 | Indizi | Di notte la babuška è scesa in cucina con la borsa a fiori. Scalza. |
| IND-02-03 | Indizi | Ha chiamato la scarpa "nonnino", tre volte, in russo. Poi pane nero e sale su un tovagliolo. E la croce al contrario. |
| IND-02-04 | Indizi | Dalla scarpa è uscita una manina pelosa, con le unghie gialle. Ha preso il pane. Poi il sale. |
| IND-02-05 | Indizi | Lui: alto come una bottiglia da un litro e mezzo. Barba fino ai piedi. Camicia rossa, cintura di corda. Naso rosso. Occhietti neri. Peloso come un gatto vecchio. |
| IND-02-06 | Indizi | Cercava la stufa. Non c'è. Ha scelto il posto dietro il frigorifero, perché "è caldo e ronza". La babuška lo ha chiamato FOMÀ. |
| RUS-09…14 | Parole russe | pirožki · domovoj · rito «Dedushka, dedushka…» · «Fu!» · «Spokojnoj noči» · Baba Jaga |
| RIC-03 | Ricordi | Le favole della mamma: Baba Jaga, l'uccello di fuoco e il domovoj, lo spirito della casa. Le raccontava prima di dormire. |
| RIC-04 | Ricordi | La telefonata di aprile. «Ha pianto la sera dopo, mentre lavava i piatti, e io ho fatto finta di non vedere.» [LIBRO §01.014] |
| FOT-02-01 | Foto | La scalinata di casa, la prima sera. |
| FOT-02-02 | Foto | Arancini contro pirožki. Pareggio. |
| FOT-GAT-01 | Foto (Gatti) | Il gatto rosso del quarto gradino. Ha aperto un occhio. Uno. |

## Fonti
- Manoscritto §02.001–02.040; `FASI_DI_SVILUPPO.md` §2 #9, Fase 4.
- [Domovoj — Wikipedia (rito del trasloco nel lapot')](https://it.wikipedia.org/wiki/Domovoj)
