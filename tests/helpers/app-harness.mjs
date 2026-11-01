// DOM minimal pour tester le vrai code app.js sans navigateur ni données utilisateur.
// Aucun rendu CSS, comportement natif de fichier ou téléchargement disque n'est simulé comme réel.
import vm from 'node:vm';
import fs from 'node:fs';
import * as core from '../../src/core.mjs';
import {guidance} from '../../src/session-guidance.js';
import {demonstrations} from '../../src/demonstrations.js';
import {parcoursMarkdown} from '../../src/parcours-data.js';

class Element {
  constructor(doc,tag,attrs={},parent=null){
    this.doc=doc;this.tagName=tag.toUpperCase();this.attrs={...attrs};this.parent=parent;
    this.dataset=Object.fromEntries(Object.entries(attrs).filter(([k])=>k.startsWith('data-')).map(([k,v])=>[k.slice(5),v]));
    this.style={};this.value=attrs.value||'';this.checked='checked' in attrs;this.hidden='hidden' in attrs;
    this.textContent='';this.files=[];this._html='';
    this.classList={toggle:()=>{}};
  }
  get id(){return this.attrs.id||''}
  set innerHTML(value){
    this._html=value;
    if(this.id==='page'){
      this.doc.nodes=this.doc.nodes.filter(n=>!n.inside(this));
      this.doc.activeElement=this.doc.body;
      this.doc.parse(value,this);
    }
  }
  get innerHTML(){return this._html}
  inside(parent){for(let n=this.parent;n;n=n.parent)if(n===parent)return true;return false}
  getAttribute(key){return this.attrs[key]??null}
  setAttribute(key,value){this.attrs[key]=String(value)}
  removeAttribute(key){delete this.attrs[key]}
  get href(){return this.attrs.href||''} set href(v){this.attrs.href=v}
  get download(){return this.attrs.download||''} set download(v){this.attrs.download=v}
  focus(){this.doc.activeElement=this}
  scrollIntoView(){}
  remove(){this.doc.nodes=this.doc.nodes.filter(n=>n!==this)}
  append(el){el.parent=this;this.doc.nodes.push(el)}
  click(){
    if(this.tagName==='A'&&this.download)this.doc.downloads.push({name:this.download,blob:this.doc.blobs.get(this.href)});
    return this.onclick?.({target:this,preventDefault(){}});
  }
}

class Document {
  constructor(){this.nodes=[];this.downloads=[];this.blobs=new Map();this.listeners={};this.body=new Element(this,'body');this.activeElement=this.body}
  parse(html,parent=this.body){
    const stack=[parent],voids=new Set(['input','img','br','hr','meta','link']);
    for(const match of html.matchAll(/<\/?([a-z][\w-]*)([^>]*)>/gi)){
      const tag=match[1].toLowerCase();
      if(match[0].startsWith('</')){
        for(let i=stack.length-1;i>0;i--)if(stack[i].tagName===tag.toUpperCase()){stack.length=i;break}
        continue;
      }
      const attrs={};
      for(const a of match[2].matchAll(/([\w-]+)(?:="([^"]*)"|='([^']*)'|=([^\s>]+))?/g))attrs[a[1]]=a[2]??a[3]??a[4]??'';
      const el=new Element(this,tag,attrs,stack.at(-1));this.nodes.push(el);
      if(tag==='option'&&'selected' in attrs)stack.at(-1).value=attrs.value;
      if(!voids.has(tag))stack.push(el);
    }
  }
  matches(el,selector){
    const [base,...parts]=selector.trim().split(/\s+/);
    if(parts.length)return this.matches(el,parts.join(' '))&&this.nodes.some(p=>this.matches(p,base)&&el.inside(p));
    const id=/^#([\w-]+)$/.exec(base);if(id)return el.id===id[1];
    const m=/^(\w+)?(?:\[([\w-]+)(?:=([^\]]+))?\])?(:checked)?$/.exec(base);
    if(!m)throw new Error('Sélecteur non pris en charge dans le DOM de test : '+selector);
    return (!m[1]||el.tagName===m[1].toUpperCase())&&(!m[2]||(m[2] in el.attrs&&(m[3]===undefined||el.attrs[m[2]]===m[3])))&&(!m[4]||el.checked);
  }
  querySelectorAll(selector){return this.nodes.filter(n=>this.matches(n,selector))}
  querySelector(selector){return this.querySelectorAll(selector)[0]||null}
  createElement(tag){return new Element(this,tag)}
  addEventListener(type,fn){(this.listeners[type]??=[]).push(fn)}
}

export function appHarness({storageValue='{}',storageError=false}={}){
  const document=new Document();
  document.parse(fs.readFileSync(new URL('../../index.html',import.meta.url),'utf8'));
  const storage=new Map([['lnia-module03-v1',storageValue]]);
  const sandbox={...core,guidance,demonstrations,parcoursMarkdown,document,Blob,console,
    location:{hash:''},history:{replaceState(){}},window:{scrollTo(){}},confirm:()=>false,
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>{if(storageError)throw new Error('quota');storage.set(k,v)}},
    URL:{createObjectURL(blob){const id='blob:test-'+document.blobs.size;document.blobs.set(id,blob);return id},revokeObjectURL(){}},
    setTimeout:()=>0};
  const context=vm.createContext(sandbox);
  const source=fs.readFileSync(new URL('../../src/app.js',import.meta.url),'utf8').replace(/^import .*?;\s*$/gm,'');
  vm.runInContext(source,context,{filename:'src/app.js'});
  const get=id=>{const el=document.querySelector('#'+id);if(!el)throw new Error('Élément absent : '+id);return el};
  return {document,storage,downloads:document.downloads,get,
    view:name=>context.view(name),
    session(id){context.view('atelier');const el=get('session');el.value=id;el.onchange({target:el})},
    fill(session){for(const [id] of session.fields){const el=get('f-'+id);el.value='FICTIF — '+id+' : consigne vérifiable';el.oninput?.({target:el})}},
    input(id,value){const el=get(id);el.value=value;el.oninput?.({target:el})},
    async importFile(file){const el=get('importFile');el.value='fichier-test';el.files=[file];await el.onchange({target:el})},
    key(key){const event={key,defaultPrevented:false,preventDefault(){this.defaultPrevented=true}};for(const f of document.listeners.keydown||[])f(event);return event},
    markup:()=>get('page').innerHTML,
  };
}
