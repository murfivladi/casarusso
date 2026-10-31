# Audio Design Document

## 1. Principi
- **Niente musica** (D-76): il gioco suona solo con il mondo (ambienti generati dal codice), le voci e i versi. Nessun tema musicale neppure nei menu: il titolo ha il suono del balcone (rondini, mare lontano, campane del Duomo a orari reali).
- **Tutto generato dal codice** per gli ambienti e gli effetti (FASI §16): Web Audio API (AudioWorklet per sintesi granulare e rumore, ConvolverNode con risposte all'impulso generate proceduralmente, nodi Panner HRTF). Le **sole registrazioni** sono le voci (ElevenLabs / Fish Audio, D-43) e i versi brevi dei personaggi.
- Ogni suono importante ha un **sottotitolo** `SFX-` (D-28, SIS-05).

## 2. Suoni generati dal codice

### 2.1 Catalogo di sintesi
| ID sintesi | Suono | Tecnica | Parametri e variazioni |
|---|---|---|---|
| SYN-01 | Brusio dell'atrio | 24 «voci» granulari da formanti (vocali sintetiche filtrate a 300–3000 Hz) con inviluppi casuali + riverbero di sala (IR proceduale 2,8 s) | densità segue il numero di NPC; picchi alle aperture della porta |
| SYN-02 | Annuncio (dindon + voce) | campanello a 2 note (sinusoidi 659/523 Hz, decadimento 1,2 s) + voce TTS registrata una volta (testi §2.3) filtrata «altoparlante» (passa-banda 400–3500 Hz, saturazione) | ogni 50–70 s |
| SYN-03 | Porta scorrevole | rumore rosa filtrato con sweep 200→900 Hz + motore (dente di sega 55 Hz con tremolo) + «tonk» di fine corsa | 2 velocità (apertura/chiusura) |
| SYN-04 | Ruote del carrello | treno di impulsi su rumore marrone, filtro risonante 120 Hz, irregolarità da giunti del pavimento (ogni 0,6 m) | velocità dal movimento |
| SYN-05 | Aria condizionata | rumore marrone + ronzio 100 Hz debole | sempre nell'aeroporto |
| SYN-06 | Motore dell'auto, abitacolo | 3 armoniche dipendenti dai giri (sinusoidi e dente di sega) + rumore di rotolamento (rumore rosa filtrato da velocità) + vento | marce simulate, frenate nel traffico |
| SYN-07 | Cicale | modulazione d'ampiezza veloce (180–250 Hz) su rumore passa-banda 4–7 kHz, 6–20 sorgenti con fase casuale | solo set–ott di giorno sopra 24 °C |
| SYN-08 | Frigorifero che ronza | ronzio 50 Hz + armoniche 100/150 Hz, compressore che parte (rampa 2 s) e si ferma ogni 6–9 min; «clic» del termostato | stato «arrabbiato» (cap. 8): +6 dB, armoniche dispari; silenzio (cap. 8 fine) |
| SYN-09 | Scricchiolii di casa | impulsi filtrati a pettine (risonanze del legno 180–900 Hz) con inviluppo stick-slip | più frequenti con `casa_crepa` alto |
| SYN-10 | 9° gradino | scricchiolio stick-slip dedicato (2 varianti, durata 0,4–0,7 s) | posizione 3D del gradino |
| SYN-11 | Crepa | crepitio granulare ad alta frequenza; «crac» = transiente + coda bassa risonante | SFX-045, SFX-046 |
| SYN-12 | Tosse della casa | colpo sordo (sinusoide 45 Hz con pitch-drop) + rumore filtrato dentro i muri (convoluzione con IR «parete») | SFX-044 |
| SYN-13 | Luce che salta | «tac» (impulso metallico) + caduta del ronzio di rete a zero | SFX-040 |
| SYN-14 | Acqua dal rubinetto | rumore bianco filtrato con modulazione caotica; variante «ruggine» con gorgoglio | — |
| SYN-15 | Passi | sintesi per superficie (pietra, marmo, legno, graniglia, asfalto, bagnato): transiente + risonanza + strisciato; piedi nudi senza tacco | velocità e postura |
| SYN-16 | Nebbia delle Donne | rumore rosa con filtro passa-banda in movimento lento + armonici di vetro (sinusoidi 1–3 kHz molto deboli) | formazione e uscita |
| SYN-17 | Braccialetti | campioni sintetici FM (metallo) 4–6 tintinnii in grappoli | per Donna (timbro diverso) |
| SYN-18 | Ventaglio | fruscio di stoffa (rumore filtrato) + schiocco (transiente di legno) | apertura lenta / chiusura secca |
| SYN-19 | Mare | onde: rumore rosa con inviluppo lento 6–10 s, risacca sui ciottoli (granulare) | intensità con il vento |
| SYN-20 | Pioggia | gocce granulari su materiali (tegole, pietra, ombrello) + rumore di fondo | intensità dal meteo |
| SYN-21 | Tuono | rumore marrone con inviluppo lungo e filtro passa-basso variabile | solo il 4/11 (lontano) |
| SYN-22 | Vento | rumore filtrato con raffiche (LFO casuali) e fischi sui bordi | — |
| SYN-23 | Funivia | ronzio del motore + cigolio del carrello sui cavi + colpi ai piloni | SFX-056 |
| SYN-24 | Treno merci | rotolamento ritmico (giunti ogni 25 m), stridii, ferro «lunghissimo» (11.023) | SFX-058 |
| SYN-25 | Macchina del caffè | pompa vibrante (100 Hz) + vapore (rumore bianco filtrato) + tazzine (FM) | bar |
| SYN-26 | Campane del Duomo | sintesi modale (5 modi inarmonici) | orari reali (12:00, 18:00 e domenica mattina) |
| SYN-27 | Rondini e passeri | sintesi FM di cinguettii | set–ott, mattina e sera |
| SYN-28 | Gatti | miagolii da formanti modulati | per gatto |
| SYN-29 | Motorini e traffico | motori a due tempi (dente di sega con jitter) su strada | Via Circonvallazione, Corso (raramente: è pedonale) |
| SYN-30 | Candela | crepitio leggero (granulare) | — |
| SYN-31 | Fuoco della biro e matita | strisciato granulare su carta (biro più liscia, matita più ruvida) | SFX-090 |
| SYN-32 | Pagina | fruscio di carta + colpo morbido | SFX-091 |
| SYN-33 | Scatto della foto | otturatore sintetico | SFX-092 |
| SYN-34 | Cuore di Vera | doppio battito (sinusoidi 50/60 Hz con inviluppo) | cap. 8, scene di tensione |
| SYN-35 | Scopa sulle tegole | strisciato granulare di rami secchi su superficie dura (14.039) | SFX-062 |

### 2.2 Letti d'ambiente per luogo e ora
| Luogo | Mattina | Pomeriggio | Sera | Notte |
|---|---|---|---|---|
| Aeroporto | — | SYN-01, 02, 05, aerei lontani | — | — |
| Auto / A18 | — | SYN-06, traffico | SYN-06, vento, cicale fuori dal finestrino | — |
| Scalinata | rondini, passi, tapparelle, radio lontana | cicale (set–ott), voci dalle finestre | TV dalle finestre, stoviglie, gelsomini (nessun suono) | grilli (set), gatti, lampione che ronza |
| Casa Russo | caffè (moka di Concetta 7:30), radio | silenzio casalingo, frigo | stoviglie, TV, voci | frigo (SYN-08), scricchiolii, russare di Fomà (dal cap. 2) |
| Corso | negozi che aprono, campane | folla, lingue diverse, applausi e voci dove nella realtà ci sarebbero musicisti di strada | folla, bicchieri | passi rari, motorino |
| Scuola | campanella (SFX-023), voci in aula | intervallo | — | — |
| Bar di papà | macchina del caffè, tazzine | radio (06.001), clienti | chiusura | — |
| Stazione | — | mare oltre i binari, annunci, treno merci | — | — |
| Pioggia (4/11) | SYN-20 su tegole e pietra, gronde | idem più leggera | pioggia leggera, vento | pioggia |

**Nota**: niente musica di strada sul Corso (regola D-76): le fonti musicali del mondo reale sono rese come rumori di gente.

### 2.3 Testi degli annunci [NUOVO]
- «Il volo proveniente da Istanbul è atterrato. I bagagli sono in consegna al nastro numero tre.» / «The flight from Istanbul has landed. Baggage is arriving at belt number three.»
- «Si ricorda ai signori passeggeri di non lasciare i bagagli incustoditi.» / «Passengers are reminded not to leave their baggage unattended.»
- Stazione: «Treno regionale per Messina Centrale, in partenza alle ore diciassette e quarantadue dal binario uno.»

## 3. Sottotitoli dei suoni (SFX)
Direzione: calcolata dalla posizione 3D della sorgente (SIS-05); in tabella la sorgente tipica. Colore «spiriti» per i suoni che sente solo Vera (★).

| ID | Sottotitolo | Sorgente / direzione tipica | Dove |
|---|---|---|---|
| SFX-001 ★ | [starnuto] | borsa a fiori, davanti-sinistra | SCN-01-12 |
| SFX-002 ★ | [brontolio in russo, impastato] | borsa | SCN-01-12 |
| SFX-003 ★ | [sospiro lungo, da vecchio] | borsa, davanti | SCN-01-15 |
| SFX-004 | [due colpetti sulla borsa] | sedile anteriore | SCN-01-15 |
| SFX-005 | [porta scorrevole] | porta degli arrivi | cap. 1 |
| SFX-006 | [annuncio dall'altoparlante] | soffitto | cap. 1 |
| SFX-007 | [ruote del carrello] | carrello | cap. 1 |
| SFX-008 | [motore dell'auto] | abitacolo | cap. 1 |
| SFX-009 | [cicale] | ambiente | libero |
| SFX-010 | [frigorifero che ronza] | cucina | capp. 2–14 |
| SFX-011 | [motorino lontano] | sotto, lontano | cap. 2 |
| SFX-012 | [il nono gradino scricchiola] | scala | ovunque |
| SFX-013 ★ | [masticare] | lapot' | SCN-02-08 |
| SFX-014 ★ | [la scarpa ondeggia] | lapot' / borsa | capp. 1–2 |
| SFX-015 ★ | [russare] | dietro il frigo / lapot' | capp. 2–14 |
| SFX-016 ★ | [voce brontolona dietro il frigo] | frigo | capp. 3–7 |
| SFX-017 ★ | [canticchiare dietro il frigo] | frigo | cap. 3 |
| SFX-018 ★ | [braccialetti che tintinnano] | Donne | capp. 3+ |
| SFX-019 ★ | [voci di donne che ridono piano] | piano di sotto | cap. 3 |
| SFX-020 ★ | [nebbia che sibila dalla serratura] | portone | capp. 3+ |
| SFX-021 ★ | [ventaglio che si chiude] | Rosalia | capp. 3, 12 |
| SFX-022 | [starnuto di Vera] | Vera | SCN-03-11 |
| SFX-023 | [campanella della scuola] | scuola | capp. 3, 12 |
| SFX-024 | [gessetto sulla lavagna] | aula | cap. 3 |
| SFX-025 | [macchina del caffè] | bar | bar |
| SFX-026 | [tazzine] | bar, cucina | — |
| SFX-027 | [una porta che sbatte] | casa | capp. 7–8 |
| SFX-028 | [passi sulle scale] | scala | capp. 2, 13 |
| SFX-029 | [un gatto miagola] | gatto | — |
| SFX-030 | [campane del Duomo] | Duomo | libero |
| SFX-031 | [la moka borbotta] | fornello | mattine |
| SFX-032 | [lenzuola che sbattono] | cortile | cap. 4, 12 |
| SFX-033 ★ | [tintinnio di tazzine nella vetrinetta] | soggiorno | cap. 4 |
| SFX-034 ★ | [vocina soddisfatta: «Gallinelle»] | dietro il frigo | SCN-04-03 |
| SFX-035 | [rametti che bruciano] | casa di Concetta | SCN-05-03 |
| SFX-036 | [accendino del gas] | cucina | SCN-06-04 |
| SFX-037 | [la candela crepita] | pavimento | capp. 6, 13 |
| SFX-038 | [radio del bar] | bar | cap. 6 |
| SFX-039 | [la casa scricchiola] | muri | capp. 7–9 |
| SFX-040 | [tac: la luce salta] | casa | capp. 7–9, 12 |
| SFX-041 | [interruttore del quadro elettrico] | sottoscala | cap. 7 |
| SFX-042 | [acqua dal rubinetto] | cucina | capp. 7–9 |
| SFX-043 | [foglie che cadono] | cortile | capp. 7–9 |
| SFX-044 | [la casa tossisce] | dentro i muri | capp. 7–9 |
| SFX-045 | [la crepa scricchiola] | muro delle scale | capp. 7–9 |
| SFX-046 | [crac: la crepa si allunga] | muro delle scale | SCN-08-05 |
| SFX-047 | [voci che litigano, basse] | cucina (sotto) | SCN-07-07 |
| SFX-048 | [ante dei pensili che sbattono] | cucina | SCN-08-05 |
| SFX-049 | [il frigorifero ronza forte, arrabbiato] | frigo | SCN-08-05 |
| SFX-050 | [la lampadina sfrigola] | sopra il tavolo | SCN-08-05 |
| SFX-051 | [mani che battono sul tavolo] | Vera | SCN-08-06 |
| SFX-052 | [un bicchiere si rovescia] | tavolo | SCN-08-05 |
| SFX-053 | [silenzio] | — | SCN-08-07 |
| SFX-054 | [intonaco che cade] | scale | SCN-09-02 |
| SFX-055 | [respiro affannato] | babuška | cap. 9 |
| SFX-056 | [motore e cavi della funivia] | cabina | capp. 10–11 |
| SFX-057 | [onde] | mare | capp. 10–11 |
| SFX-058 | [treno merci] | binario di là | SCN-11-03 |
| SFX-059 | [annuncio della stazione] | altoparlante | cap. 11 |
| SFX-060 ★ | [vocina: «Grazie, ragazze.»] | lapot' | SCN-11-06 |
| SFX-061 ★ | [un colpo di tosse dal frigo, fermato a metà] | cucina | SCN-12-08 |
| SFX-062 ★ | [scopa sulle tegole: fsss, fsss] | sopra | SCN-14-05 |
| SFX-063 | [pioggia sulle tegole] | sopra | cap. 14 |
| SFX-064 | [tuono lontano] | cielo | cap. 14 |
| SFX-065 | [vento] | — | cap. 14 |
| SFX-066 | [le due nonne ridono] | cucina | SCN-13-05 |
| SFX-067 | [forno elettrico] | cucina | SCN-13-03 |
| SFX-068 ★ | [soffio di nebbia sulla pagina] | quaderno | SCN-13-07 |
| SFX-069 | [clic leggero: ditale nel cucchiaio] | mani | SCN-13-09 |
| SFX-070 ★ | [singhiozzo o starnuto dal frigo] | frigo | SCN-14-02 |
| SFX-071 | [carte di dinosauri] | banco | cap. 3 |
| SFX-072 | [traffico] | strada | capp. 1, 10 |
| SFX-073 | [clacson] | strada | cap. 1 |
| SFX-074 | [un aereo decolla] | cielo | cap. 1 |
| SFX-075 | [Mattia saltella] | Mattia | cap. 1 |
| SFX-076 | [mollette] | filo | cap. 12 |
| SFX-077 | [straccio sul gradino] | scale | cap. 12 |
| SFX-078 | [cesto di vimini] | — | cap. 13 |
| SFX-079 | [carta della pasticceria] | borse | cap. 13 |
| SFX-080 | [lettera piegata] | Mattia | cap. 14 |
| SFX-081 | [una porta che si apre piano] | corridoio / portone | capp. 2, 13 |
| SFX-082 | [sale che cade] | fornello | SCN-04-10 |
| SFX-090 | [la biro scrive] | quaderno | ovunque |
| SFX-091 | [fruscio di pagina] | quaderno | ovunque |
| SFX-092 | [scatto della foto] | telefono | ovunque |
| SFX-093 | [torcia] | telefono | ovunque |

## 4. Battute doppiate (VOX)

Elenco generato da `work/strumenti/estrai_vox.py` (testo esatto da `work/libro.txt` o dai capitoli; i caratteri sono quelli del testo pronunciato, in cirillico per le battute russe). **Priorità**: *must* = da doppiare per il rilascio; *should* = doppiare se il budget del mese lo consente, altrimenti testo + verso breve. Direzione d'emozione per scena in §4.1; tabella completa in §4.2.

### 4.1 Direzione per scena
| Scena | Direzione |
|---|---|
| SCN-01-01, 01-15, 01-16 (narratrice) | ironica e asciutta, sorriso nella voce; l'ultima frase lenta e bassa, con mistero |
| SCN-01-02 | Giulia annoiata e piatta; Irina stanca ma paziente |
| SCN-01-06 | Mattia serissimo e didattico; il signore: «Ah.» spiazzato |
| SCN-01-09 | Irina commossa che grida; babuška severa-affettuosa, voce bassa; Salvo formale e nervoso; «Salvatore.» secco |
| SCN-01-10 | babuška lenta, tenerissima, un respiro prima di «Hai gli occhi di tuo nonno» |
| SCN-01-11 | «Ničego» troppo in fretta; Irina sorpresa e un po' commossa; babuška ostinata |
| SCN-01-12/13 | Vera sussurra, incredula; babuška: un secondo di sorpresa nella voce, poi tono fermo e stanco |
| SCN-02-02/03 | Concetta squillante, fiera; babuška cortese e rigida; Salvo che cerca di salvare la serata |
| SCN-02-07 | rito quasi cantato, a bassa voce, tre ripetizioni sempre più piano |
| SCN-02-09 | Fomà offesissimo, teatrale, poi soddisfatto; babuška sussurra con dolcezza |
| SCN-03-* | Nicolò curioso e diretto; Fomà: «Non ci sono» infantile e scontroso; Donne: Rosalia gelida e lenta, Nina pettegola, Tina meravigliata; lo scontro cresce fino a «Fuori voi!»; «Vera Russo…» lento, solenne |
| SCN-04-01 | Rosalia didattica e superiore; Fomà indignato |
| SCN-04-11 | Mattia candido e tranquillo; Salvo preoccupato e piano |
| SCN-05-03 | Concetta solenne e cortese, poi confidenziale |
| SCN-05-04 | babuška stanca, materna, nostalgica |
| SCN-06-02 | racconto lento, pause per cercare le parole, nostalgia; riso piano sul detto delle ragazze |
| SCN-06-03/04 | Fomà burbero che si incrina, voce piccola su «Niente Kolja»; «Brava, Veročka» commosso e trattenuto |
| SCN-07-07 | litigio a voce bassa e dura, mai urlato; Irina incrinata sull'ultima battuta |
| SCN-07-08 | Giulia arrabbiata e spaventata, voce che trema |
| SCN-08-* | Rosalia gelida; Fomà furioso e ferito; l'urlo di Vera vero, con il pianto che arriva alla fine; Tina meravigliata e piano; Rosalia «senza cattiveria, quasi stanca» |
| SCN-09-* | babuška roca e febbricitante; dottore calmo e paterno; Irina soffocata dalle mani |
| SCN-10-* | Mattia sicuro; Giulia col fiatone, arrabbiata, poi sconcertata; Vera decisa |
| SCN-11-* | dialogo intimo e lento; Fomà scorbutico che si scioglie; Vera onesta, senza retorica; il rito in russo con pronuncia un po' da bambina italiana |
| SCN-12-* | Rosalia controllata, poi il ricordo; Tina racconta come una fiaba; Vera educata e coraggiosa |
| SCN-13-* | nonne che si scoprono e ridono fino alle lacrime; Rosalia cerimoniosa; Fomà brusco e commosso |
| SCN-14-* | cena calda; Salvo impacciato e tenero; narratrice luminosa sul «ponte»; ombra in siciliano offesissima e comica; finale sottovoce |

### 4.2 Tabella completa
*(generata da `work/strumenti/estrai_vox.py` + `aggiorna_audio.py`; Car. = caratteri del testo pronunciato)*

| ID | Scena | Personaggio | Lingua | Testo pronunciato | Priorità | Car. |
|---|---|---|---|---|---|---|
| VOX-01-01 | SCN-01-01 | NARRATRICE | it | Mi chiamo Vera Russo, ho dodici anni, e il mio cognome è una barzelletta. | must | 73 |
| VOX-01-02 | SCN-01-01 | NARRATRICE | it | Non lo dico io. Lo dice chiunque conosca mia madre. Perché mia madre si chiama Irina, è nata a San Pietroburgo, parla l'italiano meglio di mio padre ma con l… | must | 352 |
| VOX-01-03 | SCN-01-01 | NARRATRICE | it | — Quindi ora sei Irina Russo — le dicevano tutti. — Una russa che si chiama Russo. E ridevano. Mia madre rideva anche lei, la prima volta. La centesima, un p… | must | 165 |
| VOX-01-04 | SCN-01-01 | NARRATRICE | it | Io sono venuta dopo. Poi Giulia, che in realtà è venuta prima di me, perché ha sedici anni, ma io la considero comunque dopo, perché è nata senza la parte de… | must | 269 |
| VOX-01-05 | SCN-01-01 | NARRATRICE | it | Quel sabato di settembre eravamo tutti e cinque all'aeroporto di Catania, davanti alla porta scorrevole degli arrivi, ad aspettare la babuška. | must | 142 |
| VOX-01-06 | SCN-01-02 | GIULIA | it | Quanto resta? | must | 13 |
| VOX-01-07 | SCN-01-02 | IRINA | it | Te l'ho detto. Solo per un po'. | must | 31 |
| VOX-01-08 | SCN-01-02 | GIULIA | it | Quanto è un po'? | must | 16 |
| VOX-01-09 | SCN-01-06 | MATTIA | it | Babuška vuol dire nonna. In russo. Però è una nonna vera, non una bambola. Le bambole sono le matrioške. | must | 104 |
| VOX-01-10 | SCN-01-06 | IL SIGNORE | it | Ah. | must | 3 |
| VOX-01-11 | SCN-01-09 | IRINA | ru | Мамочка! | must | 8 |
| VOX-01-12 | SCN-01-09 | BABUŠKA | ru | Ты худая. Совсем не ешь. | must | 24 |
| VOX-01-13 | SCN-01-09 | IRINA | ru | Ем, мама. | must | 9 |
| VOX-01-14 | SCN-01-09 | BABUŠKA | ru | Ты худая. | must | 9 |
| VOX-01-15 | SCN-01-09 | SALVO | it | Benvenuta, Galina Petrovna. | must | 27 |
| VOX-01-16 | SCN-01-09 | BABUŠKA | it | Salvatore. | must | 10 |
| VOX-01-17 | SCN-01-10 | BABUŠKA | ru | Верочка… Ты выросла. У тебя глаза твоего деда. | must | 46 |
| VOX-01-18 | SCN-01-11 | BABUŠKA | ru | Ничего. | must | 7 |
| VOX-01-19 | SCN-01-11 | IRINA | it | È un lapot'. | must | 12 |
| VOX-01-20 | SCN-01-11 | BABUŠKA | ru | Конечно, привезла. А что мне было делать, оставить его там? | must | 59 |
| VOX-01-21 | SCN-01-12 | VERA | it | Babuška… La scarpa ha starnutito. | must | 33 |
| VOX-01-22 | SCN-01-13 | BABUŠKA | ru | Обувь не чихает, Верочка. Пойдём. Я устала и есть хочу. | must | 55 |
| VOX-01-23 | SCN-01-15 | NARRATRICE | it | Io non dissi niente. Ma in quel momento decisi che avrei scoperto cosa c'era in quella scarpa, a qualunque costo. | must | 113 |
| VOX-01-24 | SCN-01-16 | NARRATRICE | it | Non sapevo ancora che dentro quella scarpa c'era la guerra. | must | 59 |
| VOX-02-01 | SCN-02-02 | CONCETTA | it | Arancini. Al ragù e al burro. Per la signora che viene da lontano, che avrà fame. | must | 81 |
| VOX-02-02 | SCN-02-02 | BABUŠKA | it | Grazie. Ho portato i pirožki. | must | 29 |
| VOX-02-03 | SCN-02-02 | SALVO | it | Che bello. Mangiamo tutto. Insieme. Tutti contenti. | must | 51 |
| VOX-02-04 | SCN-02-07 | BABUŠKA | ru | Дедушка, дедушка, пойдём с нами. Это новый дом. Пойдём жить с нами. ×3 | must | 210 |
| VOX-02-05 | SCN-02-09 | FOMÀ | it | Fu. | must | 3 |
| VOX-02-06 | SCN-02-09 | FOMÀ | ru | [parole in russo che la babuška non vorrà tradurre] | must | 51 |
| VOX-02-07 | SCN-02-09 | FOMÀ | it | E la stufa? Dov'è la stufa? Che casa è una casa senza stufa? | must | 60 |
| VOX-02-08 | SCN-02-09 | BABUŠKA | ru | Здесь нет печки, дедушка. Здесь тепло. Не нужно. | must | 48 |
| VOX-02-09 | SCN-02-09 | FOMÀ | it | Non serve! Non serve, dice! E io dove dormo? Sul pavimento, come un cane? In una scarpa, come un ciabattino? | must | 108 |
| VOX-02-10 | SCN-02-09 | FOMÀ | it | Qui. Qui dietro è caldo. Ronza. Mi piace. Mi metto qui. | must | 55 |
| VOX-02-11 | SCN-02-09 | BABUŠKA | ru | Спокойной ночи, Фома. | must | 21 |
| VOX-02-12 | SCN-02-09 | FOMÀ | it | Buona notte, buona notte. Senza stufa. Ma si può. | must | 49 |
| VOX-02-13 | SCN-02-10 | NARRATRICE | it | Restai sveglia a lungo, a guardare il soffitto. Da giù, ogni tanto, arrivava il ronzio del frigorifero. E una volta, una volta sola, mi sembrò di sentire qua… | must | 175 |
| VOX-03-01 | SCN-03-02 | NICOLÒ | it | Tu sei russa? | must | 13 |
| VOX-03-02 | SCN-03-02 | NICOLÒ | it | Quale metà? | must | 11 |
| VOX-03-03 | SCN-03-02 | VERA | it | Non lo so. Credo che siano mescolate. | must | 37 |
| VOX-03-04 | SCN-03-05 | FOMÀ | it | Non ci sono. | must | 12 |
| VOX-03-05 | SCN-03-05 | FOMÀ | it | Hai visto la polvere. In questa casa non pulisce nessuno. | must | 57 |
| VOX-03-06 | SCN-03-09 | ROSALIA | it | Bene, bene. Vediamo come la tengono, questa casa. | must | 49 |
| VOX-03-07 | SCN-03-09 | ROSALIA | it | Polvere. Di nuovo. | must | 18 |
| VOX-03-08 | SCN-03-09 | NINA | it | Gliel'avevo detto, Donna Rosalia. Da quando è arrivata la forestiera, qui nessuno pulisce più come si deve. Pensa che stamattina ho visto le lenzuola del bam… | must | 175 |
| VOX-03-09 | SCN-03-09 | ROSALIA | it | Donna Tina! Non si gira per le stanze senza permesso. | must | 53 |
| VOX-03-10 | SCN-03-09 | TINA | it | C'è un odore strano. Di pane. Pane nero. Non l'ho mai sentito. | must | 62 |
| VOX-03-11 | SCN-03-10 | FOMÀ | it | Chi è? Chi c'è? Chi entra a quest'ora in casa mia? | must | 50 |
| VOX-03-12 | SCN-03-10 | ROSALIA | it | Casa sua? | must | 9 |
| VOX-03-13 | SCN-03-10 | NINA | it | E questa cos'è? Un topo? | must | 24 |
| VOX-03-14 | SCN-03-10 | FOMÀ | it | Un topo! Io sono il domovoj di questa famiglia! Da duecento anni! Ho protetto sette generazioni di Ivanov, ho scaldato le loro stufe, ho intrecciato le crini… | must | 180 |
| VOX-03-15 | SCN-03-10 | TINA | it | Qui non ci sono cavalli. | must | 24 |
| VOX-03-16 | SCN-03-10 | FOMÀ | it | ...e adesso sono qui, e questa è la mia casa! | must | 45 |
| VOX-03-17 | SCN-03-10 | ROSALIA | it | Ah no, caro mio. Questa casa è nostra. Noi siamo le Donne di Fora. Veniamo in questa casa il martedì, il giovedì e il sabato, da quando c'erano i nonni dei n… | must | 355 |
| VOX-03-18 | SCN-03-10 | FOMÀ | it | Bestia! Bestia a me! Gallinelle! Gallinelle con il pizzo! | must | 57 |
| VOX-03-19 | SCN-03-10 | ROSALIA | it | Fuori. Fuori da questa casa. | must | 28 |
| VOX-03-20 | SCN-03-10 | FOMÀ | it | Fuori voi! | must | 10 |
| VOX-03-21 | SCN-03-11 | TINA | it | Lei ci vede. | must | 12 |
| VOX-03-22 | SCN-03-11 | NINA | it | Impossibile. | must | 12 |
| VOX-03-23 | SCN-03-11 | FOMÀ | it | Ci vede. Lo sapevo. Lo dicevo io. Quella mi vede dal primo giorno. | must | 66 |
| VOX-03-24 | SCN-03-11 | ROSALIA | it | Vera Russo. Figlia di Salvatore. Vieni qui. | must | 43 |
| VOX-04-01 | SCN-04-01 | ROSALIA | it | Noi siamo le signore che entrano nelle case di notte, dal buco della serratura. Se troviamo la casa in ordine, i letti fatti e le lenzuola pulite, portiamo f… | should | 377 |
| VOX-04-02 | SCN-04-01 | NINA | it | Nella scarpa. | should | 13 |
| VOX-04-03 | SCN-04-01 | FOMÀ | it | È la tradizione! Il domovoj si porta nel lapot'! Lo sanno tutti! Che ignoranza! | should | 79 |
| VOX-04-04 | SCN-04-01 | ROSALIA | it | Qui nessuno porta niente nelle scarpe. Qui nelle scarpe si mettono i piedi. | should | 75 |
| VOX-04-05 | SCN-04-02 | CONCETTA | it | Dov'è la mia moka? | should | 18 |
| VOX-04-06 | SCN-04-02 | BABUŠKA | it | Io non tocco le cose degli altri. | should | 33 |
| VOX-04-07 | SCN-04-02 | CONCETTA | it | Ah. | should | 3 |
| VOX-04-08 | SCN-04-03 | FOMÀ | it | Gallinelle. Adesso vediamo. | should | 27 |
| VOX-04-09 | SCN-04-04 | BABUŠKA | ru | Не испортился. Кто-то его испортил. | should | 35 |
| VOX-04-10 | SCN-04-05 | NINA | it | Lasciate fare a me. Gli faccio cagliare il latte, a quel topo, e alla sua padrona. | should | 82 |
| VOX-04-11 | SCN-04-11 | MATTIA | it | Il signore dice che sono state le signore | must | 41 |
| VOX-04-12 | SCN-04-11 | MATTIA | it | Quello piccolo. Quello che brontola. Lo sento la notte. Dice che le signore sono cattive e che gli hanno detto topo. | should | 116 |
| VOX-04-13 | SCN-04-11 | SALVO | it | Mattia con chi parli tu, la notte? | should | 34 |
| VOX-04-14 | SCN-04-11 | MATTIA | it | Con nessuno | should | 11 |
| VOX-04-15 | SCN-04-11 | NARRATRICE | it | E allora cosa sarebbe successo? | must | 31 |
| VOX-05-01 | SCN-05-03 | CONCETTA | it | Signore mie, la casa è pulita, i letti sono fatti. Se volete passare, siete le benvenute. | must | 89 |
| VOX-05-02 | SCN-05-03 | CONCETTA | it | E se passate anche da mio figlio, fatemi la cortesia di lasciare in pace la vecchia russa. Non è cattiva. È solo forestiera. | must | 124 |
| VOX-05-03 | SCN-05-04 | BABUŠKA | ru | Фома. Фомушка. Я знаю, что ты сердишься. Я знаю, что тебе не нравится. Печки нет, жарко, тут эти дамы. Но надо потерпеть. Мы в гостях. В чужом доме не озорни… | should | 252 |
| VOX-05-04 | SCN-05-04 | BABUŠKA | ru | Знаю. Знаю. Я тоже скучаю по дому. | should | 34 |
| VOX-05-05 | SCN-05-06 | CONCETTA | it | Alle fate? Che domande. Le fate sono nelle favole. | should | 50 |
| VOX-05-06 | SCN-05-06 | BABUŠKA | it | Veročka Sono una donna vecchia. Ho visto la guerra fredda, la perestrojka e i telefoni con le foto. Non credo a niente. | should | 119 |
| VOX-05-07 | SCN-05-06 | NARRATRICE | it | Mentivano tutte e due. E lo sapevano tutte e due. | must | 49 |
| VOX-06-01 | SCN-06-02 | BABUŠKA | ru | Сегодня Покров. | should | 15 |
| VOX-06-02 | SCN-06-02 | BABUŠKA | ru | Покров значит… покрывало. Плащ. То, что укрывает и защищает. Это праздник Богородицы. Рассказывают, что однажды, давным-давно, в Константинополе люди боялись… | should | 306 |
| VOX-06-03 | SCN-06-02 | BABUŠKA | ru | Более-менее. Но у нас Покров — это ещё и другое. В деревне у моей бабушки говорили, что Покров — это день, когда зима покрывает землю. Первым снегом. Первой … | should | 241 |
| VOX-06-04 | SCN-06-02 | BABUŠKA | ru | Часто. Не всегда. Но четырнадцатого октября это уже чувствовалось. Воздух становился тонким, холодным, пах железом. Листья на берёзах все жёлтые, и падали. П… | should | 304 |
| VOX-06-05 | SCN-06-02 | BABUŠKA | ru | Коля всегда топил печку на Покров. Всегда. Даже когда у нас в городе появились батареи, он купил чугунную печурку, вот такую маленькую, и четырнадцатого октя… | should | 245 |
| VOX-06-06 | SCN-06-03 | FOMÀ | it | Tu! Sempre tu. Non dormi mai, tu? | should | 33 |
| VOX-06-07 | SCN-06-03 | FOMÀ | it | Lo so che giorno era. Credi che non lo sappia? Duecento anni, Pokrov dopo Pokrov. La stufa accesa. Il primo fuoco. Io mi mettevo dietro, nell'angolo caldo, e… | should | 395 |
| VOX-06-08 | SCN-06-03 | FOMÀ | it | Quest'anno niente stufa. Niente neve. Niente Kolja. | should | 51 |
| VOX-06-09 | SCN-06-03 | FOMÀ | it | Il domovoj non ha nostalgia Il domovoj sta dove sta la famiglia. È la regola. Ma la famiglia è lì, e la casa era là. E adesso io non so più dove sto. | should | 149 |
| VOX-06-10 | SCN-06-04 | FOMÀ | it | Brava. Brava, Veročka. | must | 22 |
| VOX-06-11 | SCN-06-05 | NARRATRICE | it | Fuori, sul cortile, il limone si mosse appena, anche se non c'era vento. E dal buco della serratura dell'ingresso, mi sembrò, per un attimo, di vedere uscire… | must | 223 |
| VOX-07-01 | SCN-07-05 | CONCETTA | it | Sta morendo Questo limone l'ha piantato il nonno di tuo nonno, Vera. Non si è mai ammalato. Mai. Nemmeno con la siccità del Novantadue. | should | 135 |
| VOX-07-02 | SCN-07-07 | SALVO | it | ...non ho detto questo, Irina Ho detto solo che dobbiamo parlarne. | should | 66 |
| VOX-07-03 | SCN-07-07 | SALVO | it | Non ho detto di mandarla via. Ho detto che la casa è piccola. Che io lavoro sul tavolo della cucina. Che i ragazzi sono nervosi. Che tua madre e mia madre no… | should | 179 |
| VOX-07-04 | SCN-07-07 | SALVO | it | Ah, ecco. Adesso è colpa di mia madre. | should | 38 |
| VOX-07-05 | SCN-07-07 | IRINA | it | Parlarne di cosa? Di mandarla via? Mia madre è sola, Salvo. Sola. In un appartamento al quarto piano, senza ascensore, a settantaquattro anni, con il ginocch… | should | 189 |
| VOX-07-06 | SCN-07-07 | IRINA | it | Tua madre non può vedere mia madre. | should | 35 |
| VOX-07-07 | SCN-07-07 | IRINA | it | Avevi detto solo per un po'. Va bene. Ma un po' quanto, Salvo? Dimmelo tu. Quanto? | should | 82 |
| VOX-07-08 | SCN-07-07 | SALVO | it | L'hai detto. | should | 12 |
| VOX-07-09 | SCN-07-07 | SALVO | it | L'hai detto. | should | 12 |
| VOX-07-10 | SCN-07-08 | GIULIA | it | Hai sentito? | should | 12 |
| VOX-07-11 | SCN-07-08 | GIULIA | it | È tutto da quando è arrivata lei Tutto. La casa che si rompe. Mamma e papà che litigano. Le nonne che si odiano. Era tutto normale, prima. | should | 138 |
| VOX-07-12 | SCN-07-08 | GIULIA | it | E di chi è? | should | 11 |
| VOX-07-13 | SCN-07-09 | NARRATRICE | it | E io rimasi lì, al buio, divisa in due, e non sapevo più quale delle due metà fossi io. | must | 87 |
| VOX-08-01 | SCN-08-02 | ROSALIA | it | E questo cos'è? | should | 15 |
| VOX-08-02 | SCN-08-02 | ROSALIA | it | Con chi? | should | 8 |
| VOX-08-03 | SCN-08-03 | FOMÀ | it | Io non faccio la pace con le gallinelle. | should | 40 |
| VOX-08-04 | SCN-08-04 | ROSALIA | it | Io voglio che le cose stiano come sono sempre state. Questa è una casa siciliana. È la casa dei Russo da centocinquant'anni. Noi la proteggiamo da quando era… | must | 493 |
| VOX-08-05 | SCN-08-04 | FOMÀ | it | E io voglio che loro se ne vadano! Io sono il domovoj della famiglia di Galina Petrovna. Della famiglia Ivanov. La figlia di Galina Petrovna vive in questa c… | must | 470 |
| VOX-08-06 | SCN-08-06 | VERA | it | BASTA! Basta, basta, basta! Voi due, voi tre, sempre a dire mia, nostra, siciliana, russa! E io? Io cosa sono? Mia mamma è russa e mio papà è siciliano! Io h… | must | 369 |
| VOX-08-07 | SCN-08-07 | TINA | it | È vero. Lei è tutte e due le cose. Per questo ci vede. Ci vede tutti. | must | 69 |
| VOX-08-08 | SCN-08-07 | ROSALIA | it | La bambina è di tutti e due, va bene. Ma tu, vecchio, qui non sei di casa. Non lo sarai mai. Questa terra non è la tua. Il sole non è il tuo, il mare non è i… | must | 250 |
| VOX-08-09 | SCN-08-08 | NARRATRICE | it | Solo silenzio. | must | 14 |
| VOX-09-01 | SCN-09-03 | BABUŠKA | ru | Я в порядке, Верочка. Мне просто немного холодно. | should | 49 |
| VOX-09-02 | SCN-09-03 | DOTTORE | it | Niente di grave Ma è stanca, la signora. Stanca dentro. Succede, a quell'età, quando si cambia paese. | should | 101 |
| VOX-09-03 | SCN-09-04 | IRINA | it | È colpa mia L'ho portata qui. L'ho tolta da casa sua. A settantaquattro anni. | should | 77 |
| VOX-09-04 | SCN-09-04 | IRINA | it | E allora di chi è? | should | 18 |
| VOX-09-05 | SCN-09-05 | BABUŠKA | ru | Коля… Коля… Малая Посадская… печка… | should | 35 |
| VOX-09-06 | SCN-09-05 | BABUŠKA | ru | Верочка. Лапоть. Он на месте? | must | 29 |
| VOX-09-07 | SCN-09-07 | MATTIA | it | Vera Lo cerchi, il signore piccolo? | should | 35 |
| VOX-09-08 | SCN-09-07 | MATTIA | it | No Però so da che parte è andato. | must | 33 |
| VOX-10-01 | SCN-10-01 | MATTIA | it | Farina | should | 6 |
| VOX-10-02 | SCN-10-01 | MATTIA | it | Il signore piccolo ha sempre la farina sui piedi. Perché dorme dietro il frigo, e il frigo è vicino al sacco della farina della babuška. Io lo sento camminar… | should | 296 |
| VOX-10-03 | SCN-10-04 | MATTIA | it | Il signore piccolo è stanco Ha le gambe corte. Le scale sono lunghe. | should | 68 |
| VOX-10-04 | SCN-10-05 | MATTIA | it | Vera Il signore piccolo torna? | should | 30 |
| VOX-10-05 | SCN-10-05 | MATTIA | it | Se non torna, la babuška guarisce lo stesso? | should | 44 |
| VOX-10-06 | SCN-10-05 | MATTIA | it | Io voglio che torna Mi piace sentirlo russare. | should | 46 |
| VOX-10-07 | SCN-10-06 | MATTIA | it | C'è odore di pane nero. | should | 23 |
| VOX-10-08 | SCN-10-06 | MATTIA | it | È lì Il signore piccolo vuole prendere il treno. | should | 48 |
| VOX-10-09 | SCN-10-07 | GIULIA | it | Vera! Mattia! Fermi lì! | should | 23 |
| VOX-10-10 | SCN-10-07 | GIULIA | it | Che cavolo state facendo? La mamma vi crede alla Villa! Vi ho visti dalla finestra mentre attraversavate il Corso e vi ho seguiti fin qui! In funivia! Da sol… | should | 200 |
| VOX-10-11 | SCN-10-07 | GIULIA | it | Niente Giulia. Adesso torniamo a casa. Subito. | should | 46 |
| VOX-10-12 | SCN-10-07 | GIULIA | it | Alla stazione? Per andare dove? | should | 31 |
| VOX-10-13 | SCN-10-07 | GIULIA | it | Voi due siete completamente pazzi. | must | 34 |
| VOX-10-14 | SCN-10-07 | VERA | it | Dobbiamo trovare il domovoj della babuška Si chiama Fomà. È scappato giovedì notte perché le Donne di Fora gli hanno detto che qui non è di casa. Senza di lu… | should | 275 |
| VOX-10-15 | SCN-10-07 | NARRATRICE | it | Ma non mi lasciò il braccio per tornare a casa. Me lo lasciò e basta. E quando io e Mattia cominciammo a scendere verso la stazione, sentii i suoi passi diet… | must | 196 |
| VOX-11-01 | SCN-11-02 | GIULIA | it | Dove? | must | 5 |
| VOX-11-02 | SCN-11-02 | GIULIA | it | Vera, lì non c'è niente. C'è una scarpa vecchia. | must | 48 |
| VOX-11-03 | SCN-11-03 | FOMÀ | it | Vattene Sto aspettando il treno. | must | 32 |
| VOX-11-04 | SCN-11-03 | FOMÀ | it | Il treno per la Russia. | must | 23 |
| VOX-11-05 | SCN-11-03 | FOMÀ | it | Il domovoj ha tempo. Il domovoj è vecchio. Ho fatto la strada dalla Russia alla Sicilia nella pancia di un aereo, dentro una scarpa, dentro una borsa, tra le… | must | 212 |
| VOX-11-06 | SCN-11-03 | FOMÀ | it | Lei ha ragione La signora con il ventaglio. Qui non sono di casa. Il sole è troppo forte. Il mare è troppo blu. Non c'è la neve, non c'è la stufa, non ci son… | must | 279 |
| VOX-11-07 | SCN-11-03 | FOMÀ | it | Tu cosa? | must | 8 |
| VOX-11-08 | SCN-11-03 | FOMÀ | it | E allora come fai? | must | 18 |
| VOX-11-09 | SCN-11-03 | FOMÀ | it | La babuška sta male? | must | 20 |
| VOX-11-10 | SCN-11-03 | FOMÀ | it | Vecchio scemo Vecchio domovoj scemo e permaloso. | must | 48 |
| VOX-11-11 | SCN-11-03 | VERA | it | Ciao, Fomà. | must | 11 |
| VOX-11-12 | SCN-11-03 | VERA | it | Quale treno? | must | 12 |
| VOX-11-13 | SCN-11-03 | VERA | it | È lunga, Fomà Tanto lunga. | must | 26 |
| VOX-11-14 | SCN-11-03 | VERA | it | E dove vai? Il dedushka Kolja non c'è più. L'appartamento è vuoto. La babuška è qui. | must | 84 |
| VOX-11-15 | SCN-11-03 | VERA | it | E allora io? | must | 12 |
| VOX-11-16 | SCN-11-03 | VERA | it | Io sono metà forestiera Qui, sono la figlia della russa. In Russia, quando ci vado d'estate, sono l'italiana. I bambini del cortile della babuška mi chiamava… | must | 475 |
| VOX-11-17 | SCN-11-03 | VERA | it | Io sono sempre un po' forestiera, Fomà. Da tutte e due le parti. Sempre. | must | 72 |
| VOX-11-18 | SCN-11-03 | VERA | it | Non lo so bene Ma penso che una casa non sia un posto. Non è la Russia, non è la Sicilia. Non è la stufa e non è il frigorifero. Una casa sono le persone che… | must | 490 |
| VOX-11-19 | SCN-11-03 | VERA | it | Ha la febbre. Da quando te ne sei andato. | must | 41 |
| VOX-11-20 | SCN-11-04 | FOMÀ | it | Torno Ma a una condizione. Anzi, a due. | must | 39 |
| VOX-11-21 | SCN-11-04 | FOMÀ | it | La prima: mi dovete invitare. Per bene. Come si fa. Non si porta via un domovoj da una stazione come un sacco di patate. Bisogna chiamarlo con le parole giuste. | must | 160 |
| VOX-11-22 | SCN-11-04 | FOMÀ | it | La seconda è che le signore. Quelle tre. Devono chiedermelo anche loro. Devono dire che posso restare. Altrimenti è inutile. Una casa con due padroni che si … | must | 204 |
| VOX-11-23 | SCN-11-04 | VERA | it | Va bene Ci provo. | must | 17 |
| VOX-11-24 | SCN-11-05 | VERA | ru | Дедушка, дедушка, пойдём с нами. Пойдём домой. | must | 46 |
| VOX-11-25 | SCN-11-05 | FOMÀ | it | Andiamo. Ho fame. | must | 17 |
| VOX-11-26 | SCN-11-06 | MATTIA | it | È lì dentro? | must | 12 |
| VOX-11-27 | SCN-11-06 | MATTIA | it | Ciao, signore piccolo! Bentornato! | must | 34 |
| VOX-11-28 | SCN-11-06 | FOMÀ | it | Sì, sì. Ciao. Non soffiarmi in faccia. | must | 38 |
| VOX-11-29 | SCN-11-06 | GIULIA | it | Niente Andiamo. È tardi. La mamma ci ammazza. | must | 45 |
| VOX-11-30 | SCN-11-06 | NARRATRICE | it | Molto tempo dopo, mesi dopo, Giulia mi confessò che in quel momento, sulla banchina della stazione, mentre Mattia salutava la scarpa, aveva sentito una vocin… | must | 214 |
| VOX-11-31 | SCN-11-06 | NARRATRICE | it | Grazie, ragazze. | must | 16 |
| VOX-11-32 | SCN-11-07 | NARRATRICE | it | Ma non lasciò mai la mia mano. Neanche una volta. | must | 49 |
| VOX-12-01 | SCN-12-04 | CONCETTA | it | Da fuori Da Catania. | should | 20 |
| VOX-12-02 | SCN-12-04 | CONCETTA | it | E allora? È fuori. Non è di qua. | should | 32 |
| VOX-12-03 | SCN-12-04 | CONCETTA | it | Un po' sì Non tanto. Ma un po'. | should | 31 |
| VOX-12-04 | SCN-12-04 | IRINA | it | Da fuori dove? | should | 14 |
| VOX-12-05 | SCN-12-06 | ROSALIA | it | È tornato Lo sento. Puzza di pane nero da qui. | should | 46 |
| VOX-12-06 | SCN-12-06 | ROSALIA | it | L'hai riportato tu. | should | 19 |
| VOX-12-07 | SCN-12-06 | ROSALIA | it | Allora hai deciso da che parte stare. | should | 37 |
| VOX-12-08 | SCN-12-06 | ROSALIA | it | Falla | should | 5 |
| VOX-12-09 | SCN-12-06 | NINA | it | Che domanda è? | should | 14 |
| VOX-12-10 | SCN-12-06 | VERA | it | No Non ho deciso niente. Ho una domanda. Una sola. Posso farla? | should | 63 |
| VOX-12-11 | SCN-12-06 | VERA | it | Perché vi chiamate Donne di Fora? | must | 33 |
| VOX-12-12 | SCN-12-06 | VERA | it | È una domanda vera. Fora vuol dire fuori. In siciliano. Lo dice anche la nonna Concetta: quelli di fora sono quelli che vengono da fuori. Da un altro posto. … | should | 210 |
| VOX-12-13 | SCN-12-07 | NINA | it | Perché entriamo da fuori Dal buco della serratura. Veniamo da fuori della casa. È ovvio. | should | 88 |
| VOX-12-14 | SCN-12-07 | VERA | it | Può darsi Ma prima? Prima di entrare dal buco della serratura? Da dove venivate? Siete sempre state qui? Siete nate in questa casa? | should | 131 |
| VOX-12-15 | SCN-12-07 | VERA | it | Ma è vera? | should | 10 |
| VOX-12-16 | SCN-12-07 | TINA | it | No Non siamo nate qui. Nessuna di noi. | should | 38 |
| VOX-12-17 | SCN-12-07 | TINA | it | È vero, Donna Rosalia. Lo sapete anche voi. Io non me lo ricordo bene. È passato tanto tempo. Ma mi ricordo che una volta, all'inizio, eravamo noi quelle che… | must | 622 |
| VOX-12-18 | SCN-12-07 | ROSALIA | it | Tina | should | 4 |
| VOX-12-19 | SCN-12-07 | ROSALIA | it | È una storia vecchia | should | 20 |
| VOX-12-20 | SCN-12-07 | ROSALIA | it | È vera Anche noi, una volta, eravamo forestiere. | must | 48 |
| VOX-12-21 | SCN-12-08 | VERA | it | Fomà ha detto che resta solo se glielo chiedete voi. Se gli dite che può stare. Non ve lo chiede perché è orgoglioso. È orgoglioso come voi. Ma se non glielo… | should | 294 |
| VOX-12-22 | SCN-12-08 | ROSALIA | it | Hai pulito tu? | should | 14 |
| VOX-12-23 | SCN-12-08 | ROSALIA | it | Anche le scale? | should | 15 |
| VOX-12-24 | SCN-12-08 | ROSALIA | it | Una Russo che pulisce le scale di notte per tre vecchie e un topo con la barba Questo non si era mai visto in centocinquant'anni. | must | 129 |
| VOX-12-25 | SCN-12-08 | ROSALIA | it | Va bene Gli parleremo. Sabato. La notte dei Morti. Quando tutta la casa è sveglia e la porta è aperta per tutti, vivi e morti, di qua e di fuori. Ma a una co… | should | 166 |
| VOX-12-26 | SCN-12-08 | ROSALIA | it | Che la casa sia in ordine il martedì, il giovedì e il sabato. Sempre. Da adesso in poi. Le lenzuola stese dritte, con le mollette uguali. E niente briciole d… | should | 183 |
| VOX-12-27 | SCN-12-08 | NARRATRICE | it | Io sorrisi così tanto che mi fecero male le guance. | must | 51 |
| VOX-13-01 | SCN-13-01 | NARRATRICE | it | In Sicilia, la notte tra il primo e il due novembre, i morti tornano a casa. Non per fare paura. Per portare i regali ai bambini. | must | 129 |
| VOX-13-02 | SCN-13-03 | IRINA | ru | Что ты делаешь, мама? Тебе нужно отдыхать. | should | 42 |
| VOX-13-03 | SCN-13-03 | BABUŠKA | ru | Пеку хлеб. | should | 10 |
| VOX-13-04 | SCN-13-03 | BABUŠKA | ru | В России в ноябре — родительская суббота. Пекут хлеб, идут на кладбище, оставляют хлеб на могиле. Чтобы помнить. В этом году Коля далеко. Хлеб я ему здесь ос… | should | 163 |
| VOX-13-05 | SCN-13-05 | CONCETTA | it | Anche lei? | must | 10 |
| VOX-13-06 | SCN-13-05 | CONCETTA | it | Da quanto tempo lo sa? | should | 22 |
| VOX-13-07 | SCN-13-05 | CONCETTA | it | Da sempre. Mia suocera mi ha insegnato il rosmarino. Il martedì, il giovedì e il sabato. E perché non me l'ha detto? | must | 116 |
| VOX-13-08 | SCN-13-05 | CONCETTA | it | Perché pensavo che lei mi avrebbe presa per matta. | must | 50 |
| VOX-13-09 | SCN-13-05 | BABUŠKA | it | Anche lei? | should | 10 |
| VOX-13-10 | SCN-13-05 | BABUŠKA | it | Da sempre Mia nonna mi ha insegnato a dargli il latte. E lei? | should | 61 |
| VOX-13-11 | SCN-13-05 | BABUŠKA | it | Perché pensavo che lei mi avrebbe presa per matta. E lei, perché non me l'ha detto? | should | 83 |
| VOX-13-12 | SCN-13-05 | BABUŠKA+CONCETTA | it | [risata a due voci, 6 s] | must | 24 |
| VOX-13-13 | SCN-13-06 | ROSALIA | it | Signor domovoj Stanotte è la notte dei Morti. Stanotte la porta di questa casa è aperta per tutti: per i vivi e per i morti, per quelli di qua e per quelli d… | must | 296 |
| VOX-13-14 | SCN-13-06 | FOMÀ | it | Grazie Signora. | must | 15 |
| VOX-13-15 | SCN-13-09 | CONCETTA | it | Questo è di Turi. Ci cuciva le vele della barca, da giovane, prima di aprire il bar. L'ho perso trent'anni fa. | should | 110 |
| VOX-13-16 | SCN-13-09 | BABUŠKA | ru | Это Колина. Он сам вырезал, мальчишкой, в деревне. Лежала в ящике на кухне, в Петербурге. Я её не брала. Точно не брала. | should | 120 |
| VOX-13-17 | SCN-13-09 | NARRATRICE | it | Ci stava perfetto. Come se fossero stati fatti per stare insieme. | must | 65 |
| VOX-14-01 | SCN-14-02 | SALVO | it | Allora. Dobbiamo parlare di una cosa. | must | 37 |
| VOX-14-02 | SCN-14-02 | SALVO | it | Per l'inverno In Russia l'inverno è lungo, e il suo appartamento ha quattro piani di scale, e il ginocchio... insomma. Qui c'è il sole. E poi... E poi i piro… | must | 206 |
| VOX-14-03 | SCN-14-02 | SALVO | it | Li faccio al bar. Tanto d'inverno c'è tempo. E poi abbiamo pensato di chiudere il pezzo di terrazzo sopra la cucina. Farci una stanza piccola. Con una finest… | must | 302 |
| VOX-14-04 | SCN-14-02 | IRINA | it | Abbiamo pensato che la babuška resta con noi per l'inverno. | must | 59 |
| VOX-14-05 | SCN-14-02 | BABUŠKA | it | Per l'inverno? | should | 14 |
| VOX-14-06 | SCN-14-02 | BABUŠKA | it | E lo studio? I tuoi conti, Salvatore? | should | 37 |
| VOX-14-07 | SCN-14-02 | BABUŠKA | it | Salvatore Sei un brav'uomo. Magro, ma bravo. | must | 44 |
| VOX-14-08 | SCN-14-03 | NARRATRICE | it | Adesso sapevo la risposta. Non c'era una metà. Non ero mezza russa e mezza siciliana, come una pizza con due gusti. Ero tutte e due le cose insieme, intere, … | must | 293 |
| VOX-14-09 | SCN-14-03 | NARRATRICE | it | Non ero divisa. Ero un ponte. | must | 29 |
| VOX-14-10 | SCN-14-04 | MATTIA | it | Vera Lo sai cosa voglio quest'anno? | should | 35 |
| VOX-14-11 | SCN-14-04 | MATTIA | it | Quest'anno non voglio la Befana. Voglio Ded Moroz. Quello russo. Il Nonno Gelo. La babuška dice che arriva a Capodanno con la slitta e i cavalli, e che porta… | should | 286 |
| VOX-14-12 | SCN-14-04 | MATTIA | it | Ho già scritto la lettera. La babuška me la traduce in russo domani. Poi la mettiamo sulla finestra. | should | 100 |
| VOX-14-13 | SCN-14-05 | OMBRA | scn | Làida iu? Carbuni iu? E 'u Nannu Ielu, eh? 'U Nannu Ielu! Ora videmu. | must | 69 |
| VOX-14-14 | SCN-14-06 | NARRATRICE | it | Dalla cucina, di sotto, sentii Fomà che russava. Dal buco della serratura, piano, entrava un filo di nebbia che sapeva di rosmarino. Era martedì. | must | 145 |
| VOX-14-15 | SCN-14-06 | NARRATRICE | it | E l’inverno stava arrivando. | must | 28 |

### 4.3 Totali e piano dei crediti

| Rilascio | Battute | Caratteri totali | di cui *must* | Crediti con 2 take (1 credito ≈ 1 carattere) | Piano |
|---|---|---|---|---|---|
| v1.0 | 61 | 3982 | 3982 | 7964 (*must*) / 7964 (tutte) | 1 mese di ElevenLabs gratuito (≈ 8.000 crediti) per tutte le battute; versi brevi nel mese successivo |
| v2.0 | 55 | 6400 | 2331 | 4662 (*must*) / 12800 (tutte) | 2 mesi di ElevenLabs gratuito; le *should* lunghe (racconto del Pokrov) su Fish Audio se il mese non basta |
| v3.0 | 114 | 9897 | 5899 | 11798 (*must*) / 19794 (tutte) | 2–3 mesi di ElevenLabs gratuito oppure Fish Audio per le *should* |
| **Totale** | 230 | 20279 | 12212 | 24424 / 40558 | — |

Versi brevi (§6): circa 9 personaggi × 8 versi × 3 varianti, ≈ 2.500 caratteri, una sessione dedicata. Le voci di ogni rilascio si producono nella fase dei contenuti (Fase 4 per la v1.0) e si chiudono prima della Beta.

## 5. Voci: brief per ElevenLabs e Fish Audio

### 5.1 Metodo comune
1. **ElevenLabs** (piano gratuito: circa 10.000 crediti al mese, uso non commerciale con attribuzione «ElevenLabs» nei crediti, D-43): per ogni personaggio una **Voice Design** dal prompt inglese qui sotto con il modello consigliato dall'app al momento della generazione (oggi Eleven v4 / Voice Design v3: supportano italiano e russo e i tag audio tra parentesi quadre). Si generano 3 anteprime con la **frase di prova** indicata; si salva la migliore nella libreria («Save voice») con il nome `CR_<PERSONAGGIO>`.
2. **Fish Audio** (piano gratuito; modello S2.1 Pro o successivo): per le battute che non entrano nel budget mensile o per le voci russe se rendono meglio. Nella libreria «Discover» si cerca con le **parole chiave** indicate, si ascoltano almeno 5 voci con la stessa frase di prova e si sceglie con la griglia di valutazione (§5.3). Si registra l'ID della voce.
3. **Coerenza**: un personaggio usa **sempre la stessa voce e lo stesso strumento** in tutto il gioco (non si mescolano ElevenLabs e Fish per lo stesso personaggio). I parametri iniziali si annotano in `assets_in/audio/voci.json` (nome, strumento, ID voce, modello, stabilità, somiglianza, stile, velocità) e non si cambiano tra una sessione e l'altra. Ogni battuta: 2 take, si sceglie la migliore.
4. **Nessuna voce clonata di persone reali**, nessuna voce di bambini reali (D-80): solo Voice Design o voci di libreria che il servizio dichiara utilizzabili.
5. **Russo**: le battute russe si inviano in cirillico con l'accento tonico segnato dove ambiguo (es. «Верочка» → «Ве́рочка», «Фома́»); revisione di un madrelingua prima (Q-06).
6. **Formato di consegna**: WAV 48 kHz 24 bit, o MP3 320 kbps se il piano non dà WAV; nome file `VOX-CC-NN_take1.wav` in `assets_in/audio/vox/`.

### 5.2 Brief per personaggio

| Voce | Prompt di Voice Design (EN) | Frase di prova | Impostazioni di partenza (ElevenLabs) | Parole chiave Fish Audio | Note di pronuncia |
|---|---|---|---|---|---|
| **NARRATRICE** (Vera 13–14, D-42) | "A 13-year-old Italian girl from Sicily telling a story she lived a few months ago. Clear, warm, slightly husky young voice, dry wit, quick ironic timing, gentle pauses before punchlines. Standard Italian with a very light southern softness, no strong regional accent. Intimate, close-mic, like reading her own diary." | «Mi chiamo Vera Russo, ho dodici anni, e il mio cognome è una barzelletta.» | Stabilità 45%, Somiglianza 80%, Stile 25%, velocità 1,0 | ragazza, italiano, narratrice, giovane, calda, ironica | «babuška» con š (sc di «scena»); «Veročka» con č di «ciao» |
| **VERA-12** (solo urlo del cap. 8 e scene chiave dei capp. 10–12) | "The same girl at 12: brighter, a bit higher, more breathless and impulsive. Italian, light Sicilian softness. Capable of a real, raw shout that breaks into tears." | «Io sono metà e metà! Quindi di chi sono io, eh?» | Stabilità 35%, Somiglianza 80%, Stile 40% | ragazzina, italiano, emotiva | — |
| **BABUŠKA** | "A 74-year-old Russian grandmother from Saint Petersburg. Low, warm, slightly hoarse contralto, slow and deliberate, few words, dry tenderness under a stern surface. Native Russian, educated Petersburg pronunciation. When speaking Italian: heavy Russian accent, long rolled R, open vowels, short sentences." | RU «Ве́рочка… Ты вы́росла. У тебя́ глаза́ твоего́ де́да.» · IT «Salvatore. Sei un brav'uomo. Magro, ma bravo.» | Stabilità 55%, Somiglianza 85%, Stile 20%, velocità 0,92 | nonna, anziana, russo, calda, roca | in italiano «Salvatore» con R arrotata; mai cadenza siciliana |
| **IRINA** | "A 41-year-old Russian woman who has lived in Sicily for 18 years, works as a tour guide. Clear mezzo-soprano, quick and practical, emotional when tired. Fluent Italian with rolling R 'like marbles'; native Russian with her mother." | IT «Avevi detto solo per un po'. Va bene. Ma un po' quanto, Salvo?» · RU «Ма́ма. Ты всё-таки его́ привезла́.» | Stabilità 50%, Somiglianza 80%, Stile 30% | donna, 40 anni, russa, italiano con accento | — |
| **SALVO** | "A 44-year-old Sicilian man from Taormina who runs a café. Warm baritone, fast, friendly, laughs easily, nervous politeness with his mother-in-law. Moderate eastern-Sicilian accent." | «Che bello. Mangiamo tutto. Insieme. Tutti contenti.» | Stabilità 45%, Somiglianza 80%, Stile 35% | uomo, siciliano, baritono, simpatico | «Galina Petrovna» con accento sulla O |
| **GIULIA** | "A 16-year-old Sicilian girl, bored and sarcastic, flat delivery, slightly nasal, short sentences; when scared her voice trembles and anger cracks. Light Sicilian accent." | «Voi due siete completamente pazzi.» | Stabilità 40%, Somiglianza 80%, Stile 35% | adolescente, sarcastica, italiano | — |
| **MATTIA** | "A 6-year-old boy (designed voice, not a real child's clone). High, clear, very serious about strange things, matter-of-fact, slight lisp on S. Italian with a light Sicilian lilt." | «Il signore dice che sono state le signore.» | Stabilità 50%, Somiglianza 75%, Stile 30% | bambino, voce infantile, italiano | — |
| **CONCETTA** | "A 71-year-old Sicilian grandmother, loud bright old soprano that 'can be heard as far as Giardini Naxos', fast, proud, theatrical, devout; strong Sicilian intonation, regional Italian." | «Arancini. Al ragù e al burro. Per la signora che viene da lontano, che avrà fame.» | Stabilità 40%, Somiglianza 80%, Stile 45% | nonna siciliana, anziana, squillante | parole siciliane: «picciridda» (accento sulla prima i) |
| **FOMÀ** | "A tiny, ancient, grumpy house spirit, 200 years old, cat-like. Small raspy old-man voice, nasal, mouth 'full of bread', theatrical indignation, sniffs and huffs. Speaks broken Italian with a thick Russian accent and every R wrong; Russian curses mumbled." | «E la stufa? Dov'è la stufa? Che casa è una casa senza stufa?» | Stabilità 35%, Somiglianza 75%, Stile 55%, velocità 1,05 | vecchio, brontolone, creatura, voce piccola, accento russo | «Veročka» perfetto (è russo); le R italiane gutturali; tag [grumbles] [sniffs] [huffs] |
| **ROSALIA** | "An elegant, ageless Sicilian noblewoman spirit. Cold, slow, deliberate contralto, aristocratic Sicilian Italian, says icy things very quietly; rare hints of a buried memory." | «Vera Russo. Figlia di Salvatore. Vieni qui.» | Stabilità 60%, Somiglianza 85%, Stile 30%, velocità 0,9 | donna matura, elegante, fredda, siciliana | — |
| **NINA** | "A plump, gossipy Sicilian lady spirit. Chatty mezzo-soprano that turns shrill when angry, quick, sharp tongue, regional Sicilian Italian." | «E questa cos'è? Un topo?» | Stabilità 40%, Somiglianza 80%, Stile 45% | signora, pettegola, siciliana | — |
| **TINA** | "A young Sicilian woman spirit, almost a girl. Light, sweet soprano, wonder in her voice, speaks softly like telling a fairy tale; gentle Sicilian accent." | «È vero. Lei è tutte e due le cose. Per questo ci vede. Ci vede tutti.» | Stabilità 50%, Somiglianza 80%, Stile 30% | ragazza, dolce, fiaba, siciliana | — |
| **NICOLÒ** | "An 11-year-old Sicilian boy, enthusiastic, quick, nerdy about dinosaurs." | «Tu sei russa? Quale metà?» | Stabilità 50% | ragazzino, entusiasta | «Pachycephalosaurus» all'italiana |
| **DOTTORE** | "A 72-year-old Sicilian country doctor, calm, paternal, slow, reassuring." | «Niente di grave. Ma è stanca, la signora. Stanca dentro.» | Stabilità 60% | anziano, medico, calmo | — |
| **OMBRA** (Befana, D-51) | "An offended old woman's voice carried by the wind, cracked and comic, speaking strong Sicilian dialect, indignant." | SCN «Làida iu? Carbuni iu? E 'u Nannu Ielu, eh? 'U Nannu Ielu! Ora videmu.» | Stabilità 30%, Stile 60%; effetto vento in post | vecchia, strega, dialetto siciliano | verificare il siciliano (Q-07) |
| **IL SIGNORE** | "A 60-year-old Sicilian man, good-natured, slightly taken aback." | «Ah.» | — | uomo anziano | — |

### 5.3 Griglia per scegliere una voce (Fish Audio e anteprime ElevenLabs)
Voto 1–5 su: età credibile · timbro come nel brief · chiarezza delle parole · accento corretto · naturalezza delle pause · resa emotiva (prova con una seconda frase emotiva della §4.1). Si sceglie la voce con il totale più alto e nessun voto sotto 3 su «età» e «accento».

## 6. Versi brevi (non verbali)
Prodotti con le stesse voci usando i tag audio (ElevenLabs: [sighs], [laughs], [chuckles], [gasps], [grumbles]; Fish Audio: marcatori di emozione tra parentesi del modello in uso) su frasi di sole interiezioni; 3 varianti per tipo.

| Personaggio | Versi |
|---|---|
| Vera | sospiro, risatina, sbuffo, respiro trattenuto, «mh», «oh!» |
| Babuška | sospiro lungo, «ну-ну» (nu-nu), «ох» (och), risata bassa, tosse (cap. 9) |
| Irina | sospiro, risata, «Mамочка» sussurrato |
| Salvo | risata, «eh», sbuffo |
| Giulia | «ugh», sbuffo, risata nasale, «pff» |
| Mattia | risata, «uau», «eh?», sbadiglio |
| Concetta | «Gesù Maria», risata squillante, «mah!» |
| Fomà | brontolii in russo impastato (parole inventate di suono russo, nessun significato), sbuffi, «Фу», starnuto, russare, sospiro da vecchio, masticare |
| Donne | risate piano (tre timbri), «ts ts» di Rosalia, sbuffo di Nina, «oh» meravigliato di Tina |

## 7. Mix
| Bus | Livello di riferimento (LUFS integrati, scena tipica) | Note |
|---|---|---|
| Voci | −18 LUFS, picco −3 dBTP | sempre sopra tutto |
| Ambienti | −30 LUFS | **ducking** −8 dB sotto le voci (attacco 80 ms, rilascio 600 ms) |
| Effetti | −24 LUFS | ducking −4 dB |
| Interfaccia | −26 LUFS | — |
- **Audio 3D**: PannerNode HRTF per sorgenti vicine (< 15 m), equal-power oltre; distanza «inverse» con raggio di riferimento 1 m e rolloff 1,2; occlusione semplice (passa-basso 1200 Hz) attraverso muri tra stanze; riverbero per stanza con IR proceduali (bagno, scale, cucina, chiesa, stazione).
- **Spiriti**: le voci degli spiriti sono un filo più vicine e con un riverbero leggermente più lungo (+0,4 s) per distinguerle senza effetti caricaturali.
- **Accessibilità**: mono (somma L+R), riduzione della dinamica (compressore bus master 3:1), volumi separati, sottotitoli dei suoni.

## Fonti
- [ElevenLabs — Eleven v4](https://elevenlabs.io/v4)
- [ElevenLabs v3 — audio tags (guida)](https://runware.ai/docs/models/elevenlabs-v3/guides/directing-with-audio-tags.md)
- [ElevenLabs — piano gratuito e licenza (riepilogo 2026)](https://dupple.com/learn/is-elevenlabs-free)
- [Fish Audio — recensione e piani](https://www.bitdoze.com/fish-audio-review/)
- [MDN — Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
- [MDN — AudioWorklet](https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet)
