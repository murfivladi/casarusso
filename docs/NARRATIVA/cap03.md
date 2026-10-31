# Capitolo 3 — Le signore di fuori

| Voce | Valore |
|---|---|
| Data e giorno | lunedì 15 – giovedì 18 settembre 2025 (notte tra giovedì e venerdì, ~01:30) |
| Arco orario | 4 giornate giocabili (scuola 8:00–13:30, pomeriggio, sera); notte del giovedì |
| Luce | mattine limpide, luce bianca nell'aula; pomeriggi dorati sul Corso; sere in cucina; notte: ingresso buio, nebbia luminosa bianca-azzurra dal buco della serratura |
| Meteo | settembre sereno, 26–28 °C, notti tiepide |
| Luoghi | LUO-SCU scuola media (aula 1ªB, corridoio, cortile) · LUO-SCA-01 · LUO-COR Corso Umberto · LUO-BAR bar di papà · LUO-CR-CUC · LUO-CR-SCL · LUO-CR-ING |
| Durata obiettivo | 22 minuti (raccordi 9) |
| Checkpoint | CP-03-A lunedì · CP-03-B martedì · CP-03-C mercoledì · CP-03-D giovedì · CP-03-E notte · CP-03-F fine |
| Personaggi | Vera, Nicolò, prof.ssa di matematica, prof. di musica, compagni, Irina, Salvo, babuška, Giulia, Mattia, Fomà, Donna Rosalia, Donna Nina, Donna Tina; clienti del bar |
| Libro | §03.001–03.055 (pp. 14–18) |

## Sinossi
Per quattro giorni Vera fa finta di niente: la prima settimana di prima media, la professoressa che scrive i numeri come se la lavagna le avesse fatto un torto, il professore che parla solo di Bellini, Nicolò con le sue centoquaranta carte di dinosauri e la domanda che nessuno le aveva mai fatto: «Quale metà?». A casa il pane dietro il frigo sparisce ogni notte; martedì Vera vede la barba spuntare e una voce le dice «Non ci sono». Giovedì notte la casa profuma di rosmarino: dal buco della serratura entra una nebbia che diventa tre signore. Scoprono Fomà, Fomà scopre loro, e la lite finisce quando Vera starnutisce. «Vera Russo. Figlia di Salvatore. Vieni qui.»

## Struttura delle giornate
| Giorno | Mattina (raccordo scuola) | Pomeriggio (libero breve) | Sera / notte |
|---|---|---|---|
| Lun 15 (CP-03-A) | SCN-03-01 primo giorno, Nicolò e le carte; SCN-03-02 «Quale metà?» | libero 4 min: casa, scalinate, Corso | SCN-03-03 cena: formiche e topi |
| Mar 16 (CP-03-B) | raccordo breve: matematica (lavagna) | SCN-03-04 bar di papà (D-84) | SCN-03-05 la barba sotto il frigo |
| Mer 17 (CP-03-C) | raccordo breve: musica (Bellini) | libero 4 min | SCN-03-06 sera tranquilla, russare |
| Gio 18 (CP-03-D) | raccordo breve: intervallo con Nicolò | libero 3 min | a letto → notte SCN-03-07…11 |

Le mattine di scuola durano 60–120 s ciascuna (massimi in `raccordi.md`); si può saltare l'ultima ora con «Esci» al suono della campanella.

## Scene

### SCN-03-01 — Il primo giorno di prima media (raccordo) · CP-03-A
- **Trigger**: «Vai a scuola» (obiettivo della domenica) o sveglia di lunedì.
- **Obiettivo** OBJ-03-01 [NUOVO]: «Sopravvivere alla prima settimana di prima media. Fare finta di niente.»
- **Beat**: B-03-01.
- **Percorso**: colazione (SCN breve: la babuška [RU] «Доброе утро, Верочка.» · *Dobroe utro, Veročka.* · sottotitolo «Buongiorno, Veročka.» → RUS-15), discesa della scalinata, Corso, salita verso la scuola (percorso guidato dal marker, 70 s), ingresso in aula 1ªB.
- PEN-03-01 [LIBRO §03.001]: «Per quattro giorni feci finta di niente. Andai a scuola, la prima settimana di prima media, e conobbi la professoressa di matematica che scriveva i numeri come se la lavagna le avesse fatto un torto, e il professore di musica che parlava solo di Bellini.»
- PEN-03-02 [LIBRO §03.001]: «Il mio compagno di banco si chiamava Nicolò, aveva gli occhiali con la montatura blu e una collezione di carte di dinosauri che mi mostrò il primo giorno, una per una, tutte e centoquaranta.»
- **Nicolò e le carte** (seduti al banco): NICOLÒ [NUOVO]: «Questa è la uno. Allosaurus. Questa è la due…»
  - `*` (1) «Fammele vedere tutte.» → minigioco «sfoglia le carte» (140 carte, una ogni 0,4 s, si può accelerare; i nomi scorrono) → flag_nicolo_tutte_carte = true; rap_nicolo +1
  - `*` (2) «Quante sono?» → NICOLÒ [NUOVO]: «Centoquaranta. Te le mostro.» (le mostra lo stesso, sintesi di 10 s)
- **Fotografabile**: FOT-03-01 la lavagna con i numeri «arrabbiati» della prof.

### SCN-03-02 — «Quale metà?» (dialogo)
- **Trigger**: fine delle carte (o alla ricreazione).
- **Beat**: B-03-02.
- NICOLÒ [LIBRO §03.002] [VOCE VOX-03-01]: «Tu sei russa?»
- VERA [LIBRO §03.003]: «Metà.»
- NICOLÒ [LIBRO §03.004] [VOCE VOX-03-02]: «Quale metà?»
- PEN-03-03 [LIBRO §03.005]: «Ci pensai. Nessuno me l'aveva mai chiesto così.»
- **Pausa di riflessione** [NUOVO]: tre pensieri appaiono a biro e si cancellano uno dopo l'altro (non sono scelte: Vera ci pensa) — «La metà di sopra?» · «La metà che parla?» · «La metà che mangia i pirožki?» — poi:
- VERA [LIBRO §03.006] [VOCE VOX-03-03]: «Non lo so. Credo che siano mescolate.»
- PEN-03-04 [LIBRO §03.007]: «Nicolò annuì, come se fosse una risposta normale, e mi mostrò un Pachycephalosaurus.»
- Se `flag_nicolo_tutte_carte`: NICOLÒ [NUOVO]: «Questo è doppio. Tienilo.» → oggetto PRP-CARTA-PACHY nella camera di Vera; FOT-03-02 fotografabile.
- **Voci del quaderno**: IND-03-01 [NUOVO] «Nicolò mi ha chiesto: "Quale metà?". Ho detto: mescolate. Non lo so davvero.» *(Questa voce tornerà nella pagina CASA RUSSO, 14.026.)*

### SCN-03-03 — Formiche, topi e trappole (dialogo a cena)
- **Trigger**: sera di lunedì (cena alle 20:00).
- **Beat**: B-03-03.
- PEN-03-05 [LIBRO §03.008]: «A casa, intanto, la babuška lasciava il pane dietro il frigorifero ogni sera, e ogni mattina il pane non c'era più.»
- IRINA [NUOVO, dal libro «Mia madre diceva che erano le formiche»]: «Sono le formiche. Settembre, il caldo… le formiche.»
- SALVO [NUOVO, dal libro «Mio padre diceva che erano i topi e voleva mettere le trappole»]: «Formiche? Quella è roba da topi. Domani metto le trappole.»
- (la babuška lo guarda — primo piano di 2 s sul suo sguardo, ANI-BAB)
- SALVO [NUOVO]: «…O magari aspettiamo. Le formiche, sì. Le formiche.»
- PEN-03-06 [LIBRO §03.008]: «la babuška lo guardò in un modo che gli fece cambiare idea. Io non dicevo niente.»
- **Scelta di Vera** (tutte coerenti con «Io non dicevo niente»: Vera tace a tavola, la scelta è solo cosa fa):
  - `*` (1) guardare il frigorifero → PEN-03-07 [NUOVO]: «Il frigo ronzava. Come se non sapesse niente nemmeno lui.»
  - `*` (2) guardare la babuška → rap_babuska +1 → la babuška ricambia lo sguardo e versa a Vera più minestra
  - `*` (3) guardare Mattia → Mattia ha lo sguardo sul frigo, poi torna a mangiare (seme per il cap. 4) → rap_mattia +1
- **Giulia** (`rap_giulia >= 1`): GIULIA [NUOVO]: «I topi? In questa casa? Allora io dormo da Marta.» → rap_giulia invariato (battuta).
- **Dopo**: libero in casa; di notte (se Vera passa in cucina a prendere un bicchiere d'acqua) brontolii o canticchiare da dietro il frigo (SFX-016 «[voce brontolona dietro il frigo]», SFX-017 «[canticchiare dietro il frigo]»), PEN-03-08 [LIBRO §03.008]: «Ma la sera, quando passavo in cucina a prendere un bicchiere d'acqua, sentivo da dietro il frigo qualcuno che brontolava, o canticchiava, o russava.»
- **Voci del quaderno**: IND-03-02 [NUOVO] «Il pane dietro il frigo sparisce ogni notte. Mamma dice formiche. Papà dice topi. La babuška non dice niente, ma guarda.»

### SCN-03-04 — Il pomeriggio al bar di papà (raccordo, D-84)
- **Tipo**: raccordo (massimo 5 min) + primo turno di SIS-16 (tutorial).
- **Trigger**: martedì dopo la scuola.
- **Obiettivo** OBJ-03-04 [NUOVO]: «Fare i compiti al bar di papà. Al tavolino in fondo, quello vicino al bagno, che nessun turista vuole.»
- **Svolgimento**: Salvo mostra come si fa un caffè (tutorial bar: 3 ordini guidati); poi Vera può sedersi al tavolino in fondo (compiti: sfogliare il quaderno, pagine di scienze).
  - SALVO [NUOVO]: «Il caffè ha tre nemici: la fretta, l'acqua sbagliata e i turisti che chiedono il cappuccino alle cinque del pomeriggio.»
  - Al primo ordine corretto: flag_bar_cap3 = true; rap_salvo +1.
- **Clienti con battute**: `mondo_libero.md` §1.2 (set «settembre»).
- **Voci del quaderno**: nessuna di trama.

### SCN-03-05 — La barba sotto il frigo (dialogo, sera di martedì)
- **Trigger**: martedì sera, Vera entra in cucina da sola (dopo le 22:00) — guidato dall'obiettivo OBJ-03-05 [NUOVO] «Prendere un bicchiere d'acqua. Solo un bicchiere d'acqua.»
- **Beat**: B-03-04.
- PEN-03-09 [LIBRO §03.009]: «Una volta, il martedì, vidi la barba. Spuntava di sotto il frigorifero come una coda di gatto. Io mi fermai. La barba si ritirò di scatto.» (la barba è un oggetto visibile per 3 s se Vera guarda il frigo; se Vera si inginocchia rapidamente vede la barba ritirarsi)
- **Scelta** (cosa dice Vera; in tutti i rami seguono le battute del libro):
  - `*` (1) «Lo so che ci sei.» (piano) → flag_barba_gentile = true; rap_foma +1
  - `*` (2) «Lo so che ci sei, signor Fomà.» → flag_barba_gentile = true; rap_foma +1; FOMÀ aggiunge dopo «Non ci sono.» [NUOVO]: «…E non sono signore. Sono domovoj.»
  - `*` (3) «Ti ho visto, sai. Esci.» → rap_foma 0
  - In tutti i casi la prima battuta pronunciata è VERA [LIBRO §03.010] «Lo so che ci sei» (nella variante 2 seguita da «signor Fomà» [NUOVO]; nella 3 preceduta da «Ti ho visto, sai.» [NUOVO]).
- PEN-03-10 [LIBRO §03.011]: «Silenzio. Poi una voce:»
- FOMÀ [LIBRO §03.012] [VOCE VOX-03-04]: «Non ci sono.»
- VERA [LIBRO §03.013]: «Ti ho visto.»
- FOMÀ [LIBRO §03.014] [VOCE VOX-03-05]: «Hai visto la polvere. In questa casa non pulisce nessuno.»
- PEN-03-11 [LIBRO §03.015]: «E poi niente più.»
- **Voci del quaderno**: IND-03-03 [NUOVO] «Martedì: la barba sotto il frigo, come una coda di gatto. Ha detto "Non ci sono". Quindi c'è.»
- **Fotografabile**: tentativo di foto alla barba → pavimento con un po' di polvere (regola spiriti).

### SCN-03-06 — Mercoledì (raccordo serale)
- **Tipo**: raccordo (massimo 3 min).
- **Trigger**: mercoledì sera.
- **Svolgimento**: cena breve (Mattia racconta la scuola: MATTIA [NUOVO] «La maestra dice che sono in prima elementare. Io dico asilo. Facciamo a metà.»); poi a letto; dal basso SFX-015 «[russare]» — PEN-03-12 [NUOVO]: «Russava. Un domovoj che russa. Nei libri non c'era scritto.»
- **Voci del quaderno**: nessuna.

### SCN-03-07 — Giovedì notte: il profumo (guidata) · CP-03-E
- **Trigger**: giovedì, Vera si addormenta (dissolvenza); risveglio di colpo (ora 01:28).
- **Obiettivo** OBJ-03-07 [NUOVO]: «Scendere a vedere. Piano. Il nono gradino scricchiola.»
- **Beat**: B-03-05, B-03-06.
- PEN-03-13 [LIBRO §03.016]: «Il giovedì notte mi svegliai di colpo. Non so che ore fossero. So che la casa era buia e che c'era un profumo nuovo nell'aria. Non i gelsomini del vicino. Un profumo di rosmarino, e di lenzuola stese al sole, e di qualcos'altro, dolce e antico, come le chiese.»
- Particelle di profumo (filamenti dorati appena visibili, ART_BIBLE §11.6) entrano dalla porta socchiusa.
- SFX-019 «[voci di donne che ridono piano]» (sotto, davanti).
- PEN-03-14 [LIBRO §03.017–03.018]: «Poi sentii delle voci. Voci di donne, che ridevano piano. Venivano dal piano di sotto.»
- **Scale**: discesa a piedi nudi; il 9° gradino evidenziato: saltarlo (E) → nessun suono; pestarlo → SFX-012 e le voci si fermano 2 s, poi riprendono (nessun fallimento: le Donne pensano a un gatto — DONNA NINA fuori campo [NUOVO]: «Un gatto.»).
- PEN-03-15 [LIBRO §03.019]: «Scesi le scale a piedi nudi, attenta a saltare il nono gradino, che scricchiola. In fondo alle scale c'è l'ingresso, con il portone di legno, e il portone ha una serratura vecchia, enorme, con il buco della chiave grande come un dito.»
- Vera si ferma allo stipite tra scale e ingresso/cucina (punto segnato).

### SCN-03-08 — Le Donne di Fora entrano (cinematica, sguardo libero)
- **Beat**: B-03-07, B-03-08.
- **VFX**: `ART_BIBLE.md` §11 (nebbia dalla serratura, formazione dal basso, braccialetti, gonne di nebbia).
- PEN-03-16 [LIBRO §03.020–03.021]: «Dal buco della chiave stava entrando una nebbia. Una nebbia bianca e luminosa, che usciva dalla serratura come il fumo da un camino, e si raccoglieva sul pavimento dell'ingresso, e si alzava, e prendeva forma.»
- SFX-020 «[nebbia che sibila dalla serratura]».
- PEN-03-17 [LIBRO §03.021]: «Prima una gonna. Poi una vita stretta. Poi due braccia con dei braccialetti che tintinnavano. Poi una testa con i capelli raccolti in alto e un pettine di tartaruga.» — SFX-018 «[braccialetti che tintinnano]».
- PEN-03-18 [LIBRO §03.022]: «Una signora. Alta, elegante, vestita di un abito lungo color vino, con un ventaglio in mano. Aveva il viso bellissimo e severo, come le statue delle sante nelle processioni.»
- PEN-03-19 [LIBRO §03.023–03.024]: «Dietro di lei, dal buco della serratura, entrò un'altra nebbia, e poi un'altra. La seconda signora era più bassa e più tonda, vestita di verde, con una collana di perle e una bocca che non stava mai ferma.»
- PEN-03-20 [LIBRO §03.024]: «La terza era giovane, quasi una ragazza, con un vestito celeste e i capelli sciolti, e si guardava intorno con gli occhi spalancati come se fosse la prima volta che entrava in una casa.»
- **Durata**: 30 s di formazione (tre Donne sfalsate di 6 s).

### SCN-03-09 — «Vediamo come la tengono, questa casa» (dialogo osservato)
- **Beat**: B-03-09, B-03-10.
- ROSALIA [LIBRO §03.025] [VOCE VOX-03-06]: «Bene, bene. Vediamo come la tengono, questa casa.» (ventaglio sotto il mento)
- PEN-03-21 [LIBRO §03.026]: «Passò un dito sul mobile dell'ingresso. Guardò il dito. Fece una smorfia.»
- ROSALIA [LIBRO §03.027] [VOCE VOX-03-07]: «Polvere. Di nuovo.»
- NINA [LIBRO §03.028] [VOCE VOX-03-08]: «Gliel'avevo detto, Donna Rosalia. Da quando è arrivata la forestiera, qui nessuno pulisce più come si deve. Pensa che stamattina ho visto le lenzuola del bambino stese storte.»
- ROSALIA [LIBRO §03.029]: «Storte, Donna Nina?»
- NINA [LIBRO §03.030]: «Storte, Donna Rosalia. Con le mollette spaiate.»
- PEN-03-22 [LIBRO §03.031]: «La ragazza in celeste intanto era andata verso la cucina, e allungava il collo per guardare dentro.» (Tina passa a 1,5 m da Vera senza vederla: Vera può arretrare d'istinto, animazione automatica)
- ROSALIA [LIBRO §03.032] [VOCE VOX-03-09]: «Donna Tina! Non si gira per le stanze senza permesso.»
- TINA [LIBRO §03.033] [VOCE VOX-03-10]: «C'è un odore strano. Di pane. Pane nero. Non l'ho mai sentito.»
- **Voci del quaderno**: IND-03-04 [NUOVO] «Giovedì notte: dal buco della serratura è entrata una nebbia. È diventata tre signore. La prima col ventaglio, vestito color vino. La seconda verde, con le perle. La terza celeste, giovane.» · IND-03-05 [NUOVO] «Si chiamano Donna Rosalia, Donna Nina, Donna Tina. Controllano la polvere. E le lenzuola. E le mollette.»

### SCN-03-10 — Fomà contro le Donne (cinematica-dialogo osservato)
- **Beat**: B-03-11.
- PEN-03-23 [LIBRO §03.034]: «E fu allora che dal fondo della cucina, da dietro il frigorifero, venne la voce di Fomà.»
- FOMÀ [LIBRO §03.035] [VOCE VOX-03-11]: «Chi è? Chi c'è? Chi entra a quest'ora in casa mia?»
- PEN-03-24 [LIBRO §03.036]: «Le tre signore si voltarono tutte insieme. Il ventaglio di Donna Rosalia si chiuse con uno schiocco.» — SFX-021 «[ventaglio che si chiude]».
- ROSALIA [LIBRO §03.037] [VOCE VOX-03-12]: «Casa sua?»
- PEN-03-25 [LIBRO §03.038]: «Fomà uscì da dietro il frigorifero. Aveva la barba tutta arruffata e il naso più rosso del solito, e si era messo in piedi sul lapot' per sembrare più alto. Non serviva: era sempre alto come una bottiglia.» (ANI-FOM-08)
- PEN-03-26 [LIBRO §03.039]: «Le tre signore lo guardarono. Lui guardò loro. Per un lungo momento nessuno parlò.»
- NINA [LIBRO §03.040] [VOCE VOX-03-13]: «E questa cos'è? Un topo?» (mano alle perle)
- FOMÀ [LIBRO §03.041] [VOCE VOX-03-14] (diventa viola: parametro di materiale): «Un topo! Io sono il domovoj di questa famiglia! Da duecento anni! Ho protetto sette generazioni di Ivanov, ho scaldato le loro stufe, ho intrecciato le criniere dei loro cavalli...»
- TINA [LIBRO §03.042] [VOCE VOX-03-15] (sinceramente dispiaciuta): «Qui non ci sono cavalli.»
- FOMÀ [LIBRO §03.043] [VOCE VOX-03-16]: «...e adesso sono qui, e questa è la mia casa!»
- ROSALIA [LIBRO §03.044] [VOCE VOX-03-17] (un passo avanti, la nebbia della gonna si allarga sul pavimento): «Ah no, caro mio. Questa casa è nostra. Noi siamo le Donne di Fora. Veniamo in questa casa il martedì, il giovedì e il sabato, da quando c'erano i nonni dei nonni di Salvatore Russo. Noi portiamo la fortuna in questa casa, se la tengono bene. E la sfortuna, se non la tengono bene. Nessuno ci ha detto niente di una bestia forestiera dietro il frigorifero.»
- FOMÀ [LIBRO §03.045] [VOCE VOX-03-18] (salta giù dal lapot': ANI-FOM-09): «Bestia! Bestia a me! Gallinelle! Gallinelle con il pizzo!»
- ROSALIA [LIBRO §03.046] [VOCE VOX-03-19] (gelida): «Fuori. Fuori da questa casa.»
- FOMÀ [LIBRO §03.047] [VOCE VOX-03-20]: «Fuori voi!»
- **Voci del quaderno**: IND-03-06 [NUOVO] «Le Donne di Fora vengono martedì, giovedì e sabato, "da quando c'erano i nonni dei nonni di papà". Portano fortuna se la casa è pulita. Fomà dice che la casa è sua. Loro dicono che è loro. GUERRA?»

### SCN-03-11 — Lo starnuto di Vera (cinematica) · CP-03-F
- **Beat**: B-03-12.
- **Regia**: il freddo del pavimento: la camera di Vera si sporge (automatico, 1 s) oltre lo stipite; inspirazione; SFX-022 «[starnuto di Vera]».
- PEN-03-27 [LIBRO §03.048]: «E fu in quel momento che commisi l'errore. Mi sporsi troppo dallo stipite della porta, e il pavimento dell'ingresso, che era freddo, mi fece starnutire.»
- PEN-03-28 [LIBRO §03.049–03.050]: «Quattro teste si voltarono verso di me. Tre signore eleganti fatte di nebbia e un vecchietto alto come una bottiglia mi guardarono, nella cucina buia, con la stessa identica espressione.» (le quattro teste si girano insieme: ANI-DON-06 + ANI-FOM-16; la stessa espressione in blend shapes)
- TINA [LIBRO §03.051] [VOCE VOX-03-21] (piano, meravigliata): «Lei ci vede.»
- NINA [LIBRO §03.052] [VOCE VOX-03-22]: «Impossibile.»
- FOMÀ [LIBRO §03.053] [VOCE VOX-03-23]: «Ci vede. Lo sapevo. Lo dicevo io. Quella mi vede dal primo giorno.»
- Se `flag_barba_gentile`: PEN-03-29 [NUOVO]: «"Quella". Martedì gli avevo parlato gentile. Evidentemente non abbastanza.»
- PEN-03-30 [LIBRO §03.054]: «Donna Rosalia aprì il ventaglio, lentamente. Mi guardò da sopra il bordo, con gli occhi neri e lucidi.» (primo piano in prima persona su Rosalia, DOF)
- ROSALIA [LIBRO §03.055] [VOCE VOX-03-24]: «Vera Russo. Figlia di Salvatore. Vieni qui.»
- Taglio al nero sul ventaglio.
- **Effetti**: rap_rosalia +0; rap_tina +1 (Tina è meravigliata); rap_nina −0.
- **Fine del capitolo**: scheda con frase [NUOVO]: «Tre signore di nebbia e un domovoj. Tutti nella nostra cucina. E sapevano il mio nome.»
- **In v1.0**: dopo la scheda compare la pagina del quaderno «Continua…» scritta da Vera 13–14 anni [NUOVO]: «Quella notte, in cucina, cominciò la guerra delle tazzine. Ma questa è un'altra pagina.» → flag_v1_fine = true → domenica 14 settembre ripetibile (D-82). **In v2.0**: si passa a SCN-04-01 senza interruzioni.

## Voci del quaderno del capitolo

| ID | Sezione | Testo |
|---|---|---|
| IND-03-01 | Indizi | Nicolò mi ha chiesto: "Quale metà?". Ho detto: mescolate. Non lo so davvero. |
| IND-03-02 | Indizi | Il pane dietro il frigo sparisce ogni notte. Mamma dice formiche. Papà dice topi. La babuška non dice niente, ma guarda. |
| IND-03-03 | Indizi | Martedì: la barba sotto il frigo, come una coda di gatto. Ha detto "Non ci sono". Quindi c'è. |
| IND-03-04 | Indizi | Giovedì notte: dal buco della serratura è entrata una nebbia. È diventata tre signore. La prima col ventaglio, vestito color vino. La seconda verde, con le perle. La terza celeste, giovane. |
| IND-03-05 | Indizi | Si chiamano Donna Rosalia, Donna Nina, Donna Tina. Controllano la polvere. E le lenzuola. E le mollette. |
| IND-03-06 | Indizi | Le Donne di Fora vengono martedì, giovedì e sabato, "da quando c'erano i nonni dei nonni di papà". Portano fortuna se la casa è pulita. Fomà dice che la casa è sua. Loro dicono che è loro. GUERRA? |
| RUS-15 | Parole russe | «Dobroe utro» — buongiorno |
| FOT-03-01 | Foto | La lavagna della prof di matematica. I numeri sembrano arrabbiati. |
| FOT-03-02 | Foto | Il Pachycephalosaurus di Nicolò (doppio). |

## Fonti
- Manoscritto §03.001–03.055; `FASI_DI_SVILUPPO.md` Fase 4 (cap. 3).
- [Regione Siciliana — inizio lezioni 15 settembre 2025](https://www.regione.sicilia.it/la-regione-informa/anno-scolastico-202526-sicilia-campanella-inizio-lezioni-15-settembre)
- [Donne di fuori — Wikipedia](https://it.wikipedia.org/wiki/Donne_di_fuori)
