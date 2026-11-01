import test from 'node:test';
import assert from 'node:assert/strict';
import {appHarness} from './helpers/app-harness.mjs';
import {sessions,markdownFor} from '../src/core.mjs';

test('les neuf rubriques se rendent et leurs boutons s’activent',()=>{
  const app=appHarness();const nav=app.document.querySelectorAll('#nav button');assert.equal(nav.length,9);
  for(const button of nav){button.click();assert.ok(app.markup().includes('<h1>'));assert.equal(button.getAttribute('aria-current'),'page')}
});

for(const session of sessions){
  test(session.id+' : export du document et des pièces via les vrais gestionnaires',async()=>{
    const app=appHarness();app.session(session.id);app.fill(session);
    for(const id of ['v1','prompt','grille','preuve','bilan'])app.get(id).click();
    assert.equal(app.downloads.length,5);
    assert.deepEqual(app.downloads.map(output=>output.name),[
      session.file,`prompt-${session.id.toLowerCase()}.md`,`grille-relecture-${session.id.toLowerCase()}.md`,
      `preuve-seance-${session.num}.md`,'bilan-module-03.md',
    ]);
    const main=await app.downloads[0].blob.text();assert.match(main,/V1 — À RELIRE/);assert.match(main,/FICTIF/);
    for(const output of app.downloads)assert.ok((await output.blob.text()).length>80);
  });
  test(session.id+' : import du Markdown par titres et aperçu fidèle',async()=>{
    const app=appHarness();app.session(session.id);
    const values=Object.fromEntries(session.fields.map(([id])=>[id,'FICTIF — '+id+'\nTexte relu.']));
    await app.importFile({name:'fictif.md',size:100,text:async()=>markdownFor(session,values)});
    for(const [id] of session.fields)assert.equal(app.get('f-'+id).value,values[id]);
    assert.match(app.get('preview').textContent,/Texte relu/);assert.equal(app.get('importFile').value,'');
  });
}

test('les exports incomplets sont refusés sans produire de Blob',()=>{
  const app=appHarness();app.session('S09');app.get('v1').click();assert.equal(app.downloads.length,0);assert.match(app.get('status').textContent,/incomplets/);
});

test('S12 : refus sans V1, sans différence, sans journal et sans relecture ; V2 finale distincte',async()=>{
  const app=appHarness();app.session('S12');app.fill(sessions[3]);
  app.get('v2').click();assert.equal(app.downloads.length,0);assert.match(app.get('status').textContent,/d’abord la V1/);
  app.get('v1').click();const original=await app.downloads[0].blob.text();
  app.input('journal','Correction détaillée et vérifiée.');app.get('human').checked=true;app.get('v2').click();assert.equal(app.downloads.length,1);
  app.input('f-etape1','FICTIF — Action corrigée, résultat vérifiable.');app.input('journal','');app.get('v2').click();assert.equal(app.downloads.length,1);
  app.input('journal','Trop court');app.get('v2').click();assert.equal(app.downloads.length,1);
  app.input('journal','Correction détaillée et vérifiée.');app.get('human').checked=false;app.get('v2').click();assert.equal(app.downloads.length,1);assert.match(app.get('status').textContent,/relecture humaine/);
  app.get('human').checked=true;app.get('v2').click();assert.equal(app.downloads.length,2);
  assert.equal(app.downloads[1].name,'guide-pratique-v2-a-relire.md');
  const revised=await app.downloads[1].blob.text();assert.match(revised,/V2 — À RELIRE/);assert.match(revised,/## Journal de corrections/);assert.notEqual(revised,original);assert.equal(await app.downloads[0].blob.text(),original);
});

test('sauvegarde et reprise isolées ; quota et cache invalide gérés',()=>{
  const app=appHarness();app.session('S09');app.fill(sessions[0]);const before=app.get('f-sujet').value;app.get('save').click();app.view('accueil');app.view('atelier');assert.equal(app.get('f-sujet').value,before);
  const quota=appHarness({storageError:true});quota.session('S09');quota.get('save').click();assert.match(quota.get('status').textContent,/indisponible/);
  for(const storageValue of ['null','[1,2]','invalide'])assert.doesNotThrow(()=>appHarness({storageValue}).session('S09'));
});

test('une erreur de lecture conserve les champs et les notes',async()=>{
  const app=appHarness();app.session('S09');app.input('f-sujet','FICTIF — sujet existant');app.input('review','Note à conserver');
  await app.importFile({name:'illisible.md',size:100,text:async()=>{throw new Error('Lecture refusée')}});
  assert.equal(app.get('f-sujet').value,'FICTIF — sujet existant');assert.equal(app.get('review').value,'Note à conserver');assert.match(app.get('status').textContent,/impossible/);
});

// Régressions constatées en phase 07 et corrigées en phase 08.
test('un import sans titre reconnu conserve aussi les notes existantes',async()=>{
  const app=appHarness();app.session('S09');app.input('review','Note à conserver');
  await app.importFile({name:'autre.md',size:30,text:async()=>'# Autre document\n## Inconnu\nTexte'});
  assert.equal(app.get('review').value,'Note à conserver');
});
test('un fichier trop volumineux est refusé et le sélecteur est réutilisable',async()=>{
  const app=appHarness();app.session('S09');app.input('f-sujet','FICTIF — inchangé');
  await app.importFile({name:'trop-grand.md',size:500001,text:async()=>{throw new Error('ne doit pas être lu')}});
  assert.equal(app.get('f-sujet').value,'FICTIF — inchangé');assert.match(app.get('status').textContent,/volumineux/);assert.equal(app.get('importFile').value,'');
});
test('la navigation précédente/suivante conserve le focus clavier',()=>{
  const app=appHarness();app.view('presentation');app.get('next').focus();app.get('next').click();assert.match(app.markup(),/2 \/ 20/);assert.equal(app.document.activeElement.id,'next');
  app.get('prev').click();assert.match(app.markup(),/1 \/ 20/);assert.equal(app.document.activeElement.id,'prev');
});
test('les flèches changent de diapositive sans déclencher le défilement natif',()=>{
  const app=appHarness();app.view('presentation');const event=app.key('ArrowRight');assert.match(app.markup(),/2 \/ 20/);assert.equal(event.defaultPrevented,true);
});
test('un import compatible complète la trace sans effacer les notes',async()=>{
  const app=appHarness();app.session('S09');app.input('review','Note à conserver');
  await app.importFile({name:'fictif.md',size:30,text:async()=>'## Sujet\nSujet fictif'});
  assert.equal(app.get('f-sujet').value,'Sujet fictif');assert.match(app.get('review').value,/Note à conserver\nImport de fictif.md/);
});
test('un import en cours ne modifie pas une autre séance ouverte entre-temps',async()=>{
  const app=appHarness();app.session('S11');let finish;
  const pending=app.importFile({name:'plan-fictif.md',size:100,text:()=>new Promise(resolve=>{finish=resolve})});
  app.session('S12');app.fill(sessions[3]);const before=app.get('f-titre').value;
  finish(markdownFor(sessions[2],Object.fromEntries(sessions[2].fields.map(([id])=>[id,'AUTRE SÉANCE — '+id]))));
  await pending;assert.equal(app.get('f-titre').value,before);
});
test('le sommaire ouvre la dernière diapositive et les notes restent accessibles',()=>{
  const app=appHarness();app.view('presentation');const toc=app.document.querySelectorAll('[data-slide]');assert.equal(toc.length,20);toc[19].click();
  assert.match(app.markup(),/20 \/ 20/);assert.equal(app.document.activeElement.id,'next');assert.equal(app.get('note').hidden,true);app.get('notes').click();assert.equal(app.get('note').hidden,false);
});
test('le quiz peut être corrigé sans attribuer de validation au document',()=>{
  const app=appHarness();app.view('qualite');
  const correct=[1,0,1,0,0,1,0,0,0,1];
  correct.forEach((answer,i)=>app.document.querySelectorAll('input[name=q'+i+']')[answer].checked=true);
  app.get('grade').click();assert.match(app.get('result').textContent,/10\/10/);assert.match(app.get('result').textContent,/ne valide aucun document/);
});
