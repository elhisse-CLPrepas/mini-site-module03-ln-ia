// Adaptation pédagogique Automne : contrôles de fond à effectuer par l'humain.
export const guidance = {
  S09: {
    input: 'Un seul besoin réel, ou un cas clairement identifié comme FICTIF.',
    action: 'Renseigner les six rubriques. Distinguer le besoin, l’objectif du document et le résultat attendu.',
    review: 'Faire reformuler le sujet, le public et la première action par un lecteur. Corriger les formulations vagues.',
    next: 'S10',
  },
  S10: {
    input: 'La note de cadrage S09 relue, conservée à côté de la fiche.',
    action: 'Décrire la solution, les livrables, les ressources, les étapes et les critères observables. Marquer les inconnues À VÉRIFIER.',
    review: 'Comparer objectif et public à S09. Justifier les écarts et vérifier la faisabilité des étapes.',
    next: 'S11',
  },
  S11: {
    input: 'La note S09 et la fiche S10 relues.',
    action: 'Organiser Comprendre, Préparer, Produire, Vérifier et Améliorer. Pour chaque fonction, prévoir un objectif et une action du lecteur.',
    review: 'Vérifier l’ordre, les prérequis et la checklist. Choisir la partie prioritaire à rédiger en S12 ; le plan reste une architecture.',
    next: 'S12',
  },
  S12: {
    input: 'Le plan S11, le cadrage S09 et la fiche S10.',
    action: 'Rédiger au moins trois actions ordonnées avec résultat vérifiable, puis les erreurs à éviter et la checklist. Exporter et conserver V1 avant de corriger.',
    review: 'Tester les consignes, modifier le texte et expliquer passage, motif et vérification dans le journal. Déclarer la relecture avant V2 À RELIRE.',
    next: null,
  },
};
