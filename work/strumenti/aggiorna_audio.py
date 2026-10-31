# -*- coding: utf-8 -*-
"""Rigenera la tabella VOX (§4.2–4.3) di docs/AUDIO.md da work/vox.json. Eseguire dopo estrai_vox.py."""
import json,collections,re
d=json.load(open('work/vox.json',encoding='utf-8'))
must_extra={'08-04','08-05','08-06','08-07','08-08','08-09','05-01','05-02','05-07','06-10','06-11','07-13','04-11','04-15','09-06','09-08','10-13','10-15','12-11','12-17','12-20','12-24','12-27','13-01','13-05','13-07','13-08','13-12','13-13','13-14','13-17','14-01','14-02','14-03','14-04','14-07','14-08','14-09','14-13','14-14','14-15'}
rel=lambda c:'v1.0' if c<=3 else ('v2.0' if c<=8 else 'v3.0')
rows=["*(generata da `work/strumenti/estrai_vox.py` + `aggiorna_audio.py`; Car. = caratteri del testo pronunciato)*","","| ID | Scena | Personaggio | Lingua | Testo pronunciato | Priorità | Car. |","|---|---|---|---|---|---|---|"]
tot=collections.Counter(); must=collections.Counter(); n=collections.Counter()
for o in d:
    c=int(o['id'][4:6]); r=rel(c); n[r]+=1
    pr='must' if (c<=3 or o['id'][4:] in must_extra or o['id'][4:6]=='11' or o['chi']=='NARRATRICE') else 'should'
    t=o['testo'].replace('|','/'); t=t if len(t)<=160 else t[:157]+'…'
    rows.append(f"| {o['id']} | {o['scena']} | {o['chi']} | {o['lingua']} | {t} | {pr} | {o['car']} |")
    tot[r]+=o['car']; must[r]+=o['car'] if pr=='must' else 0
plan={'v1.0':'1 mese di ElevenLabs gratuito (≈ 8.000 crediti) per tutte le battute; versi brevi nel mese successivo','v2.0':'2 mesi di ElevenLabs gratuito; le *should* lunghe (racconto del Pokrov) su Fish Audio se il mese non basta','v3.0':'2–3 mesi di ElevenLabs gratuito oppure Fish Audio per le *should*'}
rows+=["","### 4.3 Totali e piano dei crediti","","| Rilascio | Battute | Caratteri totali | di cui *must* | Crediti con 2 take (1 credito ≈ 1 carattere) | Piano |","|---|---|---|---|---|---|"]
for r in ('v1.0','v2.0','v3.0'):
    rows.append(f"| {r} | {n[r]} | {tot[r]} | {must[r]} | {2*must[r]} (*must*) / {2*tot[r]} (tutte) | {plan[r]} |")
rows.append(f"| **Totale** | {len(d)} | {sum(tot.values())} | {sum(must.values())} | {2*sum(must.values())} / {2*sum(tot.values())} | — |")
rows+=["","Versi brevi (§6): circa 9 personaggi × 8 versi × 3 varianti, ≈ 2.500 caratteri, una sessione dedicata. Le voci di ogni rilascio si producono nella fase dei contenuti (Fase 4 per la v1.0) e si chiudono prima della Beta.",""]
p='docs/AUDIO.md'; s=open(p,encoding='utf-8').read()
a=s.index('### 4.2 Tabella completa'); b=s.index('## 5. Voci')
s=s[:a]+'### 4.2 Tabella completa\n'+'\n'.join(rows)+'\n'+s[b:]
open(p,'w',encoding='utf-8').write(s)
print(len(d),'battute',dict(tot),dict(must))
