# Journal qualité — Module 03

## Phase 10 — Préparation Git et GitHub Pages — 1er novembre 2026

- Le pilote valide la phase 09 et autorise commit, remote/push et déploiement Pages via Actions.
- Dépôt réel public ID 1442252931, main, initialement vide ; Pages non configuré (404).
- Stratégie : main minimal, branche release/module03-pages, PR contrôlée puis fusion et déploiement sans push forcé.
- Workflow : npm ci, contrôle public, check, tests, build et aperçu ; artefact limité à dist. Actions officielles fixées à des SHA consultés.
- Archives, Word sources et dossiers privés exclus sans suppression.

## Phase 09 — Documenter et prouver — 1er novembre 2026

- Validation explicite du pilote : « JE VALIDE la phase 8 », suivie d’une demande de phase 09. Validation attribuée à son message ; aucun statut validé attribué automatiquement aux livrables candidats et aucune autorisation de publication déduite.
- README, provenance, guide, AGENTS, prompt maître, recette et rapport phase 08 actualisés pour refléter cette décision et les réserves natives restantes. Anciennes consignes suspendues retirées du prompt actif ; historique conservé dans la provenance et les copies de travail.
- Dossier central `PHASE09-DOSSIER-PREUVES.md` : état des phases, matrice de preuves, décisions acquises/proposées et récapitulatif des fichiers.
- Diff documentaire produit depuis les huit copies `tmp/avant-phase09/` : `PHASE09-DOCUMENTATION.diff`. Diff de code phase 08 conservé : `PHASE08-CORRECTIONS.diff`. Aucun dépôt Git local détecté ; ce sont des comparaisons textuelles, pas des diffs Git.
- Inventaire factuel : `PHASE09-INVENTAIRE.json`. Relevé des sources préservées : `PHASE09-PREUVES-SOURCES.json`, avec empreintes réellement calculées et comparaison aux références existantes. Aucune empreinte ni aucun commit inventé.
- Lot strictement documentaire : code, charte graphique chargée, ressources publiques, verrou npm et sorties applicatives inchangés. Les 32 tests et le build réussis sont ceux de la phase 08 ; ils ne sont pas présentés comme réexécutés pendant ce lot documentaire.
- La recette réelle des dialogues, téléchargements, clavier natif et console Chrome reste à confirmer. Les contrôles visuel et pédagogique bureau/mobile restent attribués au pilote ; les tests DOM en mémoire ne sont pas une recette native.
- Aucune opération Git d’écriture, aucun commit, push, déploiement ni changement de permissions. Le passage à une opération de publication nécessite une instruction distincte.
- Contrôles documentaires finaux : huit documents modifiés, quatre pièces ajoutées, 28 liens locaux valides ; huit sources préservées conformes ; treize fichiers applicatifs et ressources surveillés inchangés ; diff phase 08 toujours conforme à sa base. Phase 09 documentée et preuves fournies, sans revendiquer une nouvelle validation du pilote sur cette phase.

## Complément phase 07 et corrections phase 08 — 1er novembre 2026

- Le pilote déclare avoir effectué le contrôle visuel et pédagogique bureau/mobile et demande de poursuivre les contrôles restants puis la phase 08. Retour humain consigné dans `RECETTE-PHASE07.md`, sans attribuer une validation globale ni inventer les scénarios effectués.
- Accès navigateur toujours indisponible. Capture Chrome : `FrameArrived timed out`, puis nouvelle sélection et `window capture timed out`. Aucune manipulation des travaux personnels dans le navigateur.
- Ajout de tests applicatifs exécutant le vrai app.js dans un DOM minimal en mémoire : neuf rubriques, quatre imports, quatre jeux d’exports, sauvegarde, erreurs, blocages V2, focus, flèches, sommaire, notes et quiz. Ces tests ne constituent pas une recette native Chrome ni des téléchargements disque.
- Quatre échecs dans la première suite de 17 tests : notes effacées par import sans correspondance, sélecteur non réinitialisé après fichier trop grand, focus perdu et défilement natif non empêché. Un cinquième défaut reproduit ensuite : import asynchrone S11 modifiant une séance S12 ouverte entre-temps.
- Phase 08 : cinq corrections appliquées dans `src/app.js` ; aucun changement de thème. Rapport et limites dans `PHASE08-CORRECTIONS.md` ; comparaison textuelle avant/après dans `PHASE08-CORRECTIONS.diff`.
- `npm.cmd run check` réussi ; 32 tests réussis (11 cœur, 21 applicatifs) ; build Vite réussi, neuf modules ; aperçu autonome reconstruit. L’installation `npm ci` de la passe précédente est conservée : aucun changement du verrou ni des dépendances.
- Reste à confirmer : dialogues natifs, téléchargements physiques, comportement clavier natif et console Chrome pendant les parcours. Le lot correctif phase 08 est réalisé avec ces réserves explicites.
- Contrôle complémentaire : syntaxe des deux scripts autonomes valide ; accueil, guide HTML/PDF et deux affiches SVG disponibles en HTTP 200 ; empreintes des cinq archives conformes. Les tests contrôlent aussi les noms des cinq exports de chaque séance et du fichier V2. Serveur local maintenu.

## Exécution explicite de la phase 07 — 1er novembre 2026

- Demande du pilote : réexécuter les cinq commandes et effectuer la recette réelle bureau/mobile, clavier, neuf rubriques, imports, exports et blocages V2. Rapport et matrice factuelle dans `RECETTE-PHASE07.md`.
- Premier `npm.cmd ci` échoué avec EPERM sur esbuild.exe pendant que Vite était actif. Serveur arrêté ; seconde installation réussie, 14 paquets depuis le verrou. Aucun changement de dépendance ou de permissions.
- `npm.cmd run check` réussi ; `npm.cmd test` : 11 tests réussis ; `npm.cmd run build` réussi, neuf modules ; `npm.cmd run standalone` réussi, aperçu de 4 667 490 octets.
- Computer Use Windows initialisé, fenêtre Chrome identifiée par l’inventaire. Capture arrêtée par l’outil parce qu’il ne pouvait pas déterminer l’URL courante avec assez de confiance pour appliquer sa politique. Aucune autre action navigateur après cet arrêt.
- Les contrôles réels bureau/mobile, clavier, import, téléchargements, console JS et blocages dans l’interface sont non validés. Les tests Node des conditions V2 ne les remplacent pas. Phase 07 complète toujours ouverte.
- Serveur local relancé après installation. Aucun changement graphique ni pédagogique, aucun commit, push ou déploiement public.

## Références S10/S11, surfaces blanches et typographie — 1er novembre 2026

- Nouvelle précision du pilote : s’appuyer sur ses ateliers S10/S11, optimiser blanc + bleu nuit + gold, alléger l’écriture et garder une direction stable. Consignes cumulées dans `CHARTE-VISUELLE-LN-IA.md`, lien ajouté dans AGENTS, README et prompt maître.
- Lecture des références : l’outil web n’a pas pu ouvrir les deux URL ; récupération HTTP réussie des HTML, JS et CSS publics, puis lecture des règles graphiques. Sources CSS : S10 `index-_E2bKyHz.css`, S11 `index-Bb8iaQ22.css`. Aucune inspection visuelle des pages de référence n’est déclarée.
- Composition alignée sur les styles observés : fond clair, panneaux et champs blancs, navigation latérale bleu nuit sur ordinateur, barre défilante sur écran étroit, zone d’accueil et diapositives bleu nuit, accents gold et ocre foncé pour les petits textes sur blanc. Segoe UI, corps 400, libellés 500 et titres 500–550. Les onze fonctionnalités testées précédemment et les neuf rubriques sont conservées.
- Nouveau thème `src/theme-references-ln-ia.css`, raccordé à `index.html` et au générateur autonome. Anciens thèmes conservés, non chargés. Couleur du statut d’atelier adaptée au fond blanc. Guide HTML régénéré avec palette claire et titres allégés ; PDF et Word source inchangés.
- Contrastes calculés selon la luminance relative pour dix couples de texte/fond, tous supérieurs à 4,5:1 ; minimum observé 5,07:1. Valeurs dans `CONTRASTES-LN-IA.json`. Cette mesure ciblée ne constitue pas un audit complet d’accessibilité ni une vérification de tous les états visuels.
- `npm.cmd run check` réussi ; 11 tests réussis ; compilation Vite réussie (9 modules) ; aperçu autonome régénéré. Syntaxe de ses deux scripts embarqués acceptée par `node --check`.
- Serveur local existant maintenu : accueil, nouveau thème et guide HTML répondent HTTP 200. Le build charge le nouveau thème. Aucune modification de dépendance.
- Inventaire navigateur : hôte toujours indisponible (`The browser access host is unavailable`). Recette réelle bureau/mobile, clavier, import et téléchargements non répétée ; la lecture du CSS des références et les mesures de contraste ne remplacent pas la comparaison visuelle par le pilote.
- Copies antérieures dans `tmp/avant-harmonisation-references/`. Aucun commit, push, déploiement public, changement de permissions, modification d’archive historique ou de travail candidat.

## Retour à l’identité LN-IA et organigramme en affiches — 1er novembre 2026

- Le pilote précise que la remarque « trop de bleu » ne demandait pas une palette verte. Le thème bleu nuit et gold est rétabli avec panneaux sobres, halos retirés, lisibilité et focus conservés. `src/theme-ln-ia.css` remplace le thème vert dans les feuilles chargées ; le fichier antérieur reste conservé sans être chargé. Le guide HTML utilise aussi cette palette ; Word et PDF sources non modifiés.
- Les quatre démonstrations quittent la rubrique « 4 séances » et disposent d’une rubrique dédiée, d’un bouton d’accueil et d’un lien README `#demonstrations`. Neuf rubriques désormais. Les quatre séances conservent un bouton vers les démonstrations et leurs accès aux ateliers.
- Ajout de deux affiches dans Parcours opératoire : 01, les livrables S09–S12 avec contrôle humain et boucle de reprise ; 02, V1, correction, journal, conditions techniques V2 et revue humaine finale. Les affiches restent À RELIRE et ne prétendent à aucune validation automatique.
- `scripts/build-affiches.py` génère SVG vectoriels et PNG 1200 × 1800 dans `public/ressources/`. Agrandissement/impression et téléchargements SVG/PNG accessibles depuis chaque affiche. Les textes alternatifs et les consignes détaillées restent disponibles. Le générateur utilise Pillow et les polices Segoe UI Windows.
- Inspection réelle des deux PNG ; espacement du texte corrigé dans le losange de l’affiche 02, puis nouvelle inspection. Largeurs de textes contrôlées par le générateur. SVG XML bien formés ; copies SVG/PNG identiques dans `dist/ressources/`.
- `scripts/standalone.py` embarque les quatre fichiers des affiches, en plus du guide, et hydrate les images par URL Blob à chaque changement de rubrique. Aperçu autonome reconstruit ; syntaxe de ses deux scripts embarqués acceptée par `node --check`. Cette vérification de syntaxe ne prouve pas les clics ni les téléchargements réels.
- `npm.cmd run check` réussi, 11 tests réussis, build Vite réussi (9 modules), aperçu autonome reconstruit. Contrôle de structure : neuf boutons de navigation distincts et route Démonstrations présente. Empreintes des cinq archives historiques conformes.
- Serveur local existant conservé, accueil HTTP 200. Inventaire navigateur renouvelé : `The browser access host is unavailable`. La recette du rendu complet bureau/mobile et des interactions réelles reste à faire par le pilote ; elle n’est pas remplacée par l’inspection des affiches.
- README, guide Markdown, provenance et prompt maître alignés sur cette précision. Copies antérieures de fichiers de travail dans `tmp/avant-retour-ln-ia/`. `scripts/apply-ln-ia-layout.py` est une trace de migration ponctuelle, à ne pas réexécuter. Aucun travail candidat ni source historique réécrit, aucun commit, push ou déploiement public.

## Accès au serveur local — 1er novembre 2026

- Serveur démarré avec `npm.cmd run dev`, adresse annoncée par Vite : `http://127.0.0.1:5173/`. Serveur laissé actif à la demande du pilote.
- Accueil, guide HTML et guide PDF contrôlés : réponses HTTP 200.
- README : lien vers le site local, accès directs à la présentation, aux démonstrations, aux ressources et au guide HTML ; consignes de relance et d’arrêt. Ces adresses nécessitent un serveur actif sur cet ordinateur.

## Présentation sobre, sommaire et guide PDF/HTML — 1er novembre 2026

- Demande du pilote après consultation du visuel précédent : diminuer la place du bleu, améliorer la présentation, ajouter le sommaire des diapositives, enrichir les démonstrations et recentrer l’interface et le README sur S09–S12. Le contrôle humain rapporté concerne la version précédente ; il ne vaut pas validation de cette nouvelle présentation.
- Palette éditoriale claire : ivoire, anthracite, vert et ocre, contrastes et focus visibles ; composants et points de rupture responsive conservés. Thème commun à Vite, au build et à l’aperçu autonome. Fichiers : `src/theme-editorial.css`, `index.html`, `src/app.js`.
- Sommaire cliquable des 20 diapositives, sans supprimer les notes ni la navigation précédente/suivante et clavier.
- Quatre démonstrations fictives enrichies : besoin et public, étapes S09/S10/S11/S12, extrait V1, proposition V2 À RELIRE, motif illustratif de correction et exercice personnel. Aucun résultat terrain ni témoignage inventé. Source : `src/demonstrations.js`.
- Passerelle retirée de l’interface et du README conformément à la nouvelle instruction. Prompt maître et annonce préparée alignés sur le périmètre actuel ; documents de travail antérieurs conservés pour la traçabilité.
- Guide Word source conservé intact. PDF obtenu par LibreOffice headless : premier essai sandbox sans résultat, relance avec autorisation réussie. PDF de 8 pages ; rendu PNG avec PyMuPDF, inspection de la planche des huit pages et de pages individuelles. La pagination et les coupures de la source Word sont conservées, y compris l’arborescence répartie sur deux pages.
- `scripts/export-guide-html.py` produit une version HTML autonome depuis le Word : titres, texte, quatre tableaux et illustration ; sommaire et mise en page responsive. Tous les fragments de texte du corps Word retrouvés dans l’article HTML ; toutes les ancres du sommaire correspondent à un titre. Une première assertion attendait à tort deux tableaux ; vérification de la source : quatre tableaux dans le Word et quatre dans le HTML, aucun tableau manquant. Empreinte du Word dans `EXPORT-GUIDE-SOURCE.json`.
- PDF/HTML dans `public/ressources/`, accessibles par liens relatifs depuis Ressources et copiés par Vite. L’aperçu autonome embarque les fichiers et les ouvre via des URL Blob, afin d’éviter la navigation directe vers des URL data. Le générateur du HTML autonome du guide retire la barre de liens relatifs de la version Web pour éviter des destinations inopérantes depuis une URL Blob.
- Serveur Vite local lancé pour contrôle HTTP : accueil, HTML et PDF répondent 200 avec les types de contenu attendus. Aucun déploiement public effectué ; le fonctionnement sous GitHub Pages reste à confirmer après un déploiement autorisé.
- Recette visuelle du site : hôte navigateur indisponible dans l’inventaire ; essai sur la fenêtre Chrome du mini-site terminé par `Computer Use app approval timed out`. Rendu bureau/mobile, clics du sommaire, téléchargements et console JS non certifiés pour cette nouvelle version. La vérification PDF est distincte de la recette du site.
- `tmp/` ajouté à l’exclusion Git pour garder profils LibreOffice, copies de travail et rendus de contrôle hors publication. `scripts/refine-module03.py` est la trace ponctuelle de cette adaptation, non un générateur à rejouer. Aucun commit, push, déploiement ni changement de permissions.
- Passe finale : `npm.cmd run check` réussi ; 11 tests réussis ; build Vite (9 modules) et aperçu autonome reconstruits. Syntaxe des deux scripts embarqués vérifiée par `node --check`. Contrôle final du HTML : quatre tableaux, deux blocs de code regroupés, tous les fragments du Word présents et toutes les ancres valides. PDF/HTML copiés à l’identique dans `dist/ressources/` ; résolution des chemins relatifs sous un préfixe de dépôt vérifiée sans prétendre à un déploiement réel. Empreinte Word source et empreintes des cinq archives conformes. Les huit pages PDF ont été inspectées individuellement en PNG.

## Guidage des ateliers Module 03 — 1er novembre 2026

- Inspection des références requises et de l’existant ; détail du cadrage, fichiers et limites dans `EXECUTION-ADAPTATION-MODULE03.md`.
- Ajout des consignes S09–S12, prérequis, relecture et classement. Accès direct à chaque atelier depuis « 4 séances ». Huit rubriques, modèles, diapositives, quiz et conditions V2 conservés.
- Import : erreur de lecture signalée, champ fichier nommé pour l’accessibilité ; cache JSON nul ou de type incorrect ignoré en mémoire, sans effacer le stockage. CSS adapté aux chemins longs, au sélecteur et au focus clavier.
- `npm.cmd ci` réussi : 14 paquets installés. Contrôles, tests, build et aperçu autonome réussis avant la dernière passe documentaire ; résultats finaux consignés ci-dessous.
- Accès navigateur tenté : inventaire sans navigateur connecté, puis création d’un onglet intégré refusée avec « The browser access host is unavailable ». Recette bureau/mobile, clavier, imports, téléchargements et console JS non validée.
- Copies antérieures conservées dans `tmp/avant-adaptation-module03/`. Aucun dépôt Git local ; aucun commit, push, déploiement ou changement de permissions. Archives et travaux candidats non modifiés. Statut V1 À RELIRE.
- Passe finale : `check` réussi ; 11 tests réussis, dont aller-retour Markdown des quatre séances (accents, multiligne, CRLF) et seuils V2. Build Vite réussi (7 modules), aperçu autonome reconstruit et script embarqué accepté par `node --check`. Empreintes SHA-256 des cinq archives et des deux sources organigramme conformes aux inventaires existants.

## README, communication GitHub et passerelle Module 04 — 1er novembre 2026

- Prompt maître exécuté dans le périmètre local : inspection, cadrage, production, contrôles et documentation. Détail des dix phases et relevé des fichiers dans `EXECUTION-PROMPT-PASSERELLE-MODULE04.md`. La recette visuelle et la phase de publication ne sont pas déclarées réalisées.
- README enrichi : présentation du dossier professionnel, publics, huit rubriques, pièces S09–S12, passerelle S13–S16, démarrage avec le verrou npm, usages et limites. Description About et annonce préparées dans `ANNONCE-GITHUB.md` ; aucun changement envoyé à GitHub.
- `PASSERELLE-MODULE03-MODULE04.md` traduit l’orientation demandée par le pilote. La répartition S13 cadrage, S14 visuel, S15 préparation du partage, S16 retours et correction reste une proposition ; aucun programme officiel, calendrier ou outil imposé n’est inventé.
- Bloc de continuité ajouté à l’accueil et aux ressources, en conservant les huit rubriques et les ateliers S09–S12. Aucun nouvel atelier Module 04, générateur de visuels, appel IA ou système de publication automatique.
- `npm.cmd ci` : réussi, 14 paquets installés depuis le verrou. Aucun changement de dépendance demandé.
- `npm.cmd run check` : réussi, structure et synchronisation de l’algorithme confirmées. `npm.cmd test` : 9 tests réussis.
- `npm.cmd run build` : réussi, 6 modules ; JavaScript 52,60 ko (17,85 ko gzip). Aucune économie de temps ni amélioration de performance n’est déduite de ces tailles.
- `npm.cmd run standalone` : réussi, aperçu régénéré. Présence du bloc Module 04 vérifiée dans cet HTML ; syntaxe de son script embarqué contrôlée avec `node --check`.
- Liens Markdown du README : 5 cibles locales vérifiées, aucune manquante.
- Recette réelle dans le navigateur non répétée pendant ce lot : les tentatives du lot précédent ont rencontré un navigateur intégré indisponible et une expiration de l’accès Chrome. Bureau/mobile, clavier, téléchargements et console JS restent à vérifier ; les tests Node ne prouvent pas leur réussite.
- Aucun document Word, archive historique ni travail candidat modifié. Aucun commit, push, déploiement ou changement de permissions. Le répertoire reste sans dépôt Git local ; aucune URL publique du projet n’est supposée.

## Intégration de l’organigramme — 1er novembre 2026

- Sources fournies `.md` et `.docx` conservées sans modification ; empreintes dans `EMPREINTES-ORGANIGRAMME-FOURNI.json`. Copies adaptées `Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md` et `.docx` ; aucune archive ni production candidate modifiée.
- Ajout de la huitième rubrique « Parcours opératoire » : étapes S09–S12, portes pédagogiques, retours correctifs, boutons vers chaque séance, instructions détaillées et export Markdown. Texte échappé avant affichage ; aucun rendu HTML des saisies ou du Markdown.
- Adaptation des consignes des ateliers séparés au sélecteur du mini-site ; limites de l’import et de la référence V1 explicitement documentées. Pas de gain de performance chiffré mesuré.
- Prompt maître, README, index du pack, guide et provenance actualisés. Synchronisation reproductible : `node scripts/sync-parcours.mjs`, puis check/build/standalone. `scripts/integrate-parcours.py` est une trace de migration initiale et ne doit pas être réexécuté sur le résultat.
- Installation npm : premier essai refusé (EACCES), relance autorisée réussie ; 14 paquets installés, audit npm : 0 vulnérabilité signalée. Verrou package-lock créé.
- `npm test` : 9 tests réussis, dont import, échappement et conditions V2. Ils ne remplacent pas une recette navigateur.
- Compilation Vite réussie : 6 modules, JavaScript 51,28 ko (17,40 ko gzip). Ces tailles décrivent le build observé, sans comparaison ni promesse de rapidité.
- Aperçu autonome reconstruit ; syntaxe de son script embarqué contrôlée par Node.
- Le contrôle de synchronisation a initialement échoué sur les fins de ligne CRLF de Windows ; comparaison corrigée pour normaliser CRLF en LF. Voir la relance finale du contrôle structurel.
- Relance finale : synchronisation, `npm run check` (structure, route, interactions déclarées et égalité du texte), `npm run build` et `npm run standalone` réussis. Empreintes des deux sources fournies revérifiées identiques ; XML de la copie Word bien formé. Les contrôles structurels des interactions ne sont pas des clics réels en navigateur.
- Rendu Word tenté via `render_docx.py` : échec, LibreOffice `soffice.exe` absent. La copie Word conserve la structure et les figures du document fourni ; sa mise en page n’est pas validée visuellement et reste À RELIRE.
- Recette navigateur : navigateur intégré indisponible ; inventaire sans navigateur connecté ; tentative d’accès à la fenêtre Chrome expirée (`Computer Use app approval timed out`). Bureau/mobile, clavier, parcours d’import et téléchargements restent à vérifier visuellement. Aucune absence d’erreur JS en navigateur n’est affirmée.
- Aucun commit, push, déploiement ni changement de permissions. Le dossier courant n’est pas un dépôt Git : diff Git indisponible. Le manifeste historique `CHECKSUMS-SHA256.txt` n’est pas réécrit ; il décrit l’édition antérieure, pas les fichiers modifiés ici.

**Statut :** V1 À RELIRE. Noter ici les résultats réellement obtenus.

## Contrôles prévus

- [ ] `npm install` (en absence de package-lock) et ensuite `npm ci` quand le verrou est versionné
- [ ] `npm run check`
- [ ] `npm test`
- [ ] `npm run build`
- [ ] `npm run standalone`
- [ ] Ouverture en navigateur desktop et mobile
- [ ] Navigation clavier des 20 diapositives
- [ ] Saisie, import .md et export des 4 modèles
- [ ] S12 : interdiction d’exporter V2 identique et sans journal
- [ ] Absence de secrets et de données personnelles publiées
- [ ] Relecture pédagogique humaine avant publication

## Résultats

Renseigner date, environnement, commande, résultat, anomalies, corrections et preuve. Ne jamais mentionner un déploiement comme réussi avant contrôle de l'URL et de GitHub Actions.

## Résultats observés — 1er novembre 2026

- `node scripts/verify.mjs` : réussi (4 séances, 20 slides, 4 cas, 8 questions, 10 quiz, 10 critères).
- `node --test tests/core.test.mjs` : neuf tests réussis.
- `python scripts/standalone.py` : aperçu autonome généré.
- Installation `npm install` : impossible ici (`EAI_AGAIN`, registre npm inaccessible). Compilation Vite non vérifiée.
- Recette Chromium : navigateur refuse `file://`, `localhost` et `data:` avec `ERR_BLOCKED_BY_ADMINISTRATOR`. Les parcours visuels ne sont donc pas certifiés dans cet environnement.
- Recette Windows VS Code desktop/mobile et validation humaine avant publication : à réaliser.
