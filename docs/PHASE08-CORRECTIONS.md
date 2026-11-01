# Phase 08 — Corrections fonctionnelles du Module 03

Date : 1er novembre 2026. Lot correctif réalisé ; les réserves de recette native restent ouvertes. Style et contenus pédagogiques conservés.

**Décision humaine ultérieure :** le pilote a explicitement déclaré « JE VALIDE la phase 8 » et demandé de passer à la phase 09. Le lot correctif est donc validé par le pilote dans ce périmètre. Les réserves natives décrites ci-dessous sont conservées et aucune autorisation de publication n’en est déduite. Voir [le dossier de preuves phase 09](PHASE09-DOSSIER-PREUVES.md).

## Point de départ

Le pilote déclare avoir effectué le contrôle visuel et pédagogique sur bureau et mobile. Il demande les contrôles fonctionnels restants et le passage à la phase 08. Computer Use échoue de nouveau à capturer Chrome ; la réserve est conservée dans `RECETTE-PHASE07.md`.

Pour contrôler le code de l’application, ajout d’un DOM minimal de test, sans dépendance supplémentaire, avec Node `vm`. Il exécute le vrai `src/app.js` et ses fonctions importées, en remplaçant seulement les interfaces DOM, stockage et URL de téléchargement par des objets isolés. Il ne rend pas le CSS, n’émule pas les dialogues natifs et ne télécharge rien dans le profil de l’utilisateur.

## Défauts reproduits et corrections

| Défaut constaté avant correction | Déclencheur | Correction et vérification |
|---|---|---|
| Notes de relecture remplacées par une trace d’import, même sans rubrique compatible | Importer un document avec un titre inconnu alors que des notes existent | Aucun changement si aucune rubrique ne correspond ; les imports compatibles ajoutent une trace sans effacer les notes. Tests des deux cas réussis. |
| Sélecteur conservant le fichier après refus pour taille | Sélectionner un fichier de plus de 500 000 octets | Réinitialisation placée dans `finally`, également lors d’un refus. Test du maintien des champs et de la remise à zéro réussi. |
| Focus clavier perdu après précédent/suivant | Activer un bouton de navigation de la présentation, dont le contenu est reconstruit | Fonction de navigation commune qui remet le focus sur le bouton correspondant. Tests des deux directions réussis. |
| Défilement natif laissé actif lors des flèches | ArrowRight ou ArrowLeft dans la présentation | `preventDefault()` uniquement pour les flèches prises en charge ; changement de diapositive et focus gérés ensemble. Test réussi. |
| Import en attente pouvant écrire dans une autre séance | Lancer la lecture d’un plan S11 puis ouvrir S12 avant la fin | Vérification de la séance et de l’identité du champ d’import avant toute écriture. Test avant correction : titre S12 remplacé ; test final : titre S12 conservé. |

La limite d’import reste 500 000 octets. Le rapprochement par titres et la limite de référence V1 après reconstruction de l’atelier sont conservés. Aucune fusion automatique entre séances ni validation pédagogique n’est ajoutée.

## Résultats

- Première suite applicative : 17 tests, 13 réussis et quatre échecs reproduits ; ces quatre échecs sont corrigés.
- Cas d’import asynchrone ajouté ensuite : échec reproduit avant correction, réussite après protection contre le changement d’atelier.
- Résultat final `npm.cmd test` : 32 tests réussis, aucun échec — 11 tests du cœur et 21 tests applicatifs.
- `npm.cmd run check` : réussi, syntaxe et synchronisation du parcours conformes.
- `npm.cmd run build` : réussi, neuf modules ; même feuille CSS compilée que la version précédente.
- `npm.cmd run standalone` : réussi, aperçu autonome reconstruit avec les corrections.
- La déclaration de contrôle visuel bureau/mobile vient du pilote ; les corrections de code ne valent pas nouvelle recette native de Chrome.

Les Blobs V1/V2, prompts, grilles, preuves et bilan sont contrôlés en mémoire. Leur contenu et leurs noms sont vérifiés ; la sauvegarde physique par le navigateur et sa console pendant les parcours ne sont pas certifiées.

## Fichiers et traçabilité

- `src/app.js` : corrections des imports et du clavier, avec mise en forme du gestionnaire d’import pour faciliter sa relecture.
- `tests/helpers/app-harness.mjs` : DOM de test minimal, explicitement distinct d’un navigateur.
- `tests/app.test.mjs` : 21 scénarios applicatifs et tests de non-régression.
- `APERCU-AUTONOME-MODULE03.html` et `dist/` : sorties reconstruites.
- README, recette et journal qualité : résultats et réserves actualisés.
- Copie du code avant correction : `tmp/avant-phase08/src/app.js`. Comparaison textuelle dans `PHASE08-CORRECTIONS.diff`, produite depuis cette copie ; ce n’est pas un diff Git. Le dossier courant n’est pas un dépôt Git local.

Les tests utilisent uniquement des données FICTIVES en mémoire. Aucun fichier candidat, archive historique, Word source ou PDF source n’est modifié. Aucune dépendance ajoutée, aucune permission modifiée, aucun commit, push ou déploiement public.

## Suite

Le lot de cinq corrections de phase 08 est réalisé et vérifié au niveau du code. Conserver la réserve sur les interactions natives tant que leur recette réelle n’est pas consignée. La documentation des preuves se poursuit en phase 09 ; la publication reste soumise à une autorisation distincte du pilote.
