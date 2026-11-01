# Recette de la phase 07 — Module 03

Date : 1er novembre 2026. Statut actualisé : contrôle visuel et pédagogique bureau/mobile déclaré effectué par le pilote ; contrôles techniques réussis ; recette native des interactions encore partielle. Aucune publication.

**Décision de pilotage suivante :** phase 08 explicitement validée par le pilote, puis phase 09 demandée. Cette décision est consignée dans [le dossier de preuves](PHASE09-DOSSIER-PREUVES.md), sans réécrire comme réussies les vérifications natives qui restent non effectuées.

## Complément après retour du pilote et passage à la phase 08

Le pilote indique : « j’ai fait le contrôle visuel et pédagogique dans le bureau et mode mobile », puis demande de refaire les contrôles restants et de passer à la phase 08. Ce retour est consigné comme un contrôle humain effectué, sans inventer de résolution d’écran, de détail de scénario ou de certification. Il ne prouve pas à lui seul les téléchargements ou les blocages V2 dans le navigateur.

Nouvelle tentative de recette : hôte navigateur toujours indisponible ; la capture Windows de Chrome échoue avec `FrameArrived timed out: timed out waiting on channel`, puis, après renouvellement de la sélection, `window capture timed out: timed out waiting on channel`. Aucune saisie ni action sur les fichiers candidats dans Chrome.

Des tests supplémentaires exécutent le vrai `src/app.js` dans un DOM minimal en mémoire, via les gestionnaires des contrôles. Ils ne lancent pas de navigateur et ne contournent pas le blocage de Computer Use. Les fichiers et le stockage de test sont fictifs et isolés en mémoire ; les Blobs de sortie sont lus par Node, sans téléchargement disque. Leur portée :

- rendu du code des neuf rubriques et activation de leurs commandes ;
- imports par titres pour S09–S12, refus de fichiers trop grands, erreur de lecture et conservation des notes ;
- création du document V1, prompt, grille, preuve et bilan pour chaque séance ;
- S12 : refus sans V1, sans différence, sans journal suffisant, sans relecture déclarée, puis production d’un Blob V2 À RELIRE avec journal et conservation du Blob V1 ;
- sauvegarde/reprise dans un stockage de test isolé, erreur de quota et JSON invalide ;
- commandes précédent/suivant, flèches, sommaire des vingt diapositives, affichage des notes et correction du quiz sans validation automatique.

La première suite de 17 tests fonctionnels a révélé quatre échecs ; un test supplémentaire de changement de séance pendant une lecture a révélé un cinquième défaut. Les cinq défauts sont corrigés en phase 08. Résultat final : **32 tests réussis**, comprenant 11 tests du cœur et 21 tests du code applicatif. `check`, build et génération de l’aperçu réussis. Voir `PHASE08-CORRECTIONS.md` pour les changements et leurs preuves.

| Point de recette actualisé | Résultat et portée |
|---|---|
| Visuel et pédagogie bureau/mobile | Effectués selon le retour du pilote |
| Neuf rubriques, import, sauvegarde, contenu des exports et blocages V2 | Gestionnaires testés dans le DOM en mémoire ; aucune erreur non gérée observée dans ces tests |
| Clavier et sommaire | Commandes, focus et prévention du défilement testés dans le DOM en mémoire ; comportement natif à confirmer |
| Téléchargements physiques et sélecteur natif de fichier | Non vérifiés dans Chrome ; création et contenu des Blobs testés par Node |
| Console réelle du navigateur pendant les parcours | Non vérifiée |
| Guide et affiches | Disponibilité et fichiers contrôlés ; ouvertures/téléchargements réels non exercés pendant cette passe |

Les sections suivantes conservent la trace de la première exécution. Leur état « non exécuté » se rapporte à cette première passe ; le tableau ci-dessus porte l’état actualisé. Le passage à la phase 08 est effectué sur instruction du pilote, avec cette réserve explicite sur les interactions natives.

## Commandes réellement exécutées

| Commande | Résultat observé |
|---|---|
| Premier `npm.cmd ci` | Échec EPERM lors de la suppression de `node_modules/@esbuild/win32-x64/esbuild.exe`, alors que le serveur Vite était actif. |
| Arrêt du serveur local puis `npm.cmd ci` | Réussi : 14 paquets installés depuis le verrou. |
| `npm.cmd run check` | Réussi : syntaxe, quatre séances, six rubriques S09, structure du contenu et synchronisation du parcours. |
| `npm.cmd test` | Réussi : 11 tests, aucun échec. |
| `npm.cmd run build` | Réussi : Vite 6.4.5, neuf modules, génération de `dist/`. |
| `npm.cmd run standalone` | Réussi : aperçu autonome régénéré, 4 667 490 octets. |

Le serveur Vite est relancé après ces commandes pour conserver l’accès local du pilote. Aucune dépendance ou règle de permissions n’a été modifiée.

## Portée des tests automatisés

Les 11 tests Node couvrent les quatre séances, les six rubriques S09, les cinq fonctions S11, le Markdown et son statut À RELIRE, la détection des champs incomplets, l’échappement HTML, l’import de sections, les vingt diapositives et dix questions, ainsi que l’aller-retour Markdown avec accents et fins de ligne Windows.

Les tests de la fonction V2 vérifient le refus sans référence V1, sans différence et sans journal suffisant, puis l’acceptation d’un texte différent avec journal d’au moins douze caractères. Ils ne constituent pas des clics réels sur les boutons d’export. La déclaration de relecture humaine, les téléchargements et les alertes doivent encore être exercés dans le navigateur.

## Tentative de recette navigateur

La compétence Computer Use a été initialisée. L’inventaire Windows a retourné une seule fenêtre Chrome, intitulée « Présentation | S10 · LN-IA ». La tentative de capture de cette fenêtre a été arrêtée par l’outil avec le message :

> Computer Use has been stopped for this turn because it could not determine the current browser URL on Windows with enough confidence to enforce policy.

Aucune action de navigation, saisie, import, téléchargement ou changement de taille n’a ensuite été effectuée dans le navigateur. Aucun autre moyen d’automatisation du navigateur n’a été utilisé pour contourner cet arrêt.

## Matrice des vérifications restantes

| Vérification réelle | État de cette passe |
|---|---|
| Écran large : mise en page, neuf rubriques et absence de débordement | Non exécutée — accès navigateur arrêté |
| Mobile : navigation, champs, diapositives et affiches | Non exécutée |
| Clavier : Tab, activation, focus et flèches des diapositives | Non exécutée |
| Sommaire des vingt diapositives et notes | Non exécutée |
| S09 : saisie des six rubriques et export V1 | Non exécutée |
| S10 et S11 : saisie, export V1 et cohérence avec les pièces précédentes | Non exécutée ; cohérence à relire humainement |
| Import Markdown reconnu, fichier sans titre reconnu, fichier trop volumineux et erreur de lecture | Non exécutée ; parseur testé par Node uniquement |
| Sauvegarde locale et reprise, sans toucher à des travaux personnels | Non exécutée |
| S12 : refus V2 sans V1 | Fonction testée par Node ; interface non exercée |
| S12 : refus V2 identique | Fonction testée par Node ; interface non exercée |
| S12 : refus V2 sans journal ou journal trop court | Fonction testée par Node ; interface non exercée |
| S12 : refus V2 sans déclaration de relecture | Interface non exercée |
| S12 : téléchargement réel de V1 puis V2 À RELIRE après correction | Non exécuté |
| Prompts, grilles, preuves et bilan téléchargés pour les séances | Non exécuté |
| Guide HTML/PDF et affiches ouverts et téléchargés | Non exécuté dans cette passe |
| Aperçu autonome hors ligne : images, liens et exports | Génération réussie ; utilisation non exercée |
| Console JavaScript : absence d’erreur pendant les parcours | Non vérifiée |

## Conclusion et suite

La partie technique demandée de la phase 07 est exécutée avec succès après résolution du verrou esbuild. La phase 07 complète reste ouverte : sa recette navigateur ne peut pas être déclarée réussie. Reprendre cette matrice lorsque l’outil peut identifier et contrôler le navigateur, ou consigner une recette manuelle réellement effectuée par le pilote. Utiliser uniquement des données de test fictives dans une session de test distincte des travaux candidats.

Aucun commit, push, déploiement public, suppression de source ou modification de permissions n’a été effectué.
