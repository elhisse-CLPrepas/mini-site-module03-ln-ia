# MODULE 03 — Organigramme et algorithme opératoire des séances S09 à S12
**LAB-NUMÉRIQUE-IA (LN-IA) · Challenge 100 Jours — Relance Automne 2026**  
**Pilotage pédagogique : Prof. Abderrahman EL HISSE**  
**Édition : 1er novembre 2026 · Statut : adaptation au mini-site intégré — À RELIRE**

> **Finalité :** passer d’un besoin réel à un dossier professionnel documenté, dans lequel chaque livrable est relié au précédent, relu, corrigé et accompagné d’une preuve. L’IA assiste ; la décision de validation reste humaine.

## 1. Lecture rapide — quatre séances, quatre transformations

| Séance | Fonction | Entrée principale | Résultat à exporter |
|---|---|---|---|
| **S09** | Comprendre — note de cadrage courte | Une idée / un besoin réel | `03-documents/note-cadrage-courte.md` |
| **S10** | Pratiquer — fiche projet V1 | Note S09 relue | `03-documents/fiche-projet-v1.md` |
| **S11** | Comprendre — plan du guide pratique | Note S09 + fiche projet S10 | `03-documents/plan-guide-pratique.md` |
| **S12** | Pratiquer — guide V1 puis V2 | Plan S11 et éléments S09/S10 | `03-documents/guide-pratique-v1.md ; 03-documents/guide-pratique-v2-a-relire.md` |

**Distinction :** une V1 exportée est *à relire*. Les quiz, formulaires et checklists n’accordent pas une certification. Le passage V1 → V2 nécessite une correction réelle et traçable. Les téléchargements sont déplacés **manuellement** vers le dossier candidat.

## 2. Organigramme général — embranchements et retours correctifs

```mermaid
flowchart TD
    A([Départ : choisir UN besoin réel]) --> B[Créer le dossier candidat<br/>02-prompts / 03-documents / 07-portfolio]
    B --> S09[S09 COMPRENDRE<br/>Renseigner les 6 rubriques<br/>Note de cadrage V1]
    S09 --> G09{Sujet, public, besoin, objectif,<br/>résultat, action clairs ?}
    G09 -- Non --> S09
    G09 -- Oui, relu --> S10[S10 PRATIQUER<br/>Importer S09 ; compléter 12 rubriques<br/>Fiche projet V1]
    S10 --> G10{Objectifs observables,<br/>livrables et étapes réalistes ?}
    G10 -- Non --> S10
    G10 -- Oui, relu --> S11[S11 COMPRENDRE<br/>Importer S09 + S10<br/>Plan du guide : 5 parties max.]
    S11 --> G11{Guide orienté lecteur ?<br/>Ordre, prérequis, checklist ?}
    G11 -- Non --> S11
    G11 -- Oui, relu --> S12[S12 PRATIQUER<br/>Au moins 3 étapes actionnables<br/>Exporter guide V1]
    S12 --> H[Correction humaine<br/>Modifier le texte et journaliser]
    H --> G12{V1 conservée + texte différent<br/>+ journal de corrections ?}
    G12 -- Non --> H
    G12 -- Oui --> V2[Exporter V2 à relire<br/>Grille, prompts, preuve S12 et bilan]
    V2 --> G0{Revue humaine explicite :<br/>cohérence, exactitude, confidentialité ?}
    G0 -- À corriger --> H
    G0 -- À relire --> E([Dossier en attente de validation])
    G0 -- Validé par personne habilitée --> F([Dossier prêt à transmettre<br/>selon autorisation])
    classDef step fill:#08274c,stroke:#cfa148,color:#ffffff,stroke-width:1px;
    classDef decision fill:#f6e4aa,stroke:#9d6b17,color:#07182f,stroke-width:1px;
    classDef end fill:#e8f5f4,stroke:#167e87,color:#082638;
    class S09,S10,S11,S12,H,V2,B step;
    class G09,G10,G11,G12,G0 decision;
    class A,E,F end;
```

### Comment lire les décisions

- **Non / à compléter :** revenir à la rubrique du document concerné et corriger le contenu ; ne pas avancer pour masquer un manque.
- **Oui, relu :** exporter avec un statut exact (« V1 — À RELIRE ») puis continuer.
- **V2 impossible :** garder la V1 et réviser réellement le texte ; ajouter un journal de corrections motivées.
- **Validation finale :** un participant ou responsable habilité contrôle la cohérence et décide du statut, sans validation automatique du site.

## 3. Arborescence de référence du dossier professionnel

```text
challenge-100jours-candidat/
├── 02-prompts/
│   ├── prompt-note-cadrage-s09.md
│   ├── prompt-fiche-projet-s10.md
│   ├── prompt-plan-s11.md
│   └── prompt-guide-s12.md
├── 03-documents/
│   ├── note-cadrage-courte.md
│   ├── fiche-projet-v1.md
│   ├── grille-relecture-s10.md
│   ├── plan-guide-pratique.md
│   ├── grille-relecture-s11.md
│   ├── guide-pratique-v1.md
│   ├── guide-pratique-v2-a-relire.md
│   └── grille-relecture-s12.md
└── 07-portfolio/
    ├── preuves-module-03.md  # contient ou référence la trace S09
    ├── preuve-seance-10.md
    ├── preuve-seance-11.md
    ├── preuve-seance-12.md
    └── bilan-module-03.md
```

**Convention :** la version Automne utilise `03-documents/`. Les sources historiques peuvent mentionner `02-DOCUMENTS/` : ne pas les écraser, mais adopter une seule convention dans le dossier actif. L’autoévaluation facultative peut être rangée dans le portfolio. La V2 de la fiche projet S10 est également facultative.

## 4. Algorithme détaillé — instructions, actions et résultats attendus

### Préparation
**P01 · Créer la copie de travail**
- **Instruction / manipulation :** Choisir un seul projet réel ou un cas explicitement fictif ; créer un dossier candidat et les sous-dossiers `02-prompts`, `03-documents`, `07-portfolio`.
- **Résultat attendu / porte de contrôle :** Arborescence locale disponible ; aucune information personnelle sensible dans les démonstrations.

**P02 · Ouvrir l’atelier correspondant**
- **Instruction / manipulation :** Ouvrir ce mini-site ou APERCU-AUTONOME-MODULE03.html. Consulter Accueil, Présentation, Méthode et Parcours opératoire ; choisir ensuite S09 à S12 dans le sélecteur de l’Atelier de production.
- **Résultat attendu / porte de contrôle :** Le participant sait quel document produire et quel modèle utiliser.

**P03 · Fixer la traçabilité**
- **Instruction / manipulation :** Noter le sujet, l’auteur, la date, la séance, la version et la provenance des informations ; signaler « À clarifier » ou « À vérifier » au besoin.
- **Résultat attendu / porte de contrôle :** Contexte et limites repérables avant toute génération.

### S09 — Clarifier le besoin
**09.1 · Qualifier une intention**
- **Instruction / manipulation :** Énoncer un seul besoin ou problème, un public identifiable et un usage professionnel ou pédagogique.
- **Résultat attendu / porte de contrôle :** Une phrase de sujet et un besoin compréhensible ; pas de mélange de sujets.

**09.2 · Renseigner les six rubriques**
- **Instruction / manipulation :** Dans Atelier, compléter : Sujet ; Public concerné ; Problème ou besoin ; Objectif du document ; Résultat attendu ; Première action.
- **Résultat attendu / porte de contrôle :** Note structurée avec six rubriques et une première action réalisable.

**09.3 · Employer le prompt sans déléguer la décision**
- **Instruction / manipulation :** Copier le prompt S09 dans l’outil IA choisi, si utile. Comparer le brouillon à son cadrage ; ne pas inventer de faits.
- **Résultat attendu / porte de contrôle :** Texte de travail identifiable comme proposition, non comme validation.

**09.4 · Contrôler et exporter**
- **Instruction / manipulation :** Relire les dix critères de la grille S09 ; corriger ; exporter la note V1, le prompt, la trace portfolio ; placer manuellement les téléchargements.
- **Résultat attendu / porte de contrôle :** `note-cadrage-courte.md` en V1 à relire ; preuve conservée ; sinon revenir à 09.1/09.2.

### S10 — Structurer le projet
**10.1 · Importer la source S09**
- **Instruction / manipulation :** Vérifier la note de cadrage ; dans Atelier S10 importer `.md/.txt` ou reporter manuellement les informations dans les champs correspondants. Compléter les champs proposés ; ce mini-site ne comporte pas de questionnaire préparatoire séparé.
- **Résultat attendu / porte de contrôle :** Contexte S09 présent, sans changement de l’intention.

**10.2 · Construire les douze rubriques**
- **Instruction / manipulation :** Compléter : nom, objectif, public, problème, solution, livrables, outils, étapes, critères, risques/limites, prochaine action, points humains.
- **Résultat attendu / porte de contrôle :** Fiche projet avec objectifs observables, livrables concrets et étapes faisables.

**10.3 · Traiter les inconnues**
- **Instruction / manipulation :** Écrire « À clarifier » pour les informations non connues ; distinguer proposition IA, fait vérifié et décision humaine.
- **Résultat attendu / porte de contrôle :** Aucune donnée fabriquée pour combler un manque.

**10.4 · Relire et exporter la fiche**
- **Instruction / manipulation :** Utiliser la grille S10 (10 critères), consigner corrections et limites. Exporter `fiche-projet-v1.md`, le prompt et la preuve. V2 facultative si réellement corrigée.
- **Résultat attendu / porte de contrôle :** Fiche V1 à relire + contrôle et preuve ; si critères insuffisants, retour à 10.2.

### S11 — Organiser avant de rédiger
**11.1 · Importer les acquis S09/S10**
- **Instruction / manipulation :** Relire les deux fichiers ; importer dans Atelier S11 (`.md/.txt`) ou reporter manuellement les informations dans les champs correspondants.
- **Résultat attendu / porte de contrôle :** Besoin, public, résultat et livrables de référence visibles.

**11.2 · Définir le contrat de lecture**
- **Instruction / manipulation :** Préciser le titre du guide, son public, l’action à réaliser après lecture et les prérequis nécessaires.
- **Résultat attendu / porte de contrôle :** Résultat du guide formulé comme action observable.

**11.3 · Ordonner cinq parties au maximum**
- **Instruction / manipulation :** Pour Comprendre, Préparer, Produire, Vérifier, Améliorer, écrire objectif, contenu prévu et action du lecteur ; ne pas rédiger le guide complet.
- **Résultat attendu / porte de contrôle :** Plan cohérent de cinq parties maximum et séquence pédagogique plausible.

**11.4 · Préparer le contrôle et S12**
- **Instruction / manipulation :** Ajouter checklist, points à vérifier, partie prioritaire à rédiger en S12 ; appliquer la grille S11.
- **Résultat attendu / porte de contrôle :** Plan V1 à relire avec priorités et informations à confirmer.

**11.5 · Exporter et classer**
- **Instruction / manipulation :** Exporter le plan, le prompt, la grille et la preuve portfolio ; déplacer les téléchargements dans les dossiers prévus.
- **Résultat attendu / porte de contrôle :** `plan-guide-pratique.md` disponible pour S12 ; sinon revenir à 11.2/11.3.

### S12 — Produire, corriger, prouver
**12.1 · Importer et confronter les sources**
- **Instruction / manipulation :** Dans Atelier S12, importer au minimum le plan S11 ; confronter au cadrage S09 et à la fiche S10.
- **Résultat attendu / porte de contrôle :** Cohérence de l’objectif, du public et du résultat attendu.

**12.2 · Rédiger le guide V1**
- **Instruction / manipulation :** Compléter objectif, public, résultat, prérequis, au moins trois étapes numérotées et actionnables, chacune assortie d’un résultat à vérifier.
- **Résultat attendu / porte de contrôle :** Guide V1 utilisable par son public, sans procédure inventée.

**12.3 · Prévoir l’usage et les risques**
- **Instruction / manipulation :** Ajouter erreurs à éviter, checklist, points à vérifier par l’humain et prochaine amélioration.
- **Résultat attendu / porte de contrôle :** Guide orienté action, limites explicites et contrôles observables.

**12.4 · Exporter une V1 figée**
- **Instruction / manipulation :** Prévisualiser puis exporter `guide-pratique-v1.md` ; conserver ce fichier sans l’écraser lors de la correction.
- **Résultat attendu / porte de contrôle :** Référence V1 disponible pour comparer avant/après.

**12.5 · Effectuer une correction authentique**
- **Instruction / manipulation :** Relire le document, vérifier les faits/consignes, modifier réellement le texte, préciser les corrections et leurs raisons.
- **Résultat attendu / porte de contrôle :** V2 différente de V1, journal compréhensible et déclaration de relecture humaine.

**12.6 · Appliquer la règle de passage V2**
- **Instruction / manipulation :** Si aucune V1, aucune modification effective ou aucun journal : ne pas produire une fausse V2 ; corriger puis réessayer.
- **Résultat attendu / porte de contrôle :** V2 exportable seulement si exigences de traçabilité remplies ; aucune certification automatique.

**12.7 · Exporter contrôle et capitalisation**
- **Instruction / manipulation :** Exporter V2 à relire, grille S12, prompt, preuve S12 et bilan du Module 03 ; classer manuellement.
- **Résultat attendu / porte de contrôle :** Dossier complet de pièces S09–S12, distinct du statut « validé ».

### Clôture — Validation et transmission
**C01 · Faire la revue transversale**
- **Instruction / manipulation :** Comparer note → fiche → plan → guide : intention constante, public identique ou écart justifié, résultats cohérents ; vérifier sources et confidentialité.
- **Résultat attendu / porte de contrôle :** Chaîne de décisions explicable et cohérente.

**C02 · Établir le statut réel**
- **Instruction / manipulation :** Inscrire « À RELIRE », « À CORRIGER » ou « VALIDÉ APRÈS CONTRÔLE HUMAIN » selon une décision explicite et datée d’une personne habilitée.
- **Résultat attendu / porte de contrôle :** Aucune autoévaluation, quiz ou case cochée présentée comme certification.

**C03 · Conserver et transmettre**
- **Instruction / manipulation :** Compléter le portfolio (apprentissage, production, corrections, limites, prochaine action), lister les fichiers et, après accord, versionner ou partager les pièces non confidentielles.
- **Résultat attendu / porte de contrôle :** Dossier réutilisable, partageable au bon niveau d’autorisation, traçabilité conservée.

## 5. Pseudo-algorithme de pilotage

```text
DÉBUT
  CHOISIR besoin_unique, public, usage_final
  CRÉER dossiers 02-prompts, 03-documents, 07-portfolio
  POUR chaque séance S09, S10, S11, S12 :
      LIRE les livrables prérequis
      COMPLÉTER le modèle de la séance
      SI donnée absente ALORS inscrire « À clarifier » (ne pas inventer)
      SI aide IA choisie ALORS copier le prompt hors du site ; garder la décision humaine
      RELIRE à partir de la grille correspondante
      TANT QUE conditions de qualité non satisfaites : corriger et recontrôler
      EXPORTER le fichier Markdown + prompt + preuve ; CLASSER manuellement
  FIN POUR
  EN S12 : CONSERVER guide V1
  SI texte révisé ≠ V1 ET journal renseigné ET relecture déclarée :
      EXPORTER V2 À RELIRE
  SINON : RESTER en V1 et poursuivre les corrections
  EFFECTUER revue transversale et statuer humainement
  DOCUMENTER la décision, les réserves, les preuves et autorisations de partage
FIN
```

## 6. Matrice des critères de passage

| Porte | Critères minimaux | Si échec | Traces requises |
|---|---|---|---|
| Après S09 | Six rubriques claires ; un seul sujet ; première action faisable ; relecture | Réécrire cadrage | Note + prompt + trace portfolio |
| Après S10 | Objectif observable ; public ; solution ; livrables ; étapes réalistes ; risques et inconnues | Corriger la fiche projet | Fiche V1 + grille S10 + preuve S10 |
| Après S11 | Public, résultat et prérequis ; cinq parties maximum ; checklist ; priorité S12 | Réorganiser le plan | Plan V1 + grille S11 + preuve S11 |
| V1 S12 | Trois étapes actionnables minimum avec résultat vérifiable ; erreurs ; checklist ; contrôle humain | Compléter V1 | Guide V1 conservé |
| V2 S12 | V1 existante, texte réellement différent, journal de corrections, déclaration de relecture | Revenir à la correction | V2 à relire + grille S12 + preuve |
| Clôture | Cohérence des 4 documents, faits vérifiés, confidentialité, décision humaine | Rouvrir la séance concernée | Bilan et décision explicitement datée |

## 7. Exemple pédagogique fictif de bout en bout

**Cas fictif :** « préparer un guide d’accueil pour un nouvel intervenant pédagogique ».
1. **S09 :** sujet = guide d’accueil ; public = intervenant débutant ; besoin = comprendre le fonctionnement initial ; objectif = faciliter ses premiers pas ; résultat = guide court ; première action = lister les informations déjà disponibles.
2. **S10 :** fiche projet = objectif opérationnel, destinataire, solution proposée (guide), livrables attendus, ressources disponibles, étapes et critères de réussite ; informations inconnues marquées « À vérifier ».
3. **S11 :** plan = Comprendre le contexte ; Préparer les accès ; Produire une première tâche ; Vérifier l’exécution ; Améliorer la procédure. Chaque partie annonce une action observable ; aucun texte complet à ce stade.
4. **S12 :** V1 = au moins trois procédures décrites avec résultat vérifiable. V2 = correction d’une procédure ambiguë, modification du texte et explication dans le journal. Classement des deux versions et de la preuve S12.
**Ce cas est fictif** : il ne constitue ni un livrable réellement validé ni une procédure autorisée pour un établissement réel.

## 8. Risques, limites et mesures de sécurité

- **Données sensibles :** éviter informations confidentielles et données identifiantes dans les démonstrations et prompts non autorisés.
- **Hallucinations et promesses :** signaler les faits non vérifiés ; pas de dates, coûts, procédures ou résultats inventés.
- **Confusion des versions :** conserver V1 et V2 séparément, ne jamais nommer un brouillon « validé » par défaut.
- **Pertes de fichier :** exporter régulièrement ; les ateliers téléchargent dans `Téléchargements` et n’écrivent pas automatiquement dans le dossier local.
- **Saisie locale :** des ateliers utilisent `localStorage` ; un changement de navigateur ou de profil peut rendre ces données indisponibles.
- **Publication :** contrôle d’accès, relecture et autorisation humaine avant dépôt public / partage ; pas de secret ni donnée privée dans GitHub.
- **Rôle de l’IA :** les sites d’atelier ne contactent pas automatiquement un modèle IA ; les prompts sont des consignes à copier volontairement dans l’outil choisi.

## 9. Mode d’emploi dans VS Code / navigateur

1. Ouvrir le mini-site intégré ou son aperçu autonome ; sélectionner S09 puis S10, S11 et S12 dans Atelier de production.
2. Consulter **Présentation → Méthode → Parcours opératoire → Atelier de production → Qualité & portfolio**. Les démonstrations fictives figurent dans « 4 séances » ; les prompts, grilles, preuves et bilan sont exportés depuis l’atelier.
3. Dans Atelier, importer les `.md` antérieurs quand l’option est disponible, compléter et prévisualiser. Les exemples restent fictifs.
4. Copier les prompts vers l’outil IA souhaité ; revenir pour la relecture personnelle.
5. Télécharger les livrables, puis les déplacer manuellement dans le dossier du participant. Vérifier leur présence depuis VS Code.
6. Utiliser Git pour versionner uniquement après contrôle et autorisation ; ne jamais publier de dossier personnel confidentiel.

## 10. Références déclarées par le document fourni

Le document fourni indique que les intitulés, modèles et critères de passage sont fondés sur les README, fiches candidats et modèles Markdown des quatre dépôts. L’organigramme transversal et le pseudo-algorithme sont une **synthèse proposée** à partir de ces sources ; ils ne constituent pas un écran natif unique déjà présent dans les ateliers.

- [S09 — README](https://github.com/elhisse-CLPrepas/atelier-seance-09-ln-ia/blob/main/README.md)
- [S09 — fiche candidat](https://github.com/elhisse-CLPrepas/atelier-seance-09-ln-ia/blob/main/docs/FICHE-CANDIDAT.md)
- [S09 — modèle de note](https://github.com/elhisse-CLPrepas/atelier-seance-09-ln-ia/blob/main/modeles/note-cadrage-courte.md)
- [S10 — README](https://github.com/elhisse-CLPrepas/atelier-seance-10-ln-ia/blob/main/README.md)
- [S10 — fiche candidat](https://github.com/elhisse-CLPrepas/atelier-seance-10-ln-ia/blob/main/docs/FICHE-CANDIDAT.md)
- [S10 — modèle de fiche projet](https://github.com/elhisse-CLPrepas/atelier-seance-10-ln-ia/blob/main/modeles/fiche-projet-v1.md)
- [S11 — README](https://github.com/elhisse-CLPrepas/atelier-seance-11-ln-ia/blob/main/README.md)
- [S11 — fiche candidat](https://github.com/elhisse-CLPrepas/atelier-seance-11-ln-ia/blob/main/docs/FICHE-CANDIDAT.md)
- [S11 — modèle de plan](https://github.com/elhisse-CLPrepas/atelier-seance-11-ln-ia/blob/main/modeles/plan-guide-pratique-v1.md)
- [S12 — README](https://github.com/elhisse-CLPrepas/atelier-seance-12-ln-ia/blob/main/README.md)
- [S12 — fiche candidat](https://github.com/elhisse-CLPrepas/atelier-seance-12-ln-ia/blob/main/docs/FICHE-CANDIDAT.md)
- [S12 — modèle du guide V1](https://github.com/elhisse-CLPrepas/atelier-seance-12-ln-ia/blob/main/modeles/GUIDE-PRATIQUE-V1.md)
- [S12 — modèle V2](https://github.com/elhisse-CLPrepas/atelier-seance-12-ln-ia/blob/main/modeles/GUIDE-PRATIQUE-V2-A-RELIRE.md)

---
**Signature pédagogique : LAB-NUMÉRIQUE-IA · Prof. Abderrahman EL HISSE**  
*L’IA propose. L’humain pilote. Le candidat contrôle. Le livrable prouve.*

## 11. Adaptation au mini-site intégré

Édition du 1er novembre 2026, à relire. Les deux documents fournis restent inchangés ; cette adaptation ne modifie aucune archive ni production candidate. Les liens externes de la source ne constituent pas une nouvelle vérification des dépôts.

- L’import reconnaît uniquement les titres Markdown correspondant aux libellés de la séance active. Il ne fusionne pas automatiquement S09, S10 et S11 : relire les sources et reporter les informations nécessaires. Limite : 500 000 octets par fichier.
- Les contrôles des portes S09–S12 sont des consignes pédagogiques humaines. L’application vérifie la présence des champs, pas leur exactitude ni le nombre d’actions dans le guide.
- Pour S12, exporter V1, modifier les champs, écrire un journal d’au moins 12 caractères et cocher la déclaration de relecture. La référence V1 est conservée seulement pendant l’ouverture de cet atelier ; changer de rubrique ou de séance impose de réexporter V1. Conserver aussi le fichier V1 téléchargé.
- Le bouton Sauver localement conserve les champs et les points à vérifier, pas la référence V1, le journal ni la déclaration de relecture. Le stockage dépend du navigateur.
- Les prompts et grilles téléchargés utilisent les noms indiqués par le navigateur ; les renommer si nécessaire selon les conventions du dossier candidat.
- La rubrique Parcours opératoire propose un organigramme lisible sans bibliothèque externe, les portes de contrôle et le texte détaillé téléchargeable. Le Markdown contient aussi le diagramme Mermaid pour un lecteur compatible.
- Aucun gain de temps ou de performance technique n’est affirmé sans mesure. L’amélioration recherchée porte sur l’accès aux consignes et la cohérence du parcours.
