# Phase 09 — Dossier de preuves et décisions

Module 03 LN-IA · 1er novembre 2026 · documentation locale établie à la demande du pilote.

## Décision humaine reçue

Le pilote indique : **« JE VALIDE la phase 8 »**, puis demande la phase 09 : documenter et prouver. La validation du lot de cinq corrections est enregistrée telle qu’exprimée, sans inventer de signature, d’horaire ou de résultat de test supplémentaire.

| Phase | État établi | Limite conservée |
|---|---|---|
| 07 — Vérifier | Commandes exécutées ; contrôle visuel et pédagogique bureau/mobile déclaré effectué par le pilote ; tests du code complétés | Dialogues natifs, téléchargements physiques, clavier natif et console Chrome non certifiés |
| 08 — Corriger | Cinq défauts reproduits et corrigés ; 32 tests réussis ; validation explicite du pilote | Les tests applicatifs emploient un DOM minimal en mémoire, sans navigateur |
| 09 — Documenter et prouver | Documents alignés, diffs identifiés, inventaire et preuves de préservation fournis | Aucun historique Git local disponible ; aucune reconstitution globale de diff n’est supposée |
| 10 — Valider avant de publier | Non exécutée dans ce lot | Autorisation de diffusion et d’opérations Git distincte requise |

La validation du lot technique ne transforme pas les productions S09–S12 en livrables validés. Les statuts V1/V2 À RELIRE et la décision humaine sur les contenus restent distincts.

## Matrice de preuves

| Affirmation | Pièce consultable | Portée réelle |
|---|---|---|
| Installation depuis le verrou, check, tests, build et aperçu exécutés | [Recette phase 07](RECETTE-PHASE07.md), journal et sorties de commandes consignées dans la conversation | Premier échec EPERM, serveur arrêté puis installation réussie ; aucune installation prétendue pendant la phase 09 |
| Contrôle visuel et pédagogique bureau/mobile effectué | Déclaration du pilote, reprise dans la recette | Aucun scénario, résolution ou détail non fourni n’est ajouté |
| Cinq défauts corrigés | [Rapport phase 08](PHASE08-CORRECTIONS.md) et [comparaison du code](PHASE08-CORRECTIONS.diff) | Copies source avant/après identifiées ; aucun diff Git revendiqué |
| 32 tests réussis en phase 08 | `tests/core.test.mjs`, `tests/app.test.mjs`, `tests/helpers/app-harness.mjs` et sorties de commandes | 11 tests du cœur et 21 tests applicatifs ; Blobs et stockage testés en mémoire |
| Style conforme à la direction demandée | [Charte visuelle](CHARTE-VISUELLE-LN-IA.md), `src/theme-references-ln-ia.css` | Blanc, bleu nuit, gold, typographie allégée ; pas de nouvelle modification graphique dans ce lot |
| Dix couples de couleurs mesurés | [Mesures de contraste](CONTRASTES-LN-IA.json) | Minimum mesuré 5,07:1 ; mesure ciblée, pas un audit d’accessibilité complet |
| Archives et sources fournies préservées | [Relevé de comparaison des sources](PHASE09-PREUVES-SOURCES.json) et inventaires antérieurs | SHA-256 recalculés sur les fichiers locaux et comparés aux empreintes disponibles |
| Documentation actualisée | [Diff documentaire](PHASE09-DOCUMENTATION.diff) | Comparaison avec les huit copies conservées juste avant la phase 09 |
| Fichiers présents et périmètre des changements | [Inventaire phase 09](PHASE09-INVENTAIRE.json) | Liste vérifiée sur disque ; statuts issus du lot connu et des bases identifiées, pas d’un index Git |

Les résultats réussis de la phase 08 ne sont pas présentés comme de nouveaux tests exécutés pendant la phase 09. Ce lot ajoute une preuve documentaire et ses vérifications de cohérence, sans reconstruire l’application.

## Diffs et bases de comparaison

1. **Code correctif :** `PHASE08-CORRECTIONS.diff` compare `tmp/avant-phase08/src/app.js` au code courant. Cette comparaison comprend les cinq corrections et la mise en forme du gestionnaire d’import.
2. **Documentation de cette phase :** `PHASE09-DOCUMENTATION.diff` compare README, AGENTS, provenance, journal qualité, guide, prompt maître, rapport phase 08 et recette phase 07 à `tmp/avant-phase09/`.
3. **Nouvelles pièces de preuve :** le présent dossier, le diff documentaire, l’inventaire et le relevé des sources sont des créations de phase 09. Ils sont listés dans l’inventaire ; ils ne disposent pas d’une version antérieure à comparer.

Les copies de travail sont exclues de Git par `tmp/`. L’inventaire historique et le fichier historique de checksums ne sont pas réécrits pour leur faire décrire un autre état. Aucun commit, branche ou URL déployée n’est fabriqué.

## Récapitulatif des fichiers

### Lot phase 09

**Ajoutés :**

- `docs/PHASE09-DOSSIER-PREUVES.md` : état, preuves, décisions et limites.
- `docs/PHASE09-DOCUMENTATION.diff` : comparaison des huit documents modifiés.
- `docs/PHASE09-INVENTAIRE.json` : inventaire factuel et périmètres.
- `docs/PHASE09-PREUVES-SOURCES.json` : empreintes recalculées et comparaisons aux références.

**Modifiés :**

- `README.md` : état cohérent avec la validation de phase 08, liens vers les preuves et suite de pilotage.
- `AGENTS.md` : lecture de l’état phase 09 avant la suite des travaux.
- `docs/PROVENANCE.md` : origine de la décision humaine et méthode de preuve.
- `docs/JOURNAL-QUALITE.md` : résultats et limites du présent lot.
- `docs/GUIDE-DOSSIER-PRO-MODULE03.md` : distinction entre validation technique et validation des contenus.
- `prompts/PROMPT-MAITRE-CODEX-MODULE03.md` : état actuel et instructions cohérentes ; bloc suspendu retiré du prompt actif.
- `docs/PHASE08-CORRECTIONS.md` : validation humaine explicite du lot.
- `docs/RECETTE-PHASE07.md` : renvoi à la décision ultérieure, sans transformer les contrôles restants en réussites.

### Livraisons applicatives des lots précédents

L’inventaire détaille les chemins présents. Les principales pièces sont :

| Ensemble | Ajouts ou modifications connus |
|---|---|
| Application | `src/app.js`, `src/styles.css`, `index.html`, styles successifs conservés, thème chargé `src/theme-references-ln-ia.css` |
| Consignes et démonstrations | `src/session-guidance.js`, `src/demonstrations.js` |
| Contrôles | `tests/core.test.mjs`, `tests/app.test.mjs`, `tests/helpers/app-harness.mjs` |
| Construction | `scripts/standalone.py`, générateurs `scripts/export-guide-html.py` et `scripts/build-affiches.py` |
| Guide de consultation | HTML et PDF dans `public/ressources/` ; le Word fourni est conservé |
| Affiches | Deux SVG et deux PNG dans `public/ressources/` |
| Sorties générées | `APERCU-AUTONOME-MODULE03.html` et `dist/` reconstruits en phase 08, inchangés en phase 09 |
| Pilotage | Charte, rapports, journal, provenance, annonce préparée et instructions |

Ce récapitulatif couvre les travaux connus de cette série. Il ne constitue pas un inventaire de changements externes au projet ou une comparaison avec un dépôt distant.

## Décisions acquises et proposées

| Décision | État | Conséquence |
|---|---|---|
| Valider la phase 08 | Acquise — déclaration explicite du pilote | Le lot correctif est accepté dans le périmètre indiqué |
| Conserver l’identité S10/S11 et le périmètre Module 03 | Consignes antérieures maintenues | Aucun nouveau changement de style ni élargissement pédagogique |
| Établir les preuves de phase 09 | Demandée et réalisée | Documentation, inventaire et diffs consultables |
| Traiter les réserves natives | Proposée pour la suite | Faire la recette ciblée quand elle est possible, ou consigner une décision explicite du pilote sur ces réserves |
| Préparer une publication | Proposée, non exécutée | Définir les fichiers à diffuser et obtenir une autorisation distincte avant toute opération d’écriture Git ou déploiement |

La phase 09 ne vaut pas accord sur ces propositions de suite. Aucune permission n’est modifiée et aucune publication n’est effectuée.

## Limites et transmission

Contrôles effectués sur le présent lot : huit documents effectivement modifiés et quatre pièces de preuve créées ; 28 liens locaux vérifiés ; huit sources fournies conformes à leurs empreintes de référence ; treize fichiers applicatifs et ressources surveillés inchangés depuis le début de la phase 09. Le diff de phase 08 correspond toujours à sa copie avant correction et au code courant. Aucun test npm ni build n’est réexécuté pour ce lot de documentation seule.

Le projet local n’est pas un dépôt Git lors de l’inspection de cette phase. Aucun lien avec un dépôt public n’est supposé à partir d’un nom de dossier. Les réserves de recette native sont maintenues ; elles restent visibles dans le README, la recette et le journal. Le serveur local est l’accès de contrôle demandé par le pilote, sans prétendre à un service permanent ni à un déploiement public.

La suite prévue par le prompt est la phase 10, avec une décision humaine distincte sur le périmètre, les réserves et les opérations de publication.
