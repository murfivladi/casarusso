# -*- coding: utf-8 -*-
"""Estrae l'elenco delle battute doppiate (VOX) dai capitoli e stima i caratteri.
Uso (dalla radice): python3 work/strumenti/estrai_vox.py  → work/vox.json"""
import re,glob,json,collections
par={}
for l in open('work/libro.txt',encoding='utf-8'):
    m=re.match(r'^\[(\d\d)\.(\d{3})\|p\w+\] (.*)',l)
    if m: par[f"{m.group(1)}.{m.group(2)}"]=m.group(3)
def dialog_only(t):
    if not t.startswith('—'):
        i=t.find('—');  t=t[i:] if i>=0 else t
    parts=re.split(r'\s*—\s*',t)[1:]
    return ' '.join(p for i,p in enumerate(parts) if i%2==0).strip()
TOK=re.compile(r'(?P<ru>\[RU\])|(?P<who>\b(?:VERA|BABUŠKA|IRINA|SALVO|GIULIA|MATTIA|CONCETTA|FOMÀ|ROSALIA|NINA|TINA|NICOLÒ|DOTTORE|OMBRA|IL SIGNORE|NARRATRICE)\b)|(?P<pid>(?:§|(?<=, ))\d\d\.\d{3}(?:[–-]\d\d\.\d{3})?)|(?P<q>«(?:[^«»]|«[^»]*»)*»)|(?P<vox>\[(?:VOCE )?VOX-(\d\d)-(\d\d)(?:…(\d\d))?[^\]]*\]|VOX-(\d\d)-(\d\d)(?=\s\[))')
res={}
for f in sorted(glob.glob('docs/NARRATIVA/cap*.md')):
    scene=None
    for line in open(f,encoding='utf-8'):
        h=re.match(r'### (SCN-\d\d-\d\d)',line)
        if h: scene=h.group(1); continue
        if 'VOX-' not in line: continue
        who='NARRATRICE' if 'narratrice' in line else None; pids=[]; quotes=[]; ru=False; pending=None
        for m in TOK.finditer(line):
            k=m.lastgroup
            if k=='who': who=m.group('who'); pids=[]; quotes=[]; ru=False
            elif k=='ru': ru=True
            elif k=='pid': pids.append(m.group('pid').lstrip('§')[:6])
            elif k=='q': quotes.append((m.group('q')[1:-1],ru))
            elif k=='vox':
                g=m.groups()
                if g[8]: a,b,c=g[8],g[9],None
                else: a,b,c=g[5],g[6],g[7]
                vids=[f"VOX-{a}-{n:02d}" for n in range(int(b),int(c or b)+1)]
                for i,vid in enumerate(vids):
                    if vid in res: continue
                    res[vid]=dict(id=vid,scena=scene,chi=who or 'NARRATRICE',pids=pids[:],line=line,idx=i,pos=m.end())
                pids=[]
# risolvi il testo
def rngtext(a,b,narr):
    ks=list(par.keys())
    if a not in par: return ''
    b=b or a; t=' '.join(par[k] for k in ks[ks.index(a):ks.index(b)+1])
    return t if narr else dialog_only(t)
TXT={
 'VOX-13-02':('IRINA','ru','Что ты делаешь, мама? Тебе нужно отдыхать.'),
 'VOX-13-03':('BABUŠKA','ru','Пеку хлеб.'),
 'VOX-13-04':('BABUŠKA','ru','В России в ноябре — родительская суббота. Пекут хлеб, идут на кладбище, оставляют хлеб на могиле. Чтобы помнить. В этом году Коля далеко. Хлеб я ему здесь оставлю.'),
 'VOX-13-12':('BABUŠKA+CONCETTA','it','[risata a due voci, 6 s]'),
 'VOX-13-15':('CONCETTA','it',"Questo è di Turi. Ci cuciva le vele della barca, da giovane, prima di aprire il bar. L'ho perso trent'anni fa."),
 'VOX-13-16':('BABUŠKA','ru','Это Колина. Он сам вырезал, мальчишкой, в деревне. Лежала в ящике на кухне, в Петербурге. Я её не брала. Точно не брала.'),
}
TXT.update({
 'VOX-02-02':('BABUŠKA','it','Grazie. Ho portato i pirožki.'),
 'VOX-02-04':('BABUŠKA','ru','Дедушка, дедушка, пойдём с нами. Это новый дом. Пойдём жить с нами. ×3'),
 'VOX-04-05':('CONCETTA','it',"Dov'è la mia moka?"),
 'VOX-04-06':('BABUŠKA','it','Io non tocco le cose degli altri.'),
 'VOX-04-09':('BABUŠKA','ru','Не испортился. Кто-то его испортил.'),
 'VOX-05-03':('BABUŠKA','ru','Фома. Фомушка. Я знаю, что ты сердишься. Я знаю, что тебе не нравится. Печки нет, жарко, тут эти дамы. Но надо потерпеть. Мы в гостях. В чужом доме не озорничают. Понял? Оставь в покое кофеварку синьоры Кончетты. Она хорошая женщина. Просто… сицилийка.'),
 'VOX-06-02':('BABUŠKA','ru','Покров значит… покрывало. Плащ. То, что укрывает и защищает. Это праздник Богородицы. Рассказывают, что однажды, давным-давно, в Константинополе люди боялись, шла война, и Богородица явилась в церкви и простёрла свой покров над всеми, чтобы их защитить. С тех пор четырнадцатого октября в России празднуют.'),
 'VOX-06-03':('BABUŠKA','ru','Более-менее. Но у нас Покров — это ещё и другое. В деревне у моей бабушки говорили, что Покров — это день, когда зима покрывает землю. Первым снегом. Первой белизной. И девушки говорили: Батюшка Покров, покрой землю снежком, а меня женишком.'),
 'VOX-06-04':('BABUŠKA','ru','Часто. Не всегда. Но четырнадцатого октября это уже чувствовалось. Воздух становился тонким, холодным, пах железом. Листья на берёзах все жёлтые, и падали. Первый раз затапливали печку. Окна заклеивали бумагой, чтобы не дуло. Доставали валенки. И дом… дом становился маленьким и тёплым, и все были рядом.'),
 'VOX-06-05':('BABUŠKA','ru','Коля всегда топил печку на Покров. Всегда. Даже когда у нас в городе появились батареи, он купил чугунную печурку, вот такую маленькую, и четырнадцатого октября её затапливал. Говорил, что это для домового. А я ему говорила, что он старый дурак.'),
 'VOX-08-04':('ROSALIA','it',dialog_only(par['08.027'])),
 'VOX-09-01':('BABUŠKA','ru','Я в порядке, Верочка. Мне просто немного холодно.'),
 'VOX-09-05':('BABUŠKA','ru','Коля… Коля… Малая Посадская… печка…'),
 'VOX-14-05':('BABUŠKA','it',dialog_only(par['14.009'])),
 'VOX-14-06':('BABUŠKA','it',dialog_only(par['14.012'])),
 'VOX-14-07':('BABUŠKA','it',dialog_only(par['14.016'])),
 'VOX-13-09':('BABUŠKA','it',dialog_only(par['13.028'])),
 'VOX-13-10':('BABUŠKA','it',dialog_only(par['13.033'])),
 'VOX-13-11':('BABUŠKA','it',dialog_only(par['13.035'])),
})
OVR={'VOX-06-01':'BABUŠKA','VOX-06-02':'BABUŠKA','VOX-06-03':'BABUŠKA','VOX-06-04':'BABUŠKA','VOX-06-05':'BABUŠKA','VOX-13-12':'BABUŠKA+CONCETTA'}
out=[]
for vid,o in sorted(res.items()):
    line=o['line']; before=line[:o['pos']]; rest=line[o['pos']:]
    chi=OVR.get(vid,o['chi']); narr=(chi=='NARRATRICE')
    ru=re.match(r'[^«]{0,40}\[RU\][^«]*«([^»]+)»',rest)
    lib=list(re.finditer(r'\[LIBRO §(\d\d\.\d{3})(?:[–-](\d\d\.\d{3}))?[^\]]*\]',before))
    q=re.match(r'[^«\[]{0,60}?«((?:[^«»]|«[^»]*»)*)»',rest)
    qb=re.findall(r'«((?:[^«»]|«[^»]*»)*)»[^«»]{0,30}$',before)
    lang='scn' if '[SCN]' in line else 'it'
    libr=re.match(r'\s*\[LIBRO §(\d\d\.\d{3})(?:[–-](\d\d\.\d{3}))?[^\]]*\]',rest)
    if ru: txt,lang=ru.group(1),'ru'
    elif narr and (libr or lib):
        L=libr or lib[-1]; txt=rngtext(L.group(1),L.group(2),True)
    elif q: txt=q.group(1)
    elif o['pids']:
        pid=o['pids'][min(o['idx'],len(o['pids'])-1)]; txt=rngtext(pid,None,False)
        if re.search(r'\[RU\]|russo',line[:o['pos']]) and chi in ('BABUŠKA','IRINA'): lang='ru'
    elif libr: txt=rngtext(libr.group(1),libr.group(2),False)
    elif qb: txt=qb[-1]
    else: txt=''
    if vid in TXT: chi,lang,txt=TXT[vid]
    if vid=='VOX-09-09': continue
    if re.search('[а-яА-Я]',txt): lang='ru'
    out.append(dict(id=vid,scena=o['scena'],chi=chi,lingua=lang,testo=txt,car=len(txt)*(3 if txt.endswith('×3') else 1)))
json.dump(out,open('work/vox.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'battute; caratteri',sum(x['car'] for x in out))
for x in out:
    if x['car']<2: print('VUOTA',x['id'],x['scena'],x['chi'])
c=collections.Counter()
for x in out: c[x['id'][4:6]]+=x['car']
print(dict(c))
