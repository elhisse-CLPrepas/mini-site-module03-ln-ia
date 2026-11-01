"""Exporte le guide Word fourni en HTML autonome sans modifier la source."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from html import escape
import base64
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.docx'
OUT = ROOT / 'public/ressources'
OUT.mkdir(parents=True, exist_ok=True)
NS = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}

def w(tag): return '{'+NS['w']+'}'+tag

with ZipFile(SOURCE) as z:
    xml = ET.fromstring(z.read('word/document.xml'))
    rels = {e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
    headings=[]
    def inline(p):
        result=[]
        for run in p:
            if run.tag==w('pPr'): continue
            text=[]
            for e in run.iter():
                if e.tag==w('t'): text.append(escape(e.text or ''))
                elif e.tag==w('br'): text.append('<br>')
                elif e.tag==w('tab'): text.append('    ')
                elif e.tag=='{'+NS['a']+'}blip':
                    rid=e.get('{'+NS['r']+'}embed'); target=rels.get(rid,'')
                    if target.startswith('media/'):
                        b64=base64.b64encode(z.read('word/'+target)).decode('ascii')
                        ext=Path(target).suffix.lower().lstrip('.'); mime='jpeg' if ext in ('jpg','jpeg') else ext
                        text.append(f'<img class="document-image" alt="Illustration du guide source" src="data:image/{mime};base64,{b64}">')
            value=''.join(text)
            if run.find('./w:rPr/w:b',NS) is not None: value='<strong>'+value+'</strong>'
            if run.find('./w:rPr/w:i',NS) is not None: value='<em>'+value+'</em>'
            if run.tag==w('hyperlink'):
                target=rels.get(run.get('{'+NS['r']+'}id'),'')
                if target.startswith(('https://','http://')): value=f'<a href="{escape(target,quote=True)}" rel="noopener">{value}</a>'
            result.append(value)
        return ''.join(result)

    def paragraph(p):
        content=inline(p)
        if not content.strip(): return ''
        style=p.find('./w:pPr/w:pStyle',NS)
        style=style.get(w('val'),'') if style is not None else ''
        if style=='Title': return '<h1>'+content+'</h1>'
        if style.startswith('Heading'):
            level=min(4,int(style[-1])+1) if style[-1].isdigit() else 2
            anchor='section-'+str(len(headings)+1)
            label=''.join(p.itertext())
            headings.append((level,anchor,label))
            return f'<h{level} id="{anchor}">{content}</h{level}>'
        if style=='CodeBlock': return '<pre>'+content+'</pre>'
        if style in ('ListBullet','ListParagraph'): return '<p class="bullet">• '+content+'</p>'
        return '<p>'+content+'</p>'

    blocks=[]
    for el in xml.find('w:body',NS):
        if el.tag==w('p'): blocks.append(paragraph(el))
        elif el.tag==w('tbl'):
            rows=[]
            for i,row in enumerate(el.findall('w:tr',NS)):
                cells=[]
                for cell in row.findall('w:tc',NS):
                    tag='th' if i==0 else 'td'
                    cells.append(f'<{tag}>'+''.join(paragraph(p) for p in cell.findall('w:p',NS))+f'</{tag}>')
                rows.append('<tr>'+''.join(cells)+'</tr>')
            blocks.append('<div class="table-scroll"><table>'+''.join(rows)+'</table></div>')

body_html=''.join(blocks).replace('</pre><pre>','\n')
css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;background:#f6f4ee;color:#29332b;font:17px/1.75 "Segoe UI",Arial,sans-serif}a{color:#315d42}a:focus-visible,summary:focus-visible{outline:3px solid #9a773e;outline-offset:4px}.layout{max-width:1180px;margin:auto;display:grid;grid-template-columns:260px minmax(0,1fr);gap:55px;padding:40px 28px}.toc{position:sticky;top:24px;align-self:start;max-height:90vh;overflow:auto;font-size:13px}.toc ol{padding-left:20px}.toc li{margin:8px 0}.toc a{text-decoration:none}.toc a:hover{text-decoration:underline}.topline{font-size:12px;text-transform:uppercase;letter-spacing:.12em;color:#6b775e}.toolbar{display:flex;flex-wrap:wrap;gap:10px;padding-bottom:24px;border-bottom:1px solid #d4dacb;margin-bottom:32px;font-size:13px}.toolbar a{padding:8px 12px;border:1px solid #c6d0bc;border-radius:4px;text-decoration:none}.notice{font-size:13px;color:#627059;padding:14px;background:#e9eee1;border-left:3px solid #98ac81}.document{min-width:0;background:#fffdf8;padding:40px 42px;border:1px solid #dedfd4;border-radius:6px}.document h1{font-size:44px;line-height:1.1;letter-spacing:-.04em;color:#304d37;margin:25px 0}.document h2{font-size:28px;line-height:1.25;margin-top:55px;border-top:1px solid #d8dece;padding-top:28px}.document h3{font-size:21px;margin-top:30px}.document p{margin:14px 0}.document-image{max-width:100%;height:auto;max-height:180px;object-fit:contain}.table-scroll{overflow:auto;margin:25px 0}table{border-collapse:collapse;font-size:13px;line-height:1.55;width:100%}th,td{border:1px solid #d4dccb;padding:10px;vertical-align:top;min-width:110px;overflow-wrap:anywhere}th{background:#eaf0e3;text-align:left}td p,th p{margin:0!important}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.6 Consolas,monospace;background:#eef2e7;padding:18px;border-radius:4px}.bullet{padding-left:15px}.end{font-size:12px;color:#75806c;margin-top:36px}@media(max-width:850px){.layout{display:block;padding:20px 14px}.toc{position:static;max-height:none;margin-bottom:28px}.toc details:not([open]) ol{display:none}.document{padding:25px 20px}.document h1{font-size:36px}.document h2{font-size:24px}}@media print{body{background:#fff;font-size:11pt}.layout{display:block;padding:0}.toc,.toolbar,.notice{display:none}.document{border:0;padding:0}.document h2{break-after:avoid}.table-scroll{overflow:visible}a{color:inherit}pre{font-size:8pt}}'''
# Identité actuelle du mini-site ; contenu et source Word inchangés.
palette={'#f6f4ee':'#f3f5f8','#29332b':'#152940','#315d42':'#244f78',
         '#9a773e':'#9a6c20','#6b775e':'#825d20','#c6d0bc':'#b9c8d7',
         '#d4dacb':'#d9e3ee','#627059':'#536579','#e9eee1':'#fcf8ed',
         '#98ac81':'#b28a43','#fffdf8':'#ffffff','#dedfd4':'#d9e3ee',
         '#304d37':'#12314f','#d8dece':'#d9e3ee','#d4dccb':'#d9e3ee',
         '#eaf0e3':'#edf2f7','#eef2e7':'#f5f8fc','#75806c':'#536579'}
for old,new in palette.items(): css=css.replace(old,new)
css+='h1,h2,h3{font-weight:500}body{font-weight:400}.toolbar a{font-weight:500}'
toc=''.join(f'<li><a href="#{anchor}">{escape(label)}</a></li>' for level,anchor,label in headings if level==2)
html=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Guide du dossier professionnel Module 03 LN-IA : S09 à S12, versions, contrôles et preuves."><title>Guide du dossier professionnel · Module 03 LN-IA</title><style>{css}</style></head><body><div class="layout"><aside class="toc"><p class="topline">LN-IA · Module 03</p><details open><summary>Sommaire du guide</summary><ol>{toc}</ol></details></aside><main><nav class="toolbar" aria-label="Actions du guide"><a href="../index.html#ressources">Retour aux ressources</a><a href="./Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf">Ouvrir le PDF</a><a href="./Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf" download>Télécharger le PDF</a></nav><p class="notice">Version HTML de consultation du guide Word fourni. Texte, tableaux et illustration repris du document source ; mise en page adaptée au Web. Statut V1 À RELIRE / À VALIDER. Les liens et instructions historiques du guide sont conservés.</p><article class="document">{body_html}</article><p class="end">Source : Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.docx · Édition Automne 2026. La consultation du guide ne valide aucun livrable.</p></main></div></body></html>'''
(OUT/'guide-module03.html').write_text(html,encoding='utf-8')
(ROOT/'docs/EXPORT-GUIDE-SOURCE.json').write_text(json.dumps({'source':SOURCE.name,'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'html':'public/ressources/guide-module03.html','headings':len(headings),'method':'Texte, styles de titres, tableaux et image extraits du Word ; mise en page HTML adaptée.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Guide HTML exporté :',len(headings),'titres ; source conservée.')
