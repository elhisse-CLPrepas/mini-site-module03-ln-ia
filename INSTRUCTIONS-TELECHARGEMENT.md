# Télécharger et reprendre le Mini-site Module 03 LN-IA

Cette **édition légère** est une version fonctionnelle du pack de référence qui contient l'application Vite, l'aperçu HTML autonome, le guide Word, les modèles Markdown, le prompt maître pour Codex, les exemples et les tests. Les sources historiques volumineuses sont volontairement **à télécharger séparément** pour faciliter le téléchargement.

## Lancer l'application

1. Extraire ce ZIP en conservant son dossier `mini-site-module03-ln-ia/`.
2. Ouvrir ce dossier dans VS Code puis, si nécessaire, accorder la confiance au dossier avec `Workspaces: Manage Workspace Trust`.
3. Dans le terminal, exécuter `npm.cmd install`, puis `npm.cmd run dev`.
4. Pour la présentation hors ligne sans Node.js, ouvrir `APERCU-AUTONOME-MODULE03.html`.
5. Pour piloter avec Codex, lire `AGENTS.md`, puis copier `prompts/PROMPT-MAITRE-CODEX-MODULE03.md`.

## Retrouver le pack intégral

Le ZIP d'origine contient en supplément les cinq archives, à placer **sans extraction supplémentaire** dans `mini-site-module03-ln-ia/sources-historiques/` si vous en avez besoin :

- `supports-seance-09.zip`
- `supports-seance-10(2).zip`
- `supports-seance-11(1).zip`
- `supports-seance-12(1).zip`
- `dossier-supports-seance-12.zip`

Ces sources sont des archives historiques, pas nécessaires au fonctionnement du mini-site Vite. Les fichiers actifs actualisés figurent déjà dans l'édition légère. Le `CHECKSUMS-SHA256.txt` dans le projet correspond au pack d'origine et permet la vérification après réintégration des archives.

## Contrôle

- Exécuter `npm.cmd run check`, `npm.cmd test`, puis `npm.cmd run build` une fois les dépendances installées.
- La publication GitHub Pages exige une validation humaine préalable.
