# LN-IA — Dossier professionnel · Module 03

**Challenge 100 Jours · Relance Automne 2026**  
**Module 03 · S09–S12**  
**Pilotage pédagogique : Prof. Abderrahman EL HISSE · LAB-NUMÉRIQUE-IA**

Ce mini-site accompagne la construction d’un dossier professionnel : clarifier un besoin, structurer un projet, organiser un guide, produire une première version et documenter ses corrections.

Un même projet relie les documents, les corrections, les preuves et la présentation destinée au public. Les messages et visuels s’appuient sur les pièces réellement produites ; les faits incertains restent signalés et la décision de diffusion appartient au pilote humain.

> **Pilotage : phases 08 et 09 validées par le pilote ; phase 10 autorisée, publication en préparation.** Les ateliers S09–S12 sont disponibles. Les livrables V1/V2 conservent leur statut À RELIRE ; les réserves de recette native restent signalées.

## À qui sert ce dossier ?

Aux participants des ateliers LN-IA, formateurs, enseignants, coachs, managers et porteurs de projet qui souhaitent produire un document utile, expliquer leur méthode et préparer sa transmission. Le dossier rassemble les pièces et leurs preuves ; le mini-site en est le support de travail et de présentation.

## Module 03 — Construire les pièces du dossier

| Séance | Travail accompagné | Document principal |
|---|---|---|
| S09 · Comprendre | Clarifier les six rubriques du cadrage | `note-cadrage-courte.md` |
| S10 · Pratiquer | Transformer le besoin en projet réalisable | `fiche-projet-v1.md` |
| S11 · Comprendre | Organiser le guide selon cinq fonctions | `plan-guide-pratique.md` |
| S12 · Pratiquer | Produire, relire, corriger et tracer les changements | `guide-pratique-v1.md`, puis `guide-pratique-v2-a-relire.md` |

Les cinq fonctions du plan sont Comprendre, Préparer, Produire, Vérifier et Améliorer. Les documents restent À RELIRE jusqu’à une décision explicite d’une personne habilitée. Une grille ou un quiz n’accorde aucune certification.

## Démarrage

**Dépôt réel : [elhisse-CLPrepas/mini-site-module03-ln-ia](https://github.com/elhisse-CLPrepas/mini-site-module03-ln-ia).** La [stratégie Git et Pages](docs/PHASE10-STRATEGIE-GIT-PAGES.md) décrit la branche de livraison, la Pull Request et le déploiement. Les résultats de mise en ligne seront ajoutés après vérification réelle.

**Accès au serveur local Vite : [Ouvrir le mini-site Module 03](http://127.0.0.1:5173/).**

Accès directs : [Présentation et sommaire](http://127.0.0.1:5173/#presentation) · [Démonstrations](http://127.0.0.1:5173/#demonstrations) · [Organigramme en affiches](http://127.0.0.1:5173/#parcours) · [Ressources](http://127.0.0.1:5173/#ressources) · [Guide HTML](http://127.0.0.1:5173/ressources/guide-module03.html).

Ces liens fonctionnent sur cet ordinateur tant que le serveur tourne. Pour le relancer, exécuter `npm.cmd run dev` depuis ce dossier et garder le terminal ouvert. Si le port 5173 est occupé, utiliser l’adresse indiquée par Vite. Arrêt du serveur : `Ctrl+C` dans son terminal.

- Sans installation : ouvrir `APERCU-AUTONOME-MODULE03.html` dans le navigateur.
- Dans VS Code / PowerShell :

```powershell
npm.cmd ci
npm.cmd run dev
```

- Contrôles : `npm.cmd run check`, `npm.cmd test`, `npm.cmd run build`, `npm.cmd run standalone`.

Si le nouveau dossier ne lance pas Codex, utiliser `Ctrl+Shift+P` → `Workspaces: Manage Workspace Trust` après avoir vérifié l'origine du dossier.

## Usage

Les quatre séances donnent désormais accès directement à leur atelier. Chaque atelier présente les pièces à relire avant de commencer, le travail attendu, les contrôles humains et les fichiers à conserver. Sauver localement et exporter avant de changer de séance ou de rubrique. Ces consignes accompagnent la production sans attribuer de validation.

Neuf rubriques : **Accueil**, **4 séances**, **Démonstrations**, **Présentation** (20 diapositives et notes), **Méthode**, **Parcours opératoire**, **Atelier de production**, **Qualité & portfolio**, **Ressources**. Quatre cas sont explicitement fictifs ; le quiz comporte dix questions. L’atelier accepte une saisie personnelle, importe des titres Markdown et génère les exports S09–S12, prompts, grilles, preuves et bilan.

La V2 de S12 nécessite une V1 exportée, un champ modifié, un journal des corrections et une déclaration humaine. **Le site ne fait aucun appel à l'IA**. Il ne valide pas les contenus. Les fichiers sont téléchargés dans le dossier habituel du navigateur, puis classés manuellement.

### Parcours pratique

1. Choisir un seul besoin réel, ou identifier explicitement un cas fictif.
2. Lire la méthode et le parcours opératoire ; ouvrir l’atelier S09.
3. Produire et relire les pièces S09, S10, S11 puis S12.
4. Exporter et classer les documents, prompts, grilles, preuves et bilan.
5. Conserver V1 ; corriger le texte et documenter les changements avant l’export V2 À RELIRE.
6. Faire relire, obtenir l’autorisation de diffusion, puis documenter le partage et les retours réels.

### Repères dans le dossier

| Emplacement | Contenu |
|---|---|
| `docs/` | Guide, provenance, organigramme et journal qualité |
| `prompts/` | Prompt maître de pilotage Codex |
| `02-prompts/`, `03-documents/` | Modèles S09–S12 et documents à produire |
| `07-portfolio/` | Trames de preuves et bilan |
| `dossier-modele/` | Arborescence à reprendre dans un dossier candidat privé |
| `exemples/` | Illustrations pédagogiques fictives |
| `src/`, `scripts/`, `tests/` | Application, construction et contrôles |

## Présentation pour GitHub

**Description courte proposée pour About :**

> Dossier professionnel LN-IA : ateliers S09–S12, documents Markdown, versions et preuves. Un même projet, du besoin au guide corrigé, sous contrôle humain.

Le [kit d’annonce GitHub](docs/ANNONCE-GITHUB.md) contient une présentation à relire, des thèmes suggérés et les informations à compléter avant diffusion. Les adresses réelles du dépôt et du site seront ajoutées après vérification.

## Vérifier et reconstruire

```powershell
npm.cmd run check
npm.cmd test
npm.cmd run build
npm.cmd run standalone
```

Le verrou `package-lock.json` est fourni. Si les dépendances doivent être modifiées, utiliser `npm.cmd install` et documenter le changement. Après adaptation de l’algorithme Markdown, exécuter `node scripts/sync-parcours.mjs` avant check/build/standalone. Ne pas réexécuter `scripts/integrate-parcours.py` : c’est la trace non réentrante de la migration initiale.

Les résultats observés figurent dans le [journal qualité](docs/JOURNAL-QUALITE.md). Les tests et la compilation ne remplacent pas la recette bureau/mobile, clavier, import, téléchargements et console JavaScript.

## Limites pratiques

- L’import `.md/.txt` reconnaît les titres correspondant aux champs de la séance active, avec une limite de 500 000 octets. Il ne fusionne pas les documents antérieurs.
- La sauvegarde locale dépend du navigateur et ne remplace pas les fichiers exportés.
- Quitter l’atelier S12 réinitialise sa référence V1. Réexporter une référence avant de poursuivre la correction et garder le fichier V1 antérieur.
- Le journal V2 exige au moins 12 caractères ; le site ne juge pas la qualité des corrections ni l’exactitude des faits.
- Les prompts sont à copier volontairement dans l’outil IA choisi. Aucun compte IA n’est nécessaire pour utiliser le site.

## Provenance

Lire `docs/PROVENANCE.md`. Les cinq archives originales sont préservées dans `sources-historiques/` et exclues de Git. Les résultats fictifs ne sont pas des résultats certifiés. Le répertoire `03-documents/` est la norme de cette édition Automne.

## État

Le pilote a explicitement déclaré « JE VALIDE la phase 8 » et demandé la phase 09. Le [dossier de preuves et décisions](docs/PHASE09-DOSSIER-PREUVES.md) rassemble les résultats observés, les limites restantes, les fichiers ajoutés/modifiés et les comparaisons avant/après. Cette validation concerne le lot correctif de phase 08 ; elle ne transforme pas les productions candidates en documents validés et n’autorise pas un commit, un push ou un déploiement.

Le contrôle visuel et pédagogique bureau/mobile a été déclaré effectué par le pilote. Le complément de recette et les cinq corrections fonctionnelles sont documentés dans [la recette phase 07](docs/RECETTE-PHASE07.md) et [le rapport phase 08](docs/PHASE08-CORRECTIONS.md). Les 32 tests passent, dont 21 tests des gestionnaires applicatifs dans un DOM en mémoire. Les dialogues natifs et téléchargements physiques dans Chrome restent à confirmer ; ces tests ne les remplacent pas.

La phase 10 reste une étape distincte : décider du périmètre de diffusion et du traitement des réserves, puis autoriser explicitement les opérations Git et le déploiement envisagés. Aucun dépôt Git local n’a été détecté lors de la phase 09 ; aucune URL publique, aucun commit ni aucun déploiement n’est déduit de cet état local.

### Preuves disponibles

- [Recette phase 07 et complément après contrôle du pilote](docs/RECETTE-PHASE07.md).
- [Cinq corrections de phase 08](docs/PHASE08-CORRECTIONS.md) et [comparaison du code](docs/PHASE08-CORRECTIONS.diff).
- [Dossier phase 09](docs/PHASE09-DOSSIER-PREUVES.md), [diff documentaire](docs/PHASE09-DOCUMENTATION.diff), [inventaire des fichiers](docs/PHASE09-INVENTAIRE.json) et [vérification des sources préservées](docs/PHASE09-PREUVES-SOURCES.json).

Les diffs sont des comparaisons textuelles fondées sur des copies locales identifiées, pas des diffs Git. Les empreintes du relevé de sources sont calculées à partir des fichiers présents et comparées aux inventaires disponibles ; aucun commit ni certificat de validation n’est créé.

## Parcours opératoire intégré

La rubrique « Parcours opératoire » relie les étapes S09–S12, les contrôles humains et les retours correctifs. Elle propose le texte détaillé et son export Markdown hors ligne. Les deux documents Organigramme-Algorithme fournis sont préservés dans docs/ ; la version `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md` adapte les consignes au mini-site unique.

La copie Word `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.docx` est également disponible ; sa mise en page reste à vérifier visuellement. Lire [le guide du Module 03](docs/GUIDE-DOSSIER-PRO-MODULE03.md) et [le prompt maître Codex](prompts/PROMPT-MAITRE-CODEX-MODULE03.md) pour piloter la suite.

**L’IA propose. L’humain pilote et contrôle. Le dossier conserve les preuves du travail réellement effectué.**

## Guide et présentation

Le guide Word fourni est conservé intact. Ses versions de consultation sont accessibles dans la rubrique Ressources :

- [Guide HTML avec sommaire](public/ressources/guide-module03.html).
- [Guide PDF](public/ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf).

La présentation comporte un sommaire cliquable des 20 diapositives. Les quatre démonstrations fictives détaillent S09–S12 et une correction V1/V2. La composition LN-IA blanc, bleu nuit et gold, avec typographie allégée selon les références S10/S11, est commune à Vite, au build GitHub Pages et à l’aperçu autonome. Vite copie les ressources publiques dans le build ; les liens relatifs sont prévus pour un chemin de dépôt GitHub Pages. Pour l’aperçu autonome, le générateur embarque les deux ressources du guide et utilise des URL Blob locales sans connexion réseau. Le guide HTML hors ligne demande de fermer son onglet pour revenir au mini-site.

Pour régénérer le HTML à partir du Word : `python scripts/export-guide-html.py`, puis reconstruire le site et l’aperçu. Le PDF est une conversion du Word fourni, conservant sa mise en page ; il ne reflète pas automatiquement les évolutions ultérieures du mini-site. Le Word source n’est pas modifié. Les essais réellement réalisés et les limites de recette figurent dans le journal qualité.

## Organigramme en deux affiches

Dans [Parcours opératoire](http://127.0.0.1:5173/#parcours), deux affiches présentent les étapes et les retours correctifs :

- Affiche 01 : besoin → S09 → S10 → S11 → S12, avec contrôle humain à chaque séance.
- Affiche 02 : V1 → correction → journal → V2 À RELIRE → revue et décision humaines.

Chaque affiche peut être agrandie et imprimée en SVG, ou téléchargée en PNG. Les fichiers se trouvent dans `public/ressources/affiche-01-parcours-module03.*` et `affiche-02-versions-controle-module03.*`. Pour les régénérer : `python scripts/build-affiches.py`, puis reconstruire le site et l’aperçu autonome. Les démonstrations sont désormais dans leur rubrique dédiée.

## Référence visuelle durable

La [charte visuelle LN-IA](docs/CHARTE-VISUELLE-LN-IA.md) rassemble les consignes du pilote : références des ateliers S10/S11, surfaces blanches, navigation et présentations bleu nuit, gold en accent, écriture fine et nette, contrastes de lecture. Elle doit être relue avant toute prochaine modification graphique. Les consignes cumulées sur les démonstrations, affiches, diapositives et guide y figurent aussi.

## Autorisation de phase 10

Le pilote a validé la phase 09 et autorisé explicitement commit, remote, push et déploiement Pages via Actions. Le dépôt distant réel a été consulté, puis Git local initialisé. Les constats d’absence de Git dans les rapports de phase 09 restent historiques. Les archives, Word sources et dossiers privés restent locaux et exclus du dépôt ; les modèles non remplis et exports Web demandés sont diffusables.
