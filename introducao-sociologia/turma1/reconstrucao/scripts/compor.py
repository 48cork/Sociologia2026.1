"""Composição editorial por unidade explícita; nunca substitui aula nova existente.
Fontes históricas são lidas do Git, sem checkout. Requer BeautifulSoup disponível no ambiente.
Executar: python3 compor.py arquivo-de-unidades.json
"""
from pathlib import Path
from bs4 import BeautifulSoup as Soup
import subprocess, json, re, sys, html
ROOT=Path(__file__).resolve().parents[3]

def source(n):
    return Soup(subprocess.check_output(['git','show',f'91ae797:introducao-sociologia/turma1/aulas/aula-{n:02}.html'],text=True,cwd=ROOT),'html.parser')
def section(s,ident):
    return str(s.find(id=ident))
def clean(fragment,n):
    # Atualiza remissões da numeração histórica, preservando o conteúdo conceitual.
    fragment=re.sub(r'(?i)(aula\s+)(\d{1,2})(?!\d)',lambda m:m[1]+f'{int(m[2])*2-1:02}',fragment)
    fragment=re.sub(r'aula-(\d{2})\.html',lambda m:f'aula-{int(m[1])*2-1:02}.html',fragment)
    fragment=re.sub(r'<div class="ref-pages">\s*p\..*?</div>','',fragment,flags=re.S)
    return fragment

def build(d):
    n=d['aula'];p=ROOT/f'turma1/aulas/aula-{n:02}.html'
    if p.exists() and re.search(r'Aula\s*<strong>\d+</strong> de 60',p.read_text()):
        raise SystemExit(f'Recusa sobrescrita de aula nova: {p}')
    old=source(d['fonte']);template=Soup((ROOT/'turma1/aulas/aula-13.html').read_text(),'html.parser')
    css=template.style.string+'\n'+old.style.get_text()+'''
body {max-width:100%; overflow-x:hidden; overflow-wrap:anywhere;} main{max-width:960px;margin:auto} .base-text{max-width:72ch} .base-subsection{margin-bottom:24px} table{width:100%;border-collapse:collapse}th,td{padding:8px;border:1px solid var(--border);overflow-wrap:anywhere} .table-wrap,.table-region{overflow-x:auto;max-width:100%} .teacher-guidance{margin-top:20px;padding:16px;border:1px solid var(--border)} summary{cursor:pointer;font-weight:bold} .skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;z-index:300;background:var(--bg);padding:10px} a{overflow-wrap:anywhere} @media(max-width:640px){nav{position:static;flex-wrap:wrap;height:auto;padding:12px}.nav-center{display:none}.section-nav{position:static;flex-wrap:wrap}main{padding:20px 14px}.tl-item{flex-direction:column}.aula-header{padding:20px 14px}} @media print{nav,.section-nav,.skip{display:none!important}body,main,section,.aula-header,.activity-card,.pause-box,details{background:white!important;color:black!important}*{color:inherit!important;text-shadow:none!important;box-shadow:none!important}main{max-width:none;padding:0}.base-text{max-width:none}h1,h2,h3,summary{break-after:avoid}p{orphans:3;widows:3}table{font-size:9pt}.teacher-guidance{break-inside:auto}}
'''
    subs=old.select('#texto-base .base-subsection')
    chunks=[]
    for i,k in enumerate(d.get('secoes',[]),1):
        sub=Soup(str(subs[k-1]),'html.parser').find()
        sub['id']=f'a{n:02}-conceito-{i}'
        sub.h3.string=re.sub(r'^\d+\.\s*',f'{i}. ',sub.h3.get_text())
        chunks.append(clean(str(sub),n))
    if d.get('texto'): chunks.append(d['texto'])
    body=f'<p class="base-intro">{d["abertura"]}</p>'+''.join(chunks)
    if d.get('atividade_fonte'):
        act=old.find(id='atividade'); activity=clean(str(act),n)
        activity=activity.replace('class="activity-card"','class="activity-card" data-gabarito="obrigatorio"')
    else:
        activity=f'<section id="atividade"><h2>Discussão e registro</h2><div class="activity-card" data-gabarito="obrigatorio"><p>{d["atividade"]}</p><details class="teacher-guidance"><summary>Orientação docente e resposta comentada</summary>{d["gabarito"]}</details></div></section>'
    refs=clean(section(old,'leituras'),n)
    if d.get('referencias'):refs='<section id="leituras"><h2>Referências para aprofundamento</h2>'+d['referencias']+'</section>'
    e=(n-1)//4+1;pos=(n-1)%4+1
    dates=['09/09','16/09','23/09','30/09','07/10','14/10','21/10','28/10','04/11','11/11','18/11','25/11','02/12','09/12','16/12']
    prev=f'<a href="aula-{n-1:02}.html">← Aula anterior</a>' if n>1 else ''
    nxt=f'<a href="aula-{n+1:02}.html">Próxima aula →</a>' if n<60 else ''
    title=html.escape(d['titulo'])
    objectives=''.join('<li>'+x+'</li>' for x in d['objetivos'])
    times=d.get('tempos',[10,25,20,5])
    labels=[d['abertura'],'Leitura dialogada e desenvolvimento dos conceitos desta unidade.',d.get('plano_atividade','Discussão e elaboração do registro proposto; comparação das justificativas com mediação docente.'),'Síntese e transição: '+d['transicao']]
    plan=''.join(f'<div class="tl-item"><span class="tl-duration">{t} min</span><span class="tl-text">{v}</span></div>' for t,v in zip(times,labels))
    result=f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Aula {n:02} — {title} · 2026.2</title><style>{css}</style></head><body>
<a class="skip" href="#objetivos">Pular para o conteúdo</a>
<nav aria-label="Navegação entre aulas"><div class="nav-left"><a href="../../index.html">Voltar ao curso</a></div><span class="nav-center">Encontro {e:02} de 15 · Aula {n:02} de 60</span><div class="nav-right">{prev}{nxt}</div></nav>
<div class="section-nav" aria-label="Seções"><a href="#objetivos">Objetivos</a><a href="#texto-base">Texto-base</a><a href="#plano-aula">Plano</a><a href="#atividade">Discussão</a><a href="#sintese">Síntese</a><a href="#leituras">Referências</a></div>
<main><header class="aula-header"><div class="header-meta"><span class="meta-chip">Encontro <strong>{e:02}</strong> de 15 — {dates[e-1]}/2026, quarta-feira</span><span class="meta-chip">Aula <strong>{n:02}</strong> de 60</span><span class="meta-chip">{pos}ª aula do encontro</span><span class="meta-chip">Aproximadamente 1 hora-aula</span></div><h1>{title}</h1><p>Introdução à Sociologia · T01 · 2026.2 · Código 2101000 · SIGAA 4M1234</p></header>
<section id="objetivos"><h2>Objetivos</h2><ul class="obj-list">{objectives}</ul></section>
<section id="texto-base" aria-labelledby="texto-base-title"><h2 id="texto-base-title">Texto-base</h2><div class="base-text">{body}</div></section>
<section id="plano-aula"><h2>Percurso da hora-aula</h2><div class="timeline">{plan}</div></section>
{activity}
<section id="sintese"><h2>Síntese e continuidade</h2><p>{d['sintese']}</p><p>{d['transicao']}</p></section>{refs}
</main><footer>Introdução à Sociologia · T01 · 2026.2 · <a href="../../index.html">Voltar ao curso</a></footer></body></html>
'''
    p.write_text(result)
    print(f'Aula {n:02}: {len(Soup(body,"html.parser").get_text(" ",strip=True).split())} palavras no texto-base; arquivo completo')
if __name__=='__main__':
    for d in json.loads(Path(sys.argv[1]).read_text()):build(d)
