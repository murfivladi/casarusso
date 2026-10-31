# -*- coding: utf-8 -*-
import urllib.parse,os
def u(f): return "https://commons.wikimedia.org/wiki/File:"+urllib.parse.quote(f.replace(' ','_'))
S=[
("1. Aeroporto di Catania-Fontanarossa — atrio, bar, parcheggio (v1.0)","LUO-AER-*",[
 ("Catania International Airport (CTA) 2024-04-16.jpg","Sharon Hahn Darlin","CC BY 2.0","facciata e accesso: proporzioni, vetrate, pensiline"),
 ("Nuova Aerostazione Catania-Fontanarossa.jpg","I. M. Triolo","Pubblico dominio","volume del terminal, materiali della facciata"),
 ("Catania Neu Terminal.jpg","Eugenio Di Gioia","Copyrighted free use","fronte città del terminal"),
 ("Aeroporto di Catania Terminal Check-in.jpeg","Carlo Dani","CC BY-SA 4.0","interni: controsoffitto, illuminazione, pavimento lucido"),
 ("Wv Aeroporto di Catania banner.jpeg","Carlo Dani","CC BY-SA 4.0","banchi e lucernari, colori interni"),
 ("CTA Airport Departures and Check In.png","Artemio Mishkin","CC BY-SA 4.0","altezza della sala, segnaletica (da rendere generica)"),
 ("Catania Airport Panorama.png","Artemio Mishkin","CC BY-SA 4.0","panoramica degli interni"),
 ("Canatania-Fontanarossa departure.jpg","commonsabhay","CC BY-SA 4.0","materiali del pavimento e delle colonne"),
 ("Aeroporto di catania, veduta etna.jpg","sailko","CC BY 2.5","l'Etna dal piazzale: posizione e foschia"),
 ("Aeroporto di Catania Fontanarossa.jpeg","Carlo Dani","CC BY-SA 4.0","Etna e torre di controllo"),
 ("Fontanarossa airport (Catania) (3622396098).jpg","gnuckx","CC BY 2.0","esterni e palme"),
]),
("2. Strada Catania → Taormina (A18) e l'Etna (v1.0)","LUO-A18",[
 ("A18 me-ct.jpg","Saro96","CC BY-SA 4.0","carreggiata, guard-rail, segnaletica"),
 ("A18 in Letojanni.JPG","Abxbay","Pubblico dominio","viadotti verso Taormina"),
 ("A18-fondaco parrino.JPG","Abxbay","Pubblico dominio","tratto costiero"),
 ("Etna, view from road to Taormina (4894111979).jpg","Michal Osmenda","CC BY-SA 2.0","l'Etna dalla strada: profilo, colori"),
 ("Mount Etna from Taormina (3766419586).jpg","Jerome Bon","CC BY 2.0","pennacchio e luce"),
 ("Mount Etna from Taormina (3766422688).jpg","Jerome Bon","CC BY 2.0","Etna e costa"),
 ("Etna from Taormina 001.JPG","Viktorija O.","Pubblico dominio","profilo dell'Etna da Taormina"),
 ("Taormina with Etna 27-01-2025.jpg","Jeanne Griffin","CC BY-SA 4.0","Taormina e l'Etna insieme"),
]),
("3. Scalinate di Taormina (Casa Russo, casa di nonna Concetta) (v1.0)","LUO-SCA-01, LUO-SCA-02, LUO-CR-EXT, LUO-CON",[
 ("Taormina, Salita Badia Vecchia 2024.jpg","Cayambe","CC BY 4.0","scalinata nel settore ovest (zona D-45): gradini, muri, vasi"),
 ("Taormina, scalinata 05.jpg","Palickap","CC BY-SA 4.0","pietra consumata, ringhiere, gerani"),
 ("Taormina, scalinata 06.jpg","Palickap","CC BY-SA 4.0","prospettiva in salita"),
 ("Scale,scale di Taormina.JPG","Hein56didden","CC BY-SA 3.0","rampe e pianerottoli"),
 ("Traversa Taormina.JPG","Jeanne boleyn","CC0","vicolo laterale, intonaci"),
 ("Taormina-stairs 2.JPG","Abxbay","Pubblico dominio","gradini e piante"),
 ("Walk in Taormina's streets (3765744821).jpg","Jerome Bon","CC BY 2.0","luce tra le case"),
 ("Walk in Taormina's streets (3766544518).jpg","Jerome Bon","CC BY 2.0","portoni e persiane"),
 ("Taormina-Sicilia-Italy - Creative Commons by gnuckx (3666458517).jpg","gnuckx","CC BY 2.0","scalinata con vegetazione"),
 ("Taormina, Sicilia, Italia April 2024 - Street and Stairs.jpg","Sharon Hahn Darlin","CC BY 2.0","strada che diventa scala (02.001)"),
 ("Autumn stairs.jpg","Maasaak","CC BY-SA 4.0","atmosfera autunnale"),
]),
("4. Corso Umberto (v1.0)","LUO-COR, LUO-BAR",[
 ("Corso Umberto a Taormina.jpg","Davide Mauro","CC BY-SA 4.0","larghezza, basole, facciate"),
 ("Corso Umberto I - Taormina - Italy 2015.JPG","José Luiz","CC BY-SA 4.0","negozi e balconi"),
 ("Corso Umberto Taormina Comune 2020.jpg","Jeanne Griffin","CC BY-SA 4.0","Palazzo del Comune"),
 ("Taormina - Corso Umberto.jpg","Eleassar","CC BY-SA 4.0","prospettiva lunga"),
 ("License Free Photo - Creative Commons by gnuckx (11640064144).jpg","gnuckx","CC0","dettagli di facciata"),
 ("License Free Photo - Creative Commons by gnuckx (11640291114).jpg","gnuckx","CC0","folla e luce"),
 ("Store - Corso Umberto - Taormina - Italy 2015.JPG","José Luiz","CC BY-SA 4.0","vetrine (insegne da rendere generiche)"),
 ("Stairs - Corso Umberto - Taormina - Italy 2015.JPG","José Luiz","CC BY-SA 4.0","scalinate che salgono dal Corso"),
 ("0048 - Taormina - Corso Umberto - Balcone con limoni - Foto Giovanni Dall'Orto, 19-May-2008.jpg","Giovanni Dall'Orto","Attribution","balcone con limoni, ferro battuto"),
 ("0058 - Taormina - Corso Umberto 147 - Portale gotico - Foto Giovanni Dall'Orto, 19-May-2008.jpg","Giovanni Dall'Orto","Attribution","portale gotico"),
]),
("5. Porta Messina, Porta Catania, Torre dell'Orologio, Piazza IX Aprile, Piazza Duomo (v1.0)","LUO-PME, edifici simbolo",[
 ("Porta Messina a Taormina.webp","Davidemara","CC0","Porta Messina, fronte esterno"),
 ("Porta Messina (inside) - Taormina - Italy 2015.JPG","José Luiz","CC BY-SA 4.0","Porta Messina dal Corso"),
 ("Porta Messina - Taormina - panoramio.jpg","kajikawa","CC BY 3.0","proporzioni dell'arco"),
 ("Porta Catania (inside) - Taormina - Italy 2015.JPG","José Luiz","CC BY-SA 4.0","Porta Catania"),
 ("DSC00915 - Taormina - Porta Catania e stemma aragonese del 1440 - Foto di G. DallOrto.jpg","G. Dall'Orto","Attribution","stemma e pietra"),
 ("Piazza IX Aprile (Taormina).jpg","Bernard Gagnon","CC BY 4.0","piazza, Torre dell'Orologio, belvedere"),
 ("Taormina Torre di Mezzo 23-03-2026.jpg","Jeanne Griffin","CC BY-SA 4.0","Torre dell'Orologio (Torre di Mezzo)"),
 ("Taormina, San Giuseppe.jpg","Cayambe","CC BY 4.0","chiesa di San Giuseppe sulla piazza"),
 ("Taormina, piazza Duomo.jpg","Cayambe","CC BY 4.0","Piazza Duomo e fontana"),
 ("Taormina duomo 03.jpg","Effems","CC BY-SA 4.0","facciata del Duomo"),
]),
("6. Scuola media di Via Dietro Cappuccini (v1.0, esterni)","LUO-SCU",[]),
("7. Teatro Antico (v2.0)","LUO-TEA",[
 ("Taormina - Teatro antico di Taormina.jpg","231286M","CC BY-SA 4.0","cavea e scena"),
 ("Taormina - the greek theater, with mount Etna in the background.jpg","Nicolas Chadeville","CC BY-SA 4.0","vista sull'Etna"),
 ("Teatro antico di Taormina 23-01-2023.jpg","Jeanne Griffin","CC BY-SA 4.0","mattoni e luce invernale"),
]),
("8. Villa Comunale (v2.0)","LUO-VIL",[
 ("Taormina - Villa comunale 20240105-01.jpg","Pymouss","CC BY-SA 4.0","viali e follie"),
 ("Villa comunale di Taormina 12.jpg","Davide Mauro","CC BY-SA 4.0","architetture di Florence Trevelyan"),
 ("0955 - Taormina - Villa Comunale - Foto G. DallOrto.jpg","Giovanni Dall'Orto","Attribution","vegetazione"),
]),
("9. Duomo (interno) e Palazzo Corvaja (v2.0)","edifici simbolo",[
 ("Duomo di Taormina, interior 2024.jpg","Cayambe","CC BY 4.0","navata, colonne, luce"),
 ("Palazzo Corvaja courtyard 16-12-2024.jpg","Jeanne Griffin","CC BY-SA 4.0","cortile"),
 ("Crupi, Giovanni (1861-1925) - n. 0050 - Porta del palazzo Corvaja - Tupper Scrapbook Collection, vol. 41 - Sicily - DPLA - 51ed756181740204aed046a9302cef1b (page 13).jpg","Giovanni Crupi","Pubblico dominio","portale storico"),
]),
("10. Belvedere e Odeon (v2.0)","LUO-BEL",[
 ("Taormina View from the Greek Theater.jpg","Michalakopoulos","CC BY-SA 4.0","vista dalla città sulla costa"),
 ("Roman Odeon staircase Taormina.jpg","Jeanne Griffin","CC BY-SA 4.0","Odeon"),
 ("Interior Roman Odeon Taormina 26-2-2024.jpg","Jeanne Griffin","CC BY-SA 4.0","Odeon, interno"),
]),
("11. Funivia Taormina–Mazzarò (v3.0)","LUO-FUN",[
 ("Cable cars in Taormina 01.jpg","Derbrauni","CC BY 4.0","cabine e cavi"),
 ("Funivia di Taormina.jpg","Davidemara","CC0","stazione e cabina"),
 ("Panorama dalla funivia di Taormina - panoramio.jpg","kajikawa","CC BY 3.0","vista dalla cabina"),
]),
("12. Mazzarò (v3.0)","LUO-MAZ",[
 ("Mazzaro seen from Taormina.JPG","Abxbay","Pubblico dominio","baia dall'alto"),
 ("Mazzaro Taormina 18-8-21.jpg","Jeanne Griffin","CC BY-SA 4.0","spiaggia e lungomare"),
 ("Zicht op een plein in Mazzarò, RP-P-1904-1397.jpg","Rijksmuseum","CC0","piazzetta storica"),
]),
("13. Isola Bella (v3.0)","LUO-ISB",[
 ("Isola Bella (Taormina) 01.jpg","Derbrauni","CC BY 4.0","isolotto e guado"),
 ("Isola bella - panoramio - kajikawa (1).jpg","kajikawa","CC BY 3.0","colori dell'acqua"),
 ("Baía de Isola Bella (3759240839).jpg","Leandro Neumann Ciuffo","CC BY 2.0","baia"),
]),
("14. Stazione di Taormina-Giardini (v3.0)","LUO-STA",[
 ("Stazione ferroviaria (Taormina) 03 02 2026 10.jpg","Effems","CC0","fabbricato viaggiatori"),
 ("Stazione ferroviaria (Taormina) 03 02 2026 11.jpg","Effems","CC0","pensilina e colonnine"),
 ("Stazione ferroviaria (Taormina) 03 02 2026 12.jpg","Effems","CC0","binari e mare"),
 ("Stazione di Taormina.jpg","Davidemara","CC0","facciata color crema"),
 ("Stazione di Taormina-Giardini - panoramio - kajikawa.jpg","kajikawa","CC BY 3.0","interno/atrio"),
 ("Taormina - stazione ferroviaria - binari.jpg","Coclea","Pubblico dominio","binari e lampioni"),
]),
]
L=["# Riferimenti fotografici dei luoghi reali","",
"Foto con licenza aperta da Wikimedia Commons (D-36a). Servono **solo come riferimento** per forme, materiali, colori e luce (D-75): non entrano nel gioco né nelle texture, quindi sono ammesse anche CC BY-SA e «Attribution». Le licenze sono state lette dai metadati di Commons il 31/10/2026; prima di un uso diverso dal riferimento, ricontrollare la pagina del file. Niente Google Maps / Street View / Earth (DATI_TAORMINA §2).",""]
for title,luo,rows in S:
    L+=[f"## {title}",f"Luoghi: {luo}.",""]
    if not rows:
        L+=["Wikimedia Commons non ha foto con licenza aperta di questo edificio (ricerca del 31/10/2026). Riferimenti sostitutivi:","",
            "| # | Fonte | Licenza | Cosa guardare |","|---|---|---|---|",
            "| 1 | [OpenStreetMap — Via Dietro Cappuccini](https://www.openstreetmap.org/search?query=Via%20Dietro%20Cappuccini%20Taormina) | ODbL | sagoma e affacci dell'edificio |",
            "| 2 | [Mapillary — Taormina, zona Cappuccini](https://www.mapillary.com/app/?lat=37.8545&lng=15.2885&z=17) | CC BY-SA 4.0 | facciata a livello strada |",
            "| 3–8 | **Foto di Vlad** (DAT-08): 6 foto degli esterni da via pubblica (fronte, due angoli, ingresso, cortile visto dal cancello, vista verso il mare), senza persone riconoscibili | proprietà di Vlad | misure e materiali |",""]
        continue
    L+=["| # | File (link) | Autore | Licenza | Cosa guardare |","|---|---|---|---|---|"]
    for i,(f,a,lic,what) in enumerate(rows,1):
        L.append(f"| {i} | [{f}]({u(f)}) | {a} | {lic} | {what} |")
    L.append("")
L+=["## Fonti","- [Wikimedia Commons — Category:Taormina](https://commons.wikimedia.org/wiki/Category:Taormina)","- [Wikimedia Commons — Category:Taormina-Giardini train station](https://commons.wikimedia.org/wiki/Category:Taormina-Giardini_train_station)","- [Wikimedia Commons — Category:Cable cars in Taormina](https://commons.wikimedia.org/wiki/Category:Cable_cars_in_Taormina)","- [Wikimedia Commons — Category:Stairways in Taormina](https://commons.wikimedia.org/wiki/Category:Stairways_in_Taormina)","- [Wikimedia Commons — Category:Catania–Fontanarossa Airport](https://commons.wikimedia.org/wiki/Category:Catania%E2%80%93Fontanarossa_Airport)",""]
open('docs/CONCEPT/riferimenti_luoghi.md','w',encoding='utf-8').write('\n'.join(L))
print('ok')
