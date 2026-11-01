import fs from 'node:fs';
const root=new URL('../',import.meta.url);
const markdown=fs.readFileSync(new URL('docs/Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md',root),'utf8').replace(/\r\n/g,'\n');
fs.writeFileSync(new URL('src/parcours-data.js',root),'export const parcoursMarkdown = '+JSON.stringify(markdown)+';\n');
console.log('Instructions du parcours synchronisées.');
