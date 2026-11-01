# Phase 10 — Stratégie Git et GitHub Pages

1er novembre 2026. Le pilote valide explicitement la phase 09 et autorise commit, configuration du remote, push et déploiement GitHub Pages via Actions, puis contrôle de l’URL et des journaux. Cette instruction est distincte des validations de contenus candidats.

## Dépôt réellement consulté

- Dépôt public : https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia
- Remote HTTPS : `https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia.git`.
- Identifiant retourné par GitHub : `1442252931` ; propriétaire `elhisse-CLPrepas` ; branche par défaut `main`.
- État initial observé : dépôt vide, API Contents indiquant « This repository is empty ». Aucun historique existant à réécrire.
- Configuration Pages initiale : API HTTP 404, site non configuré.

## Stratégie retenue

1. Initialiser le dépôt local sur `main` avec un premier commit limité aux exclusions `.gitignore` ; ajouter le remote exact et pousser sans forcer.
2. Créer `release/module03-pages` pour les sources, modèles pédagogiques, ressources autorisées, tests, preuves et workflow.
3. Vérifier les fichiers sélectionnés, exécuter les contrôles locaux et pousser la branche.
4. Ouvrir une Pull Request vers `main` pour rendre la livraison inspectable et exécuter la CI. La relecture humaine et les validations des phases 08/09 sont déjà déclarées par le pilote ; l’autorisation de publication est donnée dans son message de phase 10.
5. Configurer Pages sur GitHub Actions, puis fusionner la PR après réussite des contrôles. Aucun push forcé ni réécriture d’historique.
6. Contrôler le workflow de déploiement, ses jobs et journaux, puis la réponse HTTP et les ressources de l’URL effectivement retournée par GitHub Pages.
7. Consigner les identifiants réels et résultats observés dans `PHASE10-DEPLOIEMENT.md`. Aucun succès de déploiement n’est annoncé avant ces vérifications.

## Périmètre public

Le dépôt contient le code du mini-site, ses modèles non remplis, exemples FICTIFS, tests, ressources PDF/HTML et affiches demandées, ainsi que la documentation de pilotage. Le contrôle public refuse les archives historiques, `tmp/`, les dépendances, `dist/`, les dossiers privés, les Word sources et les motifs de clés. Les Word et archives restent conservés localement, sans suppression.

La mise en ligne Pages publie **uniquement `dist/`**, construit par Vite. Les archives et documents de pilotage ne sont pas copiés dans cet artefact ; les seules ressources documentaires Web sont celles de `public/`.

## Workflow

- Déclenchement sur Pull Request, push vers `main` et lancement manuel.
- Node 22, Python 3.12, installation `npm ci`, contrôle du périmètre, check, tests, build et génération autonome.
- Les PR exécutent les contrôles, sans déployer. `main` prépare l’artefact `dist/` et déploie dans l’environnement `github-pages`.
- Actions officielles fixées à des SHA réellement consultés ; permissions Pages/OIDC limitées au job de déploiement.
- Référence officielle : https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages.

## Réserves maintenues

Le pilote a effectué le contrôle visuel et pédagogique bureau/mobile. Les tests applicatifs en DOM de test ne prouvent pas les téléchargements physiques, dialogues natifs et console Chrome ; ces réserves restent documentées. L’autorisation explicite de phase 10 permet d’avancer avec ces réserves visibles, sans les transformer en tests réussis.
