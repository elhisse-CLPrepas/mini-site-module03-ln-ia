"""Adaptation ponctuelle du site à la demande du pilote. Ne pas rejouer."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
p = root / 'src/app.js'
s = p.read_text(encoding='utf-8')
s = re.sub(r'function module04Bridge\(\).*?\r?\n', '', s, count=1)
s = "import {demonstrations} from './demonstrations.js';\n" + s
s = s.replace('()=>home()+module04Bridge()', 'home').replace('()=>resources()+module04Bridge()', 'resources')
s = s.replace("bad?'#ffb5a9':'#b3e8c6'", "bad?'#9e342b':'#265b4d'")
s = s.replace('Travailler la s?ance', 'Travailler la séance')
start = s.index('<div class="cards two">${examples.map')
end = s.index(".join('')}</div>`}", start) + len(".join('')}</div>`}")
s = s[:start] + '''<div class="demo-list">${demonstrations.map((e,i)=>`<article class="card demo"><small>CAS FICTIF · ${String(i+1).padStart(2,'0')}</small><h3>${escapeHtml(e.title)}</h3><p><strong>Public :</strong> ${escapeHtml(e.public)}</p><p>${escapeHtml(e.need)}</p><details><summary>Suivre le cas de S09 à S12</summary><div class="demo-stages">${e.stages.map(([t,p])=>`<section><h4>${escapeHtml(t)}</h4><p>${escapeHtml(p)}</p></section>`).join('')}</div><div class="comparison"><section><h4>Extrait V1 à corriger</h4><p>${escapeHtml(e.before)}</p></section><section><h4>Proposition V2 À RELIRE</h4><p>${escapeHtml(e.after)}</p></section></div><p><strong>Journal illustratif :</strong> ${escapeHtml(e.reason)}</p><p class="exercise"><strong>À vous de pratiquer :</strong> ${escapeHtml(e.exercise)}</p><p class="tiny">Scénario et corrections fictifs. Aucun résultat de terrain ni validation réelle.</p><button class="button" data-session="S09">Commencer mon propre cadrage S09</button></details></article>`).join('')}</div>`}''' + s[end:]
s = s.replace('<div class="presentation"><div class="slide-controls">', '''<div class="presentation"><details class="slide-toc"><summary>Sommaire des 20 diapositives</summary><ol>${slides.map(([title],i)=>`<li><button class="toc-button" data-slide="${i}" ${i===slide?'aria-current="step"':''}><span>${String(i+1).padStart(2,'0')}</span>${escapeHtml(title)}</button></li>`).join('')}</ol></details><div class="slide-controls">''')
s = s.replace("if(active==='presentation'){$('#prev')", "if(active==='presentation'){$$('[data-slide]').forEach(b=>b.onclick=()=>{slide=Number(b.dataset.slide);view('presentation');$('#counter').scrollIntoView({block:'center'});$('#next').focus({preventScroll:true})});$('#prev')")
s = s.replace('<button class="button primary" data-view="parcours">', '''<div class="guide-links"><a class="button primary" href="./ressources/guide-module03.html" target="_blank" rel="noopener">Lire le guide complet en HTML ↗</a><a class="button" href="./ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf" target="_blank" rel="noopener">Ouvrir le guide PDF ↗</a><a class="button" href="./ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf" download>Télécharger le PDF</a></div><button class="button primary" data-view="parcours">''', 1)
s = s.replace('Le dossier professionnel.<br><em>La base de la production.</em>', 'Du besoin au guide pratique.<br><em>Construire un dossier utile.</em>')
s = s.replace('<div class="eyebrow">DE L’IDÉE À LA PREUVE</div>', '<div class="eyebrow">MODULE 03 · DOSSIER PROFESSIONNEL</div>')
s = s.replace('20 diapositives de synthèse</button>', '20 diapositives de synthèse</button><button class="button" data-view="seances">Explorer les démonstrations</button>')
p.write_text(s, encoding='utf-8')

p = root / 'README.md'; s = p.read_text(encoding='utf-8')
s = s.replace('Dossier professionnel et communication visuelle', 'Dossier professionnel · Module 03')
s = s.replace('Module 03 · S09–S12 → Réutilisation au Module 04 · S13–S16', 'Module 03 · S09–S12')
s = s.replace(' Le dossier ainsi constitué servira de matière à la communication et au partage visuel au Module 04.', '')
s = s.replace(' La passerelle S13–S16 est une proposition à valider ; elle ne constitue pas un programme officiel ni quatre nouveaux ateliers fonctionnels.', '')
s = re.sub(r'## Module 04 .*?(?=## Démarrage)', '', s, flags=re.S)
s = re.sub(r'6\. Pour le Module 04[^\n]*\n', '', s).replace('7. Faire relire', '6. Faire relire')
s = s.replace('organigramme, passerelle Module 04 et journal qualité', 'organigramme et journal qualité')
s = s.replace(' Passerelle vers le Module 04 (S13–S16) pour communiquer et partager visuellement un projet sous contrôle humain.', ' Un même projet, du besoin au guide corrigé, sous contrôle humain.')
s += '''\n## Guide et présentation\n\nLe guide Word fourni est conservé intact. Ses versions de consultation sont accessibles dans la rubrique Ressources :\n\n- [Guide HTML avec sommaire](public/ressources/guide-module03.html).\n- [Guide PDF](public/ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf).\n\nLa présentation comporte un sommaire cliquable des 20 diapositives. Les quatre démonstrations fictives détaillent S09–S12 et une correction V1/V2. La palette claire et sobre est commune à Vite, au build GitHub Pages et à l’aperçu autonome. Vite copie les ressources publiques dans le build ; les liens relatifs fonctionnent sous un chemin de dépôt GitHub Pages. Pour l’aperçu autonome, le générateur embarque les deux ressources du guide.\n'''
p.write_text(s, encoding='utf-8')

p = root / 'scripts/standalone.py'; s = p.read_text(encoding='utf-8')
s = s.replace("core=guidance+'\\n'+data+'\\n'+core", "demos=(root/'src/demonstrations.js').read_text(encoding='utf-8')\ncore=demos+'\\n'+guidance+'\\n'+data+'\\n'+core")
s = s.replace("out=root/'APERCU", '''for name,mime in [('guide-module03.html','text/html;charset=utf-8'),('Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf','application/pdf')]:
    resource=(root/'public/ressources'/name).read_bytes()
    html=html.replace('./ressources/'+name,'data:'+mime+';base64,'+base64.b64encode(resource).decode('ascii'))
out=root/'APERCU''')
p.write_text(s, encoding='utf-8')
