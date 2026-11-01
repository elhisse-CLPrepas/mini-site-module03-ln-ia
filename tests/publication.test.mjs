import test from 'node:test';
import assert from 'node:assert/strict';
import {publicationIssues} from '../scripts/verify-publication.mjs';

test('publication : archives, documents privés et fichiers d’environnement refusés',()=>{
  for(const name of ['sources-historiques/source.zip','tmp/notes.md','dossier-modele/08-archives-privees/prive.md','.env.local','docs/source.docx'])assert.ok(publicationIssues([name],()=>'' ).length>0,name);
});
test('publication : sources pédagogiques et ressources autorisées acceptées',()=>{
  assert.deepEqual(publicationIssues(['src/app.js','docs/PROVENANCE.md','public/ressources/affiche-01-parcours-module03.svg','public/ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf'],()=>'Texte pédagogique sans identifiant.'),[]);
});
test('publication : motifs de clés détectés sans les afficher',()=>{
  const secret='sk-proj-'+'a'.repeat(32);
  const issues=publicationIssues(['src/config.js'],()=>secret);
  assert.equal(issues.length,1);assert.ok(!issues[0].includes(secret));
});
