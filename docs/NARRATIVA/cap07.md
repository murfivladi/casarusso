# Capitolo 7 — La casa tossisce

| Voce | Valore |
|---|---|
| Data e giorno | mercoledì 15 – martedì 21 ottobre 2025 |
| Arco orario | 6 giornate brevi (mattina della scoperta + pomeriggio libero breve) e la sera di martedì 21 (litigio, ~21:30) |
| Luce | mattine bianche sulle scale (la crepa in luce radente); pomeriggi d'ottobre più corti (tramonto 18:20); sera: luce calda della cucina che filtra sulle scale buie |
| Meteo | ancora caldo di giorno (24 °C), notti più fresche (16 °C); il 18 velato |
| Luoghi | LUO-CR-SCL (crepa al 9° gradino) · LUO-CR-QEL quadro elettrico (sottoscala) · LUO-CR-CUC (rubinetto) · LUO-CR-COR (limone) · LUO-SCA-01 (casse d'acqua) · LUO-CR-COR2 corridoio di sopra |
| Durata obiettivo | 16 minuti (raccordi 5) |
| Checkpoint | CP-07-A crepa (mer 15) · CP-07-B luce (gio 16) · CP-07-C acqua (sab 18) · CP-07-D limone (lun 20) · CP-07-E litigio (mar 21) |
| Personaggi | Vera, Salvo, Irina, Giulia, Mattia, babuška, nonna Concetta, Fomà (voce), Donne (rigide nell'ingresso), elettricista (comparsa) |
| Libro | §07.001–07.048 (pp. 34–38) |
| Sistema principale | SIS-12 Stato della casa |

## Sinossi
Dopo il Pokrov la guerra ricomincia peggio di prima, e la casa si ammala: una crepa parte dal muro delle scale all'altezza del nono gradino e cresce di una mano al giorno; la luce salta senza motivo; dal rubinetto esce un'acqua che sa di ferro; il limone, il vero padrone di casa, perde le foglie a ottobre. Fomà borbotta tutta la notte, le Donne restano rigide nell'ingresso. Poi, un martedì sera, Vera sente mamma e papà litigare: «Ma un po' quanto, Salvo?». Giulia, spaventata: «È tutto da quando è arrivata lei». Di notte una metà di Vera pensa «forse sarebbe meglio», e l'altra metà piange.

## Scene

### SCN-07-01 — La guerra ricomincia (raccordo narrato)
- **Trigger**: mattina di mercoledì 15.
- **Beat**: B-07-01.
- **Testo del libro**: [LIBRO §07.001–07.003] come pensieri durante la colazione (Donna Nina e la candela «per bruciare la casa», le briciole nei letti di tutta la famiglia, «come una bicicletta in discesa»; «Ma questa volta successe una cosa diversa. La casa si ammalò.»).
- **Interazione**: il letto di Vera ha briciole (PEN-07-01 [NUOVO] «Briciole di pane nero nel letto. Una vendetta che pizzica.»).

### SCN-07-02 — La crepa (scoperta) · CP-07-A
- **Beat**: B-07-02. **Stato**: casa_crepa = 1 (mer), 2 (gio), 3 (ven) — avanzamento automatico per giorno (SIS-12).
- **Testo del libro**: [LIBRO §07.004–07.006] (sul muro delle scale all'altezza del nono gradino, sottile, lunga come una mano, «come un fulmine disegnato a matita»; «Papà. C'è una crepa.»; papà si gratta la testa: le case vecchie, l'umidità, il muratore; il giorno dopo due mani, poi tre).
- **Interazione**: guardare la crepa da vicino → misura con la mano di Vera (ANI: Vera appoggia la mano aperta accanto alla crepa: la crepa è lunga come la mano — giorno 1; due mani — giorno 2; tre — giorno 3). Fotografabile ogni giorno → FOT-07-01 (si aggiorna).
- SALVO [NUOVO, dal libro]: «Le case vecchie fanno così. È l'umidità. Chiamo il muratore.»
- **Voce del quaderno**: IND-07-01 [NUOVO] «Mer 15: una crepa sul muro delle scale, al nono gradino. Lunga come la mia mano. Gio: due mani. Ven: tre. Papà: "l'umidità".» (si aggiorna ogni giorno con una nuova riga)

### SCN-07-03 — La luce salta · CP-07-B
- **Beat**: B-07-03. **Stato**: casa_luce = 2.
- **Testo del libro**: [LIBRO §07.007–07.008] (a cena, mentre la mamma stira, mentre Giulia si asciuga i capelli: «tac», tutto buio; papà scende al quadro elettrico con la torcia; l'elettricista viene due volte; la terza non viene più).
- **Evento giocabile**: blackout durante la cena di giovedì (SFX-040 «[tac: la luce salta]»); Vera accende la torcia del telefono (tutorial ripasso) e accompagna papà al quadro elettrico nel sottoscala: tirare su l'interruttore (SFX-041). ELETTRICISTA (sabato, comparsa) [NUOVO]: «Signor Russo, l'impianto è a posto. Ve lo giuro sulla testa di mia madre.»
- **Voce del quaderno**: IND-07-02 [NUOVO] «La luce salta. Tac. Senza motivo. L'elettricista dice che l'impianto è a posto. La terza volta non è venuto.»

### SCN-07-04 — L'acqua che sa di ferro e le casse (raccordo) · CP-07-C
- **Tipo**: raccordo (massimo 4 min).
- **Beat**: B-07-04. **Stato**: casa_acqua = 1, poi 2 (domenica).
- **Testo del libro**: [LIBRO §07.009] (acqua limpida che sa di ferro e ruggine; le casse d'acqua del supermercato su per la scalinata, sudando, sei bottiglie per volta).
- **Raccordo giocabile**: sabato 18, portare due casse d'acqua (6 bottiglie) dalla Circonvallazione alla cucina con Irina; Vera porta una cassa (camminata lenta 0,9 m/s, respiro); sulla scalinata, il gatto rosso dorme sul quarto gradino (bisogna scavalcarlo).
  - IRINA [NUOVO]: «Sei bottiglie per volta. Tua nonna con il ginocchio non può. Tuo padre è al bar. Restiamo noi.»
  - Al termine: flag_casse_portate = true; rap_irina +1.
- **Interazione**: assaggiare l'acqua del rubinetto → PEN-07-02 [NUOVO] «Limpida. E sa di chiodo.»
- **Voce del quaderno**: IND-07-03 [NUOVO] «L'acqua del rubinetto sa di ferro e di ruggine. Anche se è limpida. Portiamo su le casse dal supermercato, sei bottiglie per volta.»

### SCN-07-05 — Il limone · CP-07-D
- **Beat**: B-07-05. **Stato**: casa_limone = 1 (sab), 2 (dom), 3 (lun).
- **Testo del libro**: [LIBRO §07.010–07.014] (il limone perde le foglie a ottobre; foglie gialle accartocciate, limoni verdi caduti; Concetta alla finestra: «Sta morendo. Questo limone l'ha piantato il nonno di tuo nonno, Vera. Non si è mai ammalato. Mai. Nemmeno con la siccità del Novantadue.»; Concetta guarda la babuška, la babuška guarda lei, niente).
- Doppiato: CONCETTA §07.012 [VOX-07-01].
- **Interazione**: raccogliere un limone verde caduto (oggetto PRP-LIMONE-VERDE in tasca, si può posare in cucina); rap_concetta +1 se Vera sta vicina a Concetta durante la battuta.
- **Fotografabile**: FOT-07-02 il limone che perde le foglie.
- **Voci del quaderno**: RIC-08 [LIBRO §07.012 + NUOVO] «Il limone del cortile l'ha piantato il nonno del nonno Turi. Non si è mai ammalato, nemmeno con la siccità del '92.» · IND-07-04 [NUOVO] «Il limone perde le foglie. A ottobre. Nonna Concetta: "Sta morendo." Poi ha guardato la babuška. La babuška ha guardato lei. Niente.»

### SCN-07-06 — La casa ha l'influenza (notte)
- **Beat**: B-07-06.
- **Trigger**: notte di domenica 19 (o qualsiasi notte libera di questi giorni dopo casa_crepa = 3).
- **Testo del libro**: [LIBRO §07.015–07.017] come pensieri (l'influenza della casa nelle pareti, nei gradini, nelle porte che sbattono da sole; la casa scricchiola come un vecchio nel letto; «una notte, giuro, sentii la casa tossire»; Fomà borbotta tutta la notte; le Donne entrano martedì, giovedì e sabato ma restano rigide nell'ingresso a guardare la cucina «come si guarda un nemico»; «La casa era malata perché loro litigavano»).
- **Eventi**: SFX-039 «[la casa scricchiola]», SFX-027 «[porta che sbatte]» (da sola), SFX-044 «[la casa tossisce]» (dai muri, colpo secco e profondo; vibrazione leggera del gamepad); SFX-016 brontolio continuo dal frigo.
- **Notte di sabato 18 (notte delle Donne)**: se Vera scende, vede le tre Donne immobili nell'ingresso; dialogo breve:
  - ROSALIA [NUOVO]: «Vai a dormire, Vera Russo.»
  - `*` (1) «La casa sta male.» → ROSALIA [NUOVO]: «Lo sappiamo.» (nient'altro) · `*` (2) «È colpa vostra?» → NINA [NUOVO]: «Nostra? Chiedilo al topo.» → rap_nina −1 · `*` (3) tornare su.
- **Voce del quaderno**: IND-07-05 [NUOVO] «La casa ha l'influenza. Scricchiola come un vecchio nel letto. Una notte l'ho sentita tossire. Fomà borbotta, le Donne stanno rigide nell'ingresso. La casa è malata perché loro litigano.»

### SCN-07-07 — Il litigio (ascolto dalle scale) · CP-07-E
- **Trigger**: martedì 21, sera (21:30), Vera fa i compiti di inglese in camera.
- **Beat**: B-07-07.
- **Testo del libro**: [LIBRO §07.018–07.031] — integrale: voci dalla cucina; «Io non li avevo mai sentiti litigare davvero»; Vera esce scalza e si siede in cima alle scale; il litigio («…non ho detto questo, Irina…» → «Ma un po' quanto, Salvo? Dimmelo tu. Quanto?» «E mio padre non rispose.»).
- Doppiato (scena chiave): SALVO §07.022, §07.024, §07.026 [VOX-07-02…04]; IRINA §07.023, §07.025, §07.030 [VOX-07-05…07]; IRINA §07.027 e SALVO §07.028 [VOX-07-08…09].
- **Regia**: Vera seduta sull'ultimo gradino in alto (postura seduta, ginocchia al petto, ANI corpo per i riflessi); la camera può guardare giù verso la luce della cucina (non si vedono i genitori, solo le ombre sul muro); le voci sono basse e dure, spazializzate; la crepa è a destra di Vera, all'altezza del 9° gradino in basso. Se `flag_casse_portate`: IRINA aggiunge prima di §07.023 [NUOVO] «Oggi Vera ha portato le casse d'acqua con me, sai? Su per la scalinata.» (poi il litigio continua uguale).
- **Interazione proibita**: scendere le scale durante il litigio → Vera si ferma al quinto gradino da sola (PEN-07-03 [NUOVO] «Le gambe non volevano scendere.») e torna su: nessun fallimento.
- PEN-07-04 [LIBRO §07.032]: «Io rimasi seduta sul gradino, con le ginocchia strette contro il petto. Sentivo una cosa nella pancia, come una mano fredda che stringeva.»
- **Voce del quaderno**: IND-07-06 [NUOVO] «Mamma e papà hanno litigato. Davvero. "Avevi detto solo per un po'. Ma un po' quanto, Salvo?" Papà non ha risposto.»

### SCN-07-08 — «Hai sentito?» (dialogo con Giulia)
- **Beat**: B-07-08.
- **Testo del libro**: [LIBRO §07.033–07.042] (Giulia con le cuffie al collo, rabbia diversa, spaventata; «Hai sentito?»; Vera annuisce; «È tutto da quando è arrivata lei. Tutto. La casa che si rompe. Mamma e papà che litigano. Le nonne che si odiano. Era tutto normale, prima.»; «Non è colpa della babuška.» «E di chi è?»; Vera non può dirglielo; «Non lo so.»; Giulia rientra e sbatte la porta; la crepa scricchiola e si allunga di un dito).
- Doppiato: GIULIA §07.034, §07.036, §07.038 [VOX-07-10…12].
- **Scelta di Vera** prima di «Non lo so» (07.039 è il pensiero «Io non potevo dirglielo…»): due tentazioni mostrate come scelte, entrambe si chiudono con la battuta del libro:
  - `*` (1) «È colpa di…» (Vera si ferma) → VERA [LIBRO §07.040]: «Non lo so.»
  - `*` (2) (abbassare gli occhi) → VERA [LIBRO §07.040]: «Non lo so.»
- **Ramo Giulia alleata** (`flag_giulia_ginevra or rap_giulia >= 2`): dopo la porta sbattuta, 3 s, la porta si riapre di due dita: GIULIA [NUOVO] «Se senti ancora rumori, bussa.» e la richiude piano (vedi `00_struttura.md` §4).
- **Evento**: SFX-045 «[la crepa scricchiola]» accanto a Vera; la crepa si allunga di un dito (animazione dello shader, casa_crepa resta 3 con sub-stadio).
- PEN-07-05 [LIBRO §07.042]: «E nel muro delle scale, accanto a me, la crepa scricchiolò, e si allungò ancora di un dito.»

### SCN-07-09 — Divisa in due (notte, fine)
- **Beat**: B-07-09.
- **Regia**: Vera a letto al buio; sguardo libero al soffitto; ogni frase del libro compare a biro e si cancella (la metà «cattiva» in grafia più piccola).
- PEN-07-06 [LIBRO §07.043–07.045]: «Quella notte, nel letto, pensai a una cosa che non avevo mai pensato prima.» · «Tutto normale. Tutto siciliano.»
- PEN-07-07 [LIBRO §07.046]: «E una metà di me, una metà piccola e cattiva, pensò: forse sarebbe meglio.»
- PEN-07-08 [LIBRO §07.047]: «E l'altra metà si mise a piangere.»
- VOX-07-13 [LIBRO §07.048] [VOCE narratrice]: «E io rimasi lì, al buio, divisa in due, e non sapevo più quale delle due metà fossi io.»
- **Fine**: scheda con frase [NUOVO]: «Una crepa, una luce che salta, un'acqua che sa di ferro, un limone che si spoglia. E due metà di me che non si parlano.»
- **Cosa cambia nel mondo**: casa malata attiva in libero (casa_crepa 3, casa_luce 2, casa_acqua 2, casa_limone 3); mercoledì 22 è giornata breve (raccordo RAC-07b in `raccordi.md`) prima del consiglio di giovedì.

## Voci del quaderno del capitolo

| ID | Testo |
|---|---|
| IND-07-01 | Mer 15: una crepa sul muro delle scale, al nono gradino. Lunga come la mia mano. Gio: due mani. Ven: tre. Papà: "l'umidità". |
| IND-07-02 | La luce salta. Tac. Senza motivo. L'elettricista dice che l'impianto è a posto. La terza volta non è venuto. |
| IND-07-03 | L'acqua del rubinetto sa di ferro e di ruggine. Anche se è limpida. Portiamo su le casse dal supermercato, sei bottiglie per volta. |
| IND-07-04 | Il limone perde le foglie. A ottobre. Nonna Concetta: "Sta morendo." Poi ha guardato la babuška. La babuška ha guardato lei. Niente. |
| IND-07-05 | La casa ha l'influenza. Scricchiola come un vecchio nel letto. Una notte l'ho sentita tossire. Fomà borbotta, le Donne stanno rigide nell'ingresso. La casa è malata perché loro litigano. |
| IND-07-06 | Mamma e papà hanno litigato. Davvero. "Avevi detto solo per un po'. Ma un po' quanto, Salvo?" Papà non ha risposto. |
| RIC-08 | Il limone del cortile l'ha piantato il nonno del nonno Turi. Non si è mai ammalato, nemmeno con la siccità del '92. |
| FOT-07-01, 02 | La crepa (si aggiorna) · Il limone che perde le foglie |

## Fonti
- Manoscritto §07.001–07.048; `FASI_DI_SVILUPPO.md` §2 #15.
