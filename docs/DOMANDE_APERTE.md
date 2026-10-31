# Domande aperte

Ogni dubbio rimasto dopo il giro unico di domande (D-38). Per ognuno è già applicato un **default** nei documenti: il lavoro può proseguire. Vlad conferma o cambia entro la fase indicata.

| ID | Domanda | Default applicato | Impatto | Da confermare entro |
|---|---|---|---|---|
| Q-01 | Punto esatto di Casa Russo nella Taormina reale | settore ovest, lato monte del Corso, a 4 gradini da Via Circonvallazione; scelta finale dallo script di visibilità con i criteri di `DATI_TAORMINA.md` §6 (D-45, D-89) | LIVELLI, celle di streaming | Fase 4 (Claude manda a Vlad la vista dal balcone per approvazione) |
| Q-02 | Licenza delle ortofoto SITR 2012–2013 | usate solo come riferimento interno, mai come texture | DATI_TAORMINA, CREDITI | Fase 4 (se CC BY, si possono usare anche per i tetti lontani) |
| Q-03 | OSM è ODbL (clausola share-alike sui database) | ammesso: il gioco è un «lavoro prodotto»; nessun database derivato viene pubblicato (D-74) | DATI_TAORMINA | Fase 1 |
| Q-04 | Tipo di hosting di Vlad: Apache o Nginx? Accesso SSH o solo SFTP/FTP? Dominio/sottocartella? | forniti entrambi i file di configurazione; deploy con `rsync` su SSH, alternativa `lftp` su SFTP (TDD §13) | deploy automatico | **Fase 1** (bloccante per il deploy) |
| Q-05 | Piano e termini d'uso di Fish Audio al momento della generazione | piano gratuito, uso privato; si usa solo se il budget ElevenLabs del mese non basta | AUDIO, CREDITI | Fase 4 |
| Q-06 | Chi rivede le frasi russe prima del doppiaggio? | traduzioni di Claude (D-48); revisione da parte di un madrelingua scelto da Vlad (o Irina-tipo di famiglia) | AUDIO, parole_russe | Fase 3 (battute del cap. 1) |
| Q-07 | Chi verifica il siciliano della Befana (D-91) e le battute dialettali dei clienti? | testo di Claude; verifica di un parlante di Taormina | cap14, comparse | Fase 7 (cap. 14); Fase 4 per i clienti del bar |
| Q-08 | Foto degli esterni della scuola di Via Dietro Cappuccini | Vlad fa 6 foto da via pubblica (CONCEPT §6); senza foto si usa Mapillary | LIVELLI, scuola | Fase 4 |
| Q-09 | L'interfaccia di Hitem3D/Tripo permette esattamente 1,5 / 1,0 / 0,5 M facce? | si usa il valore più vicino superiore e si annota in `NOTE.txt` | PIPELINE | alla prima scheda (Fase 1) |
| Q-10 | Pipeline di rendering: Frame Graph v1 di Babylon 9 o pipeline classiche? | Frame Graph con ripiego per singola funzione; decisione con misure nella scena di prova (TDD §7) | TDD | Fase 1 |
| Q-11 | Uso di asset Fab con «licenza standard Fab» (non CC) | esclusi; solo CC0/CC BY | PIPELINE, CREDITI | Fase 3 (se servisse un asset solo Fab) |
| Q-12 | Aspetto di Vera (il libro non lo descrive): capelli castano chiaro, coda, occhi grigi, braccialetto rosso e blu | D-73 | personaggi, mani in prima persona | Fase 3 (prima della scheda REQ-CHR-001) |
| Q-13 | Durate dei capitoli (227 min totali) | tabella `GDD.md` §5.1 | ritmo | Fase 3 (si misura il cap. 1) |
| Q-14 | Nome del bar di papà sull'insegna | «Bar Russo — dal 1978» [NUOVO] (aperto da nonno Turi) | LIVELLI, bar | Fase 4 |
| Q-15 | Volo della babuška da Istanbul (realismo dei collegamenti Russia–Italia nel 2025) | tabellone «Volo da Istanbul» e pensiero di Vera (SCN-01-07) | cap. 1 | Fase 3 |
| Q-16 | Grafia «dedushka»/«matrioška» del libro invece dello schema scientifico | si conserva quella del libro ovunque (D-53) | testi | Fase 2 |
| Q-17 | Il font Caveat Brush non è garantito per il cirillico | Caveat Brush solo per titoli in alfabeto latino; Caveat (con cirillico) per il resto | ART_BIBLE, quaderno | Fase 2 |
| Q-18 | Piano gratuito di Uthana e licenza delle clip Rokoko | si usano Mixamo e animazione procedurale come base; Uthana/Rokoko solo dopo verifica della licenza | PIPELINE, CREDITI | Fase 1 |
| Q-19 | Colore delle cabine della funivia | rosso come nel libro (10.018), anche se le cabine reali cambiassero | LIVELLI | Fase 7 |
| Q-20 | Testo del pensiero sul volo e sulla politica (nessun riferimento esplicito alla guerra) | solo «Dalla Russia non ci sono più voli diretti», nessun altro commento | tono | Fase 3 |
| Q-21 | Risorse hardware per i bake Cycles (GPU) | job manuale su una macchina con GPU (cloud o PC di Vlad); stesso script della CI | TDD, PIPELINE | Fase 1 |
| Q-22 | I modelli «pronti» del vecchio documento di gioco servono come confronto? | si conservano in `assets_in/archivio/` se Vlad li allega; non entrano nel gioco (D-39) | — | Fase 3 |

## Fonti
- `REGISTRO_DECISIONI.md`; `work/risposte_vlad.md`.
