"""Crée une copie adaptée du Word fourni, sans écraser la source."""
from pathlib import Path
from docx import Document

root=Path(__file__).resolve().parents[1]
base=root/'docs/Organigramme-Algorithme-Module03-LN-IA'
doc=Document(str(base)+'.docx')
replacements={
    'Chaque site télécharge dans Téléchargements ; transférer les fichiers manuellement dans ces dossiers.': 'Le mini-site télécharge dans le dossier habituel du navigateur ; transférer les fichiers manuellement dans ces dossiers.',
    'Utiliser le site public S09, puis S10, S11 et S12, ou l’aperçu autonome de chaque dépôt. Consulter Accueil, Présentation, Méthode et au moins un exemple.': 'Ouvrir le mini-site intégré ou APERCU-AUTONOME-MODULE03.html. Consulter Présentation, Méthode, Parcours opératoire et les exemples de « 4 séances ». Sélectionner ensuite S09 à S12 dans Atelier de production.',
    'Répondre aux cinq questions préparatoires.': 'Compléter les champs de l’atelier ; aucun questionnaire préparatoire séparé n’est proposé.',
    'ou coller son texte.': 'ou reporter les informations dans les champs correspondants.',
    'ou coller leur contenu.': 'ou reporter les informations dans les champs correspondants.',
}
def paragraphs(container):
    yield from container.paragraphs
    for table in container.tables:
        for row in table.rows:
            for cell in row.cells:
                yield from paragraphs(cell)
for p in paragraphs(doc):
    for old,new in replacements.items():
        if old in p.text:
            # Conserve le style du paragraphe et du premier segment.
            text=p.text.replace(old,new)
            if p.runs:
                p.runs[0].text=text
                for run in p.runs[1:]: run.text=''
            else: p.add_run(text)
doc.add_page_break()
doc.add_heading('Adaptation au mini site intégré',0)
doc.add_paragraph('Édition du 1er novembre 2026 — À RELIRE. Parcours S09 à S12 dans un atelier unique. La décision de validation reste humaine.')
extra=(root/'docs/Organigramme-Algorithme-Module03-LN-IA-INTEGRE.md').read_text(encoding='utf-8').split('## 11. Adaptation au mini-site intégré')[1]
for line in extra.strip().splitlines():
    if line.strip(): doc.add_paragraph(line.removeprefix('- '),style='List Bullet' if line.startswith('- ') else None)
doc.save(str(base)+'-INTEGRE.docx')
print('Copie adaptée créée ; source conservée.')
