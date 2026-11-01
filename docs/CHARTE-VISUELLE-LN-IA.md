# Charte visuelle du mini-site Module 03 LN-IA

Référence de travail issue des consignes du pilote du 1er novembre 2026. La recette visuelle finale reste soumise à sa relecture.

## Références demandées

- Atelier S10 : https://elhisse-clprepas.github.io/atelier-seance-10-ln-ia/
- Atelier S11 : https://elhisse-clprepas.github.io/atelier-seance-11-ln-ia/

Le HTML public et les feuilles CSS des deux références ont été récupérés le 1er novembre 2026. Le site S10 définit notamment `--navy:#071b33`, `--gold:#d6a64e`, un fond `#f2f5f9` et une encre `#152940`. S11 utilise une navigation latérale bleu nuit, des panneaux blancs, un fond clair et des sections de présentation bleu nuit. Sa dernière couche CSS allège les titres et boutons, avec Segoe UI et une graisse courante de 400. Il s’agit de faits relevés dans les CSS ; aucune capture visuelle des références n’est prétendue.

## Direction à maintenir

La combinaison demandée est **blanc + bleu nuit + gold**, répartie selon les usages. Elle ne signifie ni un site entièrement bleu, ni un remplacement du bleu par une palette verte. Toute évolution doit garder cette répartition :

| Usage | Choix Module 03 |
|---|---|
| Fond de travail | Gris blanc `#f3f5f8` |
| Cartes, champs, ressources et zones de lecture | Blanc `#ffffff` |
| Navigation et grandes surfaces de présentation | Bleu nuit `#071a31` à `#0c294c` |
| Texte sur blanc | Encre `#152940` ; texte secondaire `#536579` |
| Gold sur fond bleu nuit | `#f0cc83` ou `#edcc89` |
| Texte ocre sur blanc | `#825d20`, plus foncé que le gold décoratif |
| Séparateurs | Gris bleu `#d9e3ee` |

Le gold clair sert aux accents, aux boutons avec texte bleu nuit et au texte sur fond sombre. Sur blanc, employer l’ocre foncé pour les petits textes ; ne pas utiliser un gold clair comme couleur de lecture.

## Typographie et composition

- Segoe UI / system-ui, sans téléchargement de police ni dépendance à un CDN.
- Corps 400, boutons et libellés 500, titres 500–550 ; réserver 600 aux emphases courtes.
- Ne pas confondre finesse et texte trop pâle : conserver des couleurs contrastées et une taille de corps de 15 px avec un interligne de 1,6.
- Navigation latérale bleu nuit sur ordinateur ; navigation horizontale défilante et accessible au clavier sur écran étroit.
- Panneaux blancs, bordures fines, coins modérément arrondis, ombres légères. La zone d’accueil et les diapositives gardent le bleu nuit.
- Éviter l’accumulation de halos, de dégradés lumineux, de capitales grasses et de gros aplats sombres dans les zones de lecture.
- La CSS de référence chargée est `src/theme-references-ln-ia.css`. Les anciens thèmes sont conservés comme traces et ne sont plus chargés.

## Consignes pédagogiques à conserver

- Module 03 exclusivement dans l’interface et le README : S09, S10, S11 et S12 ; aucune réintroduction de passerelle vers un autre module.
- Rubrique Démonstrations indépendante, quatre cas clairement FICTIFS.
- Vingt diapositives, sommaire cliquable et notes.
- Organigramme sous forme de deux affiches agrandissables et téléchargeables, avec retours correctifs et contrôle humain.
- Guide Word source intact ; PDF disponible et adaptation HTML consultable. Les versions de consultation n’attribuent aucune validation automatique.
- V1 et V2 À RELIRE distinctes, contrôles V2, exports et sauvegardes conservés.
- Même présentation pour Vite, build statique et aperçu autonome. Le serveur local reste l’accès de contrôle du pilote.

## Contrôles avant une prochaine évolution

Relire cette charte et les dernières consignes du pilote avant toute modification graphique. Une nouvelle préférence explicite du pilote prévaut ; la reporter ici et dans le journal qualité pour éviter les interprétations successives contradictoires. Vérifier les contrastes des couples de couleurs utilisés, les points de rupture et la navigation clavier. Ne pas annoncer de recette visuelle réussie sans l’avoir réalisée dans le navigateur.
