import fs from 'node:fs';import {sessions,slides,examples,bigQuestions,checks,quiz} from '../src/core.mjs';
import {parcoursMarkdown} from '../src/parcours-data.js';
const root=new URL('../',import.meta.url);const read=f=>fs.readFileSync(new URL(f,root),'utf8');
const html=read('index.html');const app=read('src/app.js');
function assert(v,s){if(!v)throw new Error(s)}
assert(sessions.length===4,'4 séances attendues');assert(slides.length===20,'20 slides attendues');assert(examples.length===4,'4 exemples attendus');assert(bigQuestions.length>=8,'questions de fond manquantes');assert(checks.length===10,'grille qualité incomplète');assert(quiz.length===10,'quiz incomplet');
assert(sessions[0].fields.length===6,'S09 doit avoir 6 rubriques');assert(sessions[2].fields.some(x=>x[0]==='ameliorer'),'S11 doit proposer 5 fonctions');
for(const s of sessions){assert(s.fields.length>=6,'modèle incomplet '+s.id);assert(read('docs/GUIDE-DOSSIER-PRO-MODULE03.md').includes(s.file),'livrable absent du guide '+s.file)}
assert(html.includes('id="main"')&&html.includes('id="nav"'),'navigation absente');assert(app.includes('canExportV2'),'garde V2 absent');
assert(!html.includes('sk-proj-'),'secret détecté dans HTML');console.log('Contrôle structure : OK (4 séances, 20 slides, 4 cas, 8 questions, 10 quiz, 10 critères).');
assert(parcoursMarkdown===read('docs/Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md').replace(/\r\n/g,'\n'),'texte du parcours désynchronisé');
assert(html.includes('data-go="parcours"')&&app.includes('parcours:operatingPath'),'rubrique parcours absente');
assert(app.includes("'parcours','atelier'")&&app.includes("active==='parcours'"),'route ou interactions du parcours absentes');
console.log('Parcours opératoire : route, interactions et synchronisation Markdown OK.');
