// Scénarios pédagogiques : aucune observation de terrain ni validation réelle.
export const demonstrations = [
  {
    title: 'Un premier fichier Markdown', public: 'Formateurs débutants',
    need: 'Passer d’une page vide à une fiche structurée et vérifiable.',
    stages: [
      ['S09 · Cadrer', 'Sujet : une fiche Markdown. Public : formateurs débutants. Besoin : organiser un premier document. Objectif : guider la création. Résultat : un fichier lisible avec titre et liste. Première action : repérer le dossier de travail.'],
      ['S10 · Structurer', 'Prévoir un guide court et un exercice. Ressources : éditeur déjà disponible et dossier autorisé. Étapes : préparer, rédiger, relire. Critère : retrouver le fichier et reconnaître son titre et sa liste. Installation et environnement restent à vérifier.'],
      ['S11 · Organiser', 'Comprendre : rôle des titres. Préparer : créer le dossier. Produire : écrire la fiche. Vérifier : lire l’aperçu. Améliorer : clarifier une consigne. Priorité S12 : la création du fichier.'],
      ['S12 · Produire', '1. Créer premier-document.md dans le dossier choisi ; vérifier son nom. 2. Écrire « # Ma fiche » puis une liste ; enregistrer. 3. Ouvrir l’aperçu disponible dans l’éditeur ; comparer titre et liste au texte saisi. La commande d’aperçu dépend de l’environnement.'],
    ],
    before: 'Créez le document et vérifiez qu’il fonctionne.',
    after: 'Enregistrez premier-document.md dans le dossier choisi. Retrouvez le fichier, ouvrez-le et vérifiez la présence du titre et de la liste.',
    reason: 'La correction précise le fichier, l’action et le contrôle attendu. Aucun test avec un participant n’est déclaré.',
    exercise: 'Repérez la commande d’aperçu réellement disponible dans votre éditeur et adaptez la consigne.',
  },
  {
    title: 'Un guide d’accueil scolaire', public: 'Nouveaux élèves d’un établissement fictif',
    need: 'Savoir où chercher une information et à qui demander de l’aide.',
    stages: [
      ['S09 · Cadrer', 'Sujet : l’accueil. Public : nouveaux élèves. Besoin : repères de départ. Objectif : orienter les premières démarches. Résultat : un guide court avec interlocuteurs vérifiés. Première action : lister les informations autorisées.'],
      ['S10 · Structurer', 'Prévoir une fiche d’orientation et une checklist. Recueillir uniquement les horaires et contacts autorisés. Critère : un lecteur trouve la démarche et le service concerné. Aucun horaire ni contact réel n’est inventé.'],
      ['S11 · Organiser', 'Comprendre : le rôle du guide. Préparer : documents nécessaires à confirmer. Produire : suivre une démarche. Vérifier : identifier le bon service. Améliorer : signaler un renseignement manquant.'],
      ['S12 · Produire', '1. Consulter la liste des services approuvée ; repérer le service utile. 2. Lire ses conditions d’accueil ; confirmer les informations manquantes. 3. Préparer sa demande sans données sensibles inutiles ; vérifier la liste des pièces autorisées.'],
    ],
    before: 'Allez au secrétariat le matin avec vos papiers.',
    after: 'Consultez les horaires et la liste des pièces dans la source approuvée par l’établissement. Si ces informations manquent, demandez confirmation avant de vous déplacer.',
    reason: 'La correction retire un horaire supposé et rend visible la source à vérifier.',
    exercise: 'Listez les informations qui exigeraient une autorisation de l’établissement avant diffusion.',
  },
  {
    title: 'Une procédure administrative', public: 'Collaborateurs d’une structure fictive',
    need: 'Préparer une demande interne complète et suivre son traitement.',
    stages: [
      ['S09 · Cadrer', 'Sujet : une demande interne. Public : collaborateurs. Besoin : repérer les informations nécessaires. Objectif : décrire la préparation. Résultat : une procédure à relire par le responsable. Première action : consulter le modèle autorisé.'],
      ['S10 · Structurer', 'Prévoir une procédure et une grille de contrôle. Ressources : formulaire autorisé et règles internes disponibles. Étapes : préparer, contrôler, transmettre après accord. Critère : les champs requis et l’interlocuteur sont identifiés.'],
      ['S11 · Organiser', 'Comprendre : objet de la demande. Préparer : pièces requises. Produire : remplir les champs. Vérifier : contrôler complétude et confidentialité. Améliorer : traiter un retour du responsable.'],
      ['S12 · Produire', '1. Ouvrir le modèle en vigueur et vérifier sa référence. 2. Compléter les champs avec des informations autorisées ; signaler les inconnues. 3. Comparer aux exigences internes et demander la relecture du responsable avant transmission.'],
    ],
    before: 'Envoyez tous les justificatifs par courriel.',
    after: 'Vérifiez la liste des pièces requises, le destinataire et le canal autorisé. Transmettez uniquement les pièces nécessaires après contrôle des données sensibles.',
    reason: 'La correction précise les vérifications et limite les pièces transmises, sans inventer de règle interne.',
    exercise: 'Distinguez les champs obligatoires, les informations manquantes et les pièces qui ne doivent pas figurer dans une démonstration publique.',
  },
  {
    title: 'La préparation d’un événement associatif', public: 'Bénévoles d’une équipe fictive',
    need: 'Organiser les tâches et rendre visibles les responsabilités avant un événement.',
    stages: [
      ['S09 · Cadrer', 'Sujet : préparer un événement. Public : bénévoles. Besoin : clarifier qui prépare quoi. Objectif : guider la coordination. Résultat : un guide et une checklist à relire. Première action : recueillir les tâches connues.'],
      ['S10 · Structurer', 'Prévoir une liste de tâches, les responsables à confirmer et les contrôles. Lieu, budget, calendrier et autorisations restent À VÉRIFIER. Critère : chaque tâche possède un responsable et une condition de réalisation explicites.'],
      ['S11 · Organiser', 'Comprendre : objectif de l’événement. Préparer : ressources et autorisations. Produire : répartir les tâches. Vérifier : contrôler les éléments manquants. Améliorer : noter les retours réellement reçus.'],
      ['S12 · Produire', '1. Lister les tâches et les informations manquantes. 2. Faire confirmer responsables et moyens par le coordinateur. 3. Relire la checklist avec l’équipe et consigner les réserves avant toute action nécessitant une autorisation.'],
    ],
    before: 'Tout doit être prêt vendredi ; chaque bénévole sait quoi faire.',
    after: 'Faire confirmer l’échéance de chaque tâche et son responsable. Inscrire les moyens et autorisations manquants dans la checklist, puis demander la revue du coordinateur.',
    reason: 'La correction retire une échéance inventée et une responsabilité supposée. Elle n’affirme aucune réussite de l’événement.',
    exercise: 'Choisissez une tâche, proposez un contrôle observable et indiquez qui devrait confirmer sa faisabilité.',
  },
];
