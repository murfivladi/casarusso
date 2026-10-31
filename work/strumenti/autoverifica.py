# -*- coding: utf-8 -*-
"""Autoverifica della documentazione della Fase 0. Uso: python3 work/strumenti/autoverifica.py"""
import re,glob,os,collections,json,subprocess,sys
D=[f for f in sorted(glob.glob('docs/**/*.md',recursive=True)) if not f.endswith('FASI_DI_SVILUPPO.md')]
T={f:open(f,encoding='utf-8').read() for f in D}
err=0
def bad(msg):
    global err; err+=1; print('✗',msg)
# 1 parole vietate
VIET=[r'\bTBD\b',r'da definire',r'\beventualmente\b',r'\bper ora\b',r'semplificat',r'se possibile',r'versione base',r'rifinisce',r'rifinitura',r'\ba mano\b']
for f,s in T.items():
    if f.endswith('DOMANDE_APERTE.md') or f.endswith('REGISTRO_DECISIONI.md'): continue
    for p in VIET:
        for m in re.finditer(p,s,re.I):
            ctx=s[max(0,m.start()-50):m.end()+40].replace('\n',' ')
            bad(f'parola vietata «{m.group(0)}» in {f}: …{ctx}…')
# 2 Fonti
for f,s in T.items():
    if not re.search(r'\n## Fonti\n',s): bad(f'manca «## Fonti» in {f}')
    else:
        tail=s[s.rindex('\n## Fonti\n'):]
        if re.search(r'\n## (?!Fonti)',tail): bad(f'«Fonti» non è l\'ultima sezione in {f}')
# 3 ID unici (definizioni)
defs=collections.Counter()
for f,s in T.items():
    for m in re.finditer(r'^### (SCN-\d\d-\d\d|SIS-\d\d|REQ-[A-Z]{3}-\d{3}|CON-\d\d)\b',s,re.M): defs[m.group(1)]+=1
    for m in re.finditer(r'\b(PEN-\d\d-\d\d) \[',s): defs[m.group(1)]+=1
    if not f.endswith('README.md'):
        for m in re.finditer(r'\b(DLG-\d\d-[A-ZÀ-Ü]+-\d\d) ',s): defs[m.group(1)]+=1
s=T['docs/REGISTRO_DECISIONI.md']
for m in re.finditer(r'^\| (D-\d\d|C-\d\d) \|',s,re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (Q-\d\d) \|',T['docs/DOMANDE_APERTE.md'],re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (SFX-\d{3}) ',T['docs/AUDIO.md'],re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (RUS-\d\d) \|',T['docs/NARRATIVA/parole_russe.md'],re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (VOX-\d\d-\d\d) \|',T['docs/AUDIO.md'],re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (RAC-\d\d) \|',T['docs/NARRATIVA/raccordi.md'],re.M): defs[m.group(1)]+=1
for m in re.finditer(r'^\| (MIS-S-\d\d|SEG-\d\d|FOT-LUO-\d\d) \|',T['docs/NARRATIVA/mondo_libero.md'],re.M): defs[m.group(1)]+=1
dup=[k for k,v in defs.items() if v>1]
for k in dup: bad(f'ID definito più volte: {k} ({defs[k]})')
print('ID definiti:',len(defs))
# 4 variabili
dic=T['docs/NARRATIVA/00_struttura.md']
defined=set(re.findall(r'\b((?:rap|flag|casa|val|col)_[a-z0-9_]+)\b',dic.split('## 4.')[0]))
# espandi flag_prova_* abbreviati
defined|={'flag_prova_'+x for x in ['moka','kefir','lenzuola','calze','tazzine','pane','sale']}
used=collections.defaultdict(set)
for f,s in T.items():
    for v in re.findall(r'\b((?:rap|flag|casa|val|col)_[a-z0-9_]+)\b',s): used[v].add(f)
skip={'col_rus_n','col_ric_n','col_fot_n','col_seg_n','flag_prova_','val_','rap_','flag_','casa_','col_'}
for v,fs in sorted(used.items()):
    if v not in defined and v not in skip and not v.endswith('_'):
        bad(f'variabile non definita in 00_struttura: {v} (in {", ".join(sorted(os.path.basename(x) for x in fs))})')
print('variabili definite:',len(defined),'usate:',len(used))
# 5 SFX usati esistono
sfxdef={k for k in defs if k.startswith('SFX-')}
for f,s in T.items():
    for v in set(re.findall(r'\bSFX-\d{3}\b',s)):
        if v not in sfxdef: bad(f'{v} usato in {f} ma non nel catalogo AUDIO §3')
# 6 RUS usati esistono
rusdef={k for k in defs if k.startswith('RUS-')}
for f,s in T.items():
    for v in set(re.findall(r'\bRUS-\d\d\b',s)):
        if v not in rusdef: bad(f'{v} usato in {f} ma non in parole_russe')
# 7 VOX nei capitoli presenti in AUDIO
voxdef={k for k in defs if k.startswith('VOX-')}
for f,s in T.items():
    if 'NARRATIVA/cap' not in f: continue
    for a,b,c in re.findall(r'VOX-(\d\d)-(\d\d)(?:…(\d\d))?',s):
        for n in range(int(b),int(c or b)+1):
            v=f'VOX-{a}-{n:02d}'
            if v not in voxdef: bad(f'{v} in {f} non è nella tabella VOX di AUDIO')
# 7b riferimenti a PEN/DLG/OBJ esistenti
pen={k for k in defs if k.startswith(('PEN-','DLG-'))}
for f,s2 in T.items():
    for v in set(re.findall(r'\b(?:PEN-\d\d-\d\d|DLG-\d\d-[A-ZÀ-Ü]+-\d\d)\b',s2)):
        if v not in pen and 'ESEMPIO' not in v and not f.endswith('README.md'): bad(f'{v} citato in {f} ma non definito')
objs=set()
for f,s2 in T.items():
    if 'NARRATIVA/cap' in f: objs|=set(re.findall(r'\b(OBJ-\d\d-\d\d) \[',s2))
for f,s2 in T.items():
    for v in set(re.findall(r'\bOBJ-\d\d-\d\d\b',s2)):
        if v not in objs and not f.endswith('README.md'): bad(f'{v} citato in {f} ma non definito')
# 8 scene: ogni scena citata nei beat esiste
sys.path.insert(0,'work/strumenti'); import dati_libro as DL
scn={k for k in defs if k.startswith('SCN-')}
for b in DL.BEAT:
    for x in re.findall(r'SCN-\d\d-\d\d',b[3]):
        if x not in scn: bad(f'beat {b[0]} rimanda a {x} inesistente')
print('scene:',len(scn),'beat:',len(DL.BEAT))
# 9 citazioni del libro
r=subprocess.run([sys.executable,'work/strumenti/verifica_libro.py'],capture_output=True,text=True)
print(r.stdout.strip().split('\n')[-1]);
if r.returncode: bad('verifica_libro.py segnala errori')
# 10 piattaforme
for f,s in T.items():
    for m in re.finditer(r'\b(smartphone|cellulari|telefoni cellulari)\b',s,re.I):
        pass
print('ERRORI:',err)
sys.exit(1 if err else 0)
