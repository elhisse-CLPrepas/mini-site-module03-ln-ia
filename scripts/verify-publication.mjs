import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

export function publicationIssues(names,read){
  const issues=[];
  for(const name of names){
    const p=name.replaceAll('\\','/');
    if(/(?:^|\/)(?:sources-historiques|tmp|node_modules|dist|08-archives-privees|\.aws|\.codex|\.agents|\.git)\//i.test(p))issues.push(p+' : répertoire exclu');
    if(/(?:^|\/)\.env(?:\..*)?$/i.test(p)&&!p.endsWith('.env.example'))issues.push(p+' : environnement privé');
    if(/\.(?:docx|zip|7z|rar|tar|gz|pem|key|p12|pfx)$/i.test(p))issues.push(p+' : source privée, archive ou clé exclue');
    if(p.endsWith('.pdf')&&p!=='public/ressources/Guide-Dossier-Professionnel-Module03-LN-IA-Automne2026.pdf')issues.push(p+' : PDF hors périmètre autorisé');
    if(/\.(?:png|jpe?g|ico|pdf|woff2?)$/i.test(p))continue;
    const text=read(name);
    const patterns=[/sk-(?:proj-)?[A-Za-z0-9_-]{24,}/,/gh[pousr]_[A-Za-z0-9]{30,}/,/github_pat_[A-Za-z0-9_]{30,}/,/-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/];
    if(patterns.some(pattern=>pattern.test(text)))issues.push(p+' : motif de secret à retirer');
  }
  return issues;
}

if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  const staged=process.argv.includes('--staged');
  const args=staged?['diff','--cached','--name-only','--diff-filter=ACMR','-z']:['ls-files','-z'];
  const names=execFileSync('git',args,{encoding:'utf8'}).split('\0').filter(Boolean);
  const read=name=>staged?execFileSync('git',['show',':'+name],{encoding:'utf8',maxBuffer:12*1024*1024}):fs.readFileSync(name,'utf8');
  const issues=publicationIssues(names,read);
  if(issues.length){console.error(issues.join('\n'));process.exitCode=1}
  else console.log(`Périmètre public contrôlé : ${names.length} fichiers, aucun chemin interdit ni motif de secret détecté.`);
}
