# Il domovoj nella scarpa — Fasi di sviluppo

Piano di produzione del gioco tratto dal libro *Il domovoj nella scarpa* (Casa Russo, libro 1).
Si basa sul *Documento di gioco* e sulle 30 decisioni prese nella sessione di domande, riportate nella sezione 2.

Uso: privato (non pubblicato, nessuno scopo commerciale).

---

## Indice

1. [Visione e rilasci](#1-visione-e-rilasci)
2. [Decisioni di design (le 30 risposte)](#2-decisioni-di-design-le-30-risposte)
3. [Cosa cambia rispetto al documento di gioco](#3-cosa-cambia-rispetto-al-documento-di-gioco)
4. [Mappa delle fasi](#4-mappa-delle-fasi)
5. [Fase 0 — Concept e documentazione](#fase-0--concept-e-documentazione)
6. [Fase 1 — Pre-produzione tecnica e pipeline](#fase-1--pre-produzione-tecnica-e-pipeline)
7. [Fase 2 — Prototipo dei sistemi (First Playable)](#fase-2--prototipo-dei-sistemi-first-playable)
8. [Fase 3 — Vertical slice: capitolo 1](#fase-3--vertical-slice-capitolo-1)
9. [Fase 4 — Produzione v1.0: capitoli 2–3 e Taormina alta](#fase-4--produzione-v10-capitoli-23-e-taormina-alta)
10. [Fase 5 — Alpha, Beta e lancio v1.0](#fase-5--alpha-beta-e-lancio-v10)
11. [Fase 6 — v2.0: capitoli 4–8](#fase-6--v20-capitoli-48)
12. [Fase 7 — v3.0: capitoli 9–14, libro completo](#fase-7--v30-capitoli-914-libro-completo)
13. [Fase 8 — Post-lancio e ponte verso il libro 2](#fase-8--post-lancio-e-ponte-verso-il-libro-2)
14. [Piano dei capitoli (missioni)](#14-piano-dei-capitoli-missioni)
15. [Calendario della storia](#15-calendario-della-storia)
16. [Architettura tecnica](#16-architettura-tecnica)
17. [Budget di prestazioni](#17-budget-di-prestazioni)
18. [Qualità e test](#18-qualità-e-test)
19. [Rischi principali](#19-rischi-principali)
20. [Definition of Done](#20-definition-of-done)

---

## 1. Visione e rilasci

Un gioco 3D in prima persona, atmosferico e realistico, in cui il giocatore è **Vera Russo, 12 anni**, metà russa e metà siciliana, l'unica che vede gli spiriti di casa. Si vive il libro capitolo per capitolo; tra un capitolo e l'altro si gira liberamente per una **Taormina ricostruita fedelmente 1:1**.

Il tema del libro guida anche il design: *non sono divisa, sono un ponte*. Ogni sistema deve servire questa idea: due nonne, due tradizioni, due mondi di spiriti, e Vera che sta in mezzo.

| Rilascio | Contenuto | Zone esplorabili |
|---|---|---|
| **v1.0** | Capitoli 1–3 (aeroporto → prima notte → Donne di Fora) | Aeroporto, strada per Taormina, Casa Russo, scalinate, casa di nonna Concetta, Corso Umberto con il bar, scuola media |
| **v2.0** | Capitoli 4–8 (guerra delle tazzine → consiglio di mezzanotte) | + Teatro Antico, Villa Comunale, belvedere, negozio di prodotti dell'Est, resto di Taormina monumentale |
| **v3.0** | Capitoli 9–14 (scarpa vuota → «Solo per un po'»): **libro completo** | + Funivia, Mazzarò, Isola Bella, stazione di Taormina-Giardini |

Metodo: **vertical slice, poi espansione**. Il capitolo 1 si porta alla qualità finale con tutti i sistemi di base; gli altri capitoli si producono sopra quella base.

---

## 2. Decisioni di design (le 30 risposte)

### Produzione
| # | Tema | Decisione |
|---|---|---|
| 1 | Portata | v1.0 = capitoli 1–3; v2.0 e v3.0 completano il libro 1 |
| 2 | Metodo | Vertical slice del capitolo 1, poi espansione |
| 3 | Blender | Misto: Claude genera con script Python (Blender headless), Vlad rifinisce a mano |
| 4 | Hosting | Sito statico con caricamento a streaming (es. Vercel), asset compressi |
| 29 | Test | Vlad prova a mano + test automatici nel browser (Playwright) |

### Narrativa e struttura
| # | Tema | Decisione |
|---|---|---|
| 5 | Durata | 3–4 ore di sola trama per il libro intero (~15 min a capitolo, 25–30 per quelli d'azione) |
| 6 | Scelte | Cambiano rapporti, battute e alcune scene; gli eventi del libro restano quelli |
| 7 | Fallimento | Morbido: breve scena buffa e si riparte poco prima, nessuna perdita di progressi |
| 8 | Raccordi | **Tutto giocabile in 3D**: anche la scuola, i giorni che passano, la settimana dei dispetti |
| 30 | Russo | Le frasi russe del libro restano in russo con sottotitolo italiano; parole russe da collezionare |

### Meccaniche dei capitoli
| # | Capitolo | Decisione |
|---|---|---|
| 9 | Cap. 2, prima notte | Scena guidata: si segue la babuška e si guarda, senza rischio di essere scoperti |
| 10 | Cap. 4, guerra delle tazzine | Indagine giorno per giorno: un dispetto al giorno, prove da trovare e da mettere nel quaderno |
| 11 | Cap. 8, consiglio di mezzanotte | Barra della **tensione della casa**: le risposte la alzano o abbassano, la casa reagisce fino all'urlo «Di chi sono io?» |
| 12 | Cap. 10, impronte di farina | Mattia «sente» e indica la direzione, Vera si inginocchia e cerca le impronte; funivia giocabile |
| 13 | Cap. 12, pulizie | Minigiochi rapidi: lenzuola dritte, mollette uguali, scale, rosmarino sul piattino |
| 14 | Cap. 13, mattina dei Morti | Caccia ai cannistri nascosti; nel cesto di Vera il ditale e il cucchiaio, da unire a mano |
| 15 | Casa malata | Stato **persistente**: crepa, luce, acqua, limone peggiorano anche in esplorazione libera fino alla guarigione |
| 16 | Orientamento | Obiettivo nel quaderno + marker discreto, disattivabile dalle opzioni |

### Mondo aperto
| # | Tema | Decisione |
|---|---|---|
| 17 | Zone | Tutte: Casa Russo e scalinate, Corso Umberto, Taormina monumentale, la costa |
| 18 | Fedeltà | **Fedele 1:1** alla Taormina reale (mappe, altimetria, foto) |
| 19 | Attività | Bar di papà, missioni secondarie, segreti di casa, album e collezioni |
| 20 | Tempo | Calendario del libro: date reali della storia; martedì, giovedì e sabato notte arrivano le Donne |

### Personaggi, arte e audio
| # | Tema | Decisione |
|---|---|---|
| 21 | Fomà | Come in copertina (quasi gattesco, naso rosso, camicia rossa), reso in modo realistico con pelo e barba |
| 22 | Donne di Fora | Nebbia luminosa che entra dal buco della serratura e prende forma dal basso; semitrasparenti, con particelle |
| 23 | Voci | Doppiate solo l'intro e le scene chiave; nel resto testo + versi brevi (sospiri, risate, brontolii di Fomà) |
| 24 | Chi vede cosa | Reazioni dei personaggi: gli altri guardano «attraverso» gli spiriti e spiegano in modo normale (formiche, vento); Mattia reagisce ai suoni e vede le tracce |

### Interfaccia e piattaforme
| # | Tema | Decisione |
|---|---|---|
| 25 | Diario | Il **quaderno di scienze** di Vera: cellule e fotosintesi nelle prime pagine, poi sospettati, frecce, disegni a matita, il patto |
| 26 | Foto | Il **telefono** di Vera: fotocamera, torcia, orologio e data |
| 27 | Dispositivi | **PC e tablet**. Telefoni esclusi |
| 28 | Accessibilità | Sottotitoli dei suoni ([starnuto], [russare], [la crepa scricchiola]) + comandi rimappabili e gamepad |

---

## 3. Cosa cambia rispetto al documento di gioco

| Punto | Prima | Ora |
|---|---|---|
| Piattaforme | PC + mobile touch | PC + **tablet** (touch e tastiera). Niente telefoni |
| Pubblicazione | Artifact unico, modelli in base64 | **Sito statico** con streaming per zone; i capitoli non stanno nei 16 MB di un artifact |
| Voci | Solo testo | Voce nell'intro narrata e nelle scene chiave, anche in russo |
| Taormina | «Libera tra le missioni» | Ricostruita **1:1** da dati reali, tutte e quattro le zone |
| Diario | Diario degli indizi a 4 sezioni | Le stesse 4 sezioni dentro il **quaderno di scienze** di Vera |
| Fotocamera | Tasto Foto | Il telefono di Vera (anche torcia e calendario) |
| Rilascio 1.0 | Capitolo 1 | Capitoli 1–3 |

Restano valide le tre regole: **massimo senza semplificare**, **Blender per tutto il 3D**, **Babylon.js al massimo**.

---

## 4. Mappa delle fasi

```
FASE 0  Concept e documentazione          ── gate: documenti approvati
FASE 1  Pre-produzione tecnica e pipeline ── gate: un asset va da Blender al browser senza mani
FASE 2  Prototipo dei sistemi             ── gate: First Playable (tutti i sistemi base in greybox)
FASE 3  Vertical slice: capitolo 1        ── gate: cap. 1 a qualità finale = metro di misura
FASE 4  Produzione v1.0 (cap. 2–3)        ── gate: Content Complete v1.0
FASE 5  Alpha → Beta → RC → Lancio v1.0   ── gate: Gold v1.0
FASE 6  v2.0 (cap. 4–8)                   ── gate: Gold v2.0
FASE 7  v3.0 (cap. 9–14)                  ── gate: Gold v3.0 = libro completo
FASE 8  Post-lancio e ponte al libro 2
```

Ogni fase ha: **obiettivo**, **lavori per reparto**, **consegne**, **criteri di uscita** (gate). Una fase si chiude solo quando tutti i criteri di uscita sono soddisfatti.

Peso relativo indicativo del lavoro: Fase 0–2 ≈ 15%, Fase 3 ≈ 15%, Fase 4–5 ≈ 20%, Fase 6 ≈ 22%, Fase 7 ≈ 25%, Fase 8 ≈ 3%. La ricostruzione 1:1 di Taormina pesa su tutte le fasi dalla 4 in poi.

---

## Fase 0 — Concept e documentazione

**Obiettivo:** fissare su carta tutto ciò che serve per costruire senza tornare indietro.

### Lavori
- **Game Design Document (GDD)** aggiornato: unisce il documento di gioco e le decisioni della sezione 2.
- **Narrative Design Document**: per ognuno dei 14 capitoli, scaletta delle scene, battute fedeli al libro, punti di scelta, variabili che cambiano (rapporti, scene alternative), pensieri di Vera, battute delle comparse.
- **Bibbia dei personaggi**: età, aspetto, voce, modo di muoversi, rapporto con Vera, cosa vede e cosa non vede ognuno (Vera vede tutto; Mattia sente; Giulia quasi; gli adulti niente, ma le nonne *sanno*).
- **Art Bible**: stile atmosferico realistico, palette per ora del giorno e per mese (settembre caldo → novembre piovoso), materiali siciliani (intonaco, pietra, maiolica, ferro battuto, persiane verdi), riferimenti fotografici, regole per gli spiriti (Fomà, Donne di Fora), regole per le illustrazioni del quaderno.
- **Level Design Document**: piante di aeroporto, auto, Casa Russo (due piani, 9° gradino che scricchiola, cortile col limone, ingresso con la serratura grande), casa di nonna Concetta, scuola, bar, e la mappa 1:1 di Taormina con le zone di streaming.
- **Technical Design Document (TDD)**: architettura (sezione 16), pipeline, formati, budget (sezione 17).
- **Audio Design Document**: lista dei suoni ambientali generati dal codice, lista delle scene doppiate, regole del russo parlato.
- **Piano dei dati per Taormina 1:1**: quali fonti (mappe, altimetria, ortofoto, foto) e con quale licenza d'uso.

### Consegne
`docs/GDD.md`, `docs/NARRATIVA.md`, `docs/PERSONAGGI.md`, `docs/ART_BIBLE.md`, `docs/LIVELLI.md`, `docs/TDD.md`, `docs/AUDIO.md`, `docs/DATI_TAORMINA.md`.

### Criteri di uscita
- Ogni capitolo ha una scaletta giocabile approvata da Vlad.
- Ogni sistema ha una specifica scritta (input, regole, stato salvato, UI).
- I budget di prestazioni sono fissati per PC e tablet.

---

## Fase 1 — Pre-produzione tecnica e pipeline

**Obiettivo:** costruire la catena di montaggio. Un asset deve poter passare da Blender al gioco nel browser con un solo comando, sempre uguale.

### Lavori
- **Repository**: struttura (sezione 16), Git LFS per `.blend`, texture sorgente e audio; regole sui nomi; CI che compila e testa a ogni push.
- **Progetto di gioco**: Vite + TypeScript + Babylon.js (versione fissata), WebGPU con ripiego su WebGL2.
- **Pipeline Blender (script Python, headless)**:
  - import dei modelli personaggio da Tripo/Hitem3D → riduzione a ~40.000 triangoli → scheletro → pulizia dei pesi → retarget delle animazioni (Mixamo, Rokoko, Uthana);
  - bake in Cycles: lightmap con rimbalzi (secondo canale UV), mappe HDR dell'ambiente;
  - collisioni come forme semplici con un prefisso di nome riconoscibile;
  - export glTF 2.0 (`.glb`) con compressione geometria (meshopt o Draco) e texture KTX2/Basis.
- **Validatore degli asset**: controlla triangoli, dimensioni delle texture, UV delle lightmap, nomi, scala, origine; blocca l'export se un budget è superato.
- **Pipeline Taormina 1:1**: import di sagome degli edifici e strade da mappe aperte e dell'altimetria in Blender; generazione delle facciate con un kit modulare (vedi Fase 4); suddivisione in celle di streaming.
- **Streaming**: manifesto delle risorse per zona, caricamento e scaricamento per celle, cache nel browser (service worker), schermata di caricamento tra zone lontane.
- **Hosting**: deploy automatico su sito statico con CDN; accesso privato (protezione con password o link non pubblico).
- **Base dei test**: Playwright con Chromium in modalità headless, screenshot di riferimento, misura degli FPS su scena di prova.

### Consegne
- Un oggetto (es. il lapot') e una stanza di prova passano Blender → validatore → `.glb` compresso → Babylon → sito pubblicato, con un comando.
- Un personaggio (la babuška) arriva in gioco con le animazioni.
- Una cella di terreno reale di Taormina caricata e scaricata in streaming.

### Criteri di uscita
- Pipeline ripetibile senza passaggi manuali (a parte la rifinitura artistica di Vlad).
- CI verde: build, validatore, test di base.
- Prestazioni della scena di prova dentro i budget su un PC medio e su un tablet di riferimento.

---

## Fase 2 — Prototipo dei sistemi (First Playable)

**Obiettivo:** tutti i sistemi base funzionanti in ambienti grezzi (greybox), giocabili dall'inizio alla fine di un capitolo finto.

### Sistemi
- **Controller in prima persona**: WASD + mouse, corsa con Maiusc, accovacciarsi (serve per cercare impronte e guardare dietro il frigo); gamepad; touch per tablet (joystick virtuale + trascinamento); comandi rimappabili. Fisica Havok per le collisioni.
- **Interazione**: E / tasto Azione sull'oggetto o la persona inquadrata, evidenziazione degli oggetti interattivi.
- **Dialoghi**: motore a script (es. Ink) con variabili; testo che si scrive man mano; scelte 1–4 o tocco; il personaggio si gira, guarda Vera, parla con l'animazione; cronologia dei dialoghi.
- **Pensieri di Vera**: sottotitoli in corsivo.
- **Sottotitoli dei suoni**: [starnuto], [russare], [la crepa scricchiola], con posizione o direzione.
- **Quaderno di scienze**: 4 sezioni (Indizi, Parole russe, Ricordi, Foto) + Obiettivo + Sospettati e frecce (dal cap. 5) + il Patto (cap. 13) + la pagina «CASA RUSSO» (cap. 14). Pagine che si girano, scrittura a matita animata.
- **Telefono di Vera**: fotocamera (F), torcia, ora e data del calendario.
- **Missioni e stato**: missioni = capitoli, obiettivi, eventi a script, variabili di trama e di rapporto, checkpoint.
- **Fallimento morbido**: breve scena, poi ripartenza dall'ultimo punto sicuro senza perdere progressi.
- **Salvataggio automatico** a checkpoint; «Continua» dal titolo.
- **Calendario e tempo**: data e ora della storia, luce che cambia, notti delle Donne (martedì, giovedì, sabato).
- **Stato della casa**: variabili persistenti per crepa, luce, acqua, limone; collegate a materiali, luci, effetti e suoni.
- **Personaggi non giocanti**: navmesh Recast, routine, teste che seguono Vera con lo sguardo, reazioni «attraverso» gli spiriti.
- **Marker discreto** dell'obiettivo, disattivabile.
- **Menu**: titolo, pausa, opzioni (qualità grafica, sensibilità, inverti asse Y, volume, dimensione sottotitoli, marker, comandi).
- **Strumenti di sviluppo**: console di debug (salta al capitolo, imposta data, imposta stato della casa, mostra navmesh, contatori di prestazioni), che servono anche ai test automatici.

### Criteri di uscita (First Playable)
- Si gioca un capitolo finto in greybox: dialogo con scelta → indizio nel quaderno → foto → scena guidata → checkpoint → fine capitolo.
- Si salva, si ricarica e lo stato (scelte, quaderno, casa, data) è identico.
- Funziona con tastiera e mouse, gamepad e touch su tablet.

---

## Fase 3 — Vertical slice: capitolo 1

**Obiettivo:** il capitolo 1 «La scarpa» alla **qualità finale**. Diventa il metro di misura per tutti gli altri capitoli: se un capitolo futuro è sotto questo livello, non è finito.

### Contenuto (dal documento di gioco, sezione 4)
Intro narrata su schermo nero (doppiata) → attesa agli arrivi con dialoghi a scelta (Irina, Salvo, Giulia, Mattia, il signore) → la porta degli arrivi che si apre e richiude (turisti tedeschi, squadra di pallavolo, prete con la valigia a fiori) → arrivo della babuška → saluti e abbraccio → il lapot' nella borsa a fiori → lo starnuto e gli occhietti gialli, primo piano lento sugli occhi della babuška → parcheggio e monovolume grigia con l'ammaccatura → viaggio verso Taormina seduta dietro, Etna al tramonto → schermo nero: *«Non sapevo ancora che dentro quella scarpa c'era la guerra.»* → scheda di fine capitolo.

### Lavori
- **Ambienti (Blender)**: atrio arrivi, bar dell'aeroporto, parcheggio, interno della monovolume, strada da Catania a Taormina con l'Etna; luce pomeriggio → tramonto calcolata in Cycles; lightmap e HDR.
- **Personaggi**: babuška, Irina, Salvo, Giulia (con telefono), Mattia, comparse dell'aeroporto; animazioni nuove (carrello spinto, abbraccio, i tre baci, Mattia che saltella, colpetti alla borsa, seduti in auto).
- **Fomà (solo occhietti)**: gli occhi gialli nel buio della scarpa; il lapot' con fibre di corteccia realistiche.
- **Grafica Babylon**: PBR, tone mapping ACES, bloom, antialiasing, profondità di campo nei primi piani, SSAO, riflessi sul pavimento lucido (SSR), ombre a cascata, polvere nella luce, fumo dell'Etna, grana e vignettatura leggere.
- **Audio**: brusio, annunci, porta scorrevole, carrello, starnuto, brontolio in russo, sospiro, motore, cicale (generati dal codice); doppiaggio dell'intro e di «Veročka… Hai gli occhi di tuo nonno.», «Le scarpe non starnutiscono, Veročka.»
- **Quaderno**: tutti i contenuti del capitolo 1 (indizi, parole russe, ricordi, foto) con le illustrazioni (ricordo del nonno Kolja).
- **Test**: giro completo automatico del capitolo, screenshot di riferimento delle inquadrature chiave, misura delle prestazioni.

### Criteri di uscita
- Il capitolo dura 15–20 minuti, è fedele al libro e non ha segnaposto.
- Prestazioni dentro budget su PC medio e tablet di riferimento.
- Vlad lo approva come **riferimento di qualità** per il resto del gioco.
- Retrospettiva: si misura quanto lavoro è servito e si aggiorna la stima delle fasi successive.

---

## Fase 4 — Produzione v1.0: capitoli 2–3 e Taormina alta

**Obiettivo:** produrre i contenuti della v1.0 sopra la base della vertical slice.

### Mondo
- **Casa Russo**: due piani, cucina con il frigorifero che ronza (e lo spazio dietro), stanza della babuška (ex studio), camere di Vera, Giulia e Mattia, ingresso con la serratura antica dal buco grande, scale col 9° gradino, cortile col limone, balcone con il mare tra i tetti e l'Etna.
- **Scalinate**: gradini consumati, gerani, gatti che dormono dove metti il piede (incluso il gatto rosso del quarto gradino); casa di nonna Concetta due scalinate più su (pizzi, centrini, santi, foto di nonno Turi col lumino).
- **Corso Umberto 1:1**: bar di papà con il tavolino in fondo vicino al bagno, negozi, piazze, Porta Messina. Kit modulare di facciate (intonaci, persiane, balconi in ferro battuto, insegne, portoni) applicato alle sagome reali; edifici simbolo fatti a mano.
- **Scuola media**: classe di Vera, banco con Nicolò, la prof di matematica, il prof di musica.

### Capitoli
- **Cap. 2 — Il vecchietto dietro il frigorifero**: arrivo a casa, nonna Concetta con gli arancini contro i pirožki della babuška, cena; la notte, scena guidata: Vera segue la babuška, il rito «Nonnino, nonnino, vieni con noi» (in russo, sottotitolato), Fomà esce dalla scarpa per la prima volta.
- **Cap. 3 — Le signore di fuori**: quattro giorni giocabili (scuola, bar, casa, la barba sotto il frigo di martedì: «Non ci sono.»), poi giovedì notte: profumo di rosmarino, le Donne che entrano dal buco della serratura, lo scontro con Fomà, lo starnuto di Vera, «Vera Russo. Figlia di Salvatore. Vieni qui.»

### Personaggi nuovi
- **Fomà completo**: alto come una bottiglia da 1,5 L, peloso come un gatto vecchio, barba fino ai piedi trascinata come uno strascico, camicia rossa con cintura di corda, naso rosso. Pelo e barba fatti in Blender e portati in gioco con tecniche adatte al browser (vedi sezione 16). Animazioni: uscire dalla scarpa, annusare, strisciare dietro il frigo, arrabbiarsi, saltare sul lapot'.
- **Donne di Fora**: Rosalia (vino, ventaglio, pettine di tartaruga), Nina (verde, perle), Tina (celeste, capelli sciolti). Effetto di entrata dal buco della serratura, formazione dal basso, gonne di nebbia, braccialetti che tintinnano, profumo reso con particelle e suono.
- **Nonna Concetta**, **Nicolò**, insegnanti, abitanti della scalinata, comparse del Corso.

### Mondo libero (prima versione)
- Calendario attivo dal 13 al 18 settembre.
- Attività: aiutare al bar di papà (caffè, granite, cornetti, clienti con battute), prime missioni secondarie, segreti di casa, album e collezioni.

### Criteri di uscita (Content Complete v1.0)
- Capitoli 1–3 giocabili dall'inizio alla fine, nessun segnaposto.
- Tutte le zone della v1.0 esplorabili in streaming senza interruzioni.
- Tutti i dialoghi e i testi scritti e inseriti.

---

## Fase 5 — Alpha, Beta e lancio v1.0

| Traguardo | Significato | Criteri |
|---|---|---|
| **Alpha** | Tutto c'è, niente è rifinito | Tutte le funzioni e i contenuti della v1.0 presenti; bug noti catalogati |
| **Beta** | Tutto c'è ed è rifinito | Nessun bug bloccante; prestazioni dentro budget; rifinitura grafica e audio completata |
| **Release Candidate** | Pronto salvo sorprese | Giro completo automatico verde; Vlad gioca dall'inizio alla fine senza intoppi su PC e tablet |
| **Gold v1.0** | Pubblicato | Deploy sul sito, salvataggi stabili, versione taggata |

### Lavori
- Rifinitura: luci, materiali, animazioni, transizioni, ritmo dei dialoghi.
- Ottimizzazione: livelli di dettaglio, occlusione, compressione, preset di qualità automatici (Basso/Medio/Alto/Ultra) per PC e tablet.
- Test: Vlad gioca ogni capitolo; test automatici a ogni modifica; prove su diversi browser (Chrome, Edge, Safari su iPad, Firefox).
- **Compatibilità dei salvataggi**: i salvataggi della v1.0 devono funzionare nella v2.0 e nella v3.0 (salvataggi con numero di versione e migrazione).

---

## Fase 6 — v2.0: capitoli 4–8

**Obiettivo:** dalla guerra delle tazzine al consiglio di mezzanotte. Entra la Taormina monumentale.

### Mondo
- Teatro Antico, Villa Comunale, belvedere sull'Etna, Duomo e piazze, negozio di prodotti dell'Est. Ricostruzione 1:1 con edifici simbolo fatti a mano.
- Meteo e luce di ottobre: giornate più corte, ancora caldo (26 gradi al Pokrov).

### Capitoli
- **Cap. 4 — La guerra delle tazzine**: la notte delle tre domande di Donna Rosalia; poi l'**indagine giorno per giorno**: moka sparita, kefir cagliato, lenzuola annodate dal limone alla finestra del bagno, calze sinistre sparite, tazzine a testa in giù nella vetrinetta chiusa, pane nero ammuffito, moka piena di sale. Ogni giorno una prova da trovare (luccichio dietro il frigo, frasi delle Donne sentite di notte). Cena con Mattia: «Il signore dice che sono state le signore.»
- **Cap. 5 — Due nonne che non sanno niente**: il quaderno diventa da investigatrice (sospettati, indizi, frecce); Vera accompagna nonna Concetta e la spia dietro il vaso di gerani (rito del rosmarino, tre biscotti, rosolio); torna e trova la babuška con la candela davanti al frigo; pranzo della domenica: boršč contro parmigiana.
- **Cap. 6 — Pokrov**: pomeriggio al bar di papà (compiti al tavolino in fondo), la babuška col cappotto sul balcone, il racconto del Pokrov; di notte Fomà sul lavandino, la candela per il Pokrov, «Brava, Veročka.»
- **Cap. 7 — La casa tossisce**: il sistema **casa malata** entra in pieno (crepa che cresce dal 9° gradino, luce che salta, acqua che sa di ferro, casse d'acqua portate su per la scalinata, il limone che perde le foglie); il litigio di mamma e papà ascoltato dalle scale; Giulia arrabbiata e spaventata.
- **Cap. 8 — Il consiglio di mezzanotte**: Vera prepara il tavolo (tovaglia della domenica, biscotti e acqua da un lato, pane, sale e latte dall'altro, la candela del Pokrov, il foglio per il trattato); dialogo a più voci con la **barra della tensione della casa**; la casa reagisce (ante, lampadina, frigo, crepa) fino all'urlo «Di chi sono io?»; le parole di Donna Rosalia e il silenzio di Fomà.

### Sistemi nuovi
- Indagine con prove e sospettati collegabili nel quaderno.
- Barra della tensione della casa e reazioni dinamiche dell'ambiente.
- Rituali di casa (pane e sale, latte, rosmarino, candela) che cambiano piccole cose nell'esplorazione libera.

### Criteri di uscita
Gli stessi della Fase 5 (Alpha → Beta → RC → Gold v2.0), più: un salvataggio della v1.0 prosegue senza errori nella v2.0.

---

## Fase 7 — v3.0: capitoli 9–14, libro completo

**Obiettivo:** dalla scarpa vuota fino a «Solo per un po'». Entra la costa. Alla fine il libro 1 è giocabile tutto.

### Mondo
- **Funivia** Taormina–Mazzarò giocabile (cabina rossa, turisti tedeschi, vista sul mare, ulivi, fichi d'India, ville con piscina).
- **Mazzarò, Isola Bella**, strada lungo il mare verso Giardini.
- **Stazione di Taormina-Giardini** 1:1: pavimenti di marmo, panchine di legno, colonnine di ferro verdi, lampioni antichi, il mare oltre i binari, il cartellone degli orari (treno delle 17:42 per Messina), il treno merci.
- Meteo di novembre: il primo temporale del 4 novembre, scalinate bagnate e lucide, gatti sotto i portoni.

### Capitoli
- **Cap. 9 — La scarpa vuota**: Fomà sparito; ricerca in tutta la casa con la torcia del telefono; la casa peggiora di colpo (acqua marrone, intonaco caduto sul 9° gradino); la babuška con la febbre, il dottore; la giornata accanto al suo letto; la ricerca fuori casa; Mattia sul balcone: «So da che parte è andato.»
- **Cap. 10 — Il fratello che quasi vede**: le **impronte di farina** (Mattia indica, Vera cerca), giù per la scalinata, attraverso il Corso evitando il bar di papà, Porta Messina, funivia, Mazzarò, la strada lungo il mare; Giulia che li raggiunge e li segue.
- **Cap. 11 — Il treno per il nord**: Fomà seduto sul lapot' in fondo al binario; il dialogo sulla panchina («Io sono sempre un po' forestiera»); le due condizioni di Fomà; il rito in russo detto da Vera; la vocina che Giulia fa finta di non aver sentito; il ritorno mano nella mano.
- **Cap. 12 — Donne di fuori**: lunedì a scuola e al bar a preparare i discorsi; la cena con nonna Concetta («Da fuori dove?» «Da Catania.»); martedì: le **pulizie a minigiochi**; mezzanotte: la domanda «Perché vi chiamate Donne di Fora?», il racconto di Donna Tina, il sorriso di Donna Rosalia.
- **Cap. 13 — La notte dei Morti**: la babuška che fa il pane col cumino; la notte: le due nonne beccate ognuna con la sua offerta, la risata; le Donne e Fomà; il **patto** scritto nel quaderno (firma di nebbia che profuma di rosmarino, impronta di farina); la mattina: la casa guarita, il fiore del limone; la **caccia ai cannistri**, il ditale di nonno Turi e il cucchiaio di Kolja da unire.
- **Cap. 14 — Solo per un po'**: il temporale, la cena della decisione («Per l'inverno»), i tre baci a Salvatore, i colpetti al frigo; la pagina «CASA RUSSO» del quaderno; «Non ero divisa. Ero un ponte.»; Mattia e la lettera a Ded Moroz; l'ombra con la scopa sul tetto e la voce in siciliano stretto; Fomà che russa, la nebbia al rosmarino: era martedì.

### Dopo il finale
- Taormina resta esplorabile con la casa guarita, il calendario fermo ai primi di novembre, tutte le collezioni completabili.

### Criteri di uscita
Gli stessi della Fase 5 (Alpha → Beta → RC → Gold v3.0), più: un giro completo del libro dura 3–4 ore di sola trama; un salvataggio della v1.0 arriva fino alla fine del cap. 14.

---

## Fase 8 — Post-lancio e ponte verso il libro 2

- Correzione dei bug segnalati, aggiornamenti di Babylon.js e dei browser.
- Raccolta di ciò che si è imparato (cosa ha funzionato nella pipeline, cosa no) in `docs/RETROSPETTIVA.md`.
- Preparazione del libro 2, *La Befana contro Baba Jaga* (inverno): la stessa Taormina, nuova stagione, nuovi spiriti. L'ombra con la scopa sul tetto del cap. 14 è già l'aggancio.

---

## 14. Piano dei capitoli (missioni)

| Cap. | Titolo | Luoghi | Meccanica principale | Rilascio |
|---|---|---|---|---|
| 1 | La scarpa | Aeroporto, parcheggio, auto | Dialoghi a scelta, scena dello starnuto, viaggio seduta dietro | v1.0 |
| 2 | Il vecchietto dietro il frigorifero | Casa Russo, scalinata | Cena delle due nonne, scena guidata notturna | v1.0 |
| 3 | Le signore di fuori | Scuola, bar, casa | Giorni giocabili, prima apparizione delle Donne | v1.0 |
| 4 | La guerra delle tazzine | Casa, cortile | Indagine giorno per giorno | v2.0 |
| 5 | Due nonne che non sanno niente | Casa di nonna Concetta, scalinata | Quaderno da investigatrice, osservare di nascosto | v2.0 |
| 6 | Pokrov | Bar di papà, balcone, cucina | Racconto, rito della candela | v2.0 |
| 7 | La casa tossisce | Casa, scalinata | Casa malata, ascoltare il litigio | v2.0 |
| 8 | Il consiglio di mezzanotte | Cucina | Barra della tensione della casa | v2.0 |
| 9 | La scarpa vuota | Casa, scalinata, dintorni | Ricerca con la torcia, assistere la babuška | v3.0 |
| 10 | Il fratello che quasi vede | Scalinata, Corso, funivia, Mazzarò | Impronte di farina con Mattia | v3.0 |
| 11 | Il treno per il nord | Stazione Taormina-Giardini | Dialogo con Fomà, rito di invito | v3.0 |
| 12 | Donne di fuori | Scuola, bar, casa | Minigiochi delle pulizie, dialogo con le Donne | v3.0 |
| 13 | La notte dei Morti | Casa | Le due nonne, il patto, caccia ai cannistri | v3.0 |
| 14 | Solo per un po' | Casa, balcone, Taormina sotto la pioggia | Cena della decisione, pagina finale del quaderno | v3.0 |

---

## 15. Calendario della storia

Il libro è coerente con il calendario del **2025** (il 1° novembre 2025 è sabato, il 4 novembre è martedì: «Era martedì.»). Il gioco usa queste date per luce, meteo e notti delle Donne.

| Data | Giorno | Evento |
|---|---|---|
| 13 settembre | sabato | Cap. 1 aeroporto; cap. 2 la prima notte |
| 15–18 settembre | lun–gio | Cap. 3: prima settimana di prima media; martedì la barba sotto il frigo; giovedì notte le Donne |
| fine settembre | — | Cap. 4: la settimana dei dispetti |
| 4–5 ottobre | sab–dom | Cap. 5: investigazione, pranzo boršč e parmigiana |
| 14 ottobre | martedì | Cap. 6: Pokrov |
| 21 ottobre | martedì | Cap. 7: il litigio (la casa malata cresce nei giorni prima e dopo) |
| 23 ottobre | giovedì | Cap. 8: consiglio di mezzanotte |
| 24–25 ottobre | ven–sab | Cap. 9: la scarpa vuota |
| 26 ottobre | domenica | Cap. 10–11: impronte, funivia, stazione |
| 27–28 ottobre | lun–mar | Cap. 12: discorsi, pulizie, mezzanotte con le Donne |
| 1–2 novembre | sab–dom | Cap. 13: notte dei Morti, cannistri |
| 4 novembre | martedì | Cap. 14: primo temporale, «Solo per un po'» |

Notti delle Donne di Fora nel mondo libero: martedì, giovedì e sabato.

---

## 16. Architettura tecnica

### Struttura del repository
```
casarusso/
├── docs/                 documenti di progetto (GDD, TDD, art bible, …)
├── game/                 codice del gioco (Vite + TypeScript + Babylon.js)
│   ├── src/core/         avvio, motore, scene, streaming, salvataggi
│   ├── src/systems/      controller, interazione, dialoghi, quaderno, telefono,
│   │                     missioni, calendario, stato della casa, NPC, audio
│   ├── src/chapters/     uno per capitolo: script, eventi, checkpoint
│   ├── src/ui/           menu, opzioni, quaderno, sottotitoli, HUD
│   └── content/          dialoghi (Ink), testi, dati delle missioni
├── blender/
│   ├── scripts/          pipeline Python (import, decimazione, rig, bake, export)
│   └── sources/          file .blend (Git LFS)
├── assets/               output compressi pronti per il gioco (.glb, .ktx2, .env, audio)
├── tools/                validatore asset, generatore del manifesto, dati di Taormina
└── tests/                Playwright: giri automatici, screenshot, prestazioni
```

### Motore (Babylon.js)
- **Rendering**: WebGPU dove disponibile, WebGL2 altrimenti. PBR, HDR, tone mapping ACES, bloom, FXAA/TAA, profondità di campo, SSAO, SSR, ombre a cascata, volumetria leggera (raggi di luce, nebbia delle Donne).
- **Illuminazione**: architettura con lightmap calcolate in Cycles + mappe d'ambiente HDR da Blender; personaggi e oggetti dinamici con luce in tempo reale e sonde d'ambiente.
- **Fisica**: Havok (collisioni del giocatore, oggetti che si spostano nei dispetti).
- **Percorsi**: navmesh Recast per i personaggi; navmesh per cella di streaming.
- **Fomà**: pelo con tecnica a gusci (shell fur) o ciocche su superfici (hair cards) generate in Blender dalle curve di pelo, barba con simulazione semplice a catena di ossa.
- **Donne di Fora**: particelle GPU + materiali a nodi (Node Material) per la nebbia, dissolvenza dal basso verso l'alto, distorsione leggera.
- **Streaming**: il mondo è diviso in celle; ogni cella ha il suo `.glb`, le lightmap e la navmesh; un manifesto dice cosa caricare in base alla posizione; livelli di dettaglio per gli edifici lontani; la casa e i luoghi chiave restano in memoria.

### Narrativa e stato
- Dialoghi e scelte in **Ink** (con inkjs): variabili di rapporto (es. Giulia alleata), flag di trama, testi delle comparse che cambiano.
- Un solo stato di gioco serializzabile (JSON con numero di versione): capitolo, checkpoint, data e ora, scelte, quaderno, collezioni, stato della casa, posizione.
- Salvataggio automatico nel browser (IndexedDB) con copia di sicurezza; esportazione/importazione del salvataggio da file.

### Taormina 1:1
- Fonti: mappe aperte (sagome di edifici, strade, scalinate), modello di elevazione del terreno, ortofoto, foto di riferimento (da verificare le licenze nella Fase 0).
- Blender: terreno dall'altimetria, edifici estrusi dalle sagome, facciate dal kit modulare, edifici simbolo modellati a mano (Teatro Antico, Porta Messina, Duomo, Torre dell'Orologio, Palazzo Corvaja, stazione di Taormina-Giardini, funivia).
- Bake della luce per cella, con l'ora del giorno di riferimento; variazione di ora e meteo con luce dinamica sopra la base calcolata.

### Audio
- Suoni ambientali generati dal codice (Web Audio): brusio, annunci, porte, starnuto, brontolio, sospiro, motore, cicale, frigorifero che ronza, scricchiolii della casa, pioggia, mare, funivia, treno.
- Voci registrate o generate solo per intro e scene chiave, in italiano e in russo; versi brevi per tutti i personaggi.
- Audio posizionale 3D.

---

## 17. Budget di prestazioni

| Voce | PC medio | Tablet di riferimento |
|---|---|---|
| Frequenza | 60 FPS | 30 FPS stabili |
| Risoluzione | nativa, scalabile | dinamica |
| Triangoli visibili | ≤ 3 milioni | ≤ 800 mila |
| Draw call | ≤ 1.500 | ≤ 500 |
| Memoria texture | ≤ 1,5 GB | ≤ 600 MB |
| Personaggio | ~40.000 triangoli | LOD a ~15.000 |
| Fomà | ~40.000 + pelo | pelo semplificato |
| Primo avvio | ≤ 30 s fino al titolo | ≤ 45 s |
| Cambio cella | senza scatti visibili | senza scatti visibili |

Hardware di riferimento e preset di qualità (Basso/Medio/Alto/Ultra) si fissano nella Fase 0; i preset si scelgono da soli al primo avvio e si possono cambiare dalle opzioni.

---

## 18. Qualità e test

- **Vlad**: gioca ogni capitolo a ogni traguardo, su PC e tablet, e segna cosa non va.
- **Test automatici (Playwright)**:
  - giro completo di ogni capitolo con comandi di debug (dialoghi, scelte, checkpoint, fine capitolo);
  - salvataggio e ricaricamento: lo stato deve essere identico;
  - migrazione dei salvataggi tra versioni;
  - screenshot di riferimento delle inquadrature chiave (per accorgersi se qualcosa si rompe);
  - misure di prestazioni sulla scena di prova e sulle celle più pesanti;
  - controllo dei testi (nessuna chiave mancante, nessun refuso nelle parole russe).
- **Validatore degli asset** nella CI: nessun asset fuori budget entra nel gioco.
- **Bug tracking**: gravità (bloccante, grave, minore, estetico) e capitolo di appartenenza.

---

## 19. Rischi principali

| Rischio | Impatto | Contromisura |
|---|---|---|
| Taormina 1:1 è enorme | Tempi lunghi, peso da scaricare | Kit modulare di facciate, edifici generati dalle sagome, solo gli edifici simbolo a mano; streaming per celle; zone aperte per rilascio (v1.0 → v3.0) |
| Pelo e barba di Fomà nel browser | Prestazioni, resa | Prototipo nella Fase 1; gusci o ciocche su superfici invece di fili veri; versione semplificata sul tablet |
| Nebbia delle Donne costosa | Cali di FPS nelle scene notturne | Particelle GPU limitate, risoluzione ridotta degli effetti, test sul tablet già nella Fase 2 |
| Tablet (soprattutto iPad/Safari) | Funzioni WebGPU mancanti, memoria limitata | WebGL2 di riserva, preset dedicato, test su Safari a ogni traguardo |
| Modelli da Tripo/Hitem3D imprecisi | Mani e vestiti che si deformano male | Pulizia dei pesi via script + rifinitura a mano di Vlad |
| «Tutto giocabile in 3D» allunga i capitoli | Si sfora la durata di 3–4 ore | Ogni raccordo ha un tempo massimo nel documento narrativo; si verifica a ogni Beta |
| Salvataggi che si rompono tra versioni | Perdita dei progressi | Salvataggi con versione e migrazione, testati in automatico |
| Licenze dei dati e delle foto di Taormina | Uso non consentito | Verifica delle licenze nella Fase 0; usare solo fonti aperte o foto proprie |

---

## 20. Definition of Done

Un capitolo (o una zona) è **finito** quando:

1. È fedele al libro: eventi, battute, tono (ironico che diventa misterioso), luoghi.
2. Non ha segnaposto: ogni modello, texture, animazione, testo e suono è definitivo.
3. Raggiunge la qualità della vertical slice del capitolo 1.
4. Rispetta i budget di prestazioni su PC medio e tablet di riferimento.
5. Funziona con tastiera e mouse, gamepad e touch; i comandi sono rimappabili.
6. Ha i sottotitoli dei suoni importanti.
7. Salva e ricarica senza perdere nulla, anche partendo da salvataggi di versioni precedenti.
8. Supera tutti i test automatici.
9. Vlad lo ha giocato dall'inizio alla fine e lo ha approvato.
