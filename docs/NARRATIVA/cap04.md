# Capitolo 4 — La guerra delle tazzine

| Voce | Valore |
|---|---|
| Data e giorno | notte di giovedì 18 settembre → venerdì 26 settembre 2025 (D-54) |
| Arco orario | notte delle tre domande (01:35–02:10); ven 19 mattina e sera; lun 22 → ven 26 (una scena al mattino, una ricerca, una notte); cena di venerdì 26 |
| Luce | cucina di notte (lampione + nebbia delle Donne); mattine limpide 7:30; tramonto 19:00 circa |
| Meteo | fine settembre caldo (27 °C), aria ferma: «Non c'era vento» (04.030) |
| Luoghi | LUO-CR-CUC · LUO-CR-COR (cortile, limone, filo da bucato) · LUO-CR-BAG (finestra del bagno) · LUO-CR-SOG (vetrinetta, D-50) · LUO-CR-DIS (dispensa) · camere |
| Durata obiettivo | 25 minuti (raccordi 8) |
| Checkpoint | CP-04-A domande · CP-04-B ven 19 · CP-04-C lun 22 · CP-04-D mar 23 · CP-04-E mer 24 · CP-04-F gio 25 · CP-04-G ven 26 · CP-04-J cena |
| Personaggi | Vera, Donne di Fora, Fomà, nonna Concetta, babuška, Irina, Salvo, Giulia, Mattia |
| Libro | §04.001–04.054 (pp. 19–23) |
| Sistema principale | SIS-21 Indagine giorno per giorno |

## Sinossi
Quella notte Donna Rosalia fa a Vera tre domande e scopre che il «topo» è un domovoj arrivato in una scarpa. Da lì in poi è guerra: la moka di nonna Concetta sparisce, il kefir della babuška caglia, le lenzuola si intrecciano dal limone alla finestra del bagno, le calze sinistre spariscono, le tazzine si girano a testa in giù nella vetrinetta chiusa a chiave, il pane nero ammuffisce in una notte, la moka ricompare piena di sale. Vera sa sempre chi è stato, e lo annota nel quaderno; le nonne si guardano e non dicono niente. A cena Mattia dice: «Il signore dice che sono state le signore».

## Scene

### SCN-04-01 — Le tre domande (dialogo) · CP-04-A
- **Trigger**: continua da SCN-03-11 (in v2.0) o dal caricamento del salvataggio v1.0 migrato (SCN-04-01 come prima scena).
- **Beat**: B-04-01, B-04-02.
- **Regia**: Vera seduta su una sedia in cucina; Rosalia in piedi davanti; Nina e Tina ai lati; Fomà sul lapot' vicino al frigo.
- **Testo del libro**: [LIBRO §04.001–04.009] (le tre domande sono riferite da Vera narratrice; nel gioco diventano dialogo diretto con le stesse parole: «Da quando ci vedi?» / «Da cinque minuti» / «Bugiarda»; «Lo sai chi siamo?»; la spiegazione di Rosalia è il testo di 04.003 messo in bocca a lei in prima persona plurale — vedi nota).
  - *Nota di adattamento*: 04.003 è narrazione indiretta («mi spiegò che le Donne di Fora erano…»). La battuta di Rosalia è [NUOVO] e riporta lo stesso contenuto in discorso diretto: ROSALIA [NUOVO] [VOCE VOX-04-01]: «Noi siamo le signore che entrano nelle case di notte, dal buco della serratura. Se troviamo la casa in ordine, i letti fatti e le lenzuola pulite, portiamo fortuna. Se no, no. Un tempo eravamo tante, in tutta la Sicilia. Adesso siamo poche: la gente non ci crede più e chiude le porte con le chiavi moderne, quelle senza buco. Noi tre veniamo in casa Russo da più di cent'anni.»
- **Scelte di Vera** (alla prima domanda; l'esito del libro resta: Rosalia dice «Bugiarda» in ogni caso):
  - `*` (1) «Da cinque minuti.» [LIBRO §04.002] → flag_rosalia_sincera = true; rap_rosalia +1; PEN-04-01 [LIBRO §04.002]: «Lei disse: «Bugiarda», ma era vero.»
  - `*` (2) «Da sempre?» [NUOVO] → ROSALIA: «Bugiarda.» → PEN-04-02 [NUOVO]: «Questa volta aveva ragione lei. Ma solo questa volta.»
- **Terza domanda**: ROSALIA indica Fomà col ventaglio «come si indica una macchia sul pavimento» (ANI-ROS-03): «E lui?» [LIBRO §04.004]
  - VERA [LIBRO §04.005]: «Lui è il domovoj. È venuto con la babuška. Nella scarpa.»
  - NINA [LIBRO §04.006] [VOCE VOX-04-02]: «Nella scarpa.» (si copre la bocca per non ridere: ANI-NIN-02)
  - FOMÀ [LIBRO §04.007] [VOCE VOX-04-03]: «È la tradizione! Il domovoj si porta nel lapot'! Lo sanno tutti! Che ignoranza!»
  - ROSALIA [LIBRO §04.008] [VOCE VOX-04-04]: «Qui nessuno porta niente nelle scarpe. Qui nelle scarpe si mettono i piedi.»
  - PEN-04-03 [LIBRO §04.009]: «E da lì in poi le cose andarono male.»
- **Voci del quaderno**: IND-04-08 [NUOVO] «Le Donne di Fora: un tempo erano tante in tutta la Sicilia. Adesso poche, per colpa delle chiavi moderne senza buco. Da noi vengono da più di cent'anni.»

### SCN-04-02 — Venerdì 19: la moka sparita (dialogo osservato) · CP-04-B
- **Trigger**: dissolvenza alla mattina (7:30).
- **Beat**: B-04-03.
- **Obiettivo** OBJ-04-02 [NUOVO]: «Trovare la moka di nonna Concetta. (Io so già dov'è.)»
- **Testo del libro**: [LIBRO §04.010–04.021] — Concetta arriva alle sette e mezza; «Dov'è la mia moka?»; ricerca in famiglia (pensili, forno, lavastoviglie, balcone: Vera può aprire questi punti); papà beve il caffè al bar; la babuška scende alle otto; «Buongiorno» / «Ha visto per caso la mia moka?» / «Io non tocco le cose degli altri» / «Non ho detto che l'ha toccata. Ho detto se l'ha vista.» / «Non l'ho vista.» / «Ah.»
- Doppiato: CONCETTA «Dov'è la mia moka?» [VOX-04-05], BABUŠKA «Io non tocco le cose degli altri» (italiano con accento, D-48) [VOX-04-06], CONCETTA «Ah.» [VOX-04-07].
- PEN-04-04 [LIBRO §04.021]: «Quell'ah rimase nell'aria della cucina tutta la mattina, come l'odore del pesce fritto.»
- **Scelta di Vera** (durante la ricerca): `*` (1) aiutare a cercare nei pensili → rap_concetta +1 · `*` (2) guardare verso il frigo → porta a SCN-04-03 subito.

### SCN-04-03 — Il luccichio dietro il frigo (ricerca di prova)
- **Beat**: B-04-04.
- **Svolgimento SIS-21 (giorno 1)**: inginocchiarsi davanti al frigo (punto «Inginocchiati») e guardare nello spazio stretto: **luccichio di alluminio** (la moka). Se Vera si avvicina, SFX-034 «[vocina soddisfatta: «Gallinelle»]».
  - PEN-04-05 [LIBRO §04.022]: «Io sapevo benissimo dov'era la moka. Ero passata davanti al frigorifero e avevo visto, nello spazio stretto dietro, un luccichio di alluminio. E avevo sentito una vocina soddisfatta che diceva: Gallinelle. Adesso vediamo.»
  - FOMÀ [LIBRO §04.022] [VOCE VOX-04-08] (sottovoce, dietro il frigo): «Gallinelle. Adesso vediamo.»
- **Annotazione**: trascinare la prova («luccichio di alluminio») sulla pagina del giorno → scegliere colpevole: «Fomà» (giusto) / «le Donne» / «le nonne» (Vera scrive e cancella: PEN-04-NONNE [NUOVO] «No. Le nonne no. …Forse.»).
- flag_prova_moka = true; val_prove_cap4 +1.
- **Voce del quaderno**: IND-04-01 [NUOVO] «Ven 19: la moka di nonna Concetta è sparita. È dietro il frigo. Fomà: "Gallinelle. Adesso vediamo." È una vendetta.»
- **Perché Vera non la restituisce**: PEN-04-06 [NUOVO] «Potevo prenderla. Ma come spiegavo che sapevo dov'era? "Me l'ha detto il domovoj"?» (il punto «Prendi» è disattivato con questo pensiero).

### SCN-04-04 — Il kefir cagliato (dialogo osservato, sera di venerdì 19)
- **Beat**: B-04-05.
- **Testo del libro**: [LIBRO §04.023–04.027] (il kefir, il negozio di prodotti dell'Est vicino alla stazione — D-52, il bicchiere ogni sera, il kefir a pezzi «puzzolente come un calzino», Irina «È andato a male. Strano. L'ho comprato ieri.», la babuška «Non è andato a male. Qualcuno l'ha fatto andare a male.» e lo sguardo verso la casa di Concetta).
- Doppiato: BABUŠKA [RU] «Не испортился. Кто-то его испортил.» · *Ne isportilsja. Kto-to ego isportil.* · sottotitolo «Non è andato a male. Qualcuno l'ha fatto andare a male.» [VOX-04-09] (detta a bassa voce a Irina: famiglia, D-48).
- **Voci del quaderno**: RUS-18 kefir.

### SCN-04-05 — La notte di venerdì: Donna Nina (ricerca di prova, origliare)
- **Trigger**: la stessa notte (non è notte delle Donne: è un ricordo della notte prima). *Adattamento*: il libro dice «la notte prima, mentre tornavo a letto, avevo sentito Donna Nina» (04.028), cioè la notte delle tre domande. Nel gioco la frase si sente **in coda a SCN-04-01**, quando Vera torna a letto (Nina e Rosalia parlano nell'ingresso mentre si sciolgono in nebbia); in SCN-04-04 Vera la **ricorda** e la annota.
- **Beat**: B-04-06.
- NINA [LIBRO §04.028] [VOCE VOX-04-10] (fuori campo, in coda a SCN-04-01): «Lasciate fare a me. Gli faccio cagliare il latte, a quel topo, e alla sua padrona.»
- PEN-04-07 [LIBRO §04.028]: «Io sapevo anche questo.»
- **Annotazione**: prova «frase di Donna Nina» → colpevole «le Donne». flag_prova_kefir = true; val_prove_cap4 +1.
- **Voce del quaderno**: IND-04-02 [NUOVO] «Ven 19 sera: il kefir è cagliato. Donna Nina l'aveva detto: "Gli faccio cagliare il latte". Ora la babuška pensa che sia stata nonna Concetta.»

### Sabato 20 – domenica 21 (raccordo)
- **Tipo**: raccordo (massimo 4 min): sabato pomeriggio libero breve in casa e scalinata (le nonne si evitano: Concetta non viene la domenica, eccezione [NUOVO] → PEN-04-08 «La domenica nonna Concetta non venne a pranzo. "Mal di testa." In quarant'anni non aveva mai avuto mal di testa.»). Notte di sabato: le Donne passano (notte delle Donne): Vera le vede nell'ingresso parlottare (nessun dialogo con lei, solo NINA [NUOVO] «La forestiera ha guardato storto Donna Concetta. Bene.»).

### SCN-04-06 — Lunedì 22: le lenzuola (scoperta + prova) · CP-04-C
- **Beat**: B-04-07.
- **Testo del libro**: [LIBRO §04.029–04.030]: «Da quel giorno fu la guerra…»; le lenzuola stese in cortile intrecciate «in una specie di treccia lunghissima che andava dal limone alla finestra del bagno»; Irina ci mette un'ora a scioglierla; «disse che era stato il vento. Non c'era vento.»
- IRINA [NUOVO, dal libro]: «Il vento. È stato il vento.» → PEN-04-09 [LIBRO §04.030]: «Non c'era vento.»
- **Prova**: annusare le lenzuola (interazione «Annusa», nuova in questo capitolo): **profumo di rosmarino** sui nodi → colpevole «le Donne». flag_prova_lenzuola = true; val_prove_cap4 +1.
- Interazione facoltativa: aiutare Irina a sciogliere la treccia (minigioco di 30 s, anteprima delle pulizie del cap. 12) → rap_irina +1.
- **Fotografabile**: FOT-04-01 la treccia di lenzuola dal limone alla finestra del bagno.
- **Voce del quaderno**: IND-04-03 [NUOVO] «Lun 22: lenzuola intrecciate dal limone alla finestra del bagno. Odore di rosmarino sui nodi. Le Donne. (Mamma: "il vento". Non c'era vento.)»

### SCN-04-07 — Martedì 23: le calze sinistre · CP-04-D
- **Beat**: B-04-08.
- **Testo del libro**: [LIBRO §04.031] «Il martedì, sparirono tutte le calze sinistre della famiglia. Le destre no. Solo le sinistre.»
- **Prova**: nello spazio dietro il frigo, un **nido di calze sinistre** con dentro briciole di pane nero → colpevole «Fomà». flag_prova_calze = true; val_prove_cap4 +1.
- MATTIA [NUOVO] (con una calza destra in mano): «Io ho due piedi destri, adesso.»
- **Notte di martedì (notte delle Donne)**: le Donne passano dritte, rigide; ROSALIA a Vera [NUOVO] (se Vera è nell'ingresso): «Torna a letto, Vera Russo. Questa non è guerra tua.» → PEN-04-10 [NUOVO] «Era casa mia. Quindi era anche guerra mia.»
- **Voce del quaderno**: IND-04-04 [NUOVO] «Mar 23: tutte le calze sinistre sparite. Le ho trovate dietro il frigo, a nido, con le briciole di pane nero. Fomà.»

### SCN-04-08 — Mercoledì 24: le tazzine a testa in giù · CP-04-E
- **Beat**: B-04-09.
- **Testo del libro**: [LIBRO §04.032] (le tazzine col bordo d'oro del servizio buono di Concetta, nella vetrinetta del soggiorno di Casa Russo — D-50 —, tutte a testa in giù, nella notte, con la vetrinetta chiusa a chiave).
- **Regia**: Concetta davanti alla vetrinetta: non urla, chiude la vetrinetta piano e si fa il segno della croce (dal libro, 05.005 — anticipato qui come azione visibile, il commento di Vera resta al cap. 5).
- **Prova**: sul vetro interno della vetrinetta (eccezione all'interazione dietro vetro, SIS-02) un **velo di condensa a forma di ventaglio** → colpevole «le Donne». flag_prova_tazzine = true; val_prove_cap4 +1.
- **Fotografabile**: FOT-04-02 le tazzine a testa in giù.
- **Voce del quaderno**: IND-04-05 [NUOVO] «Mer 24: le tazzine buone di nonna Concetta tutte a testa in giù, con la vetrinetta chiusa a chiave. Sul vetro, di dentro, l'impronta di un ventaglio. Le Donne.»

### SCN-04-09 — Giovedì 25: il pane nero ammuffito · CP-04-F
- **Beat**: B-04-10.
- **Testo del libro**: [LIBRO §04.033] (il pane nero portato dalla Russia, tenuto in dispensa come un tesoro, verde di muffa in una notte; «A Taormina, a fine settembre, va bene, fa caldo. Ma in una notte.»).
- BABUŠKA [NUOVO, dal libro 05.005: «aveva sussurrato qualcosa in russo, qualcosa che sembrava pazienza»] [RU] «Терпение…» · *Terpenie…* · sottotitolo «Pazienza…» (il pensiero di Vera su questo arriva al cap. 5; qui solo la battuta) — sblocca RUS-24 al cap. 5, non qui.
- **Prova**: sulla mensola della dispensa, **tre petali di rosmarino** e un lungo capello sciolto, luminoso (Tina) → colpevole «le Donne». flag_prova_pane = true; val_prove_cap4 +1.
- **Notte di giovedì (notte delle Donne)**: TINA, rimasta indietro, a Vera [NUOVO]: «Il pane nero… non volevo che diventasse verde. Volevo solo sentirne l'odore da vicino.» → rap_tina +1; PEN-04-11 [NUOVO] «Anche le Donne di Fora hanno una che non è d'accordo.»
- **Voci del quaderno**: RUS-19 čërnyj chleb · IND-04-06 [NUOVO] «Gio 25: il pane nero della babuška verde di muffa in una notte. Rosmarino in dispensa e un capello lungo, luminoso. Donna Tina? Dice che voleva solo annusarlo.»

### SCN-04-10 — Venerdì 26: la moka col sale · CP-04-G
- **Beat**: B-04-11.
- **Testo del libro**: [LIBRO §04.034–04.035] «Il venerdì, la moka di nonna Concetta ricomparve sul fornello. Piena di sale. E ogni volta, le due nonne si guardavano. E non dicevano niente. Ma non era un niente buono. Era un niente pieno di cose.»
- **Regia**: Concetta apre la moka e il sale cade sul fornello (SFX-082 «[sale che cade]»); le due nonne si guardano (camera alternata 2 s + 2 s).
- **Prova**: sale sul pavimento in **impronte piccolissime** verso il frigo → colpevole «Fomà». flag_prova_sale = true; val_prove_cap4 +1.
- **Fotografabile**: FOT-04-03 la moka piena di sale.
- **Voce del quaderno**: IND-04-07 [NUOVO] «Ven 26: la moka è tornata. Piena di sale. Impronte piccolissime nel sale, verso il frigo. Fomà. Le nonne si guardano e non dicono niente: un niente pieno di cose.»

### SCN-04-11 — La cena: «Il signore dice che sono state le signore» (dialogo) · CP-04-J
- **Trigger**: sera di venerdì 26, cena (la babuška è già salita a dormire).
- **Beat**: B-04-12.
- **Testo del libro**: [LIBRO §04.036–04.054] — Giulia «Tu dici che è stata nonna Concetta?»; Irina «Ma figurati. È una donna di settantun anni. Cosa fa, entra di notte a girare le tazzine?»; «Allora è stata la babuška.» «Giulia.» «Cosa? Qualcuno sarà stato. Le calze non spariscono da sole.»; Salvo «Le calze spariscono da sole da quando esistono le lavatrici»; Mattia guarda il frigo: «Il signore dice che sono state le signore»; «Quale signore?» «Quello piccolo. Quello che brontola. Lo sento la notte. Dice che le signore sono cattive e che gli hanno detto topo.»; Salvo «Mattia, con chi parli tu, la notte?» «Con nessuno.»; pensieri finali di Vera 04.052–04.054.
- Doppiato: MATTIA §04.044 [VOX-04-11], §04.048 [VOX-04-12]; SALVO §04.050 [VOX-04-13]; MATTIA §04.051 [VOX-04-14].
- **Scelta di Vera** (sotto il tavolo; il libro: «io, sotto il tavolo, strinsi le mani così forte che mi fecero male» — Vera non parla):
  - `*` (1) stringere le mani (animazione delle mani in prima persona) → PEN-04-12 [LIBRO §04.053]: «Mio fratello di sei anni non vedeva niente. Ma sentiva.»
  - `*` (2) guardare Mattia → Mattia la guarda e sorride (rap_mattia +1), poi stesso pensiero.
- PEN-04-13 [LIBRO §04.053–04.054]: «E se sentiva lui, forse, prima o poi, avrebbero sentito anche gli altri. E allora cosa sarebbe successo?»
- **Fine del capitolo**: VOX-04-15 [LIBRO §04.054] [VOCE narratrice] «E allora cosa sarebbe successo?» — scheda: frase [NUOVO] secondo `val_prove_cap4`: 7 → «Sette dispetti, sette prove. Fomà tre, le Donne quattro. Nessuna nonna. Ma le nonne lo sanno?» · 4–6 → «Quasi tutte le prove. Le altre le ho capite dopo.» · < 4 → stesso testo «Le altre le ho capite dopo» (le voci mancanti si scrivono da sole).
- **Voce del quaderno**: IND-04-09 [NUOVO] «Mattia sente Fomà. "Il signore piccolo, quello che brontola." Non lo vede. Lo sente. E l'ha detto a tavola.»
- **Cosa cambia nel mondo**: moka di nuovo sul fornello; dispetti residui casuali in libero (GDD §2.4); si aprono le giornate libere 27/9, 1/10, 3/10.

## Voci del quaderno del capitolo

| ID | Testo |
|---|---|
| IND-04-01 | Ven 19: la moka di nonna Concetta è sparita. È dietro il frigo. Fomà: "Gallinelle. Adesso vediamo." È una vendetta. |
| IND-04-02 | Ven 19 sera: il kefir è cagliato. Donna Nina l'aveva detto: "Gli faccio cagliare il latte". Ora la babuška pensa che sia stata nonna Concetta. |
| IND-04-03 | Lun 22: lenzuola intrecciate dal limone alla finestra del bagno. Odore di rosmarino sui nodi. Le Donne. (Mamma: "il vento". Non c'era vento.) |
| IND-04-04 | Mar 23: tutte le calze sinistre sparite. Le ho trovate dietro il frigo, a nido, con le briciole di pane nero. Fomà. |
| IND-04-05 | Mer 24: le tazzine buone di nonna Concetta tutte a testa in giù, con la vetrinetta chiusa a chiave. Sul vetro, di dentro, l'impronta di un ventaglio. Le Donne. |
| IND-04-06 | Gio 25: il pane nero della babuška verde di muffa in una notte. Rosmarino in dispensa e un capello lungo, luminoso. Donna Tina? Dice che voleva solo annusarlo. |
| IND-04-07 | Ven 26: la moka è tornata. Piena di sale. Impronte piccolissime nel sale, verso il frigo. Fomà. Le nonne si guardano e non dicono niente: un niente pieno di cose. |
| IND-04-08 | Le Donne di Fora: un tempo erano tante in tutta la Sicilia. Adesso poche, per colpa delle chiavi moderne senza buco. Da noi vengono da più di cent'anni. |
| IND-04-09 | Mattia sente Fomà. "Il signore piccolo, quello che brontola." Non lo vede. Lo sente. E l'ha detto a tavola. |
| RUS-18, RUS-19 | kefir · čërnyj chleb |
| FOT-04-01…03 | La treccia di lenzuola · Le tazzine a testa in giù · La moka piena di sale |

## Fonti
- Manoscritto §04.001–04.054; `FASI_DI_SVILUPPO.md` §2 #10, Fase 6.
