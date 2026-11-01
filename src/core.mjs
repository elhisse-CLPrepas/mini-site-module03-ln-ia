export const sessions = [
 {id:'S09',num:'09',label:'Note de cadrage courte',verb:'Cadrer',type:'COMPRENDRE',file:'note-cadrage-courte.md',date:'23 octobre 2026',desc:'Six rubriques : sujet, public, besoin, objectif du document, résultat attendu et première action.',fields:[['sujet','Sujet'],['public','Public concerné'],['besoin','Problème ou besoin'],['objectif','Objectif du document'],['resultat','Résultat attendu'],['premiere','Première action']]},
 {id:'S10',num:'10',label:'Fiche projet V1',verb:'Structurer',type:'PRATIQUER',file:'fiche-projet-v1.md',date:'26 octobre 2026',desc:'Objectif, public, problème, solution, livrables, étapes, outils, responsabilités, critères de réussite et prochaine action.',fields:[['nom','Nom du projet'],['objectif','Objectif'],['public','Public cible'],['probleme','Problème traité'],['solution','Solution proposée'],['livrables','Livrables attendus'],['etapes','Étapes de production'],['outils','Ressources et outils'],['criteres','Critères de réussite'],['risques','Risques et limites'],['validation','Qui décide et contrôle ?'],['action','Prochaine action']]},
 {id:'S11',num:'11',label:'Plan du guide pratique',verb:'Organiser',type:'COMPRENDRE',file:'plan-guide-pratique.md',date:'30 octobre 2026',desc:'Titre, public, résultat et prérequis. Cinq parties : Comprendre, Préparer, Produire, Vérifier, Améliorer.',fields:[['titre','Titre du guide'],['public','Public visé'],['resultat','Résultat attendu'],['prerequis','Prérequis'],['comprendre','Partie 1 — Comprendre'],['preparer','Partie 2 — Préparer'],['produire','Partie 3 — Produire'],['verifier','Partie 4 — Vérifier'],['ameliorer','Partie 5 — Améliorer'],['checklist','Checklist prévue'],['incertitudes','Points à vérifier par l’humain'],['priorite','Partie prioritaire pour S12']]},
 {id:'S12',num:'12',label:'Guide pratique V1 → V2',verb:'Produire',type:'PRATIQUER',file:'guide-pratique-v1.md',date:'2 novembre 2026',desc:'Guide orienté action, V1 relue, V2 corrigée, grille qualité, journal de modifications et portfolio.',fields:[['titre','Titre du guide'],['public','Pour qui ?'],['objectif','Objectif du guide'],['resultat','Résultat attendu'],['prerequis','Prérequis'],['etape1','Étape 1 — Action et contrôle'],['etape2','Étape 2 — Action et contrôle'],['etape3','Étape 3 — Action et contrôle'],['erreurs','Erreurs à éviter'],['checklist','Checklist finale'],['incertitudes','Points à vérifier par l’humain'],['amelioration','Prochaine amélioration']]}
];
export const slides=[
 ['Pourquoi un dossier professionnel ?','Rendre le travail avec l’IA compréhensible, vérifiable et réutilisable.','Demander la différence entre un texte et un dossier documenté.'],
 ['Une chaîne complète','Besoin → Cadrage → Prompt → Production → Contrôle → Correction → Documentation → Preuve.','Localiser la décision humaine.'],
 ['Quatre séances, un projet','S09 clarifie. S10 formalise. S11 organise. S12 produit et améliore.','Utiliser un même cas fictif.'],
 ['S09 : les six rubriques','Sujet, public, besoin, objectif du document, résultat attendu, première action.','Les cinq questions historiques sont un résumé, non les six rubriques du modèle.'],
 ['Cadrage avant rédaction','Une demande vague entraîne des livrables dispersés.','Faire reformuler un besoin.'],
 ['S10 : fiche projet','Objectif, solution, livrables, étapes, moyens et critères.','Distinguer objectif et livrable.'],
 ['Rôles et responsabilités','L’IA assiste, le candidat pilote, le formateur autorise.','Qui vérifie et publie ?'],
 ['S11 : architecture du guide','Concevoir le parcours lecteur sans rédiger le guide complet.','Comparer plan et texte intégral.'],
 ['Les cinq fonctions','Comprendre / Préparer / Produire / Vérifier / Améliorer.','Associer une action à chaque partie.'],
 ['S12 : V1 actionnable','Public identifié, étapes concrètes, erreurs et checklist.','Transformer un titre abstrait en consigne.'],
 ['V2 et corrections','Une V2 explique ce qui change et pourquoi.','Montrer un journal de modification.'],
 ['Sources et faits','Identifier les informations à vérifier, ne rien inventer.','Faire marquer [À VÉRIFIER].'],
 ['Limites de l’automatisation','Un score ou une case cochée ne donne pas le statut VALIDÉ.','Distinguer contrôle technique et validation métier.'],
 ['Sécurité documentaire','Pas de secrets, de données sensibles ni de publication non autorisée.','Vérifier les fichiers publics.'],
 ['Preuve portfolio','Conserver versions, prompts, décisions et corrections.','Décrire une preuve observable.'],
 ['Dossier personnel et collectif','Git, conventions de nommage, revues et responsabilités.','Éviter la confusion entre volume et qualité.'],
 ['Production à grande échelle','Modèles réutilisables, jalons et revues humaines.','Distinguer standardisation et besoins locaux.'],
 ['Mesurer sans inventer','Qualité, temps observé, défauts, réutilisation et traçabilité.','Ne jamais supposer un gain chiffré.'],
 ['Atelier de production','Saisir, contrôler, exporter et ranger les quatre fichiers.','Montrer la fonction export, puis faire pratiquer.'],
 ['Bilan et passage à l’action','Un dossier professionnel démontre une progression réelle.','Demander une réalisation et une correction vérifiables.']
];
export const examples=[
 ['Formation à Markdown','Formateurs débutants','Un premier support pratique avec vérification de la mise en forme'],
 ['Accueil scolaire','Nouveaux élèves fictifs','Un guide d’orientation à tester par un lecteur'],
 ['Processus administratif','Collaborateurs d’une structure fictive','Une procédure avec contrôles et responsabilité humaine'],
 ['Projet associatif','Bénévoles d’une équipe fictive','Un guide de préparation avec rôles et checklist']
];
export const bigQuestions=[
 ['Pourquoi le dossier professionnel ?','Pour relier besoin, décisions, productions et preuves, et rendre un travail examinable.'],
 ['Quelle utilité ?','Conduire des projets, communiquer des consignes, former, transmettre et améliorer un processus.'],
 ['Comment le produire ?','Partir d’un besoin réel, rédiger S09, structurer S10, organiser S11, produire et corriger S12.'],
 ['Quelles dimensions ?','Pédagogie, documentation, architecture numérique, sécurité, qualité, organisation, collaboration, traçabilité.'],
 ['Produire mieux et à grande échelle ?','Normaliser les trames, attribuer les responsabilités, garder l’historique et contrôler les résultats.'],
 ['Quelle ambition ?','Passer d’utilisateur d’IA à producteur autonome capable de transmettre et maintenir ses solutions.'],
 ['Quelles limites et quels critères ?','Une IA peut inventer. Examiner exactitude, utilité, clarté, faisabilité, sécurité et validation.'],
 ['Quelles erreurs et protections ?','Éviter données sensibles, fausses promesses, confusion V1/V2, diffusion sans autorisation et preuves non vérifiées.']
];
export const checks=['Sujet, public et besoin explicites','Objectif et résultat observables','Plan et étapes cohérents','Sources et lacunes documentées','Informations essentielles vérifiées','Confidentialité et autorisations contrôlées','Prompts et contribution IA tracés','Correction humaine décrite','Versions V1/V2 distinctes','Preuves et statut conservés'];
export const quiz=[
 ['La note de cadrage comporte…',['5 sections','6 sections','12 sections'],1,'Le modèle a 6 rubriques, dont l’objectif du document.'],
 ['La fiche projet sert à…',['Structurer les actions','Effacer le besoin','Valider automatiquement'],0,'Elle opérationnalise le cadrage.'],
 ['La séance 11 produit…',['Le guide final','Un plan de guide','Un diplôme'],1,'Le plan prépare la rédaction.'],
 ['Le plan de guide est organisé en…',['Comprendre, Préparer, Produire, Vérifier, Améliorer','Rédiger, Publier','Une seule partie'],0,'Cinq fonctions maximales proposées.'],
 ['La V2 exige…',['Un texte distinct et des corrections tracées','Seulement un clic','La suppression de V1'],0,'La révision doit être explicable.'],
 ['Une checklist cochée…',['Certifie tout','Prépare le contrôle, sans certifier','Supprime les risques'],1,'La validation finale appartient à l’humain autorisé.'],
 ['Quelle information éviter sur Pages ?',['Des secrets','Un titre public','Une description générale'],0,'Un site public n’est pas un coffre privé.'],
 ['Le portfolio sert à…',['Conserver les preuves','Remplacer le guide','Inventer un résultat'],0,'Il documente les productions et corrections.'],
 ['À grande échelle, privilégier…',['Modèles et revues','Promesses chiffrées','Absence de validation'],0,'Standardiser sans retirer les contrôles.'],
 ['Un gain de temps doit être…',['Présumé','Mesuré avec observations','Imaginé'],1,'Aucun gain inventé.']
];
export function escapeHtml(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
export function markdownFor(session,values,vers='V1 — À RELIRE',notes=''){return ['# '+session.label,'',`**Module :** 03 · Dossier professionnel`,`**Séance :** ${session.id}`,`**Version :** ${vers}`,'',...session.fields.flatMap(([id,label])=>[`## ${label}`,'',values[id]?.trim()||'[À COMPLÉTER]','']),'## Vérifications humaines','',notes||'[À documenter]',''].join('\n');}
export function incomplete(session,values){return session.fields.filter(([id])=>!String(values[id]||'').trim()).map(x=>x[1]);}
export function canExportV2(snap,now,journal){return !!(snap&&now&&snap!==now&&String(journal||'').trim().length>=12);}
export function parseMarkdown(str){const out={};let key=null;for(const l of String(str).split(/\r?\n/)){let m=/^## (.+)/.exec(l);if(m){key=m[1].trim();out[key]='';}else if(key)out[key]+=(out[key]?'\n':'')+l}return out;}
