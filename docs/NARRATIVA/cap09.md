# Capitolo 9 — La scarpa vuota

| Voce | Valore |
|---|---|
| Data e giorno | venerdì 24 – sabato 25 ottobre 2025 |
| Arco orario | ven 7:20 ricerca → 10:30 dottore → giornata accanto al letto fino alle 18:00; sab pomeriggio ricerca fuori → 18:15–18:45 balcone (tramonto 18:12) |
| Luce | mattina grigia-bianca in cucina (torcia del telefono dietro il frigo); camera della babuška in penombra con le persiane socchiuse (lame di luce); sabato sera viola poi blu |
| Meteo | sereno, 22 °C |
| Luoghi | LUO-CR-CUC · LUO-CR-SCL · LUO-CR-SBA · LUO-CR-COR · LUO-SCA-01 · LUO-SCA-02 · LUO-CR-BAL |
| Durata obiettivo | 14 minuti (raccordi 3) |
| Checkpoint | CP-09-A ricerca · CP-09-B dottore · CP-09-C accanto al letto · CP-09-D sabato |
| Personaggi | Vera, babuška, Irina, il dottore, Mattia; (Salvo e Giulia fuori casa) |
| Libro | §09.001–09.042 (pp. 45–49) |

## Sinossi
La mattina dopo il consiglio il lapot' non c'è più. Dietro il frigo, con la torcia del telefono, solo polvere, una molletta, un tappo. Il pane e il latte sono intatti. La casa precipita: acqua marrone, intonaco caduto sul nono gradino, la luce che salta quattro volte, il limone a rami nudi. La babuška ha la febbre; il dottore dice «Stanca dentro». Vera resta a casa accanto al suo letto e le mente: «Sì, babuška. È al suo posto.» Sabato lo cerca anche fuori, come un gatto scappato. Al tramonto, sul balcone, Mattia in pigiama: «So da che parte è andato.»

## Scene

### SCN-09-01 — Il lapot' non c'è più (ricerca con la torcia) · CP-09-A
- **Beat**: B-09-01.
- **Obiettivo** OBJ-09-01 [NUOVO]: «Trovare Fomà. Ovunque.»
- **Testo del libro**: [LIBRO §09.001–09.006] (Vera se ne accorge appena entrata in cucina; si inginocchia e guarda dietro il frigo con la torcia del telefono: polvere, una molletta da bucato, il tappo di una bottiglia; «Fomà?» niente; pane, sale e latte intatti — «Era la prima volta da quando era arrivato»; la ricerca: sotto il lavandino, nel forno, nella dispensa, nel cesto della biancheria, nella scarpiera dell'ingresso, sotto i letti, dietro la lavatrice, nel cortile sotto il limone; «Fomà se n'era andato.»).
- **Sistema**: ricerca libera con torcia (SIS-07) in 9 punti (`LIVELLI.md` §3.6 «punti di ricerca cap. 9»); ognuno ha un'interazione e un pensiero breve [NUOVO]; dopo 6 punti (o 4 minuti) si sblocca il pensiero finale. flag_ricerca_completa = true se tutti e 9.
  | Punto | Pensiero [NUOVO] |
  |---|---|
  | Dietro il frigo (torcia, in ginocchio) | testo del libro §09.001 |
  | Sotto il lavandino | «Detersivi. Uno straccio. Niente barba.» |
  | Forno | «Vuoto. Per fortuna.» |
  | Dispensa | «Il pane nero nuovo della babuška. Intatto. Brutto segno.» |
  | Cesto della biancheria | «Calze. Tutte, destre e sinistre. Non c'è più nessuno a rubarle.» |
  | Scarpiera dell'ingresso | «Scarpe normali. Nessuna di corteccia.» |
  | Sotto i letti | «Polvere. Donna Rosalia avrebbe qualcosa da dire.» |
  | Dietro la lavatrice | «Un calzino di Mattia del 2023.» |
  | Cortile, sotto il limone | «Foglie gialle. Niente impronte. Niente.» |
- **Voce del quaderno**: IND-09-01 [NUOVO] «Ven 24: il lapot' non c'è più. Dietro il frigo: polvere, una molletta, un tappo. Pane, sale e latte intatti. Fomà non ha mangiato. Se n'è andato.»

### SCN-09-02 — La casa se ne accorge (evento)
- **Beat**: B-09-02. **Stato**: casa_acqua = 3, casa_crepa = 4 (fino al soffitto, intonaco caduto), casa_luce = 3, casa_limone = 4.
- **Testo del libro**: [LIBRO §09.007] (l'acqua marrone; la crepa al soffitto; un pezzetto di intonaco caduto proprio sul nono gradino; la luce salta quattro volte prima delle otto; il limone ha perso metà delle foglie in una notte, i rami nudi come dita).
- **Eventi**: Irina apre il rubinetto (acqua marrone, SFX-042); SFX-054 «[intonaco che cade]» dalle scale; quattro blackout in 3 minuti (SFX-040).
- Se `flag_ricerca_completa`: PEN-09-01 [NUOVO] «Avevo guardato dappertutto. La casa, invece, si era accorta subito.»
- **Fotografabile**: FOT-09-01 l'intonaco sul nono gradino.
- **Voce del quaderno**: IND-09-02 [NUOVO] «Senza Fomà la casa peggiora di colpo: acqua marrone, intonaco sul nono gradino, la luce salta quattro volte, il limone coi rami nudi come dita.»

### SCN-09-03 — La febbre e il dottore (dialogo osservato) · CP-09-B
- **Beat**: B-09-03.
- **Testo del libro**: [LIBRO §09.008–09.014] (la babuška non scende; a letto con la coperta al mento, occhi lucidi, guance rosse; «Babuška?» «Sto bene, Veročka. Ho solo un po' di freddo.» con la voce roca; la fronte che scotta; Vera chiama la mamma, la mamma il dottore; il dottore a metà mattina: influenza, attenzione all'età, letto, bere, tachipirina, richiamare se la febbre non scende in tre giorni; sulla porta: «Niente di grave. Ma è stanca, la signora. Stanca dentro. Succede, a quell'età, quando si cambia paese.»).
- **Lingua**: BABUŠKA a Vera [RU] «Я в порядке, Верочка. Мне просто немного холодно.» · *Ja v porjadke, Veročka. Mne prosto nemnogo cholodno.* · sottotitolo [LIBRO §09.011] «Sto bene, Veročka. Ho solo un po' di freddo.» [VOX-09-01]
- Doppiato: DOTTORE §09.014 [VOX-09-02].
- **Interazione**: toccare la fronte della babuška (mano di Vera in campo) → effetto calore (leggera distorsione e suono di respiro, SFX-055 «[respiro affannato]»).

### SCN-09-04 — La mamma sul gradino (dialogo)
- **Beat**: B-09-04.
- **Testo del libro**: [LIBRO §09.015–09.021] (Irina seduta sul gradino sotto la crepa, il viso nelle mani; Vera si siede accanto e le appoggia la testa sulla spalla; «È colpa mia. L'ho portata qui. L'ho tolta da casa sua. A settantaquattro anni.» «Non è colpa tua, mamma.» «E allora di chi è?»; «Era la stessa domanda di Giulia… O forse sì.»).
- Doppiato: IRINA §09.017, §09.019 [VOX-09-03…04].
- **Interazione**: sedersi accanto (punto «Siediti») e appoggiare la testa (Azione tenuta 2 s) → rap_irina +1.
- **Voce del quaderno**: IND-09-03 [NUOVO] «Mamma pensa che sia colpa sua. "E allora di chi è?" La stessa domanda di Giulia. Forse io lo so.»

### SCN-09-05 — Accanto al letto (guidata, tempo che passa) · CP-09-C
- **Beat**: B-09-05.
- **Testo del libro**: [LIBRO §09.022–09.030] (Vera resta a casa; la mamma porta turisti russi al Teatro Antico e a Castelmola; papà al bar, Giulia a scuola, Mattia «all'asilo»; il panno bagnato ogni mezz'ora; la babuška dorme, parla in russo nel sonno: il nome del dedushka, la sua via a San Pietroburgo, una parola che sembra «stufa»; poi, lucida: «Veročka. Il lapot'. È al suo posto?»; la bugia; «la peggiore bugiarda del mondo»; il domovoj protegge la famiglia — letto su internet di nascosto; «Quando il domovoj se ne va, la casa resta sola.»).
- **Sistema**: «tempo accanto al letto»: ogni ciclo (6 cicli = 3 ore di gioco, 40 s reali l'uno) Vera immerge il panno nella bacinella, lo strizza, lo posa sulla fronte (ANI-VER); tra i cicli può usare il telefono (leggere il «sito sul domovoj»: pagina con testo [NUOVO] in stile enciclopedia per ragazzi, che riassume l'appendice del libro) o guardare dalla finestra.
- **Delirio** (in russo, sottotitoli parziali): BABUŠKA [RU] «Коля… Коля…» · *Kolja… Kolja…*; «…Малая Посадская…» (via di San Pietroburgo [NUOVO]); «…печка…» · *pečka* · sottotitolo «…stufa…» [VOX-09-05].
- **La domanda** (cinematica breve, primo piano):
  - BABUŠKA [LIBRO §09.025] [VOCE VOX-09-06] [RU] «Верочка. Лапоть. Он на месте?» · *Veročka. Lapot'. On na meste?* · sottotitolo «Veročka. Il lapot'. È al suo posto?»
  - PEN-09-02 [LIBRO §09.026]: «Io esitai.»
  - **Scelta** (entrambe portano alla bugia del libro; la scelta è quanto si esita):
    - `*` (1) rispondere subito → VERA [LIBRO §09.027] «Sì, babuška. È al suo posto.» (in russo [RU] «Да, бабушка. На месте.» · *Da, babuška. Na meste.* · sottotitolo del libro)
    - `*` (2) esitare (3 s di silenzio, la babuška chiude quasi gli occhi) → stessa battuta → rap_babuska invariato; PEN-09-03 [NUOVO] «La bugia mi uscì lo stesso. Più lenta, ma uscì.»
  - PEN-09-04 [LIBRO §09.028]: «Lei chiuse gli occhi, rassicurata. E io mi sentii la peggiore bugiarda del mondo.»
- PEN-09-05 [LIBRO §09.030]: «Quando il domovoj se ne va, la casa resta sola.»
- **Voci del quaderno**: RUS-31 «Lapot' na meste?» · IND-09-04 [NUOVO] «La babuška nel sonno dice "Kolja" e "pečka". Da sveglia mi ha chiesto se il lapot' è al suo posto. Ho detto di sì. Ho mentito. Senza domovoj la casa resta sola.»

### SCN-09-06 — Sabato: cercarlo fuori (raccordo) · CP-09-D
- **Tipo**: raccordo (massimo 4 min).
- **Beat**: B-09-06. **Stato**: casa_crepa = 5 (ramo verso la camera dei genitori).
- **Testo del libro**: [LIBRO §09.031–09.032] (la febbre ancora alta; la crepa ha fatto un ramo verso la camera dei genitori; Vera cerca Fomà anche fuori: nella scalinata, nei vasi dei gerani, sotto il portone di nonna Concetta, dietro il bidone della spazzatura in fondo alla discesa; chiama il suo nome sottovoce in tutti gli angoli, come un gatto scappato; niente).
- **Svolgimento**: 6 punti di ricerca fuori (`LIVELLI.md` §4.2); interazione «Chiama» (Vera sussurra «Fomà…», SFX non sottotitolato; il gatto rosso risponde con un miagolio offeso SFX-029: PEN-09-06 [NUOVO] «Non sei tu che cerco. Scusa.»).
- **Voce del quaderno**: IND-09-05 [NUOVO] «Sab 25: l'ho cercato fuori. Scalinata, gerani, portone di nonna Concetta, il bidone in fondo alla discesa. L'ho chiamato come un gatto scappato. Niente. La crepa ha fatto un ramo nuovo.»

### SCN-09-07 — Il balcone: «So da che parte è andato» (dialogo)
- **Beat**: B-09-07.
- **Testo del libro**: [LIBRO §09.033–09.042] (al tramonto viola poi blu Vera sul gradino del balcone, dove la babuška sedeva il giorno del Pokrov; il pezzo di mare tra i tetti, l'Etna nera; il ricordo della frase di Rosalia; «Dove va un domovoj che se ne va?…»; la porta del balcone; Mattia in pigiama col coniglio di pezza: «Vera. Lo cerchi, il signore piccolo?»; «Tu lo sai dov'è?»; Mattia si siede accanto, serio, col coniglio in grembo: «No. Però so da che parte è andato.»).
- Doppiato: MATTIA §09.038 [VOX-09-07], §09.042 [VOX-09-08].
- PEN-09-07 [LIBRO §09.034] (voce della memoria, eco): «Qui sei forestiero. E i forestieri, prima o poi, se ne vanno.» (riprodotta con la voce di Rosalia VOX-08-08 filtrata, solo l'ultima frase)
- **Effetti**: rap_mattia +1.
- **Fine**: la battuta di Mattia VOX-09-08 chiude il capitolo; scheda con frase [NUOVO]: «Il lapot' non c'è, la babuška brucia di febbre, la casa cade a pezzi. Ma mio fratello sa da che parte è andato.»
- **Cosa cambia nel mondo**: → SCN-10-01 la domenica dopo pranzo.

## Voci del quaderno del capitolo

| ID | Testo |
|---|---|
| IND-09-01 | Ven 24: il lapot' non c'è più. Dietro il frigo: polvere, una molletta, un tappo. Pane, sale e latte intatti. Fomà non ha mangiato. Se n'è andato. |
| IND-09-02 | Senza Fomà la casa peggiora di colpo: acqua marrone, intonaco sul nono gradino, la luce salta quattro volte, il limone coi rami nudi come dita. |
| IND-09-03 | Mamma pensa che sia colpa sua. "E allora di chi è?" La stessa domanda di Giulia. Forse io lo so. |
| IND-09-04 | La babuška nel sonno dice "Kolja" e "pečka". Da sveglia mi ha chiesto se il lapot' è al suo posto. Ho detto di sì. Ho mentito. Senza domovoj la casa resta sola. |
| IND-09-05 | Sab 25: l'ho cercato fuori. Scalinata, gerani, portone di nonna Concetta, il bidone in fondo alla discesa. L'ho chiamato come un gatto scappato. Niente. La crepa ha fatto un ramo nuovo. |
| RUS-31 | «Lapot' na meste?» — Il lapot' è al suo posto? |
| FOT-09-01 | L'intonaco caduto sul nono gradino. |

## Fonti
- Manoscritto §09.001–09.042; `FASI_DI_SVILUPPO.md` Fase 7.
