# Narrativa — Struttura, variabili e regole

Questo file fissa la struttura dei 14 capitoli, il **dizionario delle variabili** (unica definizione di ogni variabile Ink), il modello dei rapporti, le regole di tono e di scrittura. I file `cap01.md … cap14.md` contengono le scene.

## 1. Convenzioni di scrittura delle scene

- **ID**: scene `SCN-CC-NN`; nodi di dialogo `DLG-CC-NOME-NN`; pensieri `PEN-CC-NN`; obiettivi `OBJ-CC-NN`; checkpoint `CP-CC-X`; voci del quaderno `IND-CC-NN` (indizi), `RUS-NN` (parole russe, numerazione unica, vedi `parole_russe.md`), `RIC-NN` (ricordi), `FOT-CC-NN` (foto di trama), `SEG-NN`; suoni sottotitolati `SFX-NNN` (catalogo in `AUDIO.md` §3); battute doppiate `VOX-CC-NN` (elenco in `AUDIO.md` §4).
- **Marcatori del testo**: `[LIBRO §CC.NNN]` = verbatim dal libro, paragrafo indicato · `[NUOVO]` = testo scritto per il gioco · `[VOCE]` = doppiato (con ID VOX) · `[RU]` battuta pronunciata in russo (sottotitolo = testo italiano indicato) · `[SCN]` in siciliano.
- **Citazione per ID**: per i capitoli 1–3 le battute [LIBRO] sono riportate per esteso. Per i capitoli 4–14, i blocchi di dialogo del libro sono indicati con l'intervallo di paragrafi (es. `[LIBRO §04.010–04.021]`); in Fase 2 lo strumento `tools/ink-import` copia quei paragrafi da `work/libro.txt` nel file Ink **verbatim**, separando narrazione (→ pensieri di Vera o didascalie di regia) e battute (→ righe di dialogo). Il testo [NUOVO] e tutte le scelte sono scritti per esteso.
- **Formato dei dialoghi** (pronto per Ink):
  ```
  DLG-00-ESEMPIO-01  GIULIA [NUOVO]: «Che vuoi.»
    + (1) «…» [NUOVO]            → rap_giulia +2; flag_giulia_ginevra = true → DLG-00-ESEMPIO-02
    + (2) «…» {cond: rap_giulia >= 0}  → …
  ```
  `+` = scelta che resta disponibile se si torna al personaggio; `*` = scelta che sparisce dopo l'uso; `{cond: …}` = condizione; `→` = effetti e nodo successivo.

## 2. Capitoli: date, durate, checkpoint

| Cap. | Titolo | Date (2025) | Durata | Checkpoint | Rilascio |
|---|---|---|---|---|---|
| 1 | La scarpa | sab 13/9, 17:05–19:15 | 17 min | CP-01-A attesa · CP-01-B arrivo · CP-01-C parcheggio · CP-01-D auto · CP-01-E fine | v1.0 |
| 2 | Il vecchietto dietro il frigorifero | sab 13/9, 19:30–00:15 | 14 min | CP-02-A scalinata · CP-02-B cena · CP-02-C notte · CP-02-D fine | v1.0 |
| 3 | Le signore di fuori | lun 15 – gio 18/9 (notte) | 22 min | CP-03-A lunedì · CP-03-B martedì · CP-03-C mercoledì · CP-03-D giovedì · CP-03-E notte · CP-03-F fine | v1.0 |
| 4 | La guerra delle tazzine | gio 18/9 notte – ven 26/9 | 25 min | CP-04-A domande · CP-04-B venerdì 19 · CP-04-C–I lun 22 → ven 26 (uno al giorno) · CP-04-J cena | v2.0 |
| 5 | Due nonne che non sanno niente | sab 4 – dom 5/10 | 15 min | CP-05-A quaderno · CP-05-B Concetta · CP-05-C babuška · CP-05-D pranzo | v2.0 |
| 6 | Pokrov | mar 14/10 | 12 min | CP-06-A bar · CP-06-B balcone · CP-06-C notte | v2.0 |
| 7 | La casa tossisce | mer 15 – mar 21/10 | 16 min | CP-07-A crepa · CP-07-B luce · CP-07-C acqua · CP-07-D limone · CP-07-E litigio | v2.0 |
| 8 | Il consiglio di mezzanotte | gio 23/10 | 15 min | CP-08-A preparazione · CP-08-B consiglio · CP-08-C dopo | v2.0 |
| 9 | La scarpa vuota | ven 24 – sab 25/10 | 14 min | CP-09-A ricerca · CP-09-B dottore · CP-09-C accanto al letto · CP-09-D sabato | v3.0 |
| 10 | Il fratello che quasi vede | dom 26/10, 13:45–16:45 | 18 min | CP-10-A scalinata · CP-10-B Corso · CP-10-C funivia · CP-10-D lungomare | v3.0 |
| 11 | Il treno per il nord | dom 26/10, 16:45–18:30 | 12 min | CP-11-A stazione · CP-11-B dialogo · CP-11-C ritorno | v3.0 |
| 12 | Donne di fuori | dom 26 sera – mar 28/10 00:30 | 18 min | CP-12-A lunedì · CP-12-B cena · CP-12-C pulizie · CP-12-D mezzanotte | v3.0 |
| 13 | La notte dei Morti | sab 1 – dom 2/11 | 18 min | CP-13-A pomeriggio · CP-13-B notte · CP-13-C patto · CP-13-D mattina | v3.0 |
| 14 | Solo per un po' | mar 4/11 | 11 min | CP-14-A pioggia · CP-14-B cena · CP-14-C balcone | v3.0 |
| | **Totale** | | **227 min** | | |

## 3. Dizionario delle variabili

Ogni variabile è definita **una sola volta** qui. Tipi: `int`, `bool`, `string`. Salvate nel campo dello stato indicato (TDD §4). Le variabili Ink hanno lo stesso nome.

### 3.1 Rapporti (`rap_`, int −3…+3, in `rapporti`)
| Variabile | Default | Dove si imposta | Dove si legge | Cosa cambia |
|---|---|---|---|---|
| rap_giulia | −1 | SCN-01-05, 01-15, 02-03, 03-03, 07-08, 10-07, libero | 01-15, 02-03, 07-08, 10-07, 12-05, 13-09 | Giulia copre Vera, battute più calde, aiuto nella caccia ai cannistri |
| rap_mattia | 0 | 01-06, 01-14, 03-03, 04-11, 09-07, 10-* | 10-03, 10-05, 13-09 | Mattia indica più a lungo; battute affettuose |
| rap_babuska | 0 | 01-10, 01-12, 02-02, 02-03, 05-04, 06-02, 09-05, libero | 06-02, 09-05, 14-02, libero | parole russe extra, «Veročka» davanti a tutti |
| rap_irina | 0 | 01-04, 07-04, 09-04, libero | 09-04, 14-02 | battute di Irina, un abbraccio in più |
| rap_salvo | 0 | 01-03, bar (SIS-16), 07-03 | bar, 14-02 | battute al bar, Salvo racconta del nonno Turi |
| rap_concetta | 0 | 02-02, 04-02, 05-02, 07-05, 12-04, libero | 05-02, 13-02 | Concetta offre il biscotto, racconti siciliani |
| rap_foma | 0 | 02-09 (fisso 0), 03-05, 06-03, 06-04, libero (pane/latte), 11-03 | 06-03, 11-03, 12-01, 14-05 | battute di Fomà più affettuose; in libero risponde dal frigo |
| rap_rosalia | −1 | 03-11, 04-01, 08-04, 12-06, notti libere | 08-04, 12-08 | battute; Rosalia accenna un sorriso già al cap. 12 (sempre comunque al 12.059) |
| rap_nina | −2 | 03-11, 04-01, 08-04, 12-06 | 08-04, 12-08 | battute pungenti o meno |
| rap_tina | 0 | 03-11, 04-01, 08-04, 12-06 | 08-07, 12-07 | Tina sorride di nascosto più spesso; una battuta in più nelle notti libere |
| rap_nicolo | 0 | 03-01, 03-02, 12-02, libero | 12-02, libero | carte di dinosauri regalate, adesivo sul telefono |

### 3.2 Flag di trama (`flag_`, bool, default false, in `flag`)
| Variabile | Dove si imposta | Dove si legge | Cosa cambia |
|---|---|---|---|
| flag_salvo_valigie | SCN-01-03 | 01-14 | Salvo commenta il carico delle valigie |
| flag_irina_quanto | 01-04 | 01-15 | pensiero di Vera nel viaggio |
| flag_irina_kolja | 01-04 | 01-10, 06-02 | Vera collega gli occhi del nonno al ricordo |
| flag_giulia_ginevra | 01-05 | 01-15, 02-03, 07-08, 10-07 | Giulia alleata (D-58) |
| flag_mattia_signore | 01-06 | 01-06 (signore), 01-08 | battute del signore |
| flag_starnuto_detto | 01-12 | 01-13, 02-07 | ramo della battuta 01.038 (D-83); pensiero di Vera nel cap. 2 |
| flag_auto_chiesto | 01-15 | 01-15 | Vera chiede sottovoce a Mattia o a Giulia (mai alla babuška) |
| flag_foto_etna | 01-15 | 01-16 (scheda) | foto nella scheda di fine capitolo |
| flag_valigia_aiutata | 02-01 | 02-02 | battuta di Salvo e della babuška |
| flag_arancino_primo | 02-03 | 02-03 | quale nonna guarda Vera per prima |
| flag_nicolo_tutte_carte | 03-01 | 03-02, 12-02 | Nicolò regala la carta del Pachycephalosaurus |
| flag_barba_gentile | 03-05 | 03-10, 04-01 | Fomà più conciliante con Vera |
| flag_bar_cap3 | 03-04 | 06-01 | Salvo ricorda che Vera l'ha aiutato |
| flag_prova_moka · _kefir · _lenzuola · _calze · _tazzine · _pane · _sale | 04-03 … 04-10 | 04-11, 05-01 | prove nel quaderno (SIS-21) |
| flag_rosalia_sincera | 04-01 | 08-04 | Rosalia ricorda che Vera ha detto la verità |
| flag_spia_completa | 05-03 | 05-05 | pagina del quaderno più ricca |
| flag_casse_portate | 07-04 | 07-07 | Irina ringrazia; battuta sul ginocchio della babuška |
| flag_consiglio_calma | 08-04 | 08-07 | Tina guarda Vera più a lungo (8.050) |
| flag_ricerca_completa | 09-01 | 09-02 | pensiero di Vera |
| flag_bar_evitato | 10-04 | 10-04 | se papà vede Vera: fallimento morbido |
| flag_pulizie_complete | 12-05 | 12-08 | battuta di Rosalia |
| flag_ditale_cucchiaio_uniti | 13-09 | libero, 14-03 | oggetto sulla mensola; frase nella pagina CASA RUSSO |
| flag_lettera_vista | 14-04 | 14-05 | inquadratura della vecchietta cancellata |
| flag_v1_fine | fine SCN-03-11 in v1.0 | sistema (D-82) | apre la domenica ripetibile |

### 3.3 Stato della casa (`casa_`, in `casa`)
| Variabile | Tipo, intervallo | Default | Dove si imposta | Dove si legge | Cosa cambia |
|---|---|---|---|---|---|
| casa_crepa | int 0–5 | 0 | 07-02 (1→3 nei giorni), 07-08 (+ un dito, resta 3), 08-05 (4), 09-02 (4), 09-06 (5), 13-08 (0) | SIS-12 | decal della crepa |
| casa_luce | int 0–3 | 0 | 07-03 (2), 09-02 (3), 12-01 (1), 13-08 (0) | SIS-12 | blackout |
| casa_acqua | int 0–3 | 0 | 07-04 (1), 07-06 (2), 09-02 (3), 13-08 (0) | SIS-12 | colore e sapore dell'acqua |
| casa_limone | int 0–4 | 0 | 07-05 (1→3), 09-02 (4), 13-08 (0) | SIS-12 | foglie, limoni caduti |
| casa_guarita | bool | false | 13-08 | tutto | casa sana per sempre, fiore del limone |

### 3.4 Valori (`val_`, int, in `val`)
| Variabile | Intervallo | Default | Dove si imposta | Dove si legge | Cosa cambia |
|---|---|---|---|---|---|
| val_familiari_parlati | 0–4 | 0 | 01-03…01-06 | 01-08 (porta a ≥3) | apre la porta degli arrivi |
| val_prove_cap4 | 0–7 | 0 | 04-03…04-10 | 04-11, 05-01 | frase finale del capitolo |
| val_tensione_casa | 0–100 | 40 | 08-04, 08-05 | SIS-22 | reazioni della casa |
| val_impronte_trovate | 0–24 | 0 | 10-01, 10-03, 10-06 | SIS-23 | — |
| val_discorso_scelto | 0–3 | 0 | 12-03 | 12-06 | quale discorso Vera tenta prima della domanda |
| val_pulizie_punteggio | 0–12 | 0 | 12-05 | 12-08 | battuta di Rosalia |
| val_cannistri_trovati | 0–3 | 0 | 13-09 | 13-09 | — |
| val_dolci_trovati | 0–5 | 0 | 13-09 | libero | pagina «I dolci dei Morti» |

### 3.5 Collezioni (`col_`, in `collezioni`; in Ink solo i contatori in lettura)
| Variabile | Tipo | Dove | Cosa cambia |
|---|---|---|---|
| col_rus / col_rus_n | lista di ID RUS / int | sblocchi nei dialoghi e in libero | dizionario del quaderno, ricompensa §4 GDD |
| col_ric / col_ric_n | lista RIC / int | dialoghi, oggetti | pagina «I due nonni» |
| col_fot / col_fot_n | lista FOT / int | telefono | album e ricompense |
| col_seg / col_seg_n | lista SEG / int | segreti | mappa segreta |

## 4. Modello dei rapporti

- Intervallo −3…+3; le scelte danno ±1 (raramente ±2). Nessuna scelta abbassa due persone «di parti opposte» insieme: il gioco non costringe Vera a scegliere tra russi e siciliani (tema).
- **Fasce**: freddo (≤ −2), normale (−1…+1), caldo (≥ +2). Le battute alternative esistono per le fasce, non per ogni valore.
- **Scene alternative** (gli eventi restano quelli del libro):
  | Condizione | Scena | Differenza |
  |---|---|---|
  | flag_giulia_ginevra o rap_giulia ≥ 2 | SCN-01-15 | Giulia passa il telefono per lo zoom sull'Etna e copre Vera davanti a papà |
  | idem | SCN-02-03 | a cena Giulia si siede accanto a Vera e commenta sottovoce i «complimenti» delle nonne |
  | idem | SCN-07-08 | dopo la porta sbattuta Giulia la riapre di due dita e dice una frase in più (vedi nota) |
  | rap_giulia ≥ 1 | SCN-10-07 | Giulia arriva con una bottiglietta d'acqua per Mattia |
  | rap_mattia ≥ 2 | SCN-10-03 | Mattia indica più a lungo e trova da solo un'impronta |
  | rap_foma ≥ 2 | SCN-12-01 | Fomà dice «Buonanotte, Veročka» dal frigo |
  | flag_starnuto_detto | SCN-01-13 | primo piano dopo la battuta detta a voce; altrimenti la babuška si volta sentendosi guardata |
  - *Nota SCN-07-08*: il libro dice «rientrò in camera e sbatté la porta» (07.041). Nel ramo alleato la porta **sbatte comunque** (evento del libro), ma dopo 3 secondi si riapre di due dita e Giulia dice da dentro «Se senti ancora rumori, bussa.» [NUOVO], poi la chiude piano.
- I rapporti con gli spiriti (rap_foma, rap_rosalia, rap_nina, rap_tina) cambiano tono e battute delle notti libere e dei capitoli 8 e 12, mai l'esito.

## 5. Regole di tono

1. **Ironia che diventa mistero**: la frase di Vera chiude spesso con un rovesciamento comico (01.005 «anche dei cucchiai»); il mistero arriva per sottrazione (silenzi, sguardi, un suono).
2. **Gli adulti hanno sempre una spiegazione normale** (formiche, vento, umidità, lavatrici). Non deridono mai Vera in modo crudele.
3. **Niente cattivi**: Fomà e le Donne litigano per orgoglio e nostalgia, mai per malvagità (06.041).
4. **Affetto senza sdolcinatezza**: i momenti teneri sono brevi e concreti (prendere una mano, 06.017; le orecchie rosse di papà).
5. **Ritmo delle frasi**: brevi, con ripetizioni a tre («Tutto normale. Tutto siciliano.»); dialoghi con il trattino lungo nel libro → nel gioco righe separate.

## 6. Regole per il testo [NUOVO]

- Prima persona di Vera, passato remoto per la narrazione retrospettiva, presente nei pensieri immediati del gioco («Papà conta le valigie come i clienti.»).
- Lessico da prima media; niente parolacce; al massimo «cavolo» (10.037 lo usa Giulia).
- Una battuta [NUOVO] non può: anticipare una rivelazione del libro (es. che Concetta sa delle Donne prima del cap. 5), far vedere gli spiriti a chi non li vede, contraddire un fatto della scheda «Fatti da rispettare» di `work/indice_libro.md`.
- Ogni battuta [NUOVO] di un personaggio usa i suoi «modi di dire» di `PERSONAGGI.md`.
- Lunghezza: battute ≤ 160 caratteri (due righe di sottotitolo); pensieri ≤ 120 caratteri.
- Dialetto: Concetta, le Donne e i clienti del bar usano parole siciliane comprensibili dal contesto («picciridda», «talìa», «amunì»); mai frasi intere in siciliano senza sottotitolo.

## 7. Regole per il russo

- Schema di traslitterazione scientifico del libro (D-53): ж ž · ч č · ш š · щ šč · х ch · ц c · й j · я ja · ю ju · ё ë · э è · ы y · ь ' · ъ ''. Eccezioni del libro: **dedushka**, **matrioška/matrioške**.
- Ogni battuta in russo nei documenti è scritta: cirillico · traslitterazione · sottotitolo italiano (testo del libro quando esiste).
- Chi parla russo: babuška e Irina tra loro e con i nipoti (D-48); Vera con la babuška solo dove il gioco lo indica (una frase ogni tanto, perché il giocatore capisca che può); Fomà solo sbuffi, imprecazioni non tradotte e la parola «Fu».
- Le imprecazioni di Fomà del cap. 2 (02.026: «parole in russo che non conoscevo, e che più tardi la babuška si rifiutò di tradurmi») sono borbottii **senza sottotitolo di traduzione**: il sottotitolo è «[parole in russo che la babuška non tradurrà]».
- Revisione: ogni frase russa è controllata da un madrelingua prima del doppiaggio (Irina-tipo: Vlad o persona di fiducia; vedi `DOMANDE_APERTE.md` Q-06).

## Fonti

- Manoscritto (ID in `work/libro.txt`) e `work/indice_libro.md`.
- `FASI_DI_SVILUPPO.md` §2, §14, §15.
- [Ink — documentazione del linguaggio (inkle)](https://github.com/inkle/ink/blob/master/Documentation/WritingWithInk.md)
