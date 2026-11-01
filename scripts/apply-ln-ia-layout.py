"""Trace ponctuelle du retour à l’identité LN-IA ; ne pas réexécuter."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'src/app.js';s=p.read_text(encoding='utf-8')
assert 'function demoGallery()' not in s,'Adaptation déjà appliquée'
start=s.index('function modulePath()');end=s.index('\nfunction deck()',start)
block=s[start:end];cut=block.index('<section class="section"><h2>Quatre démonstrations fictives')
intro=block[:cut]
gallery=block[cut:].replace('<h2>Quatre démonstrations fictives</h2>','<h1>Quatre démonstrations fictives</h1>',1)
section=intro+'<section class="section"><h2>Voir la méthode en situation</h2><p>Les quatre cas fictifs disposent de leur propre rubrique, avec étapes S09–S12 et corrections V1/V2.</p><button class="button" data-view="demonstrations">Ouvrir les démonstrations →</button></section>`}\nfunction demoGallery(){return `'+gallery
s=s[:start]+section+s[end:]
s=s.replace('seances:modulePath,presentation:deck','seances:modulePath,demonstrations:demoGallery,presentation:deck')
s=s.replace("'seances','presentation'","'seances','demonstrations','presentation'")
s=s.replace('data-view="seances">Explorer les démonstrations','data-view="demonstrations">Explorer les démonstrations')
s=s.replace("bad?'#9e342b':'#265b4d'","bad?'#ffb5a9':'#e8c77f'")
posters='''function pathPosters(){return `<p class="poster-help">Deux affiches à projeter, agrandir ou imprimer. Sélectionner une affiche pour ouvrir son format vectoriel ; télécharger le PNG pour l’insérer dans un support. Les contrôles pédagogiques restent humains.</p><div class="poster-grid">${[
['affiche-01-parcours-module03','01 · Un projet, quatre livrables','Organigramme : choisir un besoin, préparer le dossier, puis produire S09, S10, S11 et S12. Après chaque séance, le contrôle humain permet de poursuivre ou de reprendre la même séance. Conserver la V1 et les preuves.'],
['affiche-02-versions-controle-module03','02 · V1, correction et revue humaine','Organigramme : exporter V1, modifier les champs et écrire le journal. La V2 nécessite une référence V1, un texte différent, un journal de douze caractères minimum et une déclaration de relecture. Sinon reprendre la correction. Après V2 À RELIRE, la personne habilitée effectue la revue finale et consigne sa décision.']
].map(([name,title,alt])=>`<figure class="poster-card"><a href="./ressources/${name}.svg" target="_blank" rel="noopener" aria-label="Agrandir ${escapeHtml(title)}"><img src="./ressources/${name}.svg" alt="${escapeHtml(alt)}" width="1200" height="1800"></a><figcaption><h2>${escapeHtml(title)}</h2><p>Identité LN-IA · Bleu nuit et gold · V1 À RELIRE</p><div class="poster-actions"><a class="button" href="./ressources/${name}.svg" target="_blank" rel="noopener">Agrandir / imprimer ↗</a><a class="button" href="./ressources/${name}.svg" download>Télécharger SVG</a><a class="button" href="./ressources/${name}.png" download>Télécharger PNG</a></div></figcaption></figure>`).join('')}</div>`}

'''
s=s.replace('function operatingPath()',posters+'function operatingPath()',1)
s=s.replace('</button></section><ol class="path-flow"','</button></section>${pathPosters()}<section class="section"><h2>Reprendre les étapes dans l’atelier</h2></section><ol class="path-flow"',1)
p.write_text(s,encoding='utf-8')

p=ROOT/'README.md';s=p.read_text(encoding='utf-8')
s=s.replace('[Démonstrations](http://127.0.0.1:5173/#seances)','[Démonstrations](http://127.0.0.1:5173/#demonstrations) · [Organigramme en affiches](http://127.0.0.1:5173/#parcours)')
s=s.replace('Huit rubriques : **Accueil**, **4 séances**, **Présentation**','Neuf rubriques : **Accueil**, **4 séances**, **Démonstrations**, **Présentation**')
s=s.replace('La palette claire et sobre est commune','La palette LN-IA bleu nuit et gold est commune')
s+='''\n## Organigramme en deux affiches\n\nDans [Parcours opératoire](http://127.0.0.1:5173/#parcours), deux affiches présentent les étapes et les retours correctifs :\n\n- Affiche 01 : besoin → S09 → S10 → S11 → S12, avec contrôle humain à chaque séance.\n- Affiche 02 : V1 → correction → journal → V2 À RELIRE → revue et décision humaines.\n\nChaque affiche peut être agrandie et imprimée en SVG, ou téléchargée en PNG. Les fichiers se trouvent dans `public/ressources/affiche-01-parcours-module03.*` et `affiche-02-versions-controle-module03.*`. Pour les régénérer : `python scripts/build-affiches.py`, puis reconstruire le site et l’aperçu autonome. Les démonstrations sont désormais dans leur rubrique dédiée.\n'''
p.write_text(s,encoding='utf-8')

p=ROOT/'prompts/PROMPT-MAITRE-CODEX-MODULE03.md';s=p.read_text(encoding='utf-8').replace('avec fond clair, texte anthracite et accents discrets','dans l’identité LN-IA bleu nuit et gold, avec des surfaces sobres et des accents dorés').replace('les huit rubriques','les neuf rubriques').replace('Maintenir une huitième rubrique','Maintenir la rubrique');p.write_text(s,encoding='utf-8')
