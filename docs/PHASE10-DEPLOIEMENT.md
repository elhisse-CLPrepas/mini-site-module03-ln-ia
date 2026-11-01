# Phase 10 — Livraison Git et déploiement vérifiés

Le 1er novembre 2026, le pilote valide la phase 09 et autorise explicitement commit, remote/push, déploiement Pages via Actions et contrôle de l’URL et des journaux. Les opérations suivantes sont réellement exécutées.

## Historique Git

- Dépôt public : https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia (initialement vide, ID 1442252931).
- Remote origin HTTPS : https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia.git.
- Initialisation des exclusions : `b156ea882ae27aed4e18a8989961ba49945d10c4` (`.gitignore` et `.gitattributes`).
- Livraison sur `release/module03-pages` : `f9b5dc14d6278a13e6cc20f64a8370b51c8a12da`.
- [Pull Request nº1](https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia/pull/1), fusionnée après réussite de la CI : commit réel `cc4bc733504cbd48eb658d71b850491bd58a2180`.
- Aucun push forcé, aucune suppression d’archive, aucun changement de permissions des fichiers. La configuration Pages a été créée avec `build_type=workflow`.

## Actions et journaux consultés

- [CI de la PR, exécution 41362285699](https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia/actions/runs/41362285699) : build réussi, déploiement volontairement ignoré sur PR.
- [Premier déploiement, exécution 41362848744](https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia/actions/runs/41362848744) : build et deploy terminés avec `success`.
- Jobs réellement consultés : build `125016723727`, deploy `125016797749`. Journaux téléchargés et lus via le connecteur GitHub.
- Installation depuis le verrou, contrôle du périmètre public, `npm run check`, `npm test`, `npm run build`, `npm run standalone` : étapes réussies. Journaux de test : **35 tests, 35 réussis, 0 échec**.
- Artefact `github-pages` ID `13106295157`, taille compressée annoncée par Actions : 2 175 593 octets. Seul `dist/` est envoyé au déploiement. Le journal de déploiement retourne « Reported success! ».
- Horodatages GitHub du premier déploiement : création `2026-11-01T23:35:26Z`, fin `2026-11-01T23:36:01Z`. L’horloge locale utilisée pour le contrôle HTTP présente un décalage ; ne pas déduire de durée en croisant ces deux horloges.

## URL et ressources contrôlées

**Site : https://elhisse-clprepas.github.io/mini-site-module03-ln-ia/**

Le relevé [PHASE10-CONTROLES-HTTP.json](PHASE10-CONTROLES-HTTP.json) conserve les réponses, tailles et SHA-256 réellement calculés sur les octets reçus. L’accueil, les bundles JavaScript/CSS, le logo, le guide HTML, le PDF et les quatre affiches PNG/SVG répondent HTTP 200. Les sept fichiers de `public/` servis sont identiques octet par octet aux sources locales contrôlées.

Les trois chemins testés `.env`, archive historique et Word source répondent 404. Cette vérification ponctuelle complète les exclusions Git et le contrôle des fichiers suivis ; elle ne prétend pas constituer un audit exhaustif de secrets. Les cinq archives et les Word restent locaux.

## Périmètre et limites

Trois tests de publication s’ajoutent aux 32 tests du cœur et de l’application. Le thème et les contenus pédagogiques restent ceux des phases validées. Les contrôles HTTP et les journaux CI ne remplacent pas une recette native du navigateur : dialogues de fichiers, téléchargements physiques, clavier natif et console Chrome restent à confirmer. Le contrôle visuel et pédagogique bureau/mobile demeure attribué au pilote.

La publication du mini-site ne valide aucun travail candidat V1/V2. Les exemples restent FICTIFS. La documentation finale sera enregistrée dans un commit distinct ; le présent rapport décrit le premier déploiement attesté et ne prétend pas contenir le SHA de son propre commit.
