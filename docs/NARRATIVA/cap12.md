# Capitolo 12 — Donne di fuori

| Voce | Valore |
|---|---|
| Data e giorno | domenica 26 ottobre (sera) – martedì 28 ottobre 2025, mezzanotte (notte delle Donne) |
| Arco orario | dom 21:00 (Fomà torna) · lun 8:00 scuola, 15:00–18:00 bar, 20:00 cena · mar 18:00–23:55 pulizie · 00:00–00:35 le Donne |
| Luce | domenica sera: cucina calda, il frigo che ronza contento; lunedì: luce piena d'autunno; martedì sera: casa illuminata da tutte le lampade mentre Vera pulisce, poi a mezzanotte solo la lampada dell'ingresso e la nebbia |
| Meteo | sereno, 21 °C |
| Luoghi | LUO-CR-CUC · LUO-SCU · LUO-BAR · LUO-CR-ING · LUO-CR-SCL · camere (lenzuola) · LUO-CR-COR (filo e mollette) · LUO-CR-BAL (rosmarino) |
| Durata obiettivo | 18 minuti (raccordi 5) |
| Checkpoint | CP-12-A lunedì · CP-12-B cena · CP-12-C pulizie · CP-12-D mezzanotte |
| Personaggi | Vera, Fomà (voce), Mattia, Nicolò, prof. di storia, Salvo, nonna Concetta, Irina, Giulia; Donna Rosalia, Donna Nina, Donna Tina |
| Libro | §12.001–12.064 (pp. 61–66) |
| Sistema principale | SIS-24 Pulizie a minigiochi |

## Sinossi
Fomà torna dietro il frigo e mangia tutto, anche un pezzo di formaggio che non era per lui; per la prima volta da giorni la luce non salta. Ma la casa non è guarita: manca la seconda condizione. Lunedì Vera non sente una parola della lezione di storia e al bar scrive tre discorsi, e li cancella tutti. A cena nonna Concetta parla di una cugina «di fuori»: «Da fuori dove?» «Da Catania.» Ed ecco l'idea. Martedì Vera pulisce tutta la casa, cambia le lenzuola, posa un rametto di rosmarino. A mezzanotte fa alle Donne una domanda sola: «Perché vi chiamate Donne di Fora?» Donna Tina racconta: una volta erano loro le forestiere. Donna Rosalia sorride. «Gli parleremo. Sabato. La notte dei Morti.»

## Scene

### SCN-12-01 — Fomà è tornato (raccordo serale)
- **Beat**: B-12-01. **Stato**: casa_luce = 1 (la luce non salta più stanotte; da domani salta raramente).
- **Testo del libro**: [LIBRO §12.001–12.004] come pensieri (Fomà torna dietro il frigo la domenica sera, mangia tutto il pane, il sale, il latte e un pezzo di formaggio che non era per lui; russa così forte che Mattia, al piano di sopra, ride nel sonno; per la prima volta da giorni la luce non salta; ma la crepa, l'acqua marrone, i rami nudi, la febbre un po' più bassa: la seconda condizione non è rispettata; «Le signore.»).
- **Interazione**: posare il lapot' dietro il frigo (gesto di Vera), lasciare pane, sale, latte; se `rap_foma >= 2`: FOMÀ [NUOVO] dal frigo «Buonanotte, Veročka. …Il formaggio era buono.» (da `00_struttura.md` §4).
- SFX-015 «[russare]»; MATTIA ride nel sonno (SFX non sottotitolato).
- **Voce del quaderno**: IND-12-01 [NUOVO] «Fomà è tornato e ha mangiato tutto (anche il formaggio). La luce non salta più. Ma crepa, acqua e limone sono ancora malati. Manca la seconda condizione: le signore.»

### SCN-12-02 — Lunedì a scuola (raccordo) · CP-12-A
- **Tipo**: raccordo (massimo 2 min).
- **Beat**: B-12-02.
- **Testo del libro**: [LIBRO §12.005] (Vera passa la giornata a pensare cosa dire; a scuola non sente una parola della lezione di storia; Nicolò le dà una gomitata quando il professore la chiama alla lavagna).
- **Svolgimento**: aula; la voce del prof. di storia è un mormorio ovattato (filtro audio) mentre Vera guarda il quaderno; evento: gomitata di Nicolò (ANI-NIC-03), PROF. DI STORIA [NUOVO] «Russo! Alla lavagna. I Normanni in Sicilia.» → VERA [NUOVO] «…I Normanni. Arrivarono. Da fuori.» → PROF [NUOVO] «Da fuori. Bene. Molto da fuori. Siediti.» (seme involontario dell'idea).
- Se `flag_nicolo_tutte_carte`: NICOLÒ [NUOVO] all'uscita «Hai la faccia di quando non trovi una carta. Quale ti manca?» → VERA [NUOVO] «Una che ancora non esiste.»

### SCN-12-03 — Tre discorsi al bar (quaderno)
- **Beat**: B-12-02.
- **Testo del libro**: [LIBRO §12.005–12.008] (al bar il pomeriggio scrive sul quaderno tre discorsi diversi e li cancella tutti e tre: *Fomà è buono*; *Se litigate la casa si ammala*; *Vi prego*).
- **Sistema**: al tavolino in fondo, il quaderno mostra i tre discorsi; il giocatore li **scrive** (scegliendo l'ordine) e poi li **cancella** con un tratto di biro (gesto); ogni cancellazione mostra la ragione del libro. val_discorso_scelto = il discorso scritto per ultimo (1–3), usato in SCN-12-06 come tentativo di Vera prima della domanda (una battuta [NUOVO] che Rosalia interrompe).
  - (1) «Fomà è buono.» → [LIBRO §12.006] «Ma Donna Rosalia avrebbe detto che non le interessava se era buono, era forestiero.»
  - (2) «Se litigate la casa si ammala.» → [LIBRO §12.007] «Ma lo sapevano già. L'avevano visto anche loro. E avevano continuato.»
  - (3) «Vi prego.» → [LIBRO §12.008] «Ma non pensavo che Donna Rosalia fosse una che si convince con vi prego.»
- **Voce del quaderno**: IND-12-02 [NUOVO] «Tre discorsi per le Donne: "Fomà è buono", "Se litigate la casa si ammala", "Vi prego". Cancellati tutti e tre.»

### SCN-12-04 — «Da fuori dove?» (dialogo a cena) · CP-12-B
- **Beat**: B-12-03.
- **Testo del libro**: [LIBRO §12.009–12.019] (Concetta porta il brodo di gallina per la babuška e resta a cena; parla con Irina di una signora della parrocchia, della nipote che si sposa, della cugina «che veniva da fuori»; «Da fuori dove?» «Da fuori. Da Catania.»; Vera alza la testa: «Nonna. Catania è a cinquanta chilometri.» «E allora? È fuori. Non è di qua.» «Quindi uno di Catania qui è forestiero?» Concetta ci pensa: «Un po' sì. Non tanto. Ma un po'.»; l'idea «come una lampadina in una cucina buia»; «Fuori.»).
- Doppiato: CONCETTA §12.011, §12.013, §12.016 [VOX-12-01…03]; IRINA §12.010 [VOX-12-04].
- **Regia**: alla parola «Fuori» la lampadina della cucina si accende più forte per un istante (effetto metaforico, solo per Vera: un lieve bloom); PEN-12-01 [LIBRO §12.018–12.019]: «E mi venne un'idea. Una piccola idea, che si accese nella testa come una lampadina in una cucina buia. Fuori.»
- **Scelta**: dopo «Un po' sì. Non tanto. Ma un po'.» `*` (1) ringraziare la nonna con un bacio (rap_concetta +1; CONCETTA [NUOVO] «E questo per cosa?» VERA [NUOVO] «Per Catania.») · `*` (2) scrivere subito «FUORI» nel quaderno.
- **Voce del quaderno**: IND-12-03 [NUOVO] «Nonna Concetta: una di Catania è "di fuori". Un po' forestiera. "Non tanto. Ma un po'." FORA vuol dire FUORI. Donne di Fora = Donne di fuori. PERCHÉ?»

### SCN-12-05 — Martedì: le pulizie (minigiochi SIS-24) · CP-12-C
- **Tipo**: minigiochi + raccordo (massimo 8 min).
- **Beat**: B-12-04.
- **Obiettivo** OBJ-12-05 [NUOVO]: «Pulire tutto. Come piace alle Donne. Lenzuola dritte, mollette uguali, scale lucide, rosmarino.»
- **Testo del libro**: [LIBRO §12.020] (Vera ha pulito tutto: pavimento, mobile dell'ingresso, scale; cambiato le lenzuola a tutti i letti, anche a quello di Giulia, che si lamenta; il rametto di rosmarino del vaso del balcone su un piattino, non bruciato per paura di dare fuoco a qualcosa: «L'avevo solo messo lì, profumato.»).
- **Sequenza** (ordine libero, la casa si «illumina» di pulito a ogni minigioco):
  1. **Lenzuola dritte** — 5 letti (Vera, Giulia, Mattia, genitori, babuška: la babuška è a letto e si alza sulla poltrona: BABUŠKA [RU] «Молодец.» · *Molodec.* · sottotitolo «Brava.» — sblocca RUS-37 se non già in libero). GIULIA [NUOVO] sul suo letto: «Le mie lenzuola? Cosa sei, una fata?» → VERA [NUOVO] «Quasi.» (se `rap_giulia >= 2` Giulia aiuta a tirare un angolo).
  2. **Mollette uguali** — filo in cortile con le lenzuola lavate: 12 mollette di 4 colori, coppie dello stesso colore per lenzuolo («Storte, Donna Rosalia. Con le mollette spaiate», 03.030).
  3. **Scale** — 18 gradini col panno; il 9° ha una macchia ostinata e scricchiola; l'intonaco caduto va raccolto (casa_crepa resta 5).
  4. **Mobile dell'ingresso** — passare il dito come Rosalia (03.026): il dito resta pulito (PEN-12-02 [NUOVO] «Niente polvere. Nemmeno per sbaglio.»).
  5. **Rosmarino sul piattino** — rametto dal vaso del balcone, piattino posato nell'ingresso davanti al portone, non bruciato.
- **Valutazione**: val_pulizie_punteggio 0–12 (tre stelline per i minigiochi 1, 2, 3, 5); flag_pulizie_complete se tutti e cinque.
- **Voce del quaderno**: IND-12-04 [NUOVO] «Martedì: ho pulito tutta la casa. Lenzuola nuove a tutti (anche Giulia). Mollette uguali. Scale lucide. Rosmarino sul piattino, non bruciato. Pronta.»

### SCN-12-06 — La domanda (dialogo) · CP-12-D
- **Beat**: B-12-05.
- **Regia**: Vera seduta per terra nell'ingresso con la schiena contro il muro, davanti al portone (postura seduta); alle 00:00 la nebbia dal buco della serratura.
- **Testo del libro**: [LIBRO §12.021–12.036] — integrale (le tre Donne si formano; Nina con le labbra strette; Tina sorride di nascosto e poi torna seria; «È tornato. Lo sento. Puzza di pane nero da qui.» «Sì. È tornato.» «L'hai riportato tu.» «Sì.»; il ventaglio: «Allora hai deciso da che parte stare.»; «No. Non ho deciso niente. Ho una domanda. Una sola. Posso farla?» — Vera si alza in piedi; il cenno di Tina; «Falla.»; il respiro; «Perché vi chiamate Donne di Fora?»; silenzio; «Che domanda è?»; «È una domanda vera. Fora vuol dire fuori… Voi vi chiamate Donne di fuori. Perché?»).
- Doppiato (scena chiave): ROSALIA §12.023, 12.025, 12.028, 12.031 [VOX-12-05…08]; NINA §12.035 [VOX-12-09]; VERA (12) §12.029, 12.033, 12.036 [VOX-12-10…12].
- **Tentativo di discorso** (prima di «No. Non ho deciso niente…», solo se val_discorso_scelto > 0): VERA [NUOVO] comincia il discorso scritto per ultimo («Fomà è buono…» / «Se litigate…» / «Vi prego…»), ROSALIA la ferma col ventaglio alzato [NUOVO]: «Questo lo so già.» → poi la battuta del libro.
- Se `flag_pulizie_complete`: Tina guarda le scale pulite e sorride più a lungo (ANI-TIN).
- **Alzarsi in piedi**: il giocatore deve alzarsi (Azione) prima di fare la domanda — «perché parlare seduta a una signora così mi sembrava una mancanza di rispetto» (12.029).

### SCN-12-07 — Il racconto di Donna Tina (dialogo)
- **Beat**: B-12-06.
- **Testo del libro**: [LIBRO §12.037–12.049] (Rosalia non risponde, il ventaglio si ferma a metà, nei suoi occhi «come un ricordo»; Nina: «Perché entriamo da fuori… È ovvio.»; «Può darsi. Ma prima?… Siete nate in questa casa?»; Tina: «No. Non siamo nate qui. Nessuna di noi.»; «Tina.»; «È vero, Donna Rosalia…» — il racconto: all'inizio erano loro quelle che arrivavano, bussavano di notte, la gente aveva paura e chiudeva le porte, le chiamavano «quelle di fuori», le estranee; una signora, in un paese, una notte, lasciò la porta aperta, il pane sul tavolo e i letti puliti; da quella volta sono diventate di casa, ma il nome è rimasto; Rosalia a occhi chiusi: «È una storia vecchia.» «Ma è vera?» — «È vera. Anche noi, una volta, eravamo forestiere.»).
- Doppiato (scena chiave): NINA §12.039 [VOX-12-13]; VERA §12.040, 12.047 [VOX-12-14, 15]; TINA §12.042, 12.044 [VOX-12-16, 17] (il racconto, 50 s); ROSALIA §12.043, 12.046, 12.049 [VOX-12-18…20].
- **Regia del racconto**: mentre Tina parla, la nebbia della sua gonna si allarga sul pavimento e forma **immagini di nebbia** (VFX ART_BIBLE §11.7): porte che si chiudono, una casa di paese con una porta aperta e una candela, un tavolo con il pane — come un teatro d'ombre bianco, 3 quadri.
- **Voce del quaderno**: IND-12-05 [NUOVO] «Donna Tina: all'inizio erano loro le forestiere. "Quelle di fuori." La gente chiudeva le porte. Poi una signora lasciò la porta aperta, il pane e i letti puliti. Donna Rosalia: "Anche noi, una volta, eravamo forestiere."»

### SCN-12-08 — «Gli parleremo. Sabato.» (dialogo, fine)
- **Beat**: B-12-07.
- **Testo del libro**: [LIBRO §12.050–12.064] (silenzio; dalla cucina un colpo di tosse o uno starnuto fermato a metà: Fomà ascolta — SFX-061; la richiesta di Vera: «Fomà ha detto che resta solo se glielo chiedete voi… E io… io resto divisa a metà. Per sempre.»; Rosalia guarda la cucina, Vera, il rosmarino, le scale pulite, i letti fatti; «Hai pulito tu?» «Sì.» «Anche le scale?» «Anche le scale. E ho cambiato le lenzuola. Anche quelle di Giulia.»; il sorriso piccolo, storto, quasi rassegnato; «Una Russo che pulisce le scale di notte per tre vecchie e un topo con la barba. Questo non si era mai visto in centocinquant'anni.»; lo schiocco del ventaglio; «Va bene. Gli parleremo. Sabato. La notte dei Morti… Ma a una condizione.» «Quale?» «Che la casa sia in ordine il martedì, il giovedì e il sabato. Sempre… Le lenzuola stese dritte, con le mollette uguali. E niente briciole di pane nero sotto i letti.»; lo sbuffo offesissimo dal frigo; Vera sorride fino a far male alle guance).
- Doppiato: VERA §12.051 [VOX-12-21]; ROSALIA §12.053, 12.055, 12.058, 12.060, 12.062 [VOX-12-22…26].
- **Variante** `val_pulizie_punteggio`: ≥ 10 → prima di «Hai pulito tu?» Rosalia passa il dito sul mobile e lo guarda a lungo (ANI-ROS-02) senza fare la smorfia del cap. 3; < 6 → Rosalia nota una piega in un lenzuolo [NUOVO] «Quella piega la perdono. Per stavolta.» (le battute del libro seguono uguali).
- **Fine**: VOX-12-27 [LIBRO §12.064] [VOCE narratrice] «Io sorrisi così tanto che mi fecero male le guance.» · scheda con frase [NUOVO]: «Una domanda sola. "Perché vi chiamate Donne di Fora?" E Donna Rosalia ha sorriso.»
- **Cosa cambia nel mondo**: regola delle pulizie attiva (minigiochi ripetibili martedì/giovedì/sabato, SIS-24); se la casa non è in ordine in una notte delle Donne del mondo libero, Rosalia lo fa notare (battuta) — nessuna penalità di trama; giornate libere 29 e 31 ottobre.

## Voci del quaderno del capitolo

| ID | Testo |
|---|---|
| IND-12-01 | Fomà è tornato e ha mangiato tutto (anche il formaggio). La luce non salta più. Ma crepa, acqua e limone sono ancora malati. Manca la seconda condizione: le signore. |
| IND-12-02 | Tre discorsi per le Donne: "Fomà è buono", "Se litigate la casa si ammala", "Vi prego". Cancellati tutti e tre. |
| IND-12-03 | Nonna Concetta: una di Catania è "di fuori". Un po' forestiera. "Non tanto. Ma un po'." FORA vuol dire FUORI. Donne di Fora = Donne di fuori. PERCHÉ? |
| IND-12-04 | Martedì: ho pulito tutta la casa. Lenzuola nuove a tutti (anche Giulia). Mollette uguali. Scale lucide. Rosmarino sul piattino, non bruciato. Pronta. |
| IND-12-05 | Donna Tina: all'inizio erano loro le forestiere. "Quelle di fuori." La gente chiudeva le porte. Poi una signora lasciò la porta aperta, il pane e i letti puliti. Donna Rosalia: "Anche noi, una volta, eravamo forestiere." |

## Fonti
- Manoscritto §12.001–12.064; appendice («Fora (siciliano) — fuori»; «La storia di come le Donne di Fora diventarono «di casa»… sono invenzioni del libro»).
- [Donne di fuori — Wikipedia](https://it.wikipedia.org/wiki/Donne_di_fuori)
