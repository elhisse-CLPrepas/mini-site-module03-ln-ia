"""Affiches vectorielles et PNG LN-IA, issues du parcours intégré S09–S12."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont
import math

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/ressources'; OUT.mkdir(parents=True,exist_ok=True)
W,H=1200,1800
BG='#081729'; PANEL='#10253e'; GOLD='#e8c77f'; WHITE='#f5f4ed'; MUTED='#c2cfdb'; LINE='#4b6179'
FONT=Path('C:/Windows/Fonts/segoeui.ttf')
BOLD=Path('C:/Windows/Fonts/segoeuib.ttf')

class Poster:
    def __init__(self,number,title,subtitle):
        self.im=Image.new('RGB',(W,H),BG);self.d=ImageDraw.Draw(self.im)
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc><rect width="1200" height="1800" fill="{BG}"/>']
        self.text(72,78,'LN-IA  /  MODULE 03',23,GOLD,True)
        self.text(1128,78,number+' / 02',22,GOLD,anchor='end')
        self.text(72,160,title,49,WHITE,True)
        self.text(72,216,subtitle,23,MUTED)
        self.line([(72,254),(1128,254)],GOLD,2)
    def text(self,x,y,text,size=24,color=WHITE,bold=False,anchor='start'):
        font=ImageFont.truetype(str(BOLD if bold else FONT),size)
        anchor_pil={'start':'ls','middle':'ms','end':'rs'}[anchor]
        self.d.text((x,y),text,font=font,fill=color,anchor=anchor_pil)
        self.svg.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(text)}</text>')
        width=self.d.textlength(text,font=font)
        left=x if anchor=='start' else x-width/2 if anchor=='middle' else x-width
        assert left>=35 and left+width<=1165,(text,left,width)
    def box(self,x,y,w,h,fill=PANEL,stroke=LINE,r=14):
        self.d.rounded_rectangle((x,y,x+w,y+h),r,fill,stroke,2)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    def line(self,points,color=GOLD,width=3,arrow=False):
        self.d.line(points,fill=color,width=width,joint='curve')
        self.svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"/>')
        if arrow:
            x,y=points[-1];x0,y0=points[-2];a=math.atan2(y-y0,x-x0)
            tri=[(x,y),(x-13*math.cos(a-.45),y-13*math.sin(a-.45)),(x-13*math.cos(a+.45),y-13*math.sin(a+.45))]
            self.d.polygon(tri,fill=color)
            self.svg.append('<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in tri)+f'" fill="{color}"/>')
    def diamond(self,cx,cy,w,h):
        pts=[(cx,cy-h/2),(cx+w/2,cy),(cx,cy+h/2),(cx-w/2,cy)]
        self.d.polygon(pts,fill=PANEL,outline=GOLD,width=3)
        self.svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{PANEL}" stroke="{GOLD}" stroke-width="2"/>')
    def save(self,name):
        self.text(72,1730,'L’IA propose. L’humain pilote et contrôle.',23,GOLD,True)
        self.text(72,1770,'Adaptation pédagogique • Automne 2026 • V1 À RELIRE',18,MUTED)
        (OUT/(name+'.svg')).write_text(''.join(self.svg)+'</svg>',encoding='utf-8')
        self.im.save(OUT/(name+'.png'),optimize=True)

p=Poster('01','Un projet, quatre livrables','S09 → S10 → S11 → S12 : produire, relire et conserver les preuves.')
p.box(180,300,840,105,stroke=GOLD)
p.text(600,342,'CHOISIR UN SEUL BESOIN ET SON PUBLIC',28,GOLD,True,'middle')
p.text(600,378,'Préparer 02-prompts/ · 03-documents/ · 07-portfolio/',23,WHITE,anchor='middle')
p.line([(600,405),(600,435),(435,435),(435,470)],arrow=True)
rows=[
 ('S09','Cadrer','Sujet · Public · Besoin','Objectif · Résultat · Première action','note-cadrage-courte.md'),
 ('S10','Structurer','Objectif · Solution · Livrables · Ressources','Étapes · Critères · Risques · Responsable','fiche-projet-v1.md'),
 ('S11','Organiser','Comprendre · Préparer · Produire','Vérifier · Améliorer : le plan du guide','plan-guide-pratique.md'),
 ('S12','Rédiger le guide V1','Au moins trois actions avec résultat vérifiable','Prérequis · Erreurs · Checklist · Limites','guide-pratique-v1.md'),
]
for i,(s,title,a,b,file) in enumerate(rows):
    y=470+i*270
    p.line([(770,y+75),(820,y+75)],arrow=True)
    p.line([(1060,y+75),(1120,y+75),(1120,y-25),(435,y-25),(435,y)],color=MUTED,width=2,arrow=True)
    p.text(1100,y+117,'NON',18,MUTED,anchor='middle')
    target=470+(i+1)*270 if i<3 else 1550
    p.line([(940,y+150),(940,y+208),(435,y+208),(435,target)],arrow=True)
    p.text(972,y+192,'OUI',19,GOLD,True)
    p.box(100,y,670,150,stroke=GOLD)
    p.text(128,y+39,s+'  /  '+title,30,GOLD,True)
    p.text(128,y+76,a,22)
    p.text(128,y+106,b,22)
    p.text(128,y+134,file,19,MUTED)
    p.diamond(940,y+75,240,150)
    p.text(940,y+68,'Contrôle',23,WHITE,True,'middle')
    p.text(940,y+99,'humain',23,WHITE,True,'middle')
p.box(100,1550,670,100,stroke=GOLD)
p.text(435,1590,'V1 CONSERVÉE → AFFICHE 02',27,GOLD,True,'middle')
p.text(435,1627,'Après chaque séance : prompt + grille + preuve.',22,WHITE,anchor='middle')
p.text(840,1583,'OUI : poursuivre.',20,MUTED)
p.text(840,1615,'NON : reprendre',20,MUTED)
p.text(840,1647,'la même séance.',20,MUTED)
p.save('affiche-01-parcours-module03')

p=Poster('02','De la V1 à la V2 à relire','Corriger réellement, tracer les changements, faire décider l’humain.')
for a,b in [(430,490),(620,680),(790,870),(1090,1160),(1260,1340),(1460,1550)]:
    p.line([(600,a),(600,b)],arrow=True)
p.line([(275,980),(100,980),(100,555),(250,555)],color=MUTED,arrow=True)
p.text(100,1040,'NON',22,MUTED,True)
p.text(100,1073,'Reprendre',20,MUTED)
p.text(100,1104,'la correction.',20,MUTED)
p.line([(950,1400),(1100,1400),(1100,555),(950,555)],color=MUTED,width=2,arrow=True)
p.text(1090,1320,'À CORRIGER',19,MUTED,True,'end')
for y,h,title,body in [
 (320,110,'01  /  Exporter et conserver V1','Garder le fichier V1 comme référence.'),
 (490,130,'02  /  Relire et modifier le texte','Corriger les champs et vérifier les faits / consignes.'),
 (680,110,'03  /  Écrire le journal V1 → V2','Préciser le passage, le motif et la vérification.'),
 (1160,100,'04  /  Exporter V2 À RELIRE','Conserver V1, V2, journal et preuve S12.'),
 (1340,120,'05  /  Revue humaine finale','Cohérence · Faits · Utilité · Confidentialité'),
 (1550,105,'06  /  Consigner la décision réelle','Responsable · Date · Réserves · Statut · Autorisations'),
]:
    p.box(250,y,700,h,stroke=GOLD)
    p.text(600,y+43,title,28,GOLD,True,'middle')
    p.text(600,y+83,body,23,WHITE,anchor='middle')
p.diamond(600,980,650,220)
p.text(600,960,'V1 exportée + champs modifiés',23,WHITE,True,'middle')
p.text(600,990,'Journal : au moins 12 caractères',22,WHITE,anchor='middle')
p.text(600,1022,'Relecture humaine déclarée ?',22,WHITE,anchor='middle')
p.text(630,1130,'OUI',21,GOLD,True)
p.text(600,1694,'L’export technique ne valide ni le contenu ni sa diffusion.',22,MUTED,anchor='middle')
p.save('affiche-02-versions-controle-module03')
print('2 affiches SVG + 2 PNG générées ; limites de largeur des textes vérifiées.')
