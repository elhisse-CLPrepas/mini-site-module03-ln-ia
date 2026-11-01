import test from 'node:test';import assert from 'node:assert/strict';import {sessions,escapeHtml,markdownFor,incomplete,canExportV2,parseMarkdown,slides,quiz} from '../src/core.mjs';
test('quatre séances intégrées',()=>assert.deepEqual(sessions.map(x=>x.id),['S09','S10','S11','S12']));
test('six rubriques de S09',()=>assert.equal(sessions[0].fields.length,6));
test('S11 comporte cinq parties',()=>assert.equal(sessions[2].fields.filter(x=>['comprendre','preparer','produire','verifier','ameliorer'].includes(x[0])).length,5));
test('markdown canonique et provenance',()=>{const d=Object.fromEntries(sessions[0].fields.map(([k])=>[k,'Test']));const md=markdownFor(sessions[0],d);assert.match(md,/## Objectif du document/);assert.match(md,/À RELIRE/)});
test('incomplétude détectée',()=>assert.equal(incomplete(sessions[0],{}).length,6));
test('échappement XSS',()=>assert.equal(escapeHtml('<script>'), '&lt;script&gt;'));
test('V2 différente et journal exigés',()=>{assert.equal(canExportV2('A','A','Modification expliquée'),false);assert.equal(canExportV2('A','B',''),false);assert.equal(canExportV2('A','B','Correction précisée'),true)});
test('import sections',()=>assert.equal(parseMarkdown('# Doc\n## Sujet\nTitre\n## Public concerné\nÉlèves')['Sujet'].trim(),'Titre'));
test('slides et quiz',()=>{assert.equal(slides.length,20);assert.equal(quiz.length,10)});
test('aller-retour export/import des quatre séances avec accents et texte multiligne',()=>{
  for(const session of sessions){
    const values=Object.fromEntries(session.fields.map(([id])=>[id,'Consigne vérifiée\nDeuxième ligne <texte>']));
    const imported=parseMarkdown(markdownFor(session,values).replace(/\n/g,'\r\n'));
    for(const [id,label] of session.fields)assert.equal(imported[label].trim(),values[id]);
  }
});
test('V2 refuse une référence absente et un journal trop court',()=>{
  assert.equal(canExportV2('','B','Correction humaine documentée'),false);
  assert.equal(canExportV2('A','B','           '),false);
  assert.equal(canExportV2('A','B','12345678901'),false);
  assert.equal(canExportV2('A','B','123456789012'),true);
});
