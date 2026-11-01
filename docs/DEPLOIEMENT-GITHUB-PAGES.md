# Déploiement GitHub Pages — contrôle humain requis

1. Vérifier l'origine des sources et l'état Git. Les archives historiques sont exclues par `.gitignore`.
2. Exécuter `npm install` (ou `npm ci` si le verrou est présent), `npm run check`, `npm test`, `npm run build`.
3. Ouvrir `dist/` avec `npm run preview` et faire une recette bureau/mobile.
4. Vérifier les références aux assets et les chemins sous `/mini-site-module03-ln-ia/` grâce à `base:'./'`.
5. Après validation humaine explicite, versionner et pousser vers `main` du dépôt choisi par le pilote.
6. Settings → Pages → Source = GitHub Actions ; vérifier les jobs et le site publié.
7. Pas de publication automatique sans autorisation ; pas de push --force.
