# Casa Russo — Il domovoj nella scarpa · Documentazione della Fase 0

Documentazione completa per costruire il gioco tratto dal libro 1 della serie *Casa Russo*, dalla pipeline (Fase 1) al libro completo (Fase 7). Lingua dei documenti: italiano; prompt per Nano Banana ed ElevenLabs in inglese con riassunto «In breve».

## Indice

| Documento | In una riga |
|---|---|
| [REGISTRO_DECISIONI.md](REGISTRO_DECISIONI.md) | tutte le decisioni D-01…D-92, i 20 conflitti tra fonti risolti, cosa cambia nel piano |
| [GDD.md](GDD.md) | visione, struttura, 27 sistemi con criteri di accettazione, collezioni, durate, UX, comandi |
| [PERSONAGGI.md](PERSONAGGI.md) | bibbia dei personaggi, animazioni, matrice «chi vede cosa» |
| [NARRATIVA/00_struttura.md](NARRATIVA/00_struttura.md) | capitoli, checkpoint, dizionario delle variabili, regole di tono, di scrittura e del russo |
| [NARRATIVA/cap01.md … cap14.md](NARRATIVA/) | scene SCN-CC-NN con dialoghi, scelte, pensieri, suoni, voci, voci del quaderno |
| [NARRATIVA/raccordi.md](NARRATIVA/raccordi.md) | 26 raccordi giocabili con durata tipica e massima |
| [NARRATIVA/mondo_libero.md](NARRATIVA/mondo_libero.md) | bar, giornate libere, 12 missioni secondarie, notti delle Donne, 16 segreti, collezioni da fotografare, dopo il finale |
| [NARRATIVA/comparse.md](NARRATIVA/comparse.md) | battute delle comparse per luogo e momento |
| [NARRATIVA/parole_russe.md](NARRATIVA/parole_russe.md) | le 37 parole russe da collezionare |
| [LIVELLI.md](LIVELLI.md) | piante quotate, percorsi, punti di scena, luce, griglia di streaming di Taormina |
| [ART_BIBLE.md](ART_BIBLE.md) | stile, palette oraria e mensile, materiali siciliani, texel density, rendering, VFX delle Donne, quaderno, UI, camera |
| [AUDIO.md](AUDIO.md) | suoni generati dal codice, 86 sottotitoli SFX, 230 battute VOX con piano dei crediti, brief per ElevenLabs e Fish Audio, mix |
| [DATI_TAORMINA.md](DATI_TAORMINA.md) | fonti per la ricostruzione 1:1 con licenze e passi di download, precisione, fonti vietate, criteri per Casa Russo |
| [TDD.md](TDD.md) | architettura, interfacce TypeScript, schema del salvataggio, rendering, streaming, formati, validatore, console di debug, hardware e preset, CI, rischi |
| [PIPELINE_ASSET.md](PIPELINE_ASSET.md) | classi di asset, fasce di poligoni, modello di scheda, regole per le immagini, pipeline Blender automatica con render di revisione |
| [RICHIESTE_ASSET/00_come_usare.md](RICHIESTE_ASSET/00_come_usare.md) | guida passo passo per Vlad |
| [RICHIESTE_ASSET/personaggi_v1.md](RICHIESTE_ASSET/personaggi_v1.md) | 42 schede dei personaggi e animali della v1.0 |
| [RICHIESTE_ASSET/oggetti_cap01.md](RICHIESTE_ASSET/oggetti_cap01.md) | 14 schede degli oggetti del cap. 1 + 10 modelli CC0 dal web |
| [CONCEPT/riferimenti_luoghi.md](CONCEPT/riferimenti_luoghi.md) | foto di riferimento con licenza per ogni luogo reale |
| [CONCEPT/prompt_concept.md](CONCEPT/prompt_concept.md) | 14 prompt di concept e key art |
| [CREDITI.md](CREDITI.md) | registro delle licenze e bozza dei crediti finali |
| [DOMANDE_APERTE.md](DOMANDE_APERTE.md) | dubbi rimasti con default applicato e scadenza |
| `../work/indice_libro.md` | indice del libro capitolo per capitolo, battute verbatim, tracciabilità beat → scena |
| `../work/libro.txt` | testo del libro con ID dei paragrafi `CC.NNN` |
| `../work/strumenti/` | script: indice, verifica delle citazioni, estrazione VOX, schede di richiesta, riferimenti |

## Ordine di lettura
1. REGISTRO_DECISIONI → 2. GDD → 3. NARRATIVA/00_struttura e cap01 → 4. PERSONAGGI → 5. LIVELLI → 6. ART_BIBLE → 7. AUDIO → 8. TDD → 9. PIPELINE_ASSET → 10. RICHIESTE_ASSET/00_come_usare → 11. DOMANDE_APERTE.
Per Vlad, il minimo indispensabile: questo README, `DOMANDE_APERTE.md`, `RICHIESTE_ASSET/00_come_usare.md`.

## Convenzioni degli ID
| Prefisso | Cosa | Esempio |
|---|---|---|
| D- | decisione | D-47 |
| C- | conflitto tra fonti | C-07 |
| SCN-CC-NN | scena | SCN-01-13 |
| DLG-CC-NOME-NN | nodo di dialogo | DLG-01-GIULIA-03 |
| PEN-CC-NN | pensiero di Vera | PEN-01-24 |
| OBJ-CC-NN | obiettivo del quaderno | OBJ-01-02 |
| CP-CC-X | checkpoint | CP-01-B |
| B-CC-NN | beat del libro | B-01-14 |
| IND-, RUS-, RIC-, FOT-, SEG- | voci del quaderno e collezioni | IND-01-04, RUS-06, FOT-GAT-01 |
| VOX-CC-NN | battuta doppiata | VOX-01-17 |
| SFX-NNN | suono con sottotitolo | SFX-001 |
| SYN-NN | generatore di suono | SYN-08 |
| SIS-NN | sistema di gioco | SIS-22 |
| LUO- | luogo | LUO-CR-CUC |
| PG- | personaggio | PG-FOMA |
| ANI- | animazione | ANI-FOM-12 |
| REQ-CHR-, REQ-PRP-, WEB- | richieste di asset | REQ-PRP-001 |
| CON-NN | concept | CON-06 |
| MIS-S-NN | missione secondaria | MIS-S-03 |
| RAC-NN | raccordo | RAC-15 |
| Q- | domanda aperta | Q-04 |
| R- | rischio | R-04 |
| Variabili | `rap_`, `flag_`, `casa_`, `val_`, `col_` | `flag_giulia_ginevra` |
| `§CC.NNN` | paragrafo del libro in `work/libro.txt` | §01.044 |

## Come tenere aggiornati i documenti
- **Una decisione nuova** si scrive prima in `REGISTRO_DECISIONI.md` (nuovo D-NN, mai riusare un numero) e poi nei documenti toccati, citandone l'ID.
- **Un dubbio** va in `DOMANDE_APERTE.md` con un default; quando Vlad risponde, la riga diventa una decisione e si cancella dalla tabella.
- **Testi del gioco**: ogni riga resta marcata `[LIBRO §…]` o `[NUOVO]`; dopo ogni modifica si eseguono `python3 work/strumenti/verifica_libro.py` (citazioni) e `python3 work/strumenti/estrai_vox.py` (battute doppiate e crediti).
- **Asset**: ogni asset esterno entra in `CREDITI.md` nello stesso commit in cui entra nel repository.
- A ogni chiusura di fase si aggiorna la tabella del gate qui sotto e `FASI_DI_SVILUPPO.md` secondo `REGISTRO_DECISIONI.md` §5.

## Gate della Fase 0

| Criterio | Stato | Evidenza |
|---|---|---|
| Ogni capitolo ha una scaletta giocabile | ✅ | `NARRATIVA/cap01–14.md`: 120 scene, tracciabilità beat → scena 131/131 (`work/indice_libro.md`) |
| …approvata da Vlad | ❌ | in attesa della lettura di Vlad (è l'unico passo che non posso fare io) |
| Ogni sistema ha una specifica scritta (input, regole, stato salvato, UI) | ✅ | `GDD.md` §3: 27 sistemi con il modello fisso e criteri verificabili |
| Budget di prestazioni fissati per PC e tablet | ✅ | `TDD.md` §12 (hardware di riferimento, budget, preset, scelta automatica) |
| Ogni beat dei 14 capitoli mappato a una scena | ✅ | 131/131 |
| Ogni citazione [LIBRO] uguale al manoscritto | ✅ | `verifica_libro.py`: 0 errori |
| Date e giorni coerenti con libro e calendario 2025 (verificati con codice) | ✅ | `work/indice_libro.md` |
| Durata 3–4 ore; ogni raccordo con durata massima | ✅ | 227 min (`GDD.md` §5); `raccordi.md` |
| Ogni sistema con criteri di accettazione e campi salvati | ✅ | `GDD.md` §3, `TDD.md` §4 |
| Ogni variabile Ink definita una volta in `00_struttura.md` | ✅ | controllo automatico (vedi relazione di autoverifica) |
| Ogni battuta doppiata ha un VOX in `AUDIO.md`; ogni suono importante ha un SFX | ✅ | `AUDIO.md` §3–§4 |
| Ogni parola russa in `parole_russe.md` | ✅ | 37 voci |
| Ogni personaggio v1.0 e ogni oggetto del cap. 1 ha una scheda con fascia di poligoni | ✅ | `RICHIESTE_ASSET/` |
| Ogni fonte esterna con licenza in `CREDITI.md`; nessuna NC/ND/SA usata senza segnalazione | ✅ | OSM (ODbL) segnalato in Q-03 |
| Nessun lavoro manuale di Vlad in Blender previsto da alcun documento | ✅ | controllo automatico |
| Nessuna delle parole vietate dal brief (rinvii, versioni ridotte, lavoro manuale) fuori dalle domande aperte | ✅ | `work/strumenti/autoverifica.py` |
| Solo PC e tablet; budget e preset coerenti tra TDD e ART_BIBLE | ✅ | |
| Ogni documento termina con «Fonti» | ✅ | controllo automatico |
| ID unici | ✅ | controllo automatico |

## Fonti
- `FASI_DI_SVILUPPO.md` (Fase 0, criteri di uscita) e brief della Fase 0.
