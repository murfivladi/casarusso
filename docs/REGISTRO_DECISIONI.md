# Registro delle decisioni

Fonte unica di tutte le decisioni del progetto *Casa Russo — Il domovoj nella scarpa*. Ogni altro documento cita le decisioni con il loro ID.
Priorità delle fonti in caso di conflitto: **1.** risposte di Vlad (anche quelle della pre-sessione, D-31…D-38) · **2.** il libro · **3.** `FASI_DI_SVILUPPO.md` sezioni 2 e 3 · **4.** il documento di gioco originale.

Legenda colonna *Fonte*: **Vlad** = scelta di Vlad · **Libro** = imposta dal testo · **Claude** = default motivato di Claude (confermabile, vedi `DOMANDE_APERTE.md` quando indicato).

---

## 1. Decisioni D-01…D-30 (dalla sessione di domande, `FASI_DI_SVILUPPO.md` §2)

La numerazione D-NN corrisponde al numero # del piano.

| ID | Tema | Decisione | Motivazione | Impatto su | Fonte |
|---|---|---|---|---|---|
| D-01 | Portata | v1.0 = capitoli 1–3; v2.0 = 4–8; v3.0 = 9–14 (libro completo) | Rilasci giocabili e completi a ogni tappa | Fasi 4–7, LIVELLI, TDD streaming | Vlad |
| D-02 | Metodo | Vertical slice del capitolo 1, poi espansione | Il cap. 1 diventa il metro di qualità | Fase 3, Definition of Done | Vlad |
| D-03 | Blender | **Sostituita da D-31** (prima: Claude genera con script, Vlad rifinisce a mano) | — | PIPELINE_ASSET | Vlad |
| D-04 | Hosting | Sito statico con caricamento a streaming, asset compressi. Il fornitore è precisato da D-44 | I capitoli non stanno in un singolo file | TDD §build e hosting | Vlad |
| D-05 | Durata | 3–4 ore di sola trama per il libro intero; precisata da D-65 (227 minuti) | Ritmo da romanzo breve per 10–14 anni | NARRATIVA/00_struttura, GDD §5 | Vlad |
| D-06 | Scelte | Le scelte cambiano rapporti, battute e alcune scene; gli eventi del libro restano quelli | Fedeltà al libro | NARRATIVA (tutte), GDD dialoghi | Vlad |
| D-07 | Fallimento | Morbido: breve scena buffa, ripartenza poco prima, nessuna perdita | Pubblico giovane, nessuna frustrazione | GDD fallimento morbido, ogni capitolo | Vlad |
| D-08 | Raccordi | Tutto giocabile in 3D, anche scuola e giorni che passano | Si *vive* il libro | NARRATIVA/raccordi, LIVELLI | Vlad |
| D-09 | Cap. 2 | Scena guidata: si segue la babuška e si guarda, senza rischio di essere scoperti | Momento di meraviglia, non di stealth | cap02, GDD scene guidate | Vlad |
| D-10 | Cap. 4 | Indagine giorno per giorno, un dispetto al giorno, prove da trovare e mettere nel quaderno | Trasforma la «guerra» in gioco | cap04, GDD indagine | Vlad |
| D-11 | Cap. 8 | Barra della tensione della casa fino a «Di chi sono io?» | Rende visibile l'ansia del capitolo | cap08, GDD tensione | Vlad |
| D-12 | Cap. 10 | Mattia «sente» e indica, Vera si inginocchia e cerca le impronte; funivia giocabile | Fedele al libro, valorizza Mattia | cap10, GDD impronte, LIVELLI funivia | Vlad |
| D-13 | Cap. 12 | Minigiochi rapidi: lenzuola dritte, mollette uguali, scale, rosmarino | Fedele alla condizione delle Donne | cap12, GDD pulizie | Vlad |
| D-14 | Cap. 13 | Caccia ai cannistri nascosti; ditale e cucchiaio da unire a mano | Chiusura tattile del tema «ponte» | cap13, GDD cannistri | Vlad |
| D-15 | Casa malata | Stato persistente: crepa, luce, acqua, limone peggiorano anche in esplorazione libera fino alla guarigione | Il mondo ricorda la storia | GDD stato della casa, TDD salvataggio | Vlad |
| D-16 | Orientamento | Obiettivo nel quaderno + marker discreto, disattivabile | Autonomia senza perdersi | GDD missioni, opzioni | Vlad |
| D-17 | Zone | Tutte: Casa Russo e scalinate, Corso Umberto, Taormina monumentale, la costa | Mondo aperto completo a v3.0 | LIVELLI, DATI_TAORMINA | Vlad |
| D-18 | Fedeltà | Taormina fedele 1:1 (mappe, altimetria, foto) | Luogo reale come personaggio | DATI_TAORMINA, PIPELINE_ASSET | Vlad |
| D-19 | Attività | Bar di papà, missioni secondarie, segreti di casa, album e collezioni | Contenuto tra i capitoli | mondo_libero, GDD | Vlad |
| D-20 | Tempo | Calendario del libro (2025); martedì, giovedì e sabato notte arrivano le Donne | Coerenza con il libro | GDD calendario | Vlad |
| D-21 | Fomà | Come in copertina (quasi gattesco, naso rosso, camicia rossa), realistico con pelo e barba; occhi precisati da D-47 | Identità visiva del libro | PERSONAGGI, ART_BIBLE, RICHIESTE | Vlad |
| D-22 | Donne di Fora | Nebbia luminosa dal buco della serratura, forma dal basso, semitrasparenti, particelle | Fedele al libro (03.020–03.021) | ART_BIBLE VFX, TDD | Vlad |
| D-23 | Voci | Doppiate solo l'intro e le scene chiave; altrove testo + versi brevi. Strumenti: D-34, D-43 | Budget e coerenza | AUDIO | Vlad |
| D-24 | Chi vede cosa | Gli adulti guardano «attraverso» gli spiriti e spiegano in modo normale; Mattia sente e vede le tracce | Fedele al libro | PERSONAGGI matrice, GDD NPC | Vlad |
| D-25 | Diario | Il quaderno di scienze di Vera (cellule e fotosintesi, poi sospettati, frecce, patto, pagina CASA RUSSO). Stile: D-41 | Oggetto del libro | GDD quaderno, ART_BIBLE | Vlad |
| D-26 | Foto | Il telefono di Vera: fotocamera, torcia, orologio e data | Oggetto del libro (09.001, 10.025) | GDD telefono | Vlad |
| D-27 | Dispositivi | PC e tablet; telefoni esclusi. Riferimenti: D-46 | Controllo e leggibilità | TDD preset, GDD comandi | Vlad |
| D-28 | Accessibilità | Sottotitoli dei suoni + comandi rimappabili + gamepad | Inclusività | GDD, AUDIO | Vlad |
| D-29 | Test | Vlad prova a mano + test automatici Playwright | Qualità ripetibile | TDD test | Vlad |
| D-30 | Russo | Frasi russe del libro in russo con sottotitolo italiano; parole russe da collezionare. Precisata da D-48 e D-53 | Il russo è metà di Vera | parole_russe, AUDIO | Vlad |

## 2. Decisioni D-31…D-38 (pre-sessione con Vlad)

| ID | Tema | Decisione | Motivazione | Impatto su | Fonte |
|---|---|---|---|---|---|
| D-31 | Blender | **Claude fa tutto in Blender con script Python headless** (modellazione procedurale, retopologia/decimazione, UV, bake, rigging, pesi, retarget, illuminazione, export). Vlad fornisce solo immagini generate, modelli 3D ottenuti da immagine e i modelli scaricati dal web che Claude gli indica. Al posto della rifinitura manuale: **controllo qualità automatico** (controlli via script + render di revisione che Claude ispeziona) | Pipeline ripetibile senza lavoro manuale di Vlad | PIPELINE_ASSET, TDD, rischi, DoD, gate di fase | Vlad |
| D-32 | Immagine → 3D | Schede di richiesta con prompt Nano Banana; Vlad genera immagini e modello in Tripo o Hitem3D con fascia poligoni **1,5 M / 1,0 M / 0,5 M** indicata e motivata; Claude ritopologizza/decima e fa il bake normal, AO, curvatura | Sorgenti high-poly omogenee | PIPELINE_ASSET, RICHIESTE_ASSET | Vlad |
| D-33 | Modelli dal web | Ammessi solo CC0 e CC-BY (crediti obbligatori per CC-BY); niente NC, ND, SA, «editorial» senza segnalazione in `DOMANDE_APERTE.md`; tutto in `CREDITI.md` | Licenze pulite | CREDITI, PIPELINE_ASSET | Vlad |
| D-34 | Voci | Voci dell'intro e delle scene chiave (italiano e russo) progettate con ElevenLabs; in Fase 0 solo brief e liste. Esteso da D-43 (Fish Audio) | Qualità vocale | AUDIO | Vlad |
| D-35 | Hardware | Claude sceglie PC medio, tablet di riferimento e minimo, con preset e regole di scelta automatica. Esito: D-46, D-71 | Budget verificabili | TDD | Vlad |
| D-36 | Concept | Due forme: foto reali con licenza aperta dei luoghi reali + prompt Nano Banana per ciò che va disegnato | Fedeltà + design | CONCEPT/ | Vlad |
| D-37 | Documenti | File Markdown in `docs/` del repository `casarusso/` | Versionabili | Tutti | Vlad |
| D-38 | Autonomia | Un solo giro di domande, poi lavoro fino alla fine; i dubbi successivi hanno un default e una voce in `DOMANDE_APERTE.md` | Ritmo di lavoro | DOMANDE_APERTE | Vlad |

## 3. Decisioni dalla sessione di Fase 0 (D-39…)

| ID | Tema | Decisione | Motivazione | Impatto su | Fonte |
|---|---|---|---|---|---|
| D-39 | Modelli esistenti | I 5 modelli «Pronti (A-pose)» del documento di gioco (babuška, Irina, Salvo, Giulia, Mattia) **si rigenerano tutti** con il protocollo D-32; i vecchi restano solo come confronto | Qualità e proporzioni uniformi | RICHIESTE_ASSET/personaggi_v1 | Vlad |
| D-40 | Titolo | Titolo **«Casa Russo»**, sottotitolo **«Il domovoj nella scarpa»** | Il marchio della serie in primo piano, pronto per i libri 2–4 | GDD UX, ART_BIBLE UI, CREDITI | Vlad |
| D-41 | Quaderno | Illustrazioni e scritte del quaderno in **biro blu + matita grafite** | Quaderno di scuola vero | ART_BIBLE §quaderno, CONCEPT | Vlad |
| D-42 | Narratrice | Intro e frasi finali dei capitoli narrate da **Vera a 13–14 anni** che racconta mesi dopo | Coerente con il libro (11.064 «Molto tempo dopo, mesi dopo») e vicina al pubblico | AUDIO voce VOX-NAR, PERSONAGGI | Vlad |
| D-43 | Strumenti voce | **ElevenLabs piano gratuito** (circa 10.000 crediti al mese, uso non commerciale con attribuzione) + **Fish Audio** come secondo strumento per le battute che non entrano nel budget mensile o rendono meglio lì. Claude fornisce testi, brief e criteri di scelta della voce per entrambi | Budget a costo zero; uso privato compatibile | AUDIO, CREDITI | Vlad |
| D-44 | Hosting | **Hosting proprio di Vlad, senza protezione**: indirizzo non pubblicizzato, `noindex` e `robots.txt` che escludono i motori di ricerca; HTTPS obbligatorio (WebGPU e service worker lo richiedono) | Scelta di Vlad | TDD build e deploy | Vlad |
| D-45 | Casa Russo nella Taormina reale | Zona: **lato monte del Corso Umberto, settore ovest tra Porta Catania e Piazza IX Aprile**, dentro una scalinata che sale verso Via Circonvallazione; nonna Concetta due scalinate più su. Il punto esatto lo fissa in Fase 4 uno script di visibilità (DTM + edifici OSM) con i criteri di `DATI_TAORMINA.md` §6 | Vlad ha chiesto di decidere con i dati; il percorso del cap. 10 (Corso → bar → Porta Messina) richiede una casa a ovest del bar | LIVELLI, DATI_TAORMINA | Vlad → Claude |
| D-46 | Hardware di riferimento | **Tablet di riferimento: iPad 11ª generazione (A16), iPadOS 26, Safari** (è il dispositivo di Vlad); **PC medio: classe RTX 3060 / RTX 4060, 6 core, 16 GB, 1920×1080, Chrome/Edge**; **minimo: iPad 10ª gen (A14) e PC con Iris Xe / GTX 1650, 8 GB** | Vedi TDD §12 con fonti | TDD, ART_BIBLE, budget | Claude (con dato di Vlad) |
| D-47 | Occhi di Fomà | **Neri e lucidi** come nel libro (02.025, 03.054 per Rosalia, 11.031); nel cap. 1 nel buio della scarpa si vedono due puntini neri bagnati che catturano la luce calda dell'atrio | Fedeltà al libro | ART_BIBLE, PERSONAGGI, cap01, CONCEPT | Vlad |
| D-48 | Lingua della babuška | **Russo in famiglia** (con Irina, Vera, Mattia, Fomà) con sottotitolo italiano = testo del libro; **italiano con accento** con Salvo, Concetta, il dottore e gli altri. Eccezione: quando il libro dice che parla in italiano (02.006) | Vera: «Io parlo russo con la babuška» (08.040) | NARRATIVA, AUDIO, parole_russe | Vlad |
| D-49 | Cap. 13, Concetta sulle scale | Concetta entra, **sale al piano di sopra a nascondere i cannistri** (saltando il 9° gradino per non svegliare nessuno), poi scende in cucina | Rende coerente 13.017 con la pianta del cap. 3 e prepara la caccia | cap13, LIVELLI Casa Russo | Vlad |
| D-50 | Vetrinetta | Le tazzine col bordo d'oro di Concetta stanno nella **vetrinetta del soggiorno di Casa Russo** | Come la moka, il servizio buono sta da noi; la guerra resta in casa | LIVELLI, cap04 | Vlad |
| D-51 | Voce della Befana | Ombra con la scopa doppiata **in siciliano** (testo [NUOVO]), sottotitolo = frase del libro | Il libro dice «siciliano stretto» | cap14, AUDIO | Vlad |
| D-52 | Negozio di prodotti dell'Est | Vicino al **terminal bus di Via Pirandello** | Raggiungibile a piedi ogni settimana; entra con la v2.0 | LIVELLI, mondo_libero | Vlad |
| D-53 | Traslitterazione | Schema **scientifico italiano** usato dal libro (š, ž, č, šč, ch per х, j per й, ja/ju/ë, ' per ь). Eccezioni lessicali del libro conservate ovunque: **dedushka**, **matrioška / matrioške** | Regola «schema del libro» del brief | parole_russe, tutti i testi | Libro / Claude |
| D-54 | Calendario | Date confermate con codice (vedi `work/indice_libro.md`). Precisazioni: cap. 4 inizia la notte di **giovedì 18/9** (le tre domande), moka sparita **venerdì 19/9**, dispetti **lun 22 – ven 26/9**, cena di Mattia **venerdì 26/9 sera** | Il testo del cap. 4 continua il 3 | NARRATIVA, GDD calendario | Libro / Claude |
| D-55 | Altezza occhi | Vera alta **152 cm**, occhi a **1,41 m**; accovacciata 0,95 m; in ginocchio 0,70 m; seduta in auto 1,08 m dal suolo dell'abitacolo | Media di una dodicenne italiana | GDD controller, ART_BIBLE camera | Claude |
| D-56 | Altezza di Fomà | **32 cm** in piedi (bottiglia PET da 1,5 L ≈ 31–33 cm); barba lunga 38 cm, ne strascicano 8–10 | 02.025 | PERSONAGGI, ART_BIBLE | Libro / Claude |
| D-57 | Mattia e il signore | La scena del libro accade **sempre**: se Vera lo manda, Mattia ci va subito e Vera assiste da vicino; altrimenti Mattia ci va da solo dopo 90 s e Vera la vede da lontano | D-06: gli eventi del libro restano | cap01 | Claude |
| D-58 | Giulia alleata | La risposta «Convenzione di Ginevra» imposta `flag_giulia_ginevra` e `rap_giulia +2`; cambia **il viaggio in auto (SCN-01-15)** (Giulia passa a Vera il telefono per zoomare sull'Etna e la copre davanti a papà), poi la **cena del cap. 2** e la **scena delle scale del cap. 7** | Il documento di gioco chiede che cambi «una scena successiva» | cap01, cap02, cap07 | Claude |
| D-59 | Motore | **Babylon.js 9.x**, versione fissata in Fase 1 sull'ultima patch pubblicata da almeno 14 giorni (oggi la più recente è 9.33.1 del 29/10/2026) | Frame graph v1, clustered lighting, volumetria | TDD | Claude |
| D-60 | Formati | glTF 2.0 `.glb` con **EXT_meshopt_compression** (non Draco) e texture **KTX2** (UASTC per normali e mappe dati, ETC1S per colori di sfondo e lightmap secondo TDD §8) | Decodifica più veloce, comprime anche animazioni | TDD, PIPELINE_ASSET | Claude |
| D-61 | Dialoghi | **Ink + inkjs 2.4.x** | Variabili e scelte native, editor Inky | TDD, NARRATIVA | Claude |
| D-62 | Navigazione | **Navigation Plugin V2** di Babylon (addons, basato su recast-navigation-js) | V1 sarà deprecato | TDD NPC | Claude |
| D-63 | Blender | **Blender 5.2 LTS** in modalità headless; nella CI il modulo `bpy` 5.2.x da PyPI | LTS fino a luglio 2028 | PIPELINE_ASSET | Claude |
| D-64 | Scheletro | Scheletro umanoide unico con nomi compatibili Mixamo, generato da meta-rig Rigify adattato a punti di riferimento rilevati via script; pesi automatici + pulizia via script + controlli di deformazione | Retarget uniforme per tutte le fonti di animazione | PIPELINE_ASSET | Claude |
| D-65 | Durate | Trama totale **227 minuti** (vedi tabella in `NARRATIVA/00_struttura.md`) | Dentro 3–4 ore | NARRATIVA, GDD | Claude |
| D-66 | Mondo libero | Si apre solo dove il libro ha un vuoto di almeno mezza giornata; ogni vuoto offre 1–3 giornate giocabili; il giocatore può andare avanti in qualsiasi momento («Vai a dormire» dal quaderno) | Rispetta il calendario senza allungare a forza | GDD §2, mondo_libero | Claude |
| D-67 | Lingua dell'interfaccia | Solo italiano; il russo resta nelle voci e nelle scritte di gioco, sempre sottotitolato; opzione «mostra traslitterazione» | Pubblico italiano 10–14 | GDD UX | Claude |
| D-68 | Salvataggi | Stato unico JSON versionato in IndexedDB, 3 slot + autosalvataggio + copia di sicurezza; export/import da file; migrazioni in catena | Compatibilità v1→v3 | TDD §4 | Claude |
| D-69 | Collezioni | Insiemi: Parole russe (RUS), Ricordi (RIC), Foto (FOT, con album Luoghi/Gatti/Persone), Segreti di casa (SEG); conteggi in GDD §4 | Varietà senza grind | GDD, mondo_libero | Claude |
| D-70 | Deploy | GitHub Actions: build, test, validatore; deploy con `rsync` su SSH o `lftp` su SFTP verso l'hosting di Vlad | Hosting proprio (D-44) | TDD | Claude |
| D-71 | Preset | Basso/Medio/Alto/Ultra con scelta automatica (classe GPU + prova di 3 s sulla scena del titolo); tablet di riferimento = Medio a 30 FPS | Budget verificabili | TDD §12 | Claude |
| D-72 | Fallimento morbido cap. 1 | Nel parcheggio Mattia scappa verso le macchinine a gettoni / i carrelli; se Vera si allontana troppo o lo perde di vista per 25 s, scenetta buffa e ripartenza | Il documento di gioco: «a volte bisogna andarlo a riprendere» | cap01 | Claude |
| D-73 | Aspetto di Vera | Capelli castano chiaro lunghi fino alle scapole, coda bassa; occhi grigi (10.023); mani con unghie corte, un braccialetto di filo rosso e blu; abiti per stagione in PERSONAGGI | Il libro non descrive Vera; serve per mani, riflessi, foto | PERSONAGGI, ART_BIBLE | Claude |
| D-74 | OpenStreetMap | Dati OSM (licenza **ODbL**, con clausola share-alike sui database) usati come sorgente delle sagome: il gioco è un «lavoro prodotto», attribuzione «© OpenStreetMap contributors» nei crediti | Unica fonte aperta completa; la clausola SA riguarda solo un database derivato pubblico | DATI_TAORMINA, CREDITI, DOMANDE_APERTE Q-03 | Claude |
| D-75 | Foto di riferimento | Foto CC BY-SA e «Attribution» di Wikimedia Commons ammesse **solo come riferimento** (non entrano nel gioco né nelle texture) | D-33 vale per ciò che si distribuisce | CONCEPT, CREDITI | Claude |
| D-76 | Musica | Nessuna musica: solo suoni ambientali generati dal codice e voci | Documento di gioco | AUDIO | Libro/doc. di gioco |
| D-77 | Ricordi illustrati | I Ricordi (nonno Kolja, nonno Turi…) sono disegnati da Vera nel quaderno (stile D-41), animati con tratto che si disegna | Coerenza: tutto il diario è il quaderno | GDD quaderno, ART_BIBLE | Claude |
| D-78 | Orario del cap. 1 | Atterraggio 17:05, porta che si apre alle 17:40, partenza dal parcheggio 18:15, Etna al tramonto sull'A18 alle 19:05–19:15 (tramonto alle 19:13 del 13/9/2025 a Catania) | Il documento di gioco vuole pomeriggio → tramonto; il libro: «un'ora di macchina, traffico» e Concetta alla sera | cap01, ART_BIBLE luce | Claude |
| D-79 | Lingua di Fomà | Fomà parla l'italiano «strano, impastato, con tutte le erre sbagliate» (02.026), con imprecazioni e sbuffi in russo non tradotti dove il libro non li traduce (02.026: «la babuška si rifiutò di tradurmi») | Fedeltà | AUDIO, NARRATIVA | Libro |
| D-80 | Voci dei bambini | Le voci di Mattia (6 anni) e Vera (12) non si doppiano mai con voci clonate di persone reali; si usano solo voci progettate da descrizione o voci di libreria con licenza d'uso | Tutela e licenze | AUDIO | Claude |
| D-81 | Confessione di Giulia | La frase 11.064–11.065 («Molto tempo dopo… Grazie, ragazze.») è narrata da Vera 13–14 anni (VOX-NAR) sopra l'inquadratura di Giulia | È narrazione retrospettiva | cap11, AUDIO | Claude |
| D-82 | Fine della v1.0 | Dopo il cap. 3 la v1.0 lascia esplorare Taormina in una **domenica 14 settembre ripetibile** (ora scelta dal telefono); con la v2.0 lo stesso salvataggio riprende dal cap. 4 | Evita di anticipare eventi del cap. 4 | GDD §2, mondo_libero, TDD migrazioni | Claude |
| D-83 | Starnuto del cap. 1 | La scelta del documento di gioco «dirlo / guardarla in silenzio» cambia il *modo*: in entrambi i rami Vera pronuncia la battuta del libro 01.038 (nel ramo silenzioso la babuška si volta sentendosi osservata e Vera la dice colta in flagrante) | D-06 | cap01 | Claude |
| D-84 | Bar del cap. 3 | Il pomeriggio al bar di papà del cap. 3 (nel piano) è un raccordo [NUOVO]: il libro non lo esclude e il cap. 6 lo presenta come abitudine («dove andavo il pomeriggio dopo la scuola») | Abitudine dichiarata in 06.001 | cap03, raccordi | Claude |
| D-85 | Budget texture tablet | Memoria texture tablet abbassata da 600 MB a **450 MB**, memoria complessiva della pagina ≤ 1,3 GB | Safari su iPad chiude le schede sotto pressione di memoria senza preavviso (bug WebKit 300782, 290623) | TDD, ART_BIBLE | Claude |
| D-86 | Ricostruzione 1:1 | Per l'altimetria: DTM LiDAR 1 m della Regione Siciliana (CC BY 4.0) dove copre; TINITALY 10 m (CC BY 4.0) come base continua; Copernicus GLO-30 per il paesaggio lontano (Etna) | Licenze aperte, precisione adeguata | DATI_TAORMINA | Claude |
| D-87 | Scuola media | La scuola di Vera è collocata nel complesso reale della scuola secondaria di primo grado di Via Dietro Cappuccini, ma resa come scuola **senza nome reale** («Scuola media di Taormina»), interni inventati | Fedeltà 1:1 senza usare l'identità di un istituto reale | LIVELLI, DATI_TAORMINA | Claude |
| D-88 | Monovolume | Monovolume grigia **generica** (nessun marchio né modello riconoscibile), proporzioni di una 7 posti europea da 4,6 m | Niente marchi | RICHIESTE_ASSET, ART_BIBLE | Claude |
| D-89 | Posizione di Casa Russo nella scalinata | Casa Russo sta **nella parte alta della scalinata, a 4 gradini dalla strada carrabile** (Via Circonvallazione): l'auto si ferma in cima, il portone è a pochi metri (02.002, 02.005), il gatto dorme sul quarto gradino (02.008); per andare al Corso si scende la scalinata (10.010) | Concilia «casa dentro la scalinata» con «la babuška scese dalla macchina» davanti al portone | LIVELLI, DATI_TAORMINA §6, cap02 | Libro / Claude |
| D-90 | Viaggio in auto | Nel cap. 1 Vera non parla mai alla babuška della borsa durante il viaggio (01.043 «Io non dissi niente»); la scelta del documento di gioco «chiedere della borsa» diventa «chiedere sottovoce a Mattia o a Giulia» | D-06 | cap01 | Claude |
| D-91 | Siciliano della Befana | Testo [NUOVO] «Làida iu? Carbuni iu? E 'u Nannu Ielu, eh? 'U Nannu Ielu! Ora videmu.»; da far verificare a un parlante di Taormina prima del doppiaggio (Q-07) | D-51 | cap14, AUDIO | Claude |
| D-92 | Citazioni del libro nei capitoli 4–14 | Le battute del libro sono indicate per intervallo di paragrafi e importate verbatim da `work/libro.txt` in Fase 2; lo script `work/strumenti/verifica_libro.py` controlla ogni citazione esplicita | Nessun errore di trascrizione | NARRATIVA, TDD strumenti | Claude |

---

## 4. Tabella dei conflitti tra le fonti

| # | Conflitto | Fonti coinvolte | Risoluzione | Decisione |
|---|---|---|---|---|
| C-01 | Occhietti di Fomà «gialli» nel cap. 1 vs occhi «neri e lucidi» | Documento di gioco §4.1.7, FASI Fase 3 ↔ libro 02.025, 11.031 | Neri e lucidi con riflesso caldo | D-47 |
| C-02 | Rifinitura manuale di Vlad in Blender | FASI §2 #3, Fase 1 criteri, rischi ↔ pre-sessione | Tutto automatico con controllo qualità via script e render | D-31 |
| C-03 | Pubblicazione come artifact unico con modelli in base64 | Documento di gioco §7 ↔ FASI §3 | Sito statico a streaming su hosting di Vlad | D-04, D-44 |
| C-04 | Piattaforma «mobile touch» | Documento di gioco §3 ↔ FASI §3 | PC + tablet, telefoni esclusi | D-27 |
| C-05 | Mandare Mattia dal signore «e allora la scena succede davvero» (scena opzionale) vs evento del libro 01.007 | Documento di gioco §4.1.2 ↔ libro, D-06 | La scena accade sempre, cambia il modo | D-57 |
| C-06 | Scelta «guardarla in silenzio» toglierebbe la battuta 01.038 | Documento di gioco §4.1.7 ↔ libro, D-06 | La battuta c'è in entrambi i rami | D-83 |
| C-07 | Concetta «sale le scale» per arrivare in cucina (13.017) vs cucina accanto all'ingresso in fondo alle scale (03.019, 03.048) | libro ↔ libro | Sale per nascondere i cannistri, poi scende | D-49 |
| C-08 | Concetta abita «due scalinate più in là» (02.003) / «più in là» (04.027) vs «più su» (05.008, AP.001) | libro ↔ libro | Due scalinate più su (e quindi anche più in là) | D-45 |
| C-09 | «dedushka» (grafia inglese) nel libro vs schema scientifico (deduška) | libro ↔ brief | Si conserva la grafia del libro | D-53 |
| C-10 | Plan §15 «fine settembre» generico per il cap. 4 | FASI §15 ↔ libro 04.001, 04.010 | Date precise 18–26/9 | D-54 |
| C-11 | Battuta doppiata «Veročka… Hai gli occhi di tuo nonno.» pensata in italiano | FASI Fase 3 ↔ D-48 | Voce in russo, sottotitolo italiano del libro | D-48 |
| C-12 | Tablet: texture ≤ 600 MB | FASI §17 ↔ ricerca su Safari/iPad | 450 MB | D-85 |
| C-13 | «Pulizia dei pesi via script + rifinitura a mano di Vlad» | FASI §19 ↔ D-31 | Pulizia via script + render di deformazione ispezionati da Claude + soglie | D-31 |
| C-14 | Vetrinetta del soggiorno: di quale casa (04.032) | libro ambiguo | Casa Russo | D-50 |
| C-15 | Calendario del mondo libero v1.0 «dal 13 al 18 settembre» vs fine del cap. 3 la notte del 18 | FASI Fase 4 ↔ libro | Domenica 14 ripetibile dopo la fine della v1.0 | D-82 |
| C-16 | «Giulia: si può parlare con lei, risponde con battute sarcastiche» e cap. 1 del libro dove Giulia parla solo con la mamma | Documento di gioco ↔ libro | Le battute di Giulia con Vera sono [NUOVO] e non contraddicono il libro | D-06 |
| C-17 | Babylon «FXAA/TAA» generico | FASI §16 ↔ ricerca (TAA disponibile come post-process e nel frame graph) | TAA su Alto/Ultra, FXAA su Basso/Medio | TDD §7 |
| C-18 | Hosting «es. Vercel» con password | FASI Fase 1 ↔ risposta di Vlad | Hosting proprio, nessuna password | D-44 |
| C-19 | Il documento di gioco prevede «chiedere della borsa» in auto; il libro: «Io non dissi niente» (01.043) | Documento di gioco §4.1.9 ↔ libro | Si chiede sottovoce a Mattia o Giulia, mai alla babuška | D-90 |
| C-20 | «Casa dentro la scalinata» (02.001) ma la babuška «scese dalla macchina» davanti al portone (02.005) | libro ↔ libro | Casa a 4 gradini dalla strada carrabile in cima alla scalinata | D-89 |

## 5. Cosa cambia rispetto a `FASI_DI_SVILUPPO.md` e al documento di gioco (da aggiornare in Fase 1)

| Documento e punto | Testo attuale | Nuovo testo / effetto |
|---|---|---|
| FASI §2 #3 | «Misto: Claude genera con script, Vlad rifinisce a mano» | «Claude fa tutto in Blender con script headless; controllo qualità automatico» (D-31) |
| FASI §2 #4 | «es. Vercel» | «hosting proprio di Vlad, senza protezione, HTTPS» (D-44) |
| FASI §2 #23 | voci generiche | ElevenLabs (gratuito) + Fish Audio (D-43) |
| FASI Fase 0, consegne | `docs/NARRATIVA.md` unico | cartella `docs/NARRATIVA/` con 20 file + RICHIESTE_ASSET, CONCEPT, PIPELINE_ASSET, CREDITI, DOMANDE_APERTE, REGISTRO_DECISIONI, README |
| FASI Fase 1, criteri di uscita | «(a parte la rifinitura artistica di Vlad)» | da togliere; aggiungere «render di revisione generati e ispezionati per ogni asset» |
| FASI Fase 1, hosting | «protezione con password o link non pubblico» | deploy su hosting di Vlad, `noindex` (D-44, D-70) |
| FASI Fase 3, contenuto | «gli occhi gialli nel buio della scarpa» | «due occhietti neri lucidi che catturano la luce» (D-47) |
| FASI Fase 3, audio | doppiaggio di «Veročka… Hai gli occhi di tuo nonno.» | in russo con sottotitolo (D-48) |
| FASI Fase 4, mondo libero | «Calendario attivo dal 13 al 18 settembre» | domenica 14 + pomeriggi 15–18 + domenica 14 ripetibile dopo la fine (D-82) |
| FASI §15 | «fine settembre» | 18 → 26 settembre con giorni precisi (D-54) |
| FASI §17 | tablet 600 MB di texture | 450 MB; aggiunta riga «memoria pagina ≤ 1,3 GB» (D-85); riferimenti hardware (D-46) |
| FASI §19, riga Tripo/Hitem3D | «Pulizia dei pesi via script + rifinitura a mano di Vlad» | «Pulizia dei pesi via script, pose di deformazione renderizzate e controllate da Claude, soglie numeriche; se un modello non passa, nuova scheda di richiesta con correzioni del prompt» |
| FASI §20 DoD | — | aggiungere: «ogni asset ha superato il validatore e i render di revisione» |
| Documento di gioco §3 | «PC e mobile» | PC e tablet |
| Documento di gioco §4.1.7 | occhietti gialli | neri lucidi |
| Documento di gioco §6 | modelli «Pronto» | da rigenerare (D-39) |
| Documento di gioco §7 | artifact base64 | sito statico a streaming |

## Fonti

- `FASI_DI_SVILUPPO.md` e `Il_domovoj_nella_scarpa_documento_di_gioco.md` (allegati di Vlad).
- Manoscritto *Il domovoj nella scarpa* (PDF), citato con gli ID di `work/libro.txt`.
- Risposte di Vlad: `work/risposte_vlad.md`.
- [Babylon.js su npm (@babylonjs/core 9.33.1)](https://www.npmjs.com/package/@babylonjs/core)
- [Annuncio Babylon.js 9.0 — Windows Developer Blog](https://blogs.windows.com/windowsdeveloper/2026/03/26/announcing-babylon-js-9-0)
- [Babylon.js Navigation Plugin V2](https://doc.babylonjs.com/features/featuresDeepDive/crowdNavigation/v2Intro)
- [WebKit Bugzilla 300782 — pagine WebGL ricaricate sotto pressione di memoria](https://bugs.webkit.org/show_bug.cgi?id=300782)
- [WebKit Bugzilla 290623 — crash WebGL su iPad Pro](https://bugs.webkit.org/show_bug.cgi?id=290623)
- [Blender 5.2 LTS rilasciato](https://gamefromscratch.com/blender-5-2-lts-released/)
- [bpy su PyPI](https://pypi.org/project/bpy/)
- [Prezzi ElevenLabs 2026 (piano gratuito)](https://dupple.com/learn/is-elevenlabs-free)
- [Regione Siciliana — inizio lezioni 15 settembre 2025](https://www.regione.sicilia.it/la-regione-informa/anno-scolastico-202526-sicilia-campanella-inizio-lezioni-15-settembre)
- [TINITALY 1.1 — INGV](https://tinitaly.pi.ingv.it/Download_Area1_1.html)
- [DTM LiDAR 1 m Regione Sicilia — INSPIRE Geoportal (CC BY 4.0)](https://inspire-geoportal.ec.europa.eu/srv/api/records/m_amte:299FN3:8740c0d0-8f32-4e85-9856-42f8b88853da)
