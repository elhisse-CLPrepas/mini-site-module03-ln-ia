"""Intégration locale non destructive des supports opératoires."""
from pathlib import Path
import json, re, hashlib

root = Path(__file__).resolve().parents[1]
def read(p): return (root/p).read_text(encoding='utf-8')
def write(p, text): (root/p).write_text(text, encoding='utf-8')

source = 'docs/Organigramme-Algorithme-Module03-LN-IA'
md = read(source+'.md')
md = md.replace('Statut : document de synthèse à relire', 'Statut : adaptation au mini-site intégré — À RELIRE')
md = md.replace('Utiliser le site public S09, puis S10, S11 et S12, ou l’aperçu autonome de chaque dépôt. Consulter Accueil, Présentation, Méthode et au moins un exemple.', 'Ouvrir ce mini-site ou APERCU-AUTONOME-MODULE03.html. Consulter Accueil, Présentation, Méthode et Parcours opératoire ; choisir ensuite S09 à S12 dans le sélecteur de l’Atelier de production.')
md = md.replace('Répondre aux cinq questions préparatoires.', 'Compléter les champs proposés ; ce mini-site ne comporte pas de questionnaire préparatoire séparé.')
md = md.replace('ou coller leur contenu.', 'ou reporter manuellement les informations dans les champs correspondants.')
md = md.replace('ou coller son texte.', 'ou reporter manuellement les informations dans les champs correspondants.')
md = md.replace('1. Ouvrir le site S09 puis S10, S11, S12 dans l’ordre, ou télécharger leur version HTML autonome depuis les dépôts.', '1. Ouvrir le mini-site intégré ou son aperçu autonome ; sélectionner S09 puis S10, S11 et S12 dans Atelier de production.')
md = md.replace('2. Dans chaque site : passer par **Présentation → Méthode → Démonstrations → Atelier → Prompts → Validation → Portfolio**. L’ordre est une recommandation de travail ; les onglets peuvent être consultés librement.', '2. Consulter **Présentation → Méthode → Parcours opératoire → Atelier de production → Qualité & portfolio**. Les démonstrations fictives figurent dans « 4 séances » ; les prompts, grilles, preuves et bilan sont exportés depuis l’atelier.')
md = md.replace('Les intitulés, modèles et critères de passage ci-dessus sont fondés', 'Le document fourni indique que les intitulés, modèles et critères de passage sont fondés')
md = md.replace('## 10. Sources GitHub consultées', '## 10. Références déclarées par le document fourni')
md += '''
## 11. Adaptation au mini-site intégré

Édition du 1er novembre 2026, à relire. Les deux documents fournis restent inchangés ; cette adaptation ne modifie aucune archive ni production candidate. Les liens externes de la source ne constituent pas une nouvelle vérification des dépôts.

- L’import reconnaît uniquement les titres Markdown correspondant aux libellés de la séance active. Il ne fusionne pas automatiquement S09, S10 et S11 : relire les sources et reporter les informations nécessaires. Limite : 500 000 octets par fichier.
- Les contrôles des portes S09–S12 sont des consignes pédagogiques humaines. L’application vérifie la présence des champs, pas leur exactitude ni le nombre d’actions dans le guide.
- Pour S12, exporter V1, modifier les champs, écrire un journal d’au moins 12 caractères et cocher la déclaration de relecture. La référence V1 est conservée seulement pendant l’ouverture de cet atelier ; changer de rubrique ou de séance impose de réexporter V1. Conserver aussi le fichier V1 téléchargé.
- Le bouton Sauver localement conserve les champs et les points à vérifier, pas la référence V1, le journal ni la déclaration de relecture. Le stockage dépend du navigateur.
- Les prompts et grilles téléchargés utilisent les noms indiqués par le navigateur ; les renommer si nécessaire selon les conventions du dossier candidat.
- La rubrique Parcours opératoire propose un organigramme lisible sans bibliothèque externe, les portes de contrôle et le texte détaillé téléchargeable. Le Markdown contient aussi le diagramme Mermaid pour un lecteur compatible.
- Aucun gain de temps ou de performance technique n’est affirmé sans mesure. L’amélioration recherchée porte sur l’accès aux consignes et la cohérence du parcours.
'''
write(source+'-INTEGRE.md', md)
# Texte embarqué : utilisable hors ligne, sans fetch ni CDN.
write('src/parcours-data.js', 'export const parcoursMarkdown = '+json.dumps(md, ensure_ascii=False)+';\n')
app=read('src/app.js')
app="import {parcoursMarkdown} from './parcours-data.js';\n"+app
app=app.replace('methode:method,atelier:editor', 'methode:method,parcours:operatingPath,atelier:editor')
app=app.replace("'methode','atelier'", "'methode','parcours','atelier'")
function='''
function operatingPath(){const gates=[
['S09','Clarifier le besoin','Six rubriques : sujet, public, problème, objectif, résultat et première action.','Si le besoin reste flou, revenir au cadrage.'],
['S10','Structurer le projet','Comparer la fiche à S09 : objectif observable, solution, livrables, ressources, étapes et risques.','Si un ajout est injustifié, corriger la fiche ou expliquer le changement.'],
['S11','Organiser le guide','Prévoir cinq fonctions au maximum : Comprendre, Préparer, Produire, Vérifier, Améliorer.','Si la progression ne permet pas au lecteur d’agir, réorganiser le plan.'],
['S12','Produire puis corriger','Rédiger au moins trois actions avec résultat vérifiable ; exporter V1 et conserver le fichier.','Modifier les champs, documenter les corrections et déclarer la relecture pour exporter V2 À RELIRE.']
];return `<section class="section"><h1>Parcours opératoire</h1><p>Du besoin au dossier professionnel : quatre séances, des contrôles et des retours correctifs. Synthèse adaptée aux deux documents fournis, à relire.</p><button class="button primary" id="download-path">Télécharger l’algorithme détaillé (.md)</button></section><ol class="path-flow" aria-label="Organigramme des séances">${gates.map(([id,title,check,back])=>`<li class="card"><small>${id} · V1 À RELIRE</small><h2>${title}</h2><p>${check}</p><p class="path-gate"><strong>Contrôle humain :</strong> ${back}</p><button class="button" data-session="${id}">Ouvrir l’atelier ${id}</button></li>`).join('')}</ol><div class="banner">S12 : V1 exportée → texte modifié → journal → relecture déclarée → V2 À RELIRE<span>Si une condition manque : revenir à la correction. La validation finale reste une décision humaine explicite.</span></div><section class="section"><h2>Préparer et clôturer le dossier</h2><p>Choisir un seul besoin, créer 02-prompts/, 03-documents/ et 07-portfolio/. Après chaque séance, exporter et classer manuellement. À la clôture, vérifier la cohérence note → fiche → plan → guide, les faits et la confidentialité ; documenter la décision humaine et ses réserves.</p><h2>Limites pratiques de l’atelier</h2><p>L’import reprend les titres correspondant aux champs de la séance active, sans fusion automatique des documents antérieurs. Les portes ci-dessus demandent une relecture humaine. Changer de rubrique réinitialise la référence V1 de S12 : garder la V1 téléchargée et réexporter une référence avant la correction.</p></section><details class="path-detail"><summary>Lire toutes les instructions et la matrice des critères</summary><pre>${escapeHtml(parcoursMarkdown)}</pre></details>`}
'''
app=app.replace('function editor()', function+'\nfunction editor()')
app=app.replace("function bindView(){", "function bindView(){if(active==='parcours'){$('#download-path').onclick=()=>download('Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md',parcoursMarkdown);$$('[data-session]').forEach(b=>b.onclick=()=>{chosen=b.dataset.session;view('atelier')})}")
app=app.replace('Modèles, guides, prompts et références originales clairement séparés.</p>', 'Modèles, guides, prompts et références originales clairement séparés.</p><button class="button primary" data-view="parcours">Consulter l’organigramme et l’algorithme →</button>')
write('src/app.js', app)
write('index.html', read('index.html').replace('<button data-go="atelier">','<button data-go="parcours">Parcours opératoire</button><button data-go="atelier">'))
write('src/styles.css',read('src/styles.css')+'\n.path-flow{display:grid;gap:18px;list-style:none;padding:0;counter-reset:path}.path-flow li{position:relative}.path-flow li+li:before{content:"↓";position:absolute;top:-24px;left:24px;color:var(--gold)}.path-gate{border-left:3px solid var(--gold);padding-left:12px}.path-detail summary{cursor:pointer;color:var(--gold);padding:15px}.path-detail pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 Consolas,monospace;padding:16px;background:var(--panel);max-height:75vh;overflow:auto}\n')
standalone=read('scripts/standalone.py').replace("core=re.sub", "data=(root/'src/parcours-data.js').read_text(encoding='utf-8').replace('export const ', 'const ', 1)\ncore=data+'\\n'+core\ncore=re.sub",1)
write('scripts/standalone.py', standalone)
prompt=read('prompts/PROMPT-MAITRE-CODEX-MODULE03.md')
prompt=prompt.replace('## Protocole', '''## Composante organigramme et algorithme

Lire les deux documents `docs/Organigramme-Algorithme-Module03-LN-IA.md` et `.docx`, préservés comme sources fournies, puis `docs/Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md`, adaptation au mini-site unique. Conserver les versions fournies ; journaliser toute adaptation. Ne pas prétendre avoir revérifié les références externes sans le faire.

Maintenir une huitième rubrique « Parcours opératoire » : préparation, S09 → S10 → S11 → S12, portes de contrôle, retours correctifs, V1 → V2 et revue humaine finale. Relier chaque séance au sélecteur de l’atelier. Donner accès au texte détaillé et à son téléchargement Markdown, y compris dans l’aperçu autonome, sans CDN ni rendu Mermaid obligatoire.

Respecter les limites réelles : import par titres correspondant aux champs actifs, aucune fusion automatique des acquis ; contrôles de fond humains ; référence V1 S12 perdue lorsque l’atelier est recréé ; journal de 12 caractères minimum et déclaration de relecture pour V2. Distinguer conditions techniques d’export et qualité pédagogique. Ne pas inventer un contrôle automatique de trois actions ou de cinq parties. Ne pas promettre de gain technique sans mesure.

Le texte détaillé est embarqué dans `src/parcours-data.js`. Après adaptation du Markdown, synchroniser ce texte et reconstruire l’aperçu. Ne pas exécuter à nouveau `scripts/integrate-parcours.py` : c’est la trace de la migration initiale, non un générateur réentrant.

## Protocole''',1)
prompt=prompt.replace('les sept rubriques','les huit rubriques').replace('navigation/UI, contenus,','navigation/UI, parcours opératoire, contenus,')
prompt=prompt.replace('- [ ] Sources et limites', '- [ ] Parcours : liens S09–S12, portes, retours, téléchargement Markdown et consultation autonome hors ligne.\n- [ ] Sources et limites')
write('prompts/PROMPT-MAITRE-CODEX-MODULE03.md', prompt)
for p in ['README.md','INDEX-PACK.md']:
    write(p,read(p)+'\n## Parcours opératoire intégré\n\nLa rubrique « Parcours opératoire » relie les étapes S09–S12, les contrôles humains et les retours correctifs. Elle propose le texte détaillé et son export Markdown hors ligne. Les deux documents Organigramme-Algorithme fournis sont préservés dans docs/ ; la version `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md` adapte les consignes au mini-site unique.\n')
write('docs/PROVENANCE.md',read('docs/PROVENANCE.md')+'\n## Intégration du parcours — 1er novembre 2026\n\nLes fichiers Organigramme-Algorithme-Module03-LN-IA.md et .docx sont des documents supplémentaires fournis par le pilote. Ils restent inchangés. Leur adaptation INTEGRE explicite les différences entre les quatre ateliers séparés et ce mini-site. Les références GitHub déclarées par ces documents n’ont pas été revérifiées pour cette intégration. La rubrique Parcours opératoire est une adaptation pédagogique, sans valeur de certification.\n')
write('docs/GUIDE-DOSSIER-PRO-MODULE03.md',read('docs/GUIDE-DOSSIER-PRO-MODULE03.md')+'\n## Complément — Parcours opératoire\n\nHuitième rubrique du mini-site : organigramme S09–S12, contrôles et retours correctifs, accès direct à chaque atelier et téléchargement de l’algorithme détaillé. Lire `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md` pour les manipulations adaptées et les limites réelles. Les documents initiaux Markdown et Word sont conservés.\n')
hashes={p:hashlib.sha256((root/(source+p)).read_bytes()).hexdigest() for p in ['.md','.docx']}
write('docs/EMPREINTES-ORGANIGRAMME-FOURNI.json',json.dumps(hashes,indent=2)+'\n')
