# Bibbia dei personaggi

Ogni personaggio ha un ID `PG-`. Le citazioni usano gli ID dei paragrafi di `work/libro.txt`. Le misure sono in centimetri (scala reale, 1 unità Blender = 1 m). Dove il libro tace, la scelta è marcata **[NUOVO]** e non contraddice il testo. Voci dettagliate per ElevenLabs/Fish Audio in `AUDIO.md` §5.

## 0. Libreria di animazioni comuni (ID `ANI-COM-`)

Tutti gli umani condividono lo scheletro D-64; queste animazioni sono retargettate su ogni personaggio con varianti di età (parametri di ampiezza e velocità).

| ID | Animazione | ID | Animazione |
|---|---|---|---|
| ANI-COM-01 | Fermo, respiro (idle) con 3 varianti | ANI-COM-11 | Seduto, parla |
| ANI-COM-02 | Camminata | ANI-COM-12 | Si alza dalla sedia |
| ANI-COM-03 | Corsa leggera | ANI-COM-13 | Sale le scale |
| ANI-COM-04 | Parla, gesti piccoli | ANI-COM-14 | Scende le scale |
| ANI-COM-05 | Parla, gesti ampi («siciliano») | ANI-COM-15 | Indica |
| ANI-COM-06 | Annuisce | ANI-COM-16 | Ride |
| ANI-COM-07 | Scuote la testa | ANI-COM-17 | Sospira |
| ANI-COM-08 | Si gira sul posto (90°/180°) | ANI-COM-18 | Braccia incrociate |
| ANI-COM-09 | Si siede su una sedia | ANI-COM-19 | Seduto in auto (con cintura) |
| ANI-COM-10 | Seduto, fermo | ANI-COM-20 | Mangia a tavola (forchetta/cucchiaio) |

Più: sguardo procedurale (testa/collo/occhi, SIS-13), ammiccamenti, labiale a visemi (TDD §9) per le battute doppiate e labiale generico per le battute solo testo.

---

## 1. Famiglia Russo

### PG-VERA — Vera Russo (la giocatrice)
- **Ruolo**: protagonista e narratrice; la giocatrice la vede in prima persona.
- **Età**: 12 anni (prima media). Narratrice dell'intro e delle chiusure: Vera a 13–14 anni (D-42).
- **Altezza e corporatura**: 152 cm, esile; occhi a 141 cm (D-55).
- **Viso, capelli, mani** [NUOVO, D-73]: occhi **grigi** (10.023: «Aveva gli occhi grigi, come la babuška. Come il dedushka. Come me.»); capelli castano chiaro lunghi fino alle scapole, coda bassa con elastico blu, ciuffi che scappano; mani sottili, unghie corte (una mangiucchiata), braccialetto di filo rosso e blu al polso sinistro, a volte una macchia di biro blu sul dito medio destro (quaderno, D-41).
- **Parti visibili in prima persona**: mani e avambracci (quaderno, telefono, interazioni), maniche, ginocchia quando è seduta o in ginocchio, piedi nudi nelle scene notturne (02.015 lei la babuška scalza; 03.019 Vera «a piedi nudi»), riflesso negli specchi del bagno e dell'ingresso, nei vetri della vetrinetta, nei finestrini dell'auto e della funivia (riflesso morbido, rendering del corpo completo a bassa risoluzione solo per i riflessi), foto di famiglia.
- **Abiti** [NUOVO]:
  | Momento | Abiti |
  |---|---|
  | Cap. 1 (aeroporto, 13/9) | maglietta bianca a righe blu sottili, salopette di jeans corta, scarpe da ginnastica bianche, zainetto blu |
  | Settembre a casa | maglietta larga grigia, pantaloncini, ciabatte di gomma |
  | Notte (capp. 2–14) | pigiama di cotone azzurro con piccole stelle, a piedi nudi |
  | Scuola (sett.–ott.) | felpa blu con cappuccio aperta su maglietta bianca, jeans, zaino blu con portachiavi a matrioška (regalo della babuška dal cap. 2, [NUOVO]) |
  | Ottobre fuori | jeans, maglietta, cardigan verde salvia |
  | 4 novembre (pioggia) | felpa gialla, jeans, stivaletti di gomma blu |
- **Modo di muoversi**: veloce e curiosa; si ferma a guardare; di notte cammina in punta di piedi (camera più bassa di 2 cm e passi più lenti).
- **Voce** (pensieri non doppiati; narrazione VOX-NAR): ragazzina di 13–14 anni, voce chiara, ironica, asciutta; pause prima delle battute comiche; italiano senza accento regionale marcato, con «r» pulita; sa pronunciare bene il russo.
- **Modi di dire dal libro**: «e il mio cognome è una barzelletta» (01.001); ironia sui grandi («un po' era una di quelle parole che i grandi usano quando non lo sanno nemmeno loro», 01.013); «Credo che siano mescolate» (03.006).
- **Rapporto con Vera e variabili**: —; le variabili sono quelle degli altri verso di lei.
- **Cosa vede, sente, sa**: vede tutti gli spiriti, sente tutto (08.045: «Lei è tutte e due le cose. Per questo ci vede. Ci vede tutti.»). Nel cap. 1 sente starnuto e sospiro, vede due occhietti nel buio (D-47).
- **Presenza**: tutti i capitoli.
- **Animazioni necessarie (prima persona, braccia)**: ANI-VER-01 apre/chiude quaderno; ANI-VER-02 sfoglia; ANI-VER-03 scrive a biro; ANI-VER-04 alza telefono / scatta / abbassa; ANI-VER-05 accende torcia; ANI-VER-06 abbraccio (cap. 1, 11); ANI-VER-07 prende oggetto piccolo; ANI-VER-08 si inginocchia e tocca il pavimento; ANI-VER-09 mano tesa verso Mattia (tenere per mano, cap. 10–11); ANI-VER-10 batte le mani sul tavolo (cap. 8); ANI-VER-11 posa la candela; ANI-VER-12 tiene il lapot' con due mani (cap. 11); ANI-VER-13 minigiochi pulizie (lenzuola, mollette, straccio, rametto); ANI-VER-14 unisce ditale e cucchiaio; ANI-VER-15 servizio al bar (tazzina, granita); ANI-VER-16 si asciuga le guance (cap. 8). Corpo intero (solo riflessi e foto): ANI-COM-01/02/09/10.
- **Citazioni di riferimento**: «Mi chiamo Vera Russo, ho dodici anni» (01.001); «Io sono metà e metà! Quindi di chi sono io, eh?» (08.040); «Io sono sempre un po' forestiera, Fomà.» (11.030); «Non ero divisa. Ero un ponte.» (14.028).

### PG-BABUSKA — babuška Galina Petrovna (Ivanova)
- **Ruolo**: la nonna russa, madre di Irina; porta Fomà nel lapot'.
- **Età**: 74 anni (01.014).
- **Altezza e corporatura**: 149 cm, 150 con il fazzoletto (02.005 «erano alte uguali» a Concetta); piccola, spalle un po' curve, mani forti da chi impasta.
- **Viso, capelli, mani**: occhi grigi chiari «con tante pieghe intorno, come se avesse passato la vita a strizzarli per guardare lontano» (01.026); capelli grigio-argento raccolti in uno chignon basso sotto il fazzoletto [NUOVO]; viso tondo, zigomi alti, pelle chiara con rughe fini; mani nodose, fede d'oro rosso consumata all'anulare destro (uso russo) [NUOVO].
- **Abiti**: cap. 1 **cappotto di lana verde** (verde bottiglia scuro, taglio anni '80, bottoni grandi), **fazzoletto annodato sotto il mento** (lana fine color crema con fiori rossi e blu, stile Pavlovo Posad senza marchio) [NUOVO per colori], gonna grigia al polpaccio, calze color carne, scarpe nere basse, borsa di stoffa a fiori sottobraccio. Casa: vestito di cotone a fiori minuti con grembiule; notte: **camicia da notte** bianca lunga, **scalza** (02.015); **vestaglia di lana** blu e pantofole di feltro (13.023); cap. 6 cappotto verde sul balcone con 26 gradi (06.002–003); capp. 9–12 a letto, coperta fino al mento (09.009).
- **Modo di muoversi**: camminata da anziana, passi corti e decisi, ginocchio destro rigido (07.023 «il ginocchio che non va»): si inginocchia piano appoggiandosi (02.019); scende le scale un gradino alla volta tenendosi al corrimano (02.015); il segno della croce **da destra a sinistra** (02.019).
- **Voce**: contralto basso, roco e caldo, lento; in russo madrelingua (San Pietroburgo, pronuncia colta); in italiano «con la erre lunga lunga» (02.006), vocali aperte russe, frasi brevi.
- **Modi di dire dal libro**: «Sei magra. Non mangi.» (01.019); «Cosa dovevo fare, lasciarlo lì?» (01.033); «Le scarpe non starnutiscono, Veročka.» (01.040); «Io non tocco le cose degli altri» (04.017); «Non credo a niente.» (05.040); «Salvatore. Sei un brav'uomo. Magro, ma bravo.» (14.017).
- **Lingua** (D-48): russo con Irina, Vera, Mattia, Fomà (sottotitolo italiano del libro); italiano con accento con Salvo, Concetta, dottore e gli altri.
- **Rapporto con Vera e variabili**: `rap_babuska` (default 0): sale se Vera la ascolta, la aiuta, parla russo con lei; non scende mai sotto −1 (vuole bene ai nipoti). Effetti: a +2 la babuška chiama Vera «Veročka» anche davanti a Concetta e le insegna una parola russa in più (RUS libera).
- **Cosa vede, sente, sa**: non vede gli spiriti ma **sa** (05.025, 13.033 «Da sempre. Mia nonna mi ha insegnato a dargli il latte»); sente la presenza (si stringe la vestaglia, 13.038).
- **Presenza**: 1, 2, 3 (sera), 4, 5, 6, 7, 9, 10 (a letto), 12 (a letto), 13, 14.
- **Animazioni**: ANI-BAB-01 spinge il carrello con tre valigie; ANI-BAB-02 abbraccia e tiene a distanza con le mani sulle spalle (01.018); ANI-BAB-03 tre baci destra-sinistra-destra; ANI-BAB-04 stringe la borsa sottobraccio e la sistema; ANI-BAB-05 due colpetti alla borsa (01.042) / al frigo (14.018); ANI-BAB-06 rito: tiene il lapot' come una tazza troppo piena, si inginocchia, posa, croce destra-sinistra (02.016–019); ANI-BAB-07 sistema il fazzoletto; ANI-BAB-08 seduta sul balcone stretta nel cappotto; ANI-BAB-09 a letto con la febbre (respiro, mano sulla coperta); ANI-BAB-10 impasta il pane; ANI-BAB-11 ride con le mani davanti alla bocca, poi appoggiata al frigo (13.031); ANI-BAB-12 si pulisce la bocca col tovagliolo con calma (05.039); ANI-BAB-13 taglia il pane e si ferma col coltello a mezz'aria (14.009); più ANI-COM-01–20.
- **Citazioni**: «Veročka — disse lei, e mi guardò a lungo.» (01.026); «Buona notte, Fomà.» (02.034); «Lo so. Anche a me manca casa.» (05.027).

### PG-IRINA — Irina Russo (mamma)
- **Ruolo**: madre; nata a San Pietroburgo, in Sicilia da 18 anni; guida turistica in russo (AP.001, 09.022).
- **Età**: 41 [NUOVO, coerente con 18 anni in Sicilia e Giulia 16].
- **Altezza e corporatura**: 168 cm, slanciata.
- **Viso, capelli, mani**: occhi azzurro-grigi [NUOVO], capelli biondo cenere lunghi fino alle spalle, spesso raccolti con una pinza; viso ovale, zigomi alti; mani curate, unghie corte senza smalto, orologio sottile.
- **Abiti**: cap. 1 camicia di lino bianca, pantaloni blu, sandali bassi, borsa a tracolla, cartello di Mattia in mano; lavoro (ottobre): tailleur pantalone blu, badge da guida senza logo, foulard; casa: maglione morbido grigio; sera del litigio: maglietta e pantaloni da casa.
- **Modo di muoversi**: rapida, pratica; quando è triste si siede sui gradini (09.015) e si copre il viso.
- **Voce**: mezzosoprano chiaro; italiano ottimo ma «con le erre che rotolano come biglie» (01.002); russo madrelingua con la babuška.
- **Modi di dire dal libro**: «Solo per un po'.» (01.011); «Mamma. L'hai portato davvero.» (01.032); «Ma figurati.» (04.037); «Avevi detto solo per un po'. Va bene. Ma un po' quanto, Salvo?» (07.030); «È colpa mia» (09.017).
- **Rapporto e variabili**: `rap_irina` (0): sale ascoltandola nel cap. 1 (ricordo di Kolja), aiutandola (casse d'acqua, babuška malata).
- **Spiriti**: non vede; riconosce il lapot' e conosce le favole (02.038); spiega con formiche (03.008), vento (04.030).
- **Presenza**: 1, 2, 3 (sere), 4, 5 (esce), 7, 9, 10 (in casa), 12, 13, 14.
- **Animazioni**: ANI-IRI-01 tiene il cartello; ANI-IRI-02 corre incontro e abbraccia (01.017); ANI-IRI-03 lava i piatti; ANI-IRI-04 litiga a bassa voce (gesti trattenuti); ANI-IRI-05 seduta sul gradino, mani sul viso; ANI-IRI-06 abbraccia la babuška da dietro mentre impasta (13.014); ANI-IRI-07 scioglie la treccia di lenzuola (04.030).
- **Citazioni**: «— Mamočka! — gridò mia madre, e le corse incontro.» (01.017).

### PG-SALVO — Salvatore «Salvo» Russo (papà)
- **Ruolo**: padre; ha il bar sul Corso Umberto, aperto da suo padre nonno Turi (13.053).
- **Età**: 44 [NUOVO].
- **Altezza e corporatura**: 178 cm, robusto, pancia leggera.
- **Viso, capelli, mani**: occhi castano scuro, capelli neri ricci corti con tempie grigie, barba di due giorni; mani grandi, segno dell'abbronzatura dell'orologio.
- **Abiti**: cap. 1 polo blu scuro, jeans, mocassini; al bar camicia bianca con maniche arrotolate e grembiule nero lungo senza scritte; casa: maglietta; 4 novembre: maglione blu.
- **Modo di muoversi**: cammina avanti e indietro con le mani in tasca (01.009); sorriso «per i clienti difficili» (01.022); orecchie che diventano rosse (01.024, 14.018).
- **Voce**: baritono caldo, accento siciliano orientale (Messina-Catania) moderato, veloce, ride spesso.
- **Modi di dire dal libro**: «Benvenuta, Galina Petrovna.» (01.023); «Che bello. Mangiamo tutto. Insieme. Tutti contenti.» (02.009); «Le calze spariscono da sole da quando esistono le lavatrici» (04.041); «Allora. Dobbiamo parlare di una cosa.» (14.005).
- **Rapporto e variabili**: `rap_salvo` (0): sale aiutando al bar (SIS-16), scende di poco se Vera evita il bar nel cap. 10 e lui lo scopre (non lo scopre mai nel libro: nessun effetto in trama).
- **Spiriti**: non vede; spiega con topi e trappole (03.008), umidità (07.006).
- **Presenza**: 1, 2, 3, 4, 6 (bar), 7, 9 (bar), 10 (bar, da evitare), 12 (bar), 14.
- **Animazioni**: ANI-SAL-01 cammina avanti e indietro nervoso; ANI-SAL-02 riceve i tre baci rigido; ANI-SAL-03 al bar: macchina del caffè, granita, banco; ANI-SAL-04 scende al quadro elettrico con la torcia; ANI-SAL-05 si gratta la testa davanti alla crepa; ANI-SAL-06 guida (cap. 1); ANI-SAL-07 posa la forchetta (14.004).
- **Citazioni**: «Mio padre dice che il limone è il vero padrone di casa, e noi siamo in affitto.» (02.001).

### PG-GIULIA — Giulia Russo (sorella)
- **Ruolo**: sorella maggiore; «non crede a niente. O quasi» (AP.001).
- **Età**: 16 anni.
- **Altezza e corporatura**: 165 cm, magra.
- **Viso, capelli, mani**: occhi castani di papà [NUOVO], capelli scuri lunghi e lisci con riga in mezzo, eyeliner sottile; unghie con smalto blu notte scheggiato; il telefono sempre in mano (oggetto separato, D-39/RICHIESTE).
- **Abiti**: cap. 1 felpa oversize grigia con cappuccio, shorts di jeans, sneakers nere alte, cuffie grandi al collo; casa: maglietta larga; ottobre: giacca di jeans; capp. 10–11: felpa nera, vento nei capelli.
- **Modo di muoversi**: appoggiata alle colonne, peso su una gamba; occhi al cielo; cammina veloce con le mani in tasca.
- **Voce**: alto giovane, nasale annoiato, frasi brevi sarcastiche; accento siciliano leggero.
- **Modi di dire dal libro**: «Quanto resta?» «Quanto è un po'?» (01.010–012); «Qualcuno sarà stato. Le calze non spariscono da sole.» (04.040); «È tutto da quando è arrivata lei» (07.036); «Voi due siete completamente pazzi.» (10.050); «Niente. Andiamo. È tardi. La mamma ci ammazza.» (11.062).
- **Rapporto e variabili**: `rap_giulia` (default −1); `flag_giulia_ginevra` (cap. 1, D-58). A ≥ +2 copre Vera e la aiuta (scene alternative in cap01, cap02, cap07, cap10).
- **Spiriti**: non vede; nel cap. 11 **sente** «Grazie, ragazze.» (11.064–065) e lo confessa mesi dopo; dal cap. 11 piccoli ritardi «come se avesse sentito».
- **Presenza**: 1, 2, 3, 4, 7, 10, 11, 12, 13, 14.
- **Animazioni**: ANI-GIU-01 appoggiata alla colonna col telefono; ANI-GIU-02 si fa baciare «come chi viene vaccinato» (01.025); ANI-GIU-03 occhi al cielo; ANI-GIU-04 cuffie, ride da sola coi video; ANI-GIU-05 sbatte la porta; ANI-GIU-06 corre col fiatone e afferra il braccio (10.036–040); ANI-GIU-07 appoggiata alla colonnina con le braccia incrociate (11.011); ANI-GIU-08 labbro che trema, si gira veloce (11.063); ANI-GIU-09 cammina tenendo per mano due bambini.
- **Citazioni**: «la faccia di chi è stata trascinata fuori dal letto contro la Convenzione di Ginevra» (01.009).

### PG-MATTIA — Mattia Russo (fratello)
- **Ruolo**: fratellino; «non vede gli spiriti, ma li sente» (AP.001).
- **Età**: 6 anni (prima elementare, lui dice «asilo», 09.022).
- **Altezza e corporatura**: 116 cm, magro, ginocchia sbucciate.
- **Viso, capelli, mani**: occhi **grigi** (10.023); capelli castano chiaro arruffati, un ciuffo dritto; dentino che manca davanti [NUOVO]; mani appiccicose.
- **Abiti**: cap. 1 maglietta con un dinosauro verde, pantaloncini, sandali con lo strappo; **cappellino da baseball storto** e zainetto con il **coniglio di pezza** dalle orecchie che escono dalla cerniera (10.008); pigiama a righe con il coniglio sotto il braccio (09.038, 14.030).
- **Modo di muoversi**: saltella (01.037), corre, gira in tondo «come un cagnolino che annusa» (10.013), si appiccica ai vetri (10.018).
- **Voce**: bambino di 6 anni, acuto, serissimo nelle frasi strane; non usare voci clonate di bambini reali (D-80).
- **Modi di dire dal libro**: «Babuška vuol dire nonna… Le bambole sono le matrioške.» (01.007); «Il signore dice che sono state le signore» (04.044); «So da che parte è andato.» (09.043); «Io voglio che torna. Mi piace sentirlo russare.» (10.024); «Voglio Ded Moroz.» (14.033).
- **Rapporto e variabili**: `rap_mattia` (0); `flag_mattia_signore` (cap. 1, D-57). A ≥ +2 nel cap. 10 indica le impronte più a lungo (aiuto automatico).
- **Spiriti**: sente passi, voci, russare; vede briciole e impronte di farina (10.007–008); non vede Fomà.
- **Presenza**: 1, 2, 3, 4, 9, 10, 11, 12, 13, 14.
- **Animazioni**: ANI-MAT-01 saltella intorno al carrello; ANI-MAT-02 si butta addosso alla babuška (01.025); ANI-MAT-03 spiega serio al signore (indica, mani aperte); ANI-MAT-04 annusa girando la testa; ANI-MAT-05 indica per terra; ANI-MAT-06 naso schiacciato contro il vetro; ANI-MAT-07 seduto sul gradino col coniglio; ANI-MAT-08 scappa verso le macchinine (fallimento morbido cap. 1); ANI-MAT-09 dorme a bocca aperta; ANI-MAT-10 infila la faccia nel lapot' (11.056); ANI-MAT-11 piega la lettera.
- **Citazioni**: «Era come uno che non può guardare il sole ma sente il caldo sulla faccia.» (10.008).

### PG-CONCETTA — nonna Concetta Russo
- **Ruolo**: nonna siciliana, madre di Salvo; abita due scalinate più su (D-45).
- **Età**: 71 anni.
- **Altezza e corporatura**: 146 cm + 4 cm di capelli cotonati = 150 (02.003); rotonda, energica.
- **Viso, capelli, mani**: occhi neri vivaci; capelli cotonati tinti castano ramato [NUOVO]; orecchini di corallo; mani piccole, anelli; voce «che si sente fino a Giardini Naxos» (02.003).
- **Abiti**: **vestaglia color fucsia** (02.003, 05.016, 13.022) di sera; di giorno vestito a fiori scuri con cardigan; scarpe con tacco basso; borsa della pasticceria; un anno di nero dopo la morte di Turi (ricordo).
- **Modo di muoversi**: veloce sulle scale nonostante l'età (le conosce da quarant'anni, 13.017); braccia incrociate quando è offesa (04.013); segno della croce da sinistra a destra.
- **Voce**: soprano anziano potente; siciliano stretto con i suoi, italiano regionale con la babuška; ritmo veloce.
- **Modi di dire dal libro**: «Arancini. Al ragù e al burro.» (02.004); «Ha visto per caso la mia moka?» (04.016); «Ah.» (04.020); «Signore mie, la casa è pulita, i letti sono fatti.» (05.018); «Sta morendo» (07.012); «Da fuori. Da Catania.» (12.012); «Un po' sì. Non tanto. Ma un po'.» (12.017).
- **Rapporto e variabili**: `rap_concetta` (0).
- **Spiriti**: non vede ma **sa** (05.020; 13.034 «Mia suocera mi ha insegnato il rosmarino»).
- **Presenza**: 2, 4, 5, 7, 12, 13, 14 (citata), mondo libero (ogni mattina alle 7:30 con la moka, dal cap. 4 a casa nostra).
- **Animazioni**: ANI-CON-01 porge il vassoio di arancini; ANI-CON-02 moka sul fornello; ANI-CON-03 seduta a braccia incrociate, faccia scura; ANI-CON-04 rito del rosmarino: gira per le stanze col piattino e fa il fumo verso gli angoli (05.016); ANI-CON-05 seduta parla verso il portone; ANI-CON-06 sale la scalinata con tre borse; ANI-CON-07 ride fino a doversi sedere (13.031); ANI-CON-08 mano sul cuore alla finestra (13.051); ANI-CON-09 segno della croce sinistra-destra.
- **Citazioni**: «E se passate anche da mio figlio, fatemi la cortesia di lasciare in pace la vecchia russa. Non è cattiva. È solo forestiera.» (05.018).

### PG-KOLJA — dedushka Kolja (ricordo illustrato)
- **Ruolo**: nonno russo morto in primavera; presente solo come ricordo disegnato nel quaderno (D-77) e oggetti.
- **Età**: 77 alla morte [NUOVO]. **Altezza**: alto e magro (182 cm nei disegni) [NUOVO].
- **Aspetto**: **camicia a quadri**, odore di tabacco e mele (01.014); occhi grigi (10.023); baffi grigi [NUOVO]; gioca a scacchi barando.
- **Voce**: nessuna (non doppiato; nei ricordi le sue parole sono riferite).
- **Rapporto**: chiamava Vera «Veročka» (01.014).
- **Presenza**: ricordi RIC-01, RIC-02, RIC-05, RIC-06, RIC-13; cucchiaio di legno rosso e oro (13.054).
- **Animazioni**: nessuna (illustrazioni con tratto animato).
- **Citazioni**: «Kolja accendeva la stufa il giorno del Pokrov. Sempre.» (06.016).

### PG-TURI — nonno Turi (foto con lumino)
- **Ruolo**: nonno siciliano morto sei anni fa (02.003); foto sulla credenza con lumino sempre acceso (05.008); aprì il bar; da giovane cuciva le vele della barca con il ditale d'argento con la R (13.053).
- **Aspetto** [NUOVO]: nella foto ha circa 60 anni, camicia bianca, baffi, sorriso largo, sfondo di mare.
- **Presenza**: foto in casa di Concetta (cap. 5), ricordi RIC-07, RIC-08, RIC-12; ditale (cap. 13); pagina CASA RUSSO (14.025).

---

## 2. Gli spiriti

### PG-FOMA — Fomà, il domovoj della famiglia Ivanov
- **Ruolo**: spirito della casa della famiglia della babuška; arriva nel lapot'; vive dietro il frigorifero.
- **Età**: «Da duecento anni» (03.041).
- **Altezza e corporatura**: **32 cm** in piedi, come una bottiglia d'acqua da 1,5 L (02.025, D-56); testa grande (⅓ dell'altezza, proporzioni da vecchietto-gatto); corpo coperto di **peli morbidi come un gatto vecchio**, grigio-tabby con sfumature fulve; pancia rotonda.
- **Viso, capelli, mani** (come in copertina, reso realistico, D-21): muso **quasi gattesco** (naso grosso **rosso** e lucido come una ciliegia, guance pelose, orecchie a punta coperte dai capelli), **occhietti neri e lucidi** con riflessi (D-47); capelli grigi **tutti arruffati**; **barba grigia lunghissima fino ai piedi**, trascinata come uno strascico (lunghezza 38 cm, 8–10 cm a terra), che si arrotola in grembo quando è seduto (08.014, 11.005); **manine piccole e pelose con unghie lunghe e gialle** (02.023); piedi nudi pelosi, con farina sulle piante (10.007).
- **Abiti**: **camicia rossa** (rosso mattone, tessuto grezzo di lino con ricamo bianco al collo) con **cintura di corda**; niente scarpe: «la sua scarpa era quella da cui era uscito» (02.025).
- **Modo di muoversi**: passi brevi e strascicati, barba che fruscia; salta dentro e fuori dal lapot'; si arrampica su sedia → tavolo (08.014); si siede a gambe incrociate; quando è offeso diventa **viola** (03.041) o **rosso come la sua camicia** (08.028): variazione di colore del naso e delle guance (parametro di materiale).
- **Voce**: vecchio piccolo, roco, brontolone, nasale; italiano «strano, impastato, con tutte le erre sbagliate» (02.026), sbuffi, imprecazioni russe non tradotte (D-79); a volte voce «piccola piccola» (11.036).
- **Modi di dire dal libro**: «Fu.» «E la stufa? Dov'è la stufa? Che casa è una casa senza stufa?» (02.026); «Qui dietro è caldo. Ronza. Mi piace.» (02.031); «Non ci sono.» (03.012); «Gallinelle! Gallinelle con il pizzo!» (03.045); «Il domovoj sta dove sta la famiglia. È la regola.» (06.032); «Brava, Veročka.» (06.038); «Vecchio domovoj scemo e permaloso.» (11.040); «Andiamo. Ho fame.» (11.052).
- **Rapporto e variabili**: `rap_foma` (0, max +3): sale con pane/latte lasciati da Vera in libero, la candela, la ricerca; effetti: battute più affettuose, chiama Vera per nome già dal cap. 6 (dal libro: prima volta in 06.038; mai prima).
- **Chi lo vede**: Vera sempre; Mattia lo sente; Giulia lo sente una volta (cap. 11); gli adulti mai (sentono russare in modo vago: «il frigo fa un rumore strano»).
- **Presenza**: 1 (occhietti, starnuto, sospiro), 2, 3, 4 (voce), 5 (brontolio), 6, 7 (borbottio), 8, 9 (assente), 11, 12, 13, 14.
- **Animazioni**: ANI-FOM-01 mano che esce dalla scarpa, tasta, afferra pane/sale (02.023); ANI-FOM-02 esce dalla scarpa; ANI-FOM-03 si guarda intorno offeso, alza le braccia (02.028); ANI-FOM-04 annusa l'aria; ANI-FOM-05 giro della cucina strisciando la barba; ANI-FOM-06 infila la testa dietro il frigo ed esce impolverato; ANI-FOM-07 spinge il lapot' e ci salta dentro; ANI-FOM-08 in piedi sul lapot' per sembrare più alto (03.038); ANI-FOM-09 si arrabbia, salta giù, pugni agitati; ANI-FOM-10 seduto sul lavandino con i piedi a penzoloni (06.018) e sobbalzo; ANI-FOM-11 si tira la barba; ANI-FOM-12 seduto a gambe incrociate con le mani verso la fiamma (06.037); ANI-FOM-13 sale sedia→tavolo; ANI-FOM-14 raccoglie il pane, lo spolvera, si trascina via (08.052); ANI-FOM-15 seduto immobile «come un sasso» sul lapot' verso nord (11.005); ANI-FOM-16 si gira e guarda; ANI-FOM-17 si accoccola nella scarpa con la barba come coperta (11.051); ANI-FOM-18 piccolo inchino con la barba (13.045); ANI-FOM-19 firma con l'impronta di farina; ANI-FOM-20 russa dietro il frigo (solo suono + respiro visibile se illuminato); ANI-FOM-21 starnuto/sospiro nella scarpa (cap. 1: la borsa si muove).
- **Citazioni**: «Era alto come una bottiglia d'acqua da un litro e mezzo.» (02.025).

### Le Donne di Fora (comune)
Figure del folklore siciliano (Pitrè, appendice AP); nel libro tre, con nomi inventati (AP). Entrano **dal buco della serratura** come una nebbia bianca e luminosa, si raccolgono sul pavimento e **prendono forma dal basso**: «Prima una gonna. Poi una vita stretta. Poi due braccia con dei braccialetti che tintinnavano. Poi una testa» (03.021). **Semitrasparenti**, la gonna resta **nebbia** che scende «come una cascata» e **galleggiano un dito sopra il legno** (08.015). Profumo di **rosmarino, lenzuola stese al sole e qualcosa di dolce e antico come le chiese** (03.016), reso con particelle e suono (D-22). Braccialetti che tintinnano (SFX). Vengono **martedì, giovedì e sabato**. Altezza riferita alla figura formata (la gonna di nebbia tocca terra). Specifica VFX: `ART_BIBLE.md` §11.
- **Movimento comune**: scivolano senza passi (spostamento fluido a 0,6 m/s con ondeggiare della gonna), si girano tutte insieme (03.036); uscendo tornano nebbia dall'alto in basso e rientrano dalla serratura.
- **Chi le vede**: solo Vera; le nonne sentono il rosmarino e l'aria più fresca (13.038); Mattia sente le voci di notte («le signore», 04.048).
- **Animazioni comuni**: ANI-DON-01 formazione dal basso (shader + mesh che emerge, 4 s); ANI-DON-02 scioglimento in nebbia e uscita dalla serratura (3 s); ANI-DON-03 galleggiamento idle; ANI-DON-04 scivolare; ANI-DON-05 seduta «un dito sopra» la sedia; ANI-DON-06 voltarsi insieme.

### PG-ROSALIA — Donna Rosalia
- **Ruolo**: la prima e capo delle tre.
- **Aspetto**: **alta** (178 cm), **elegante**; **abito lungo color vino** (bordeaux `#6E2433`) con corpetto a vita stretta stile fine Ottocento; **capelli raccolti in alto con un pettine di tartaruga**; **ventaglio** in mano (pizzo nero e stecche di tartaruga); viso **bellissimo e severo, come le statue delle sante nelle processioni** (03.022); **occhi neri e lucidi** (03.054); braccialetti d'oro sottili.
- **Movimento**: lento, controllato; il ventaglio sotto il mento, si chiude **con uno schiocco** (03.036, 12.061), si apre lentamente (03.054, 08.026); passa il dito sui mobili e guarda il dito (03.026).
- **Voce**: contralto gelido, scandito, siciliano colto; dice «cose gelide, pianissimo, che erano peggio degli urli» (08.036).
- **Modi di dire dal libro**: «Vediamo come la tengono, questa casa.» (03.025); «Polvere. Di nuovo.» (03.027); «Questa casa è nostra. Noi siamo le Donne di Fora.» (03.044); «Vera Russo. Figlia di Salvatore. Vieni qui.» (03.055); «Qui nelle scarpe si mettono i piedi.» (04.008); «Qui sei forestiero. E i forestieri, prima o poi, se ne vanno.» (08.049); «Anche noi, una volta, eravamo forestiere.» (12.051); «Se volete restare, restate.» (13.042).
- **Variabili**: `rap_rosalia` (default −1).
- **Presenza**: 3, 4, (6 filo di nebbia), 7, 8, 12, 13, 14 (nebbia), notti libere.
- **Animazioni specifiche**: ANI-ROS-01 ventaglio apre/chiude/schiocco; ANI-ROS-02 dito sul mobile; ANI-ROS-03 indica col ventaglio (04.004); ANI-ROS-04 inchino col ventaglio (13.045); ANI-ROS-05 occhi chiusi, ricordo (12.047); ANI-ROS-06 sorriso piccolo e storto (12.059).

### PG-NINA — Donna Nina
- **Aspetto**: **più bassa e più tonda** (158 cm), **vestita di verde** (verde bosco `#2F5A3A`), **collana di perle** a tre fili, **bocca che non sta mai ferma** (03.024), riccioli grigi raccolti con una retina [NUOVO], scialle di pizzo.
- **Movimento**: agitato, mani alle perle (03.040), si copre la bocca per non ridere (04.006), smorfie.
- **Voce**: mezzosoprano stridula quando urla (08.036), pettegola, veloce, siciliana.
- **Modi di dire**: «Da quando è arrivata la forestiera, qui nessuno pulisce più come si deve.» (03.028); «Storte, Donna Rosalia. Con le mollette spaiate.» (03.030); «E questa cos'è? Un topo?» (03.040); «Lasciate fare a me. Gli faccio cagliare il latte» (04.028); «Un topo con la barba!» (08.023).
- **Variabili**: `rap_nina` (default −2).
- **Presenza**: come Rosalia.
- **Animazioni**: ANI-NIN-01 mano alle perle; ANI-NIN-02 risata coperta; ANI-NIN-03 sbuffo e smorfia; ANI-NIN-04 urla agitando le braccia.

### PG-TINA — Donna Tina
- **Aspetto**: **giovane, quasi una ragazza** (163 cm), **vestito celeste** (`#A9C9E2`), **capelli sciolti** lunghi, castano chiaro mossi; **occhi spalancati** curiosi (03.024); piedi che non si vedono (gonna di nebbia).
- **Movimento**: curiosa, allunga il collo (03.031), si guarda intorno, sorride di nascosto (12.024), esita (08.050).
- **Voce**: soprano leggero, dolce, meravigliato; siciliano morbido.
- **Modi di dire**: «C'è un odore strano. Di pane. Pane nero.» (03.033); «Qui non ci sono cavalli» (03.042); «Lei ci vede» (03.051); «È vero. Lei è tutte e due le cose. Per questo ci vede. Ci vede tutti.» (08.045); il racconto di 12.046.
- **Variabili**: `rap_tina` (default 0; sale facilmente).
- **Animazioni**: ANI-TIN-01 allunga il collo verso la cucina; ANI-TIN-02 piccolo cenno con la testa (12.032); ANI-TIN-03 passo avanti con la gonna che si allarga (12.046); ANI-TIN-04 esitazione e bocca che si apre (08.050).

### PG-OMBRA — l'ombra con la scopa (cap. 14)
- **Ruolo**: aggancio al libro 2 (la Befana); solo un'ombra sul tetto contro le nuvole.
- **Aspetto**: silhouette **lunga e storta, con una gobba**, scopa di rami secchi, gonne al vento; mai vista da vicino (sagoma 2D/volumetrica a 25–40 m).
- **Voce**: vecchia arrabbiata, «offesissima», **in siciliano stretto** (D-51) portata dal vento; sottotitolo con la frase del libro (14.042–043).
- **Suono**: «Fsss. Fsss.» (14.039) rami trascinati sulle tegole.
- **Animazioni**: ANI-OMB-01 volo che si allontana (traiettoria su spline, 6 s).

---

## 3. Altri personaggi

### PG-NICOLO — Nicolò
- **Ruolo**: compagno di banco di Vera.
- **Età/altezza**: 11–12 anni, 148 cm, magro.
- **Aspetto**: **occhiali con la montatura blu** (03.001); capelli neri a spazzola; maglietta con un T-rex; zaino pieno di **carte di dinosauri (140)**.
- **Movimento**: mostra le carte una per una; spinge gli occhiali sul naso; dà gomitate (12.006).
- **Voce**: ragazzino, entusiasta, parla veloce di dinosauri, accento siciliano.
- **Modi di dire**: «Tu sei russa?» «Quale metà?» (03.002–004).
- **Variabili**: `rap_nicolo` (0).
- **Spiriti**: niente.
- **Presenza**: 3, 12, mondo libero (scuola, piazza IX Aprile).
- **Animazioni**: ANI-NIC-01 mostra carta; ANI-NIC-02 sistema occhiali; ANI-NIC-03 gomitata; ANI-COM-10/11.

### PG-PROF-MAT — la professoressa di matematica
- **Aspetto**: 50 anni, 165 cm, capelli corti grigi, occhiali da lettura sulla catenella, gessetto; «scriveva i numeri come se la lavagna le avesse fatto un torto» (03.001).
- **Movimento**: gesti secchi alla lavagna. **Voce**: secca, precisa.
- **Animazioni**: ANI-PMA-01 scrive con forza alla lavagna; ANI-PMA-02 si volta verso la classe.
- **Presenza**: 3, 12 (citata), mondo libero.

### PG-PROF-MUS — il professore di musica
- **Aspetto**: 60 anni, 175 cm, capelli bianchi lunghi dietro, giacca di velluto a coste, foulard; «parlava solo di Bellini» (03.001).
- **Voce**: tenore teatrale, accento catanese (Bellini era catanese). **Animazioni**: ANI-PMU-01 dirige con la matita; ANI-PMU-02 canticchia un'aria (solo testo + mormorio).
- **Presenza**: 3, mondo libero.

### PG-PROF-STO — il professore di storia [NUOVO nome di ruolo; il libro dice «il professore», 12.006]
- **Aspetto**: 40 anni, 170 cm, barba curata, maglione. **Presenza**: 12. **Animazioni**: ANI-COM-04/15.

### PG-DOTTORE — il dottore
- **Aspetto**: «un signore anziano con la borsa di cuoio che conosceva tutti nella scalinata» (09.013); 72 anni, 170 cm, panciotto, occhiali tondi, stetoscopio.
- **Voce**: calma, paterna, siciliana. **Battute**: 09.013–014 («Stanca dentro.»).
- **Presenza**: 9; mondo libero (scalinata, saluta).
- **Animazioni**: ANI-DOT-01 visita (misura la febbre, ascolta); ANI-DOT-02 parla sulla porta.

### PG-SIGNORE-AER — il signore dell'aeroporto
- **Ruolo**: comparsa del cap. 1 a cui Mattia spiega la babuška (01.007–008).
- **Aspetto** [NUOVO]: 60 anni, 175 cm, panama chiaro, camicia celeste a maniche corte, giornale piegato sotto il braccio, attende la moglie.
- **Voce**: siciliana bonaria; battute variabili (cap01, D-57).
- **Animazioni**: ANI-SIG-01 si allontana di due passi (01.008); ANI-SIG-02 guarda il tabellone; ANI-COM-01/04.

### PG-GATTO-ROSSO — il gatto rosso del quarto gradino
- **Aspetto**: gatto europeo rosso tigrato, grosso, un orecchio con una tacca; dorme sul **quarto gradino** della scalinata di Casa Russo e **apre un occhio** (02.008).
- **Comportamento**: dorme dove devi mettere il piede (02.001); fotografabile (album Gatti, FOT-GAT-01); ricompensa della collezione gatti (GDD §4).
- **Animazioni**: ANI-GAT-01 dorme; ANI-GAT-02 apre un occhio; ANI-GAT-03 si stira e cammina; ANI-GAT-04 si sposta di malavoglia; ANI-GAT-05 sotto il portone col pelo bagnato e l'aria offesa (14.002).

### Comparse ricorrenti (specifica sintetica; battute in `NARRATIVA/comparse.md`)
| ID | Comparsa | Dove/quando | Aspetto | Animazioni |
|---|---|---|---|---|
| PG-CMP-TED (×4) | Turisti tedeschi «abbronzati in anticipo» (01.016) | aeroporto cap. 1; funivia cap. 10 | sandali con calze, cappelli, zaini, pelle arrossata | trolley, foto, ANI-COM |
| PG-CMP-PAL (×8) | Squadra di pallavolo | aeroporto cap. 1 | tute uguali blu e bianche senza marchi, borsoni | camminata di gruppo, ridono |
| PG-CMP-PRETE | Prete con la valigia a fiori | aeroporto cap. 1 | clergyman nero, 55 anni, valigia rigida a fiori rosa | trascina la valigia, saluta |
| PG-CMP-AER (×12) | Viaggiatori e attese | aeroporto | varietà di età | attesa, cartelli, abbracci |
| PG-CMP-BARIS | Barista dell'aeroporto | bar aeroporto | 30 anni, camicia nera | macchina del caffè |
| PG-CMP-AUT | Autista di taxi / addetto parcheggio | parcheggio | gilet giallo | gesti |
| PG-CMP-SCA (×6) | Abitanti della scalinata (signora dei gerani, vicino coi gelsomini, ragazzo col motorino, ecc.) | scalinate | tipici del luogo | annaffiare, stendere, salutare |
| PG-CMP-COR (×20) | Turisti e paesani del Corso | Corso Umberto | per stagione (pantaloncini e infradito a metà ottobre, 06.001) | crowd |
| PG-CMP-BARC (×8) | Clienti del bar di papà | bar | paesani e turisti | ordinare, bere, leggere |
| PG-CMP-SCU (×18) | Compagni di classe | scuola | 11–12 anni | banco, intervallo |
| PG-CMP-STA (×3) | Signore col giornale, coppia di turisti che fotografa il soffitto, gatto bianco (11.003) | stazione | — | leggere, fotografare, dormire |
| PG-CMP-FUN | Bigliettaio della funivia | funivia | divisa senza logo | biglietti |

---

## 4. Matrice «chi vede cosa»

Legenda: **V** vede · **S** sente · **T** vede tracce (briciole, impronte, cose spostate) · **P** percepisce (profumo, freddo, presenza) · **Sa** sa che esistono · **–** niente (spiega con cose normali).

| Personaggio | Fomà cap.1 (starnuto, sospiro) | Fomà capp.2–8 | Fomà assente (9–10) | Fomà capp.11–14 | Donne capp.3–8 | Donne capp.12–14 | Casa malata (7–12) | Scopa sul tetto (14) |
|---|---|---|---|---|---|---|---|---|
| Vera | S (+ occhietti) | V S | — (cerca) | V S | V S | V S | V S P | V(ombra) S |
| Mattia | – | S T | T (impronte, odore) | S (mezzo e mezzo, 11.058) | S (voci) | S | P | – (non sente, 14.041) |
| Giulia | – | – | – | S una volta (11.065) | – | – | P (spiegazione: tutto da quando è arrivata lei) | – |
| Babuška | Sa (finge) | Sa | Sa (lo chiede, 09.025) | Sa | – | P (13.038) | Sa (tace) | – |
| Concetta | – | – (non sa di Fomà; attribuisce i dispetti alla babuška) | – | Sa (13.033) | Sa (rito, 05.018) | Sa + P | Sa (tace, 07.013) | – |
| Irina | – (riconosce il lapot') | – (formiche) | – | – | – | – | – (umidità, idraulico) | – |
| Salvo | – | – (topi) | – | – | – | – | – (umidità, elettricista) | – |
| Nicolò, prof., dottore, comparse | – | – | – | – | – | – | – | – |

Nota sulla babuška e Concetta: nessuna delle due **vede** gli spiriti (13.038 «Non le vedevano, lo capii subito»); entrambe *sanno* e fanno le offerte. Concetta non sa di Fomà fino alla notte dei Morti (13.027 «Anche lei?»).

## Fonti

- Manoscritto *Il domovoj nella scarpa* (ID in `work/libro.txt`), appendice «Chi abita in Casa Russo» (AP.001) e «Le due tradizioni» (AP).
- Documento di gioco §6; `FASI_DI_SVILUPPO.md` §2 #21–#24.
- [Giuseppe Pitrè e le Donne di Fora — voce «Donne di fuori», Wikipedia](https://it.wikipedia.org/wiki/Donne_di_fuori)
- [Domovoj — Wikipedia](https://it.wikipedia.org/wiki/Domovoj)
