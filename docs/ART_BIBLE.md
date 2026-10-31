# Art Bible

Stile: **atmosferico realistico** (documento di gioco §3). Riferimento di qualità: la vertical slice del capitolo 1 (D-02). Le funzioni del motore citate sono di Babylon.js 9.x (D-59); i preset di qualità sono definiti in `TDD.md` §12 e qui si indicano solo gli obiettivi visivi.

## 1. Pilastri di stile
1. **Luce vera di un luogo vero**: la luce di Taormina per data e ora (sole calcolato, TDD §5) è il primo strumento narrativo; la palette segue il calendario, da settembre caldo a novembre piovoso.
2. **Materiali che si toccano**: pietra consumata, intonaco scrostato, maiolica, ferro battuto, legno vissuto. Niente superfici «nuove» se non dove la storia lo chiede (l'aeroporto, la funivia).
3. **Il quotidiano è realistico, il magico è luminoso e morbido**: gli spiriti sono resi realisticamente nei materiali (pelo, stoffa) ma con una luce propria leggermente più fredda e un'aura morbida; mai effetti «da videogioco» saturi.
4. **Sguardo di una dodicenne**: camera a 1,41 m, ottiche naturali, profondità di campo solo nei primi piani narrativi.
5. **Niente marchi**: insegne, veicoli, abbigliamento e prodotti generici.

## 2. Palette oraria e mensile

### 2.1 Ora del giorno (valori di riferimento per cielo, luce diretta, ombre)
| Momento | Cielo zenit | Luce diretta | Ombre / ambiente | Temperatura | Note |
|---|---|---|---|---|---|
| Alba (6:45 set) | `#7F95B8` | `#F2B98A` | `#3E4A63` | 3200 K | foschia sul mare |
| Mattina | `#5E8FC9` | `#FFF1DC` | `#5C6E86` | 5600 K | contrasti netti sulle scalinate |
| Mezzogiorno | `#4F86C6` | `#FFFFFF` | `#6A7A8E` | 6000 K | luce dura, ombre corte, bianco degli intonaci |
| Pomeriggio | `#6A96CC` | `#FFE2B0` | `#6B6A80` | 4800 K | pietra dorata |
| Tramonto | `#E9A36A` → `#5B6FA6` | `#FF9A55` | `#4A3E5E` | 2600 K | l'Etna viola, poi nera (06.006, 06.017) |
| Crepuscolo blu | `#2E4374` | — | `#1E2A44` | 9000 K (cielo) | lampioni accesi 2200 K |
| Notte | `#0E1630` | luna `#C9D6F0` | `#0A0F1E` | 4100 K luna | sodio `#FFB35C` dei lampioni |
| Spiriti (notte) | — | nebbia `#E8F2FF`, alone `#BFD7E8` | — | 7500 K | sempre più fredda della scena |

### 2.2 Mese
| Periodo | Dominante | Accento | Saturazione | Atmosfera |
|---|---|---|---|---|
| Settembre (capp. 1–4) | oro caldo `#E8B86B` | blu mare `#2F6FA3` | +8% | aria limpida, cicale, gelsomini |
| Inizio ottobre (5–6) | ambra `#D9A15E` | viola dell'Etna `#6B4E7A` | +4% | giorni ancora estivi, tramonti più presto |
| Seconda metà di ottobre (7–12) | ocra spento `#BFA27A` | verde salvia `#8EA58B` | −4% (−10% nelle scene della casa malata) | luce più bassa, ombre lunghe |
| Novembre (13–14) | grigio perla `#9CA3AA` | verde lucido dopo la pioggia `#4F7F5A`, giallo ombrello `#E7C23A` | −8% | pioggia, riflessi, nuvole veloci |

## 3. Grading (obiettivi)
- **Tone mapping ACES** (FASI §16), esposizione automatica limitata (±1 EV) con adattamento 1,5 s.
- LUT per mese (4) + LUT «casa malata» (desaturazione verde-grigia −10%, contrasto −5%) + LUT «notte degli spiriti» (ombre fredde +blu, alte luci invariate).
- Grana leggera (intensità 6–8 su 100 sul preset Alto/Ultra), vignettatura 0,15 (0 in mondo libero di giorno, 0,25 nelle scene notturne).
- Bloom morbido (soglia 1,1, intensità 0,25; 0,45 sulla nebbia delle Donne).

## 4. Regole di illuminazione
| Situazione | Regola |
|---|---|
| Esterni di giorno | sole dinamico + cielo fisico; lightmap baked con AO e rimbalzi per architettura; ombre a cascata (4 cascate PC, 2 tablet) |
| Interni di giorno | luce dalla finestra baked + sonde d'ambiente (reflection probe/IBL locale) per i personaggi |
| Interni di sera | lampade come luci reali (clustered lighting di Babylon 9 per > 8 luci) |
| Notte esterna | lampioni a sodio 2200 K (puntiformi con ombre solo per i 4 più vicini), luna da calendario |
| Blackout (cap. 7, 9) | luce minima di sicurezza (luna/lampione) mai sotto 0,02 lux equivalenti; torcia come luce principale |
| Spiriti | ogni spirito ha una luce propria debole (Fomà: rim light calda 2700 K tenue; Donne: luce volumetrica fredda dalla nebbia) |
| Pioggia (cap. 14) | superfici bagnate (roughness × 0,35, albedo × 0,8, pozzanghere con SSR), cielo coperto, luce diffusa 7000 K |

## 5. Libreria dei materiali siciliani (PBR)
Valori metallic/roughness lineari. Fonti: texture CC0 di Poly Haven e ambientCG rielaborate, o materiali procedurali baked in Blender (`PIPELINE_ASSET.md` §4). Tutte le fonti in `CREDITI.md`.

| Materiale | Albedo (sRGB, gamma) | Roughness | Metallic | Normal / dettagli | Fonte di partenza |
|---|---|---|---|---|---|
| Intonaco a calce giallo paglierino | `#D8C59A`–`#E4D3A8` | 0,85–0,95 | 0 | screpolature, macchie di umidità (decal) | ambientCG «Plaster» + maschere procedurali |
| Intonaco rosa antico / ocra | `#D9A98F` / `#C99B5C` | 0,85–0,95 | 0 | idem | idem |
| Pietra di Taormina (calcare chiaro) | `#C9BCA6` | 0,6–0,85 (consumata 0,45) | 0 | bordi arrotondati, gradini lucidati al centro | Poly Haven «rock/stone» + bake |
| Pietra lavica (basole del Corso) | `#3B3A3A` | 0,55–0,75 (bagnata 0,2) | 0 | porosità, giunti | ambientCG «PavingStones» |
| Maiolica di Caltagirone (riggiole) | motivi blu `#2C5C9E`, giallo `#E3B23C`, verde `#3E7D4F` su bianco `#EFE9DC` | smalto 0,08–0,15 | 0 | craquelure; clearcoat 0,8 | dipinta proceduralmente in Blender (motivi originali) |
| Ferro battuto (ringhiere) | `#2A2A2A` vernice / ruggine `#7A4A2A` | 0,45 / 0,8 | 0,0 vernice / 0,6 metallo scoperto | ruggine nei giunti | ambientCG «Metal» + maschere |
| Persiane verdi | `#3F6B4A` (sbiadito `#6E8F6F`) | 0,7 | 0 | vernice scrostata sul legno | procedurale |
| Granito dell'aeroporto | `#8C8F93` con macchie | 0,12 | 0 | lucido, SSR | ambientCG «Granite» |
| Marmo (stazione, Duomo) | `#E6E1D8` | 0,2–0,35 | 0 | venature | Poly Haven «marble» |
| Legno vissuto (portoni, tavoli) | `#6B4A2E`–`#9A6B3F` | 0,55–0,8 | 0 | usura sugli spigoli | Poly Haven «wood» |
| Cemento / asfalto | `#7E7B76` / `#3A3A3B` | 0,9 / 0,85 | 0 | crepe, macchie d'olio | ambientCG |
| Tessuti (cotone, lana, lino) | per costume | 0,8–0,95 | 0 | **sheen** 0,3–0,6 (lana del cappotto verde 0,6) | bake da Tripo/Hitem3D + dettaglio tiling |
| Corteccia del lapot' (tiglio) | `#C9B48A`–`#A89268` | 0,75 | 0 | fibre intrecciate, punta consumata e scurita | da modello 1,5 M (REQ-PRP-001) |
| Vegetazione (limone, gerani, ulivi, fichi d'India, bouganville) | foglie `#3E6B2F`–`#5E8A3A` | 0,5–0,7 | 0 | translucency 0,3 | Poly Haven/«Quixel» esclusi (vedi CREDITI); foglie da CC0 + modelli procedurali |

## 6. Densità di texel e risoluzioni

| Classe | Texel density (px/m) | Risoluzione massima della mappa | Mappe | Note |
|---|---|---|---|---|
| Architettura vicina (Casa Russo, interni, scalinata) | 1024 px/m | tiling + atlas 2048 | albedo, normal, ORM + lightmap (UV2) | dettagli con decal |
| Architettura del Corso (facciate kit) | 512 px/m | atlas 2048 | idem | kit modulare |
| Architettura lontana (> 150 m) | 128 px/m | atlas 1024 per cella | albedo+normal | LOD2/impostor |
| Personaggi principali (corpo) | ~ 1100 px/m | 2048 corpo + 2048 testa (4096 testa su Ultra per babuška, Fomà) | albedo, normal, ORM, (subsurface mask) | |
| Comparse | ~ 600 px/m | 2048 unica | albedo, normal, ORM | |
| Fomà | testa 4096 (Ultra) / 2048 | + mappe del pelo (densità, lunghezza, direzione) | | |
| Oggetti eroe (lapot', borsa a fiori, quaderno, telefono, ditale, cucchiaio) | 2048–4096 px/m | 2048 (4096 lapot' e quaderno su Ultra) | albedo, normal, ORM | visti a 30–50 cm |
| Oggetti secondari | 512–1024 px/m | 1024 | albedo, normal, ORM | |
| Lightmap | 32 px/m (interni 64) | 2048 per cella | HDR (RGBM o RGBD) | TDD §5 |

Su tablet (preset Medio) tutte le texture scendono di un livello (mip 1) salvo lightmap e testa dei personaggi in primo piano.

## 7. Usura e decal
- Ogni superficie ha almeno un livello di usura: sporco ai piedi dei muri (gradiente 0–40 cm), colature sotto i davanzali, consumo al centro dei gradini, macchie d'umidità.
- Decal (proiettati, max 64 per cella su PC, 24 su tablet): manifesti strappati, edicole, impronte di farina (decal speciali con visibilità angolare, SIS-23), **crepa della casa** (6 stadi con maschera di crescita), briciole, foglie.
- Pioggia: decal di pozzanghere e mappa di bagnato globale (D-15 del meteo).

## 8. Personaggi: rendering
| Elemento | Tecnica | Valori guida |
|---|---|---|
| Pelle | PBR con **subsurface** (translucency/scattering di PBRMaterial) e mappa di spessore | colore di scattering `#C9634B`; roughness 0,45–0,55; micro-normal di pori su volto |
| Occhi | mesh separate: sclera + iride con parallasse + cornea con clearcoat; riflesso sempre presente | iride grigia per Vera/babuška/Mattia/Kolja |
| Capelli | hair cards (alpha test + alpha blend ordinato) con anisotropia (PBR anisotropy) | 2 livelli di card, ombre a contatto |
| Stoffa | PBR con **sheen** | lana 0,6, cotone 0,3, seta delle Donne: vedi §11 |
| Rughe e espressioni | blend shapes (FACS ridotti: 32) + normal map di rughe dinamiche per babuška e Concetta | primo piano del cap. 1 (SCN-01-13) |
| LOD | LOD0 40 000 tri (Fomà 40 000 + pelo), LOD1 15 000, LOD2 5 000 | FASI §17 |

### 8.1 Fomà: pelo e barba
- **Pelo**: tecnica a gusci (shell fur) con 24 gusci su Ultra, 16 su Alto, 10 su Medio, 6 su Basso; mappa di densità/lunghezza/pettinatura generata in Blender dalle curve del sistema hair; colore grigio-tabby con radice più scura; luce di bordo calda.
- **Barba**: mesh a ciocche (12 ciocche principali) su catena di ossa (8 ossa) con simulazione di molla e collisione col pavimento e il corpo; la parte a terra strascica con attrito; quando è seduto si arrotola in grembo (posa di animazione dedicata).
- **Naso**: materiale con clearcoat e parametro di «rossore» (0 normale, 0,5 «più rosso del solito», 1 «rosso come la camicia») e una variante «viola» (03.041).
- **Camicia rossa** lino grezzo `#9E2B25` con sheen 0,35; cintura di corda (geometria + normal).
- **Occhi**: neri, lucidi, riflesso netto (D-47). Nel cap. 1 si vedono **solo** gli occhi nel buio della scarpa: due riflessi caldi su sfere nere per 1,2 s.

## 9. Camera
| Voce | Valore |
|---|---|
| Altezza occhi | 1,41 m (accovacciata 0,95, in ginocchio 0,70, seduta in auto 1,08) |
| FOV | 72° verticale-equivalente su PC 16:9, 70° su tablet 4:3/3:2; opzione 60–90° |
| Head bob | 1,2 cm a 1,9 Hz in camminata; disattivabile |
| Primi piani (DOF) | focale equivalente 50–85 mm (FOV 27–40°), f/1,8–f/2,8, messa a fuoco sugli occhi del personaggio |
| Dialoghi | FOV ridotto di 6° in 0,4 s, DOF leggero f/4 sul personaggio |
| Quaderno | quaderno in primo piano a 38 cm, sfondo con DOF f/2 |
| Cinematiche | barre 2,39:1, movimenti lenti (≤ 25°/s di rotazione), sempre dal punto di vista di Vera salvo i neri |

## 10. Post-processing per tipo di scena
| Tipo | Effetti e valori |
|---|---|
| Interno di giorno | SSAO (raggio 0,5 m, intensità 0,8), SSR sui pavimenti lucidi, bloom 0,2, grana 6, vignetta 0,1, TAA/FXAA secondo preset |
| Esterno al tramonto | luce volumetrica (raggi tra le case) intensità 0,3, bloom 0,3, foschia di distanza (densità 0,0006), LUT del mese |
| Notte con spiriti | luce volumetrica sulla nebbia 0,6, bloom 0,45, vignetta 0,25, grana 8, cromatica leggera 0,15 sui bordi solo durante le apparizioni |
| Pioggia | SSR forte sulle superfici bagnate, gocce sulla camera disattivate (prima persona realistica: niente gocce su «lenti»), particelle di pioggia GPU, nebbia di distanza 0,0012 |
| Aeroporto | SSR sul granito, polvere nella luce (particelle GPU nei fasci del sole, 400 al preset Alto, scalate dal moltiplicatore del preset: 160 su Medio) |
| Auto (cap. 1) | riflessi del finestrino, fumo dell'Etna (particelle GPU + mesh volumetrica lontana) |

## 11. Donne di Fora — specifica VFX
1. **Ingresso dal buco della serratura** (3 s): un getto di nebbia bianca luminosa esce dal foro 9 × 18 mm «come il fumo da un camino» (03.021): particelle GPU (PC 6 000 / tablet 1 500) con velocità iniziale 0,6 m/s, rallentamento e caduta, luminanza 1,4 (HDR), colore `#E8F2FF`.
2. **Raccolta sul pavimento** (2 s): la nebbia forma un disco di 1,4 m di diametro, alto 10 cm, con turbolenza (rumore 3D animato in Node Material) e luce volumetrica.
3. **Formazione dal basso** (4 s per Donna, sfalsate di 6 s): shader di dissolvenza con soglia che sale dal pavimento alla testa; nell'ordine del libro: **gonna → vita stretta → braccia con i braccialetti → testa** (03.021). Il bordo della soglia è luminoso (fascia di 3 cm, intensità 2,0). I braccialetti suonano quando compaiono (SFX-018).
4. **Figura formata**: corpo e vestito resi come stoffa reale ma **semitrasparenti** (opacità 0,72 tronco/testa, 0,55 braccia), fresnel luminoso sui bordi; la **gonna resta nebbia** sotto il ginocchio: volume di particelle + mesh con dissolvenza verso il basso, che «scende come una cascata» e si allarga sul pavimento (08.015, 12.046); le Donne galleggiano 2 cm (un dito) sopra le superfici.
5. **Colori**: Rosalia vino `#6E2433` (nebbia tinta `#F2E4EA`), Nina verde `#2F5A3A` (nebbia `#E6F2E8`), Tina celeste `#A9C9E2` (nebbia `#EAF4FB`). Oggetti: ventaglio di pizzo nero e tartaruga (Rosalia), pettine di tartaruga, perle (Nina, specular forte), capelli sciolti mossi da un vento che non c'è (Tina).
6. **Profumo**: filamenti dorati sottilissimi (particelle a nastro, 40–80) che seguono le correnti verso Vera; più forti con il rosmarino in scena.
7. **Racconto di Tina** (cap. 12): la nebbia della sua gonna disegna sul pavimento tre quadri a rilievo (porte chiuse, porta aperta con candela, tavolo col pane): mesh di nebbia generate da maschere 2D estruse, 4 s ciascuno.
8. **Uscita**: dissolvenza dall'alto in basso (3 s) e risucchio della nebbia nel buco della serratura.
9. **Budget**: costo GPU della scena con tre Donne ≤ 3,5 ms su PC medio, ≤ 6 ms su tablet (TDD §12); risoluzione delle particelle a metà su tablet.

## 12. Il quaderno di scienze (D-41: biro blu + matita)
- **Oggetto**: quaderno A5 a quadretti da 5 mm, copertina rigida verde salvia con etichetta «SCIENZE — Vera Russo — 1ªB»; margine rosso; 96 pagine.
- **Tratti**: scritte a **biro blu** (`#1E3F8C`, tratto 0,5 mm con piccole sbavature), disegni e schizzi a **matita grafite** (HB/2B, `#4A4A4A`, sfumature), cancellature a biro (righe) e a gomma (alone). Nessun altro colore (eccezione: il tocco rosso del margine stampato).
- **Grafia**: font OFL «Caveat» per la grafia di Vera (con varianti di glifi alternati per naturalezza), «Caveat Brush» per i titoli in stampatello; versione leggibile «Noto Sans» (opzione).
- **Layout delle pagine (esempi)**:
  | Pagina | Composizione |
  |---|---|
  | Cellule (prima pagina) | titolo a biro «LA CELLULA» sottolineato due volte; disegno a matita di una cellula vegetale con frecce e nomi (parete, membrana, nucleo, cloroplasti); voto «8» a penna rossa della prof. (unico rosso, stampato) |
  | Fotosintesi | schema sole → foglia → zucchero con frecce a biro; foglia disegnata a matita |
  | Indizi | data a biro in alto a destra, voce come elenco puntato; schizzo a matita dell'oggetto (borsa, scarpa, occhietti) nel margine |
  | Parole russe | colonna sinistra cirillico a biro grande, a destra traslitterazione a matita e traduzione a biro piccola |
  | Ricordi | disegno a matita a mezza pagina (Kolja agli scacchi, nonno Turi col lumino), testo sotto |
  | Foto | foto stampate «incollate» con nastro adesivo agli angoli, didascalia a biro |
  | Sospettati e frecce | elenco SOSPETTATI in stampatello, ritratti a matita (Fomà «che non gli somiglia per niente», Rosalia col ventaglio «venuto bene», 14.020), frecce a biro dagli indizi; frecce tratteggiate per «da verificare» |
  | Il Patto | clausole numerate a biro in bella; alone di nebbia (macchia chiara leggermente lucida) e impronta di farina (polvere bianca in rilievo) |
  | CASA RUSSO | titolo in stampatello grande; elenco con piccoli schizzi; ultima riga staccata; in fondo «Non ero divisa. Ero un ponte.» |
- **Animazione**: scrittura progressiva (2 s), pagine che girano con fisica del foglio, ombra della mano di Vera.

## 13. Interfaccia (UI)
| Voce | Specifica |
|---|---|
| Font | sottotitoli e menu: **Noto Sans** (OFL, latino+cirillico), corsivo per i pensieri; titoli: **Caveat Brush** (OFL); grafia del quaderno: **Caveat** (OFL) |
| Dimensioni sottotitoli (1080p) | S 26 px · M 32 px · L 38 px · XL 46 px; interlinea 1,3; max 2 righe da 42 caratteri |
| Colori | testo `#FFF8EC`; nomi dei personaggi: Vera `#9EC9FF`, babuška `#E8C07A`, Irina `#C9B6FF`, Salvo `#FFB38A`, Giulia `#FF9EC4`, Mattia `#A8E6A1`, Concetta `#FF8A8A`, Fomà `#E6A86B`, Rosalia `#D88A9E`, Nina `#9ED3A8`, Tina `#A9D3F0`; suoni degli spiriti `#BFD7E8` |
| Sfondo dei sottotitoli | nero 55% (opzione 0–100%), angoli 6 px |
| Icone | disegnate a biro e matita come il quaderno (telefono, quaderno, pausa, azione); contorno chiaro per il contrasto su sfondi scuri |
| Interattivi | contorno caldo `#F2D49B` 2 px (4 px in alto contrasto) |
| Marker discreto | cerchio 14 px con punto, `#F2D49B` al 70% |
| Menu | pagine del quaderno in 3D sfocato dietro, voci scritte a biro, selezione sottolineata a matita |
| Contrasto | WCAG AA minimo per tutto il testo |

## 14. Coerenza con i budget
Le densità e le risoluzioni di §6 rispettano i budget di `TDD.md` §12 (texture ≤ 1,5 GB PC, ≤ 450 MB tablet, D-85). Gli effetti di §10–11 sono attivati per preset secondo la tabella dei preset del TDD.

## Fonti
- [Babylon.js — PBR (sheen, clearcoat, subsurface, anisotropy)](https://doc.babylonjs.com/features/featuresDeepDive/materials/using/introToPBR)
- [Babylon.js — Fur Material](https://doc.babylonjs.com/toolsAndResources/assetLibraries/materialsLibrary/furMat)
- [Annuncio Babylon.js 9.0 (clustered lighting, volumetric lighting)](https://blogs.windows.com/windowsdeveloper/2026/03/26/announcing-babylon-js-9-0)
- [Poly Haven — licenza CC0](https://polyhaven.com/license)
- [ambientCG — licenza CC0](https://ambientcg.com/list)
- [Google Fonts — Caveat (OFL)](https://fonts.google.com/specimen/Caveat) · [Noto Sans (OFL)](https://fonts.google.com/noto/specimen/Noto+Sans)
- Manoscritto (03.021, 06.006, 08.015, 14.020) e `FASI_DI_SVILUPPO.md` §16.
