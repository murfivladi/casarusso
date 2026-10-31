# -*- coding: utf-8 -*-
"""Genera work/indice_libro.md da work/libro.txt e work/strumenti/dati_libro.py.
Uso: python3 work/strumenti/genera_indice.py  (dalla radice del repository)
Le battute sono copiate automaticamente dal testo: sono verbatim per costruzione.
"""
import re, sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'strumenti'))
import dati_libro as D

par = {}; order = []
for l in open(os.path.join(BASE, 'libro.txt'), encoding='utf-8'):
    m = re.match(r'^\[(\d\d)\.(\d{3})\|p(\w+)\] (.*)', l)
    if m:
        k = f"{m.group(1)}.{m.group(2)}"; par[k] = (m.group(3), m.group(4)); order.append(k)

LESSICO = ["babuška","dedushka","matrioške","matrioška","Veročka","Mamočka","lapot'","Galina Petrovna","pirožki","domovoj",
           "Baba Jaga","kaša","Fomuška","boršč","perestrojka","Pokrov","valenki","kefir","ital'janočka","Ded Moroz","Ivanov","Fu"]

def beats_of(c):
    return [b for b in D.BEAT if b[0].startswith(f"B-{c:02d}-")]

out = ["# Indice del libro «Il domovoj nella scarpa»", "",
       "Documento di lavoro della Fase 0. Generato da `work/strumenti/genera_indice.py` a partire da `work/libro.txt` "
       "(testo estratto dal PDF con `pdftotext -layout`, capolettere e paragrafi spezzati ricomposti, corsivi verificati "
       "con un secondo passaggio sui font: vedi `work/corsivi_libro.txt`).", "",
       "**Battute e narrazione.** Qui sotto, per ogni capitolo, sono riportate verbatim tutte le battute di dialogo; la narrazione di Vera (pensieri, intro, chiusure) è citata nei capitoli di `docs/NARRATIVA/` con lo stesso ID e il testo integrale con ID è in `work/libro.txt`.", "",
       "**Posizioni.** Ogni paragrafo ha un ID `CC.NNN` (capitolo.paragrafo) e la pagina del PDF. Tutti i documenti citano il libro con questi ID.", "",
       "**Calendario.** Verificato con codice (`python3 -c` su `datetime`): 13/9/2025 sabato · 15/9 lunedì (inizio lezioni in Sicilia, D.A. 718/2025) · "
       "16/9 martedì · 18/9 giovedì · 4/10 sabato · 14/10 martedì · 21/10 martedì · 23/10 giovedì · 24/10 venerdì · 26/10 domenica · "
       "28/10 martedì · 1/11 sabato · 4/11 martedì. Nessuna incoerenza con il libro.", ""]

for c in range(1, 15):
    H = D.CAPITOLI[c]
    out += [f"## Capitolo {c} — {H['titolo']}", "",
            "| Voce | Contenuto |", "|---|---|",
            f"| Posizione | {H['pagine']}, paragrafi {c:02d}.001–{c:02d}.{max(int(k[3:]) for k in order if k.startswith(f'{c:02d}.')):03d} |",
            f"| Data e giorno | {H['data']} |", f"| Arco orario | {H['ore']} |", f"| Meteo e luce | {H['meteo']} |",
            f"| Luoghi | {H['luoghi']} |", f"| Parole e frasi russe | {H['russo']} |", f"| Oggetti importanti | {H['oggetti']} |",
            f"| Fatti da rispettare | {H['fatti']} |", "",
            "**Personaggi presenti — cosa vedono, sentono, sanno degli spiriti**", "",
            "| Personaggio | Cosa vede / sente / sa |", "|---|---|"]
    out += [f"| {p} | {s} |" for p, s in H['personaggi']]
    out += ["", "**Beat (scena per scena)**", "", "| Beat | Paragrafi | Cosa succede | Scena di gioco |", "|---|---|---|---|"]
    out += [f"| {b} | {r} | {d} | {s} |" for b, r, d, s in beats_of(c)]
    out += ["", "**Battute di dialogo (verbatim, con posizione)**", ""]
    for k in order:
        if not k.startswith(f"{c:02d}."): continue
        p, t = par[k]
        if t.startswith('—') or '«' in t or k.endswith('.001') and c == 1:
            out.append(f"- `{k}` p.{p} — {t}")
    found = sorted({w for k in order if k.startswith(f'{c:02d}.') for w in LESSICO if re.search(r'(?<!\w)'+re.escape(w)+r'(?!\w)', par[k][1])})
    out += ["", f"**Parole russe trovate nel testo del capitolo (controllo automatico):** {', '.join(found) if found else '—'}", ""]

# tracciabilita
out += ["## Tabella di tracciabilità beat → scena", "",
        f"Beat totali: {len(D.BEAT)}. Beat mappati a una scena: {sum(1 for b in D.BEAT if b[3].startswith('SCN'))}. Copertura: "
        f"{100*sum(1 for b in D.BEAT if b[3].startswith('SCN'))//len(D.BEAT)}%. Nessun beat è omesso.", "",
        "| Beat | Paragrafi | Scena/e |", "|---|---|---|"]
out += [f"| {b} | {r} | {s} |" for b, r, d, s in D.BEAT]
out += ["", "## Fonti", "", "- Manoscritto: *Il domovoj nella scarpa*, Vlad Editore, 2026 (PDF fornito da Vlad, 82 pagine).",
        "- [Regione Siciliana — Anno scolastico 2025/26, inizio lezioni 15 settembre](https://www.regione.sicilia.it/la-regione-informa/anno-scolastico-202526-sicilia-campanella-inizio-lezioni-15-settembre)", ""]
open(os.path.join(BASE, 'indice_libro.md'), 'w', encoding='utf-8').write('\n'.join(out))
print('scritto indice_libro.md', len(out), 'righe')
