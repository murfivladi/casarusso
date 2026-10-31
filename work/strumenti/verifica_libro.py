# -*- coding: utf-8 -*-
"""Verifica che ogni citazione [LIBRO §CC.NNN(–CC.NNN)] nei documenti corrisponda al testo del libro.
Uso: python3 work/strumenti/verifica_libro.py  (dalla radice del repository)"""
import re, os, sys, glob
BASE=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
par={}
for l in open(os.path.join(BASE,'work','libro.txt'),encoding='utf-8'):
    m=re.match(r'^\[(\d\d|AP)\.(\d{3})\|p\w+\] (.*)',l)
    if m: par[f"{m.group(1)}.{m.group(2)}"]=m.group(3)
keys=list(par.keys())
def norm(t):
    t=t.replace('’',"'").replace('‘',"'").replace('«','').replace('»','').replace('"','')
    t=re.sub(r'\s*—\s*',' ',t); t=re.sub(r'\.\.\.','…',t)
    return re.sub(r'\s+',' ',t).strip().lower()
def rng(a,b):
    if a not in par or b not in par: return None
    i,j=keys.index(a),keys.index(b)
    return ' '.join(par[k] for k in keys[i:j+1])
errs=0; n=0; ids=0
for f in sorted(glob.glob(os.path.join(BASE,'docs','**','*.md'),recursive=True)):
    for ln,line in enumerate(open(f,encoding='utf-8'),1):
        for m in re.finditer(r'\[LIBRO §(\d\d\.\d{3})(?:[–-](\d\d\.\d{3}))?([^\]]*)\]',line):
            a=m.group(1); b=m.group(2) or a; ids+=1
            txt=rng(a,b)
            if txt is None:
                print(f"ID inesistente {a}-{b}  {os.path.relpath(f,BASE)}:{ln}"); errs+=1; continue
            if '+' in (m.group(3) or ''): continue   # citazione mista [LIBRO + NUOVO]: solo controllo ID
            rest=line[m.end():]
            q1=rest.find('«')
            nxt=re.search(r'\[LIBRO §',rest)
            if q1<0 or (nxt and nxt.start()<q1) or q1>24: continue
            d=0; end=None
            for i,ch in enumerate(rest[q1:],q1):
                if ch=='«': d+=1
                elif ch=='»':
                    d-=1
                    if d==0: end=i; break
            seg=rest[q1+1:end] if end else rest[q1+1:]
            if re.search('[а-яА-ЯёЁ]',seg):
                st=re.search(r'sottotitolo(?: \[LIBRO[^\]]*\])? «((?:[^«»]|«[^»]*»)*)»',rest)
                if not st: continue
                seg=st.group(1)
            n+=1
            T=norm(txt)
            frags=[x.strip().strip('…').strip() for x in re.split(r'[.!?…:;]\s|\s—\s|\s·\s|\.$',norm(seg)) if len(x.strip())>=10]
            bad=[x for x in frags if x not in T]
            if bad:
                errs+=1; print(f"NON TROVATO in §{a}-{b}  {os.path.relpath(f,BASE)}:{ln}\n   → {bad[0][:110]}")
print(f"riferimenti: {ids}, citazioni verificate: {n}, errori: {errs}")
sys.exit(1 if errs else 0)
