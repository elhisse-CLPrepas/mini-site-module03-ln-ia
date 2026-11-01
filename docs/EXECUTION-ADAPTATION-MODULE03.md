# Adaptation des ateliers Module 03 — 1er novembre 2026

Statut : V1 À RELIRE. Travail local, sans publication.

## Inspection et cadrage

README, provenance, guide, prompt maître, journal qualité, passerelle Module 04 et annonce lus. Organigrammes Markdown lus ; contenu XML du Word source extrait sans modification, sans validation de sa mise en page. Quatre séances, huit rubriques, 20 diapositives, quatre cas fictifs et dix questions de quiz déjà présents. Aucun dépôt Git local détecté.

| Besoin | Source / adaptation | Action | Recette attendue |
|---|---|---|---|
| Guider chaque séance | Guide S09–S12 ; formulation Automne ajoutée | Consignes, prérequis, contrôle humain, classement | Vérifier les quatre ateliers |
| Accéder à la production | Chaîne note → fiche → plan → guide | Boutons depuis les quatre séances | Ouvrir la bonne séance |
| Préserver le contrôle humain | Prompt maître, limites de l’import et V2 | Rappels visibles ; conditions V2 conservées | Vérifier les refus V2 |
| Rendre les erreurs compréhensibles | Sécurité applicative | Capture des erreurs de lecture ; garde sur le cache local | Tester import illisible et cache invalide |
| Maintenir l’usage hors ligne | Aperçu autonome existant | Embarquer les nouvelles consignes | Reconstruire et contrôler le script |

## Lots réalisés et fichiers

- `src/session-guidance.js` : textes pédagogiques par séance, sans validation automatique ni faits nouveaux.
- `src/app.js` : encart de travail, boutons par séance, nom accessible de l’import, gestion des erreurs de lecture et cache invalide.
- `src/styles.css` : présentation des consignes, retour à la ligne des chemins, sélecteur contraint à sa largeur, focus du fichier importé et des résumés.
- `scripts/standalone.py` : intégration du nouveau module dans le HTML autonome.
- README, provenance, guide et journal qualité : description et limites actualisées.
- `dist/` et `APERCU-AUTONOME-MODULE03.html` : sorties régénérées.

Les copies antérieures des sources modifiées sont conservées dans `tmp/avant-adaptation-module03/`. Aucun diff Git disponible ; comparaison possible avec ces copies. Archives et travaux candidats conservés.

## Limites et décision humaine

La recette réelle bureau/mobile, clavier, imports, téléchargements et console JS reste nécessaire : l’accès navigateur indique « The browser access host is unavailable ». Les tests Node et la compilation ne prouvent pas ces interactions. Les contrôles pédagogiques restent humains. Sauver et exporter avant navigation ; la référence V1 S12 reste réinitialisée lorsque l’atelier est recréé.

La phase de publication n’est pas exécutée. La relecture pédagogique et la recette visuelle restent attendues avant toute décision du pilote sur commit, push ou déploiement.
