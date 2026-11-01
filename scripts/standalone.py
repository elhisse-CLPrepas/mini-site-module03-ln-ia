"""Construit un aperçu hors ligne sans appeler Vite ni CDN."""
from pathlib import Path
import base64,re
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
css=(root/'src/styles.css').read_text(encoding='utf-8')
theme=(root/'src/theme-references-ln-ia.css').read_text(encoding='utf-8')
core=(root/'src/core.mjs').read_text(encoding='utf-8')
app=(root/'src/app.js').read_text(encoding='utf-8')
data=(root/'src/parcours-data.js').read_text(encoding='utf-8').replace('export const ', 'const ', 1)
guidance=(root/'src/session-guidance.js').read_text(encoding='utf-8')
demos=(root/'src/demonstrations.js').read_text(encoding='utf-8')
core=demos+'\n'+guidance+'\n'+data+'\n'+core
core=re.sub(r'(?m)^export ', '', core)
app=re.sub(r'(?m)^import .*?;\s*$', '', app)
logo=base64.b64encode((root/'public/assets/logo-ln-ia.png').read_bytes()).decode('ascii')
html=html.replace('<link rel="stylesheet" href="./src/styles.css">','<style>'+css+'</style>')
html=html.replace('<link rel="stylesheet" href="./src/theme-references-ln-ia.css">','<style>'+theme+'</style>')
html=html.replace('./assets/logo-ln-ia.png','data:image/png;base64,'+logo)
html=html.replace('<script type="module" src="./src/app.js"></script>','<script>\n'+core+'\n'+app+'\n</script>')
assert 'type="module"' not in html and 'import {' not in html
resources=[]
files=[('guide-module03.html','text/html;charset=utf-8'),('Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf','application/pdf')]
for poster in ['affiche-01-parcours-module03','affiche-02-versions-controle-module03']:
    files.extend([(poster+'.svg','image/svg+xml'),(poster+'.png','image/png')])
for name,mime in files:
    resource=(root/'public/ressources'/name).read_bytes()
    if name.endswith('.html'):
        guide=resource.decode('utf-8')
        guide=re.sub(r'<nav class="toolbar".*?</nav>','<p class="notice">Guide autonome : fermez cet onglet pour revenir au mini-site. Le PDF est disponible dans sa rubrique Ressources.</p>',guide,flags=re.S)
        resource=guide.encode('utf-8')
    resources.append("'./ressources/"+name+"':{mime:'"+mime+"',data:'"+base64.b64encode(resource).decode('ascii')+"'}")
# Les URL Blob permettent d'ouvrir les ressources depuis file:// sans navigation
# vers une URL data:, bloquée par plusieurs navigateurs. Aucun appel réseau.
offline="""
const offlineResources={RESOURCE_MAP};
function offlineResourceUrl(resource){
    if(!resource.url){
        const bytes=Uint8Array.from(atob(resource.data),c=>c.charCodeAt(0));
        resource.url=URL.createObjectURL(new Blob([bytes],{type:resource.mime}));
    }
    return resource.url;
}
function offlineImages(){
    document.querySelectorAll('img[src^="./ressources/"]').forEach(img=>{
        const resource=offlineResources[img.getAttribute('src')];
        if(resource)img.src=offlineResourceUrl(resource);
    });
}
offlineImages();
new MutationObserver(offlineImages).observe(document.getElementById('page'),{childList:true,subtree:true});
document.addEventListener('click',event=>{
    const link=event.target.closest('a');
    const resource=link&&offlineResources[link.getAttribute('href')];
    if(!resource)return;
    event.preventDefault();
    offlineResourceUrl(resource);
    if(link.hasAttribute('download')){
        const a=document.createElement('a');a.href=resource.url;
        a.download=link.getAttribute('href').split('/').pop();
        document.body.append(a);a.click();a.remove();
    }else window.open(resource.url,'_blank','noopener');
});
""".replace('RESOURCE_MAP',','.join(resources))
html=html.replace('</body>','<script>'+offline+'</script></body>')
out=root/'APERCU-AUTONOME-MODULE03.html';out.write_text(html,encoding='utf-8');print(out,out.stat().st_size)
