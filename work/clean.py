import re,sys
src=open(sys.argv[1],encoding='utf-8').read()
pages=src.split('\f')
out=[];cur=None;chap=0;para=0
def flush():
    global cur,para
    if cur is not None:
        t=re.sub(r'\s+',' ',cur).strip()
        if t:
            para+=1
            out.append(f"[{chap:02d}.{para:03d}|p{pg}] {t}")
    cur=None
pending_title=[]
for pi,page in enumerate(pages):
    lines=page.split('\n')
    # page number = last nonblank digits line
    pg=None
    for l in reversed(lines):
        if l.strip():
            if l.strip().isdigit(): pg=int(l.strip())
            break
    pgs=pg if pg else f"x{pi+1}"
    pg=pgs
    i=0
    while i<len(lines):
        l=lines[i]; s=l.strip()
        if not s or s.isdigit() and l.startswith('   '*5) or s=='CASA RUSSO' or set(s)<=set('• '):
            if s.isdigit() and len(l)-len(l.lstrip())>20: i+=1; continue
            if not s: i+=1; continue
            if s=='CASA RUSSO' or set(s)<=set('• '): i+=1; continue
        m=re.match(r'^\s*CAPITOLO (\d+)\s*$',l)
        if m:
            flush(); chap=int(m.group(1)); para=0
            # title lines follow
            j=i+1; tl=[]
            while j<len(lines) and len(tl)<2:
                if lines[j].strip(): tl.append(lines[j].strip())
                j+=1
            sub=re.sub(r'(?<=\S) (?=\S)','',tl[1]) if len(tl)>1 else ''
            out.append(f"\n===== CAPITOLO {chap} — {tl[0]} — {tl[1] if len(tl)>1 else ''} =====")
            i=j; continue
        if s=='✦':
            flush(); out.append(f"[{chap:02d}.---|p{pg}] * * *"); i+=1; continue
        m=re.match(r'^([A-ZÈÀ])\s{3,}(\S.*)$',l)
        if m:
            flush(); cur=m.group(1)+m.group(2); i+=1; continue
        if re.match(r'^ {2,4}\S',l) and not re.match(r'^ {5,}',l):
            flush(); cur=s; i+=1; continue
        if re.match(r'^ {5,}\S',l) and cur is not None and len(l)-len(l.lstrip())<12:
            cur+=' '+s; i+=1; continue
        if re.match(r'^ {12,}\S',l):
            # centered thing
            flush(); out.append(f"[{chap:02d}.c|p{pg}] {s}"); i+=1; continue
        if cur is None: cur=s
        else: cur+=' '+s
        i+=1
flush()
open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(out)+'\n')
