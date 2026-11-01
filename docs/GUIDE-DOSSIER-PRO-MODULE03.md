# Guide de référence — Le dossier professionnel comme base de la production avec l'IA

> **Périmètre demandé par le pilote :** le mini-site est centré sur le Module 03 et ses quatre séances S09–S12. Le guide Word fourni dispose de versions de consultation PDF et HTML dans la rubrique Ressources.

**LAB-NUMÉRIQUE-IA (LN-IA)** — Challenge 100 Jours · Relance Automne 2026  
**Module 03 : Dossier professionnel · Semaines pédagogiques 05 et 06 · Séances 09 à 12**  
**Pilotage : Prof. Abderrahman EL HISSE**  
**Édition : V1 de synthèse · 1er novembre 2026 · À RELIRE / À VALIDER**

**État du pilotage du mini-site :** phase 08 validée explicitement par le pilote ; dossier documentaire de phase 09 dans [PHASE09-DOSSIER-PREUVES.md](PHASE09-DOSSIER-PREUVES.md). La validation de ce lot technique ne valide pas les productions candidates ni la diffusion. Les réserves de recette native restent indiquées dans le dossier de preuves. Le contenu de ce guide conserve son statut de synthèse À RELIRE.

> **Thèse pédagogique.** L'IA permet d'accélérer certaines opérations documentaires. Elle ne remplace pas le cadrage, la vérification, la décision et la responsabilité humaines. Un dossier professionnel sert à rendre le cheminement de l'idée au livrable explicable, contrôlable et transmissible.

## Sommaire

1. Pourquoi le dossier professionnel ?
2. Les usages et la valeur du dossier
3. Architecture et progression S09–S12
4. Séance 09 — La note de cadrage courte
5. Séance 10 — La fiche projet V1
6. Séance 11 — Le plan du guide pratique
7. Séance 12 — Le guide pratique V1 et sa correction V2
8. Arborescence de référence et conventions de nommage
9. Prompts, preuves et portfolio
10. Critères de qualité et validation humaine
11. Difficultés, risques et sécurité
12. Produire mieux et à plus grande échelle
13. Développement numérique et mini-site Vite
14. Évaluation et critères de réussite
15. Étude de cas fictive fil rouge
16. Guide de mise en œuvre du pack et sources

## 1. Pourquoi le dossier professionnel ?

Un prompt peut produire une réponse immédiatement. Cette réponse isolée ne garantit ni sa pertinence pour un public, ni la justesse des faits, ni la possibilité de la reprendre plus tard. Le dossier professionnel ajoute une structure stable : le besoin de départ, les choix du candidat, le livrable, la relecture, la correction et la preuve du travail effectivement réalisé.

Le dossier répond à quatre besoins : **cadrer** pour éviter la dispersion ; **rendre l'action possible** par une structure ; **contrôler** les résultats avec des critères ; **transmettre** la méthode et les fichiers à une autre personne. Sa valeur vient moins du nombre de pages que de la possibilité de vérifier comment un document a été produit et pourquoi il a été corrigé.

Le dossier est également une pédagogie de la responsabilité : l'IA propose, l'utilisateur arbitre, le formateur accompagne et le pilote habilité valide. La présence d'une checklist ou d'un score de quiz ne vaut jamais décision de validation professionnelle.

## 2. Raison, utilité et bénéficiaires

- **Enseignant / formateur** : planifier une séquence, préparer un support et expliquer ses limites.
- **Coach / accompagnateur** : traduire un besoin en plan de travail, sans promettre un résultat garanti.
- **Entrepreneur / manager** : cadrer une initiative, répartir les tâches et définir des critères observables.
- **Étudiant / apprenant** : apprendre à documenter ses choix, produire une V1 et argumenter ses corrections.
- **Équipe professionnelle** : partager une convention de classement et organiser la revue avant diffusion.

Le dossier doit être **utile à une personne identifiée**. Avant de commencer, demander : pour qui travaille-t-on, quel problème doit être traité et qu'est-ce qui permettra de constater un résultat ?

## 3. Les quatre séances comme architecture d'un seul projet

| Séance | Posture | Question principale | Livrable | Preuve |
|---|---|---|---|---|
| S09 — 23/10/2026 | Comprendre | Que veut-on réellement traiter et pour qui ? | `note-cadrage-courte.md` | `preuve-seance-09.md` |
| S10 — 26/10/2026 | Pratiquer | Comment transformer ce besoin en projet réalisable ? | `fiche-projet-v1.md` | `preuve-seance-10.md` |
| S11 — 30/10/2026 | Comprendre | Quelle structure aidera le lecteur à agir ? | `plan-guide-pratique.md` | `preuve-seance-11.md` |
| S12 — 02/11/2026 | Pratiquer | Comment rédiger, contrôler et améliorer le guide ? | `guide-pratique-v1.md`, `guide-pratique-v2-a-relire.md` | `preuve-seance-12.md` |

La logique est cumulative : il faut pouvoir suivre **un même besoin** dans tous les fichiers. Si la fiche projet ne correspond plus à la note de cadrage, l'écart doit être expliqué. Si le guide ajoute un nouveau public ou une promesse, revenir à la fiche projet et documenter la décision.

### Un point d'harmonisation des sources

Les supports historiques S09 utilisent parfois *cinq questions clés* comme aide de démarrage, mais le modèle documenté comporte **six rubriques** : sujet, public, problème ou besoin, objectif du document, résultat attendu, première action. La présente édition conserve ces six rubriques. Les archives sont préservées sans modification.

Certains fichiers historiques utilisent le dossier `02-DOCUMENTS/`. Pour éviter les doubles classements, l'édition Automne adopte `03-documents/` pour les livrables, `02-prompts/` pour les consignes et `07-portfolio/` pour les preuves.

## 4. Séance 09 — Comprendre la note de cadrage courte

**Intention.** Délimiter une demande avant de générer un contenu. La note n'est pas un rapport, ni un texte promotionnel. Elle fournit le cadre minimal à partir duquel une autre personne pourrait commencer le projet.

**Six rubriques canoniques :**

1. **Sujet** : décrire ce dont il est question en une phrase.
2. **Public concerné** : nommer les destinataires du document.
3. **Problème ou besoin** : expliquer ce qui manque ou mérite d'être résolu.
4. **Objectif du document** : préciser son rôle et son utilité.
5. **Résultat attendu** : décrire le livrable observable.
6. **Première action** : choisir une action concrète et réalisable.

**Exercice.** Produire une note courte pour un projet réel, puis la faire relire par une personne qui n'en connaît pas le contexte. Demander à cette personne de reformuler le sujet, le public et le résultat attendu. Corriger les formulations vagues ou les promesses excessives.

**Livrable.** `03-documents/note-cadrage-courte.md` — statut `V1 — À RELIRE`. La preuve doit expliquer ce que l'IA a proposé, ce qui a été modifié et quelle information reste incertaine.

## 5. Séance 10 — Pratiquer : de la note à la fiche projet V1

**Intention.** Transformer une intention claire en proposition de production réalisable. La fiche projet sert au pilotage : elle distingue objectif, solution, ressources, livrables, étapes et conditions de réussite.

**Champs conseillés :** nom du projet, objectif, public cible, problème traité, solution proposée, livrables attendus, outils et ressources, étapes de production, critères de réussite, risques/limites, responsabilité de contrôle, prochaine action. Cette trame de douze champs est une **harmonisation pédagogique de l'édition Automne**, pas l'affirmation que tous les supports historiques portaient exactement ces douze intitulés.

**Exercice.** Comparer chaque rubrique à la note S09. Rechercher les ajouts non justifiés. Remplacer les promesses générales par des actions et des critères observables. Conserver les hypothèses sous la mention `[À VÉRIFIER]`.

**Livrable.** `03-documents/fiche-projet-v1.md`. Garder aussi `02-prompts/prompt-fiche-projet-s10.md`, une grille de relecture et la trace S10.

## 6. Séance 11 — Comprendre le plan du guide pratique

**Intention.** Concevoir un parcours de lecture avant la rédaction. Le plan est une architecture documentaire, pas le guide complet.

Le plan identifie le titre, le public, le résultat que le lecteur doit pouvoir obtenir, les prérequis et **cinq parties au maximum** :

1. **Comprendre** — problème, contexte, notions de base.
2. **Préparer** — matériel, documents, connaissances et prérequis.
3. **Produire** — étapes prévues et livrables.
4. **Vérifier** — critères, contrôles et erreurs à détecter.
5. **Améliorer** — corrections et évolution de la version suivante.

Chaque partie doit posséder un objectif et au moins une action du lecteur. La structure comporte aussi une checklist finale, des points à contrôler par l'humain et une partie prioritaire pour la séance 12.

**Livrable.** `03-documents/plan-guide-pratique.md`. Ne pas confondre architecture et rédaction : cette distinction est centrale dans les supports S11.

## 7. Séance 12 — Produire la V1 puis une V2 corrigée

**Intention.** Transformer le plan en guide d'usage. Une V1 constitue une première version suffisamment claire pour être testée et corrigée, non une version certifiée.

Un guide pratique minimal doit comporter : objectif, public, résultat attendu, prérequis, au moins trois actions ordonnées, erreurs à éviter, checklist finale, points à vérifier, prochaine amélioration. Les **cinq fonctions du plan** servent d'organisation ; elles ne remplacent pas les instructions concrètes du guide.

**Cycle de version :**

1. Produire un brouillon avec l'aide éventuelle d'un modèle IA.
2. Identifier les passages imprécis, erreurs factuelles, oublis et risques.
3. Corriger sous contrôle humain et enregistrer `guide-pratique-v1.md`.
4. Proposer une nouvelle version avec modifications effectivement réalisées.
5. Rédiger un journal : passage modifié, motif, vérification et responsable.
6. Enregistrer `guide-pratique-v2-a-relire.md`, sans présumer de sa validation.

**Règle de preuve.** Une V2 identique à la V1, sans journal, ne démontre aucune correction. Une correction de style et une correction de fond doivent être distinguées. Toute publication requiert une décision humaine explicite.

## 8. Arborescence de référence

```text
challenge-100-jours-module-03/
├── 00-pilotage/
│   ├── README.md
│   ├── charte-projet.md
│   └── journal-decisions.md
├── 01-besoin/
│   ├── fiche-identification-projet.md
│   └── sources-autorisées.md
├── 02-prompts/
│   ├── prompt-note-cadrage-s09.md
│   ├── prompt-fiche-projet-s10.md
│   ├── prompt-plan-s11.md
│   └── prompt-guide-s12.md
├── 03-documents/
│   ├── note-cadrage-courte.md
│   ├── fiche-projet-v1.md
│   ├── plan-guide-pratique.md
│   ├── guide-pratique-v1.md
│   ├── guide-pratique-v2-a-relire.md
│   ├── grille-relecture-s12.md
│   └── journal-corrections-v1-v2.md
├── 04-ressources/
│   ├── bibliographie.md
│   └── registre-sources.md
├── 05-controles/
│   ├── grille-qualite-module-03.md
│   ├── verification-faits.md
│   └── registre-risques.md
├── 06-publication/
│   ├── controle-diffusion.md
│   └── preparation-github-pages.md
├── 07-portfolio/
│   ├── preuve-seance-09.md
│   ├── preuve-seance-10.md
│   ├── preuve-seance-11.md
│   ├── preuve-seance-12.md
│   ├── preuves-module-03.md
│   └── bilan-module-03.md
└── 08-archives-privees/
    └── README.md
```

**Convention.** Fichiers UTF-8, Markdown lisible, noms stables en minuscules avec traits d'union. Le numéro du dossier ne représente pas une séance. Éviter `final-final.md`, les noms avec dates arbitraires et les renommages sans journal. Le répertoire des archives personnelles reste **privé**, jamais dans le site public.

Les dossiers `00-`, `01-`, `04-`, `05-`, `06-` et `08-` sont des **ajouts de structuration proposés ici** pour rendre le système complet. Les séances sources portent principalement sur les documents, prompts et preuves.

## 9. Prompts, livrables, preuves et portfolio

Un **prompt** décrit la mission de l'assistant, les données de départ, les contraintes, le format attendu, les points à vérifier et le rôle de l'humain. Il n'est pas la preuve que les faits produits sont exacts.

Un **livrable** est le document produit pour un public et une finalité. Il porte un titre, une version, un statut de relecture et une provenance.

Une **preuve** explique ce qui a réellement été réalisé : fichier, date, situation de départ, contribution de l'IA, actions du candidat, contrôle humain, modifications et limites restantes. Elle peut citer un commit, un rapport de test ou un retour humain réellement disponible.

Le **portfolio** rassemble les preuves et les décisions sans prétendre que toutes les versions sont validées. Il permet de présenter le développement d'une compétence par les réalisations et les corrections.

### Trame de preuve commune

```markdown
# Preuve SXX — Intitulé
Date : [à renseigner]
Fichier : [chemin relatif]
Statut : V1 / V2 À RELIRE
Besoin initial : ...
Prompt / assistance IA utilisée : ...
Livrable produit : ...
Corrections effectuées par l'humain : ...
Limites, faits et autorisations à vérifier : ...
Décision du pilote (si obtenue) : ...
Prochaine étape : ...
```

## 10. Critères, validation et limites

**Contrôles minimaux :** clarté du besoin ; public nommé ; objectif observable ; livrables cohérents ; étapes actionnables ; faits vérifiés ; absence de données non autorisées ; traces des versions ; correction humaine ; preuve classée. Des grilles S09 à S12 sont proposées dans le pack.

**Statuts distincts :** `Brouillon`, `V1 — À RELIRE`, `V2 — À RELIRE`, `À COMPLÉTER`, `VALIDÉ PAR [responsable] LE [date]`. Le statut « validé » doit être attribué sur décision réelle de la personne autorisée. Ni le site, ni le quiz, ni une case cochée n'attribuent ce statut automatiquement.

**Limites de l'IA :** hallucination, omissions, ambiguïtés, erreurs dans les chiffres, approximations juridiques, dépendance au prompt, biais de sélection. Les productions doivent être lues et vérifiées dans leur contexte. Les cas fictifs ne doivent jamais être présentés comme des expériences réelles.

## 11. Erreurs, sécurité et droits

- **Données sensibles** : ne pas saisir de secrets, identifiants, informations confidentielles ou données personnelles dans un site public ou un prompt partagé sans base appropriée.
- **Publication** : une GitHub Page est accessible publiquement ; ne pas inclure les archives personnelles, les sources privées, les fichiers locaux des candidats ou des clés API.
- **Provenance** : différencier données du participant, démonstrations fictives, sources documentaires et interprétations de l'IA.
- **Droits d'usage** : contrôler les droits sur les images, contenus tiers, citations et modèles avant diffusion.
- **Sécurité applicative** : valider les entrées, échapper les contenus affichés, limiter l'import et éviter de placer des données privées en stockage local partagé.
- **Validation métier** : les décisions en droit, santé, finances ou sécurité demandent la vérification par une personne compétente ; ne pas utiliser l'IA comme autorité finale.
- **Erreurs de méthode** : ne pas confondre longueur et profondeur, plan et guide, V1 et V2, preuve et certification, assistance et autorisation.

## 12. Produire mieux et à plus grande échelle

Le passage d'un travail individuel à une production collective ne consiste pas à générer le maximum de fichiers. Il exige une architecture stable et une gouvernance explicite.

**Six leviers proposés :**

1. **Normaliser** les gabarits et nommages sans supprimer l'adaptation au contexte.
2. **Séparer** production, contrôle et validation.
3. **Versionner** les changements avec Git et revue par Pull Request lorsque pertinent.
4. **Automatiser** les opérations répétables (build, syntaxe, liens, tests) sans automatiser la responsabilité.
5. **Capitaliser** les décisions, corrections et retours d'expérience.
6. **Mesurer** les résultats réels et identifier les limites avant de reproduire la méthode.

Le développement numérique vise une autonomie de production : comprendre les besoins, piloter des agents et des outils, organiser un dossier de preuves, déployer si autorisé, puis maintenir le résultat. Le bénéfice recherché est la qualité et la transmissibilité ; aucun taux de gain n'est affirmé sans mesure.

## 13. Mini-site Vite : rôle et séparation des responsabilités

Chaque atelier affiche ses prérequis documentaires, le travail attendu, la relecture humaine et les pièces à classer. Les boutons de la rubrique « 4 séances » ouvrent la séance correspondante. Avant de naviguer, sauvegarder et exporter ; les contrôles de contenu restent à effectuer par une personne.

Le mini-site du pack doit **expliquer** le module, permettre **d'exercer** les quatre productions, **exporter** les versions Markdown et **guider** la constitution d'un portfolio. Il ne doit pas dépendre d'une clé API, ni communiquer les saisies à un service externe, ni certifier automatiquement les productions.

Ses neuf rubriques : Accueil ; Quatre séances ; Démonstrations ; Présentation (20 diapositives) ; Méthode ; Parcours opératoire ; Atelier de production ; Qualité et portfolio ; Ressources. Le projet est construit avec Vite et JavaScript natif, du CSS responsive, des tests Node et un workflow GitHub Pages à utiliser uniquement après validation.

**Contrainte technique.** Le navigateur télécharge dans le dossier habituel. Il ne peut pas écrire automatiquement dans l'arborescence locale de VS Code ; le participant classe lui-même les fichiers exportés. Le stockage local éventuel est propre à son navigateur et ne doit pas contenir de secrets.

## 14. Mesures et critères de réussite

| Dimension | Indicateur proposé | Mode de collecte |
|---|---|---|
| Complétude | 4 fichiers S09–S12 présents | inventaire des fichiers |
| Traçabilité | prompt, source, version et auteur retrouvables | grille et dossier de preuve |
| Qualité | défauts importants détectés puis corrigés | revue humaine avec commentaires |
| Actionnabilité | un lecteur peut suivre les étapes et vérifier le résultat | test avec une personne cible |
| Sécurité | aucune information non autorisée dans la publication | revue avant publication |
| Évolution | écarts V1/V2 identifiables | journal des corrections |
| Réutilisation | document adapté à un second contexte | test de reprise documenté |

Le suivi doit rester proportionné. Un taux de conformité ou une économie de temps ne peut être communiqué qu'après un protocole et une collecte réelle de données. Une mesure non disponible doit être déclarée « non mesurée », pas estimée comme un résultat.

## 15. Étude de cas fictive fil rouge

**Situation fictive :** une formatrice souhaite aider des enseignants débutants à apprendre la création d'un premier document Markdown dans VS Code. Les noms, résultats et critères ci-dessous sont **illustratifs**, pas des résultats observés.

- **S09** — Sujet : préparer une première fiche d'aide. Public : formateurs débutants. Besoin : difficultés à créer un fichier structuré. Objectif : faciliter une prise en main. Résultat : une fiche partageable. Première action : lister les trois gestes de base.
- **S10** — Fiche projet : objectif concret, public, solution sous forme d'un support court, livrables (fiche et mini-exercice), outils (éditeur et navigateur), trois étapes, critères (fichier créé et relu), points à vérifier.
- **S11** — Plan : Comprendre le Markdown ; Préparer l'environnement ; Produire un fichier ; Vérifier l'affichage ; Améliorer la lisibilité.
- **S12** — Guide : instructions de création, exemple `# Mon premier titre`, checklist de validation, erreurs à éviter, relecture puis V2 avec corrections documentées.

**À vérifier avant usage réel :** matériel, version du logiciel, conditions d'installation, accessibilité et autorisation de partage. Aucun participant fictif ne doit être présenté comme une personne ayant réellement testé le guide.

## 16. Mode d'emploi du pack et sources

1. Lire ce guide et `docs/PROVENANCE.md`.
2. Extraire `mini-site-module03-ln-ia/` puis ouvrir le dossier dans VS Code.
3. Lancer `npm.cmd install`, `npm.cmd run check`, `npm.cmd test` et `npm.cmd run dev`.
4. Lire `AGENTS.md` et copier `prompts/PROMPT-MAITRE-CODEX-MODULE03.md` dans Codex.
5. Tester les exports S09, S10, S11 puis S12/V1/V2 sur ordinateur et mobile.
6. Corriger les problèmes constatés, renseigner `docs/JOURNAL-QUALITE.md` et obtenir un accord humain avant publication.
7. Ranger les livrables sous `03-documents/` et leurs preuves sous `07-portfolio/`.

**Sources analysées et conservées sans modification :** `supports-seance-09.zip` (49 fichiers) ; `supports-seance-10(2).zip` (25) ; `supports-seance-11(1).zip` (51) ; `supports-seance-12(1).zip` (46) ; `dossier-supports-seance-12.zip` (9). Le nombre de fichiers et les empreintes figurent dans `docs/INVENTAIRE-SOURCES.json`.

**Comparaison des sources :** S09 fournit des modèles, prompts, corrigés et portfolio ; S10 des prompts de passage de la note à la fiche ; S11 une architecture en cinq parties et des grilles de qualité ; S12 la rédaction, la correction et la trace portfolio. Ces supports proviennent de l'édition d'été 2026 : leur contenu a été **adapté** pour la relance Automne, sans remplacer les archives historiques.

**Éléments ajoutés dans cette synthèse :** nomenclature intégratrice, dossiers de pilotage/risques/sécurité, gouvernance pour la production collective, critères de mesure, mini-site Vite et ses tests. Il s'agit de recommandations de conception, non de faits fournis par les archives.

---

**LN-IA — Règle finale :** *L'IA propose. L'humain pilote et vérifie. Le livrable prouve seulement ce qui a réellement été produit et documenté.*

## Complément — Parcours opératoire

L’organigramme est aussi présenté en deux affiches bleu nuit et gold : les quatre séances avec leurs contrôles humains, puis V1 → correction → V2 À RELIRE et revue finale. Chaque affiche s’agrandit en SVG et se télécharge en SVG/PNG. Les quatre démonstrations fictives sont accessibles dans une rubrique dédiée « Démonstrations ». Le site comporte désormais neuf rubriques ; les documents Word sources conservent leur état d’origine.

Rubrique du mini-site : organigramme S09–S12, contrôles et retours correctifs, accès direct à chaque atelier et téléchargement de l’algorithme détaillé. Lire `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md` pour les manipulations adaptées et les limites réelles. Les documents initiaux Markdown et Word sont conservés.
