<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard Soporte Jelou 2026</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:13px;background:#f4f5f7;color:#1a1a2e;min-height:100vh}
  .topbar{background:#fff;border-bottom:1px solid #e2e5ea;padding:12px 24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;position:sticky;top:0;z-index:100}
  .topbar h1{font-size:16px;font-weight:600;color:#0f1729}
  .topbar .sub{font-size:11px;color:#6b7280;margin-top:2px}
  .tabs{display:flex;gap:6px}
  .tab{padding:6px 16px;border-radius:7px;border:1px solid #d1d5db;font-size:12px;font-weight:500;cursor:pointer;background:#fff;color:#6b7280;transition:all .15s}
  .tab.g-active{background:#EFF6FF;color:#1d4ed8;border-color:#3b82f6}
  .tab.o-active{background:#ECFDF5;color:#065f46;border-color:#10b981}
  .btn-upload{padding:6px 14px;border-radius:7px;border:1px solid #d1d5db;background:#fff;font-size:12px;cursor:pointer;color:#374151;display:flex;align-items:center;gap:5px}
  .btn-upload:hover{background:#f9fafb}
  .wrap{padding:20px 24px;max-width:1100px;margin:0 auto}
  .drop-zone{border:2px dashed #cbd5e1;border-radius:14px;padding:52px 24px;text-align:center;cursor:pointer;color:#94a3b8;transition:all .15s;background:#fff}
  .drop-zone:hover{border-color:#3b82f6;background:#eff6ff}
  .drop-zone .icon{font-size:36px;margin-bottom:10px}
  .drop-zone h2{font-size:15px;font-weight:600;color:#374151;margin-bottom:6px}
  .drop-zone p{font-size:12px}
  .cards{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px}
  .card{background:#fff;border-radius:10px;padding:14px 16px;flex:1;min-width:140px;border:1px solid #e5e7eb}
  .card .lbl{font-size:11px;color:#6b7280;margin-bottom:4px}
  .card .val{font-size:22px;font-weight:600;color:#111827}
  .card .sub{font-size:11px;margin-top:3px}
  .ok{color:#059669}.warn{color:#d97706}.bad{color:#dc2626}
  .sec{background:#fff;border-radius:12px;padding:16px 18px;margin-bottom:12px;border:1px solid #e5e7eb}
  .sec h3{font-size:13px;font-weight:600;margin-bottom:14px;color:#111827}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px}
  canvas{max-height:220px}
  table{width:100%;border-collapse:collapse;font-size:12px}
  th{text-align:left;padding:7px 10px;font-size:11px;color:#6b7280;font-weight:500;border-bottom:1px solid #f3f4f6}
  td{padding:7px 10px;border-bottom:1px solid #f9fafb;color:#374151}
  .badge{display:inline-block;padding:2px 8px;border-radius:20px;font-size:11px;font-weight:500}
  .b-open{background:#FEF3C7;color:#92400e}
  .b-closed{background:#D1FAE5;color:#065f46}
  .pane{display:none}.pane.show{display:block}
  .error-box{background:#FEF2F2;border:1px solid #FECACA;border-radius:8px;padding:10px 14px;font-size:12px;color:#991b1b;margin-bottom:12px}
  .file-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
  .chip{background:#EFF6FF;color:#1d4ed8;border-radius:20px;padding:3px 10px;font-size:11px}
  @media(max-width:640px){.grid2{grid-template-columns:1fr}.cards{flex-direction:column}}
</style>
</head>
<body>

<div class="topbar">
  <div>
    <h1>Dashboard de soporte al cliente</h1>
    <div class="sub" id="sub-lbl">Sin datos cargados — arrastra tus archivos Excel para comenzar</div>
  </div>
  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">
    <div class="tabs">
      <button class="tab g-active" onclick="setView('g')">Vista gerencial</button>
      <button class="tab" onclick="setView('o')">Vista operacional</button>
    </div>
    <button class="btn-upload" onclick="document.getElementById('fi').click()">
      &#128196; Cargar archivos
    </button>
    <input type="file" id="fi" multiple accept=".xlsx,.xls" style="display:none" onchange="handleFiles(this.files)">
  </div>
</div>

<div class="wrap">
  <div id="err-box" class="error-box" style="display:none"></div>

  <div id="drop-zone" class="drop-zone"
    ondragover="event.preventDefault();this.style.borderColor='#3b82f6'"
    ondragleave="this.style.borderColor='#cbd5e1'"
    ondrop="event.preventDefault();this.style.borderColor='#cbd5e1';handleFiles(event.dataTransfer.files)"
    onclick="document.getElementById('fi').click()">
    <div class="icon">📂</div>
    <h2>Carga tus archivos Excel aquí</h2>
    <p>Canal Chat.xlsx · Canal Correo.xlsx · CSAT Operadores.xlsx · CSAT AI Agent.xlsx · Chats AI Agent.xlsx</p>
    <p style="margin-top:6px;font-size:11px">Puedes cargar los archivos en cualquier orden — se acumulan</p>
    <div class="file-chips" id="chip-area" style="justify-content:center;margin-top:10px"></div>
  </div>

  <div id="pane-g" class="pane show">
    <div class="cards" id="g-cards"></div>
    <div class="sec"><h3>Evolución mensual — volumen de tickets</h3><canvas id="ch-vol"></canvas></div>
    <div class="grid2">
      <div class="sec"><h3>TTR promedio mensual (horas)</h3><canvas id="ch-ttr"></canvas></div>
      <div class="sec"><h3>CSAT promedio mensual (escala 1–5)</h3><canvas id="ch-csat"></canvas></div>
    </div>
    <div class="grid2">
      <div class="sec"><h3>Tickets por tipo de gestión</h3><canvas id="ch-tipo"></canvas></div>
      <div class="sec"><h3>Distribución por canal</h3><canvas id="ch-canal"></canvas></div>
    </div>
    <div class="sec"><h3>Tickets y TTR por agente</h3><canvas id="ch-agente"></canvas></div>
  </div>

  <div id="pane-o" class="pane">
    <div class="cards" id="o-cards"></div>
    <div class="sec"><h3>Evolución semanal — tickets (barras) y CSAT (línea)</h3><canvas id="ch-sem-vol"></canvas></div>
    <div class="sec"><h3>TTR semanal promedio (horas)</h3><canvas id="ch-sem-ttr"></canvas></div>
    <div class="sec">
      <h3>Carga por agente</h3>
      <table><thead><tr><th>Agente</th><th>Total tickets</th><th>Abiertos</th><th>TTR prom (h)</th></tr></thead>
      <tbody id="tbl-agentes"></tbody></table>
    </div>
    <div class="sec">
      <h3>Tickets recientes (últimos 20)</h3>
      <div style="overflow-x:auto">
      <table><thead><tr><th>Ticket</th><th>Tipo</th><th>Canal</th><th>Agente</th><th>Estado</th><th>Fecha</th></tr></thead>
      <tbody id="tbl-tickets"></tbody></table>
      </div>
    </div>
  </div>
</div>

<script>
const MONTHS=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"];
let rawData={}, processed=null, charts={}, currentView='g';

function parseDateField(v){
  if(!v)return null;
  if(v instanceof Date)return isNaN(v)?null:v;
  const s=String(v).trim();
  if(!s)return null;
  let d=new Date(s);
  if(!isNaN(d))return d;
  const p=s.split(/[\/\-]/);
  if(p.length===3){const a=new Date(`${p[2]}-${p[1].padStart(2,'0')}-${p[0].padStart(2,'0')}`);if(!isNaN(a))return a;}
  return null;
}
const is2026=d=>d&&d.getFullYear()===2026;
const monthLabel=d=>d?MONTHS[d.getMonth()]:"";
function weekLabel(d){
  if(!d)return"";
  const j=new Date(d.getFullYear(),0,1);
  const w=Math.ceil(((d-j)/86400000+j.getDay()+1)/7);
  return`S${w}`;
}
function standardizeCsat(val){
  if(val===null||val===undefined||val==="")return null;
  const n=parseFloat(String(val).replace(",","."));
  if(!isNaN(n)&&n>=1&&n<=5)return n;
  if(!isNaN(n)&&n>=6&&n<=10)return Math.round(n/2);
  const s=String(val).toLowerCase();
  if(["sí","si","yes","satisfecho","bueno","excelente","muy bien"].some(x=>s.includes(x)))return 5;
  if(["regular","neutral","más o menos"].some(x=>s.includes(x)))return 3;
  if(["no","mal","insatisfecho","no realmente","pésimo"].some(x=>s.includes(x)))return 2;
  return null;
}
const avg=a=>a.length?a.reduce((s,x)=>s+x,0)/a.length:0;
function groupBy(arr,fn){return arr.reduce((acc,x)=>{const k=fn(x)||"Sin dato";(acc[k]=acc[k]||[]).push(x);return acc;},{});}
const isClosed=e=>{const s=(e||"").toLowerCase();return s.includes("cerr")||s.includes("resuel")||s==="close"||s==="closed";};

function processFiles(raw){
  const chat=raw["Canal Chat.xlsx"]||[];
  const correo=raw["Canal Correo.xlsx"]||[];
  const csatOp=raw["CSAT Operadores.xlsx"]||[];
  const csatAI=raw["CSAT AI Agent.xlsx"]||[];
  const chatsAI=raw["Chats AI Agent.xlsx"]||[];
  const tmap={};
  const addRow=(row,source)=>{
    const ticket=String(row["Ticket"]||row["Numero de registro"]||"").trim();
    if(!ticket)return;
    const fc=parseDateField(row["Fecha creacion"]||row["Fecha de creación"]);
    const fci=parseDateField(row["Fecha cerrado"]||row["Fecha actualizacion"]||row["Fecha de actualización"]);
    if(!is2026(fc))return;
    if(!tmap[ticket])tmap[ticket]={
      ticket,source,
      agente:row["Tech Support"]||row["Resuelto por"]||"",
      tipo:row["Tipo de gestion"]||row["Tipo de gestión"]||"",
      estado:row["Estado"]||"",
      canal:source==="chat"?(row["Canal"]||"Chat"):"Correo",
      fc,fci,
      ttr:(fc&&fci&&fci>fc)?(fci-fc)/3600000:null,
      mesLabel:fc?monthLabel(fc):"",
      semana:fc?weekLabel(fc):"",
    };
  };
  chat.forEach(r=>addRow(r,"chat"));
  correo.forEach(r=>addRow(r,"correo"));
  const tickets=Object.values(tmap);
  const csatRows=csatOp.filter(r=>is2026(parseDateField(r["Fecha de creación"]))).map(r=>({
    csat:standardizeCsat(r["Satisfacion"]),fecha:parseDateField(r["Fecha de creación"]),operador:r["Operador"]||""
  })).filter(r=>r.csat!==null);
  const aiChats=chatsAI.filter(r=>is2026(parseDateField(r["Fecha de creación"]))).map(r=>({
    fecha:parseDateField(r["Fecha de creación"]),mesLabel:monthLabel(parseDateField(r["Fecha de creación"])),semana:weekLabel(parseDateField(r["Fecha de creación"]))
  }));
  return{tickets,csatRows,aiChats};
}

async function handleFiles(files){
  showErr(null);
  for(const f of Array.from(files)){
    try{
      const buf=await f.arrayBuffer();
      const wb=XLSX.read(buf,{type:"arraybuffer",cellDates:true});
      const ws=wb.Sheets[wb.SheetNames[0]];
      rawData[f.name]=XLSX.utils.sheet_to_json(ws,{defval:"",raw:false});
    }catch(e){showErr(`Error leyendo ${f.name}: ${e.message}`);}
  }
  const names=Object.keys(rawData);
  document.getElementById('sub-lbl').textContent=`Datos 2026 — ${names.length} archivo(s) cargado(s)`;
  const chips=document.getElementById('chip-area');
  chips.innerHTML=names.map(n=>`<span class="chip">${n}</span>`).join('');
  try{
    processed=processFiles(rawData);
    document.getElementById('drop-zone').style.display='none';
    renderAll();
  }catch(e){showErr("Error procesando datos: "+e.message);}
}

function showErr(msg){
  const b=document.getElementById('err-box');
  if(msg){b.textContent=msg;b.style.display='block';}else{b.style.display='none';}
}

function destroyChart(id){if(charts[id]){charts[id].destroy();delete charts[id];}}

function mkLine(id,labels,datasets){
  destroyChart(id);
  const ctx=document.getElementById(id)?.getContext('2d');
  if(!ctx)return;
  charts[id]=new Chart(ctx,{type:'line',data:{labels,datasets},options:{responsive:true,maintainAspectRatio:true,plugins:{legend:{labels:{font:{size:11},boxWidth:12}}},scales:{x:{ticks:{font:{size:10}}},y:{ticks:{font:{size:10}}}}}});
}
function mkBar(id,labels,datasets,opts={}){
  destroyChart(id);
  const ctx=document.getElementById(id)?.getContext('2d');
  if(!ctx)return;
  charts[id]=new Chart(ctx,{type:'bar',data:{labels,datasets},options:{responsive:true,maintainAspectRatio:true,indexAxis:opts.h?'y':'x',plugins:{legend:{labels:{font:{size:11},boxWidth:12}}},scales:{x:{ticks:{font:{size:10}}},y:{ticks:{font:{size:10}}}}}});
}
function mkPie(id,labels,data,colors){
  destroyChart(id);
  const ctx=document.getElementById(id)?.getContext('2d');
  if(!ctx)return;
  charts[id]=new Chart(ctx,{type:'pie',data:{labels,datasets:[{data,backgroundColor:colors}]},options:{responsive:true,maintainAspectRatio:true,plugins:{legend:{position:'right',labels:{font:{size:11},boxWidth:12}}}}});
}
function mkMixed(id,labels,barData,lineData,barLabel,lineLabel){
  destroyChart(id);
  const ctx=document.getElementById(id)?.getContext('2d');
  if(!ctx)return;
  charts[id]=new Chart(ctx,{type:'bar',data:{labels,datasets:[
    {type:'bar',label:barLabel,data:barData,backgroundColor:'rgba(55,138,221,0.7)',borderRadius:4,yAxisID:'y'},
    {type:'line',label:lineLabel,data:lineData,borderColor:'#1D9E75',backgroundColor:'transparent',borderWidth:2,pointRadius:3,yAxisID:'y2'}
  ]},options:{responsive:true,maintainAspectRatio:true,plugins:{legend:{labels:{font:{size:11},boxWidth:12}}},scales:{y:{ticks:{font:{size:10}}},y2:{position:'right',min:1,max:5,ticks:{font:{size:10}}}}}});
}

function cards(id,items){
  document.getElementById(id).innerHTML=items.map(c=>`
    <div class="card">
      <div class="lbl">${c.label}</div>
      <div class="val">${c.value??'—'}</div>
      ${c.sub?`<div class="sub ${c.cls||''}">${c.sub}</div>`:''}
    </div>`).join('');
}

function renderAll(){
  if(!processed)return;
  renderGerencial();
  renderOperacional();
}

function renderGerencial(){
  const{tickets,csatRows,aiChats}=processed;
  const bm=groupBy(tickets,t=>t.mesLabel);
  const cm=groupBy(csatRows.filter(r=>r.fecha),r=>monthLabel(r.fecha));
  const am=groupBy(aiChats,r=>r.mesLabel);
  const meses=MONTHS.filter(m=>bm[m]||cm[m]||am[m]);

  const evo=meses.map(m=>{
    const ts=bm[m]||[],cs=cm[m]||[],ai=am[m]||[];
    const ttrs=ts.filter(t=>t.ttr>0&&t.ttr<720).map(t=>t.ttr);
    return{mes:m,tickets:ts.length,cerrados:ts.filter(t=>isClosed(t.estado)).length,
      csat:cs.length?+avg(cs.map(c=>c.csat)).toFixed(2):null,
      ttr:ttrs.length?+avg(ttrs).toFixed(1):null,ai:ai.length};
  });

  const total=tickets.length;
  const cerrados=tickets.filter(t=>isClosed(t.estado)).length;
  const pct=total?Math.round(cerrados/total*100):0;
  const ttrsAll=tickets.filter(t=>t.ttr>0&&t.ttr<720).map(t=>t.ttr);
  const ttrAvg=ttrsAll.length?+avg(ttrsAll).toFixed(1):null;
  const csatAvg=csatRows.length?+avg(csatRows.map(c=>c.csat)).toFixed(2):null;

  cards('g-cards',[
    {label:'Tickets 2026',value:total.toLocaleString()},
    {label:'Resueltos',value:cerrados.toLocaleString(),sub:`${pct}% del total`,cls:pct>=70?'ok':'warn'},
    {label:'TTR promedio',value:ttrAvg?`${ttrAvg}h`:'—',sub:'Tiempo de resolución'},
    {label:'CSAT promedio',value:csatAvg?`${csatAvg}/5`:'—',sub:csatAvg?(csatAvg>=4?'Sobre meta (4.0)':'Bajo meta (4.0)'):'',cls:csatAvg?(csatAvg>=4?'ok':'warn'):''},
    {label:'Chats IA 2026',value:aiChats.length.toLocaleString(),sub:'Agente automático'},
  ]);

  mkLine('ch-vol',meses,[
    {label:'Tickets',data:evo.map(e=>e.tickets),borderColor:'#378ADD',backgroundColor:'transparent',borderWidth:2,pointRadius:4},
    {label:'Resueltos',data:evo.map(e=>e.cerrados),borderColor:'#1D9E75',backgroundColor:'transparent',borderWidth:2,pointRadius:4},
    {label:'Chats IA',data:evo.map(e=>e.ai),borderColor:'#BA7517',backgroundColor:'transparent',borderWidth:2,pointRadius:4},
  ]);

  const ttrMes=evo.filter(e=>e.ttr);
  mkBar('ch-ttr',ttrMes.map(e=>e.mes),[{label:'TTR (h)',data:ttrMes.map(e=>e.ttr),backgroundColor:'rgba(55,138,221,0.75)',borderRadius:4}]);

  const csatMes=evo.filter(e=>e.csat);
  mkLine('ch-csat',csatMes.map(e=>e.mes),[{label:'CSAT',data:csatMes.map(e=>e.csat),borderColor:'#1D9E75',backgroundColor:'transparent',borderWidth:2,pointRadius:4}]);

  const bt=groupBy(tickets.filter(t=>t.tipo),t=>t.tipo);
  const tipoD=Object.entries(bt).map(([t,a])=>({tipo:t,n:a.length})).sort((a,b)=>b.n-a.n).slice(0,7);
  mkBar('ch-tipo',tipoD.map(d=>d.tipo),[{label:'Tickets',data:tipoD.map(d=>d.n),backgroundColor:'rgba(55,138,221,0.75)',borderRadius:4}],{h:true});

  const bc=groupBy(tickets,t=>t.canal);
  const canalD=Object.entries(bc).map(([c,a])=>({c,n:a.length}));
  mkPie('ch-canal',canalD.map(d=>d.c),canalD.map(d=>d.n),['#378ADD','#1D9E75','#BA7517','#E24B4A','#888780']);

  const ba=groupBy(tickets.filter(t=>t.agente),t=>t.agente);
  const agD=Object.entries(ba).map(([a,ts])=>{
    const ttrs=ts.filter(t=>t.ttr>0&&t.ttr<720).map(t=>t.ttr);
    return{a:a.split(" ")[0],total:ts.length,ttr:ttrs.length?+avg(ttrs).toFixed(1):0};
  }).sort((a,b)=>b.total-a.total).slice(0,9);
  mkBar('ch-agente',agD.map(d=>d.a),[
    {label:'Tickets',data:agD.map(d=>d.total),backgroundColor:'rgba(55,138,221,0.75)',borderRadius:4},
    {label:'TTR prom (h)',data:agD.map(d=>d.ttr),backgroundColor:'rgba(186,117,23,0.75)',borderRadius:4},
  ]);
}

function renderOperacional(){
  const{tickets,csatRows,aiChats}=processed;
  const bs=groupBy(tickets,t=>t.semana);
  const cs=groupBy(csatRows.filter(r=>r.fecha),r=>weekLabel(r.fecha));
  const semanas=[...new Set([...Object.keys(bs),...Object.keys(cs)])].filter(Boolean).sort((a,b)=>parseInt(a.slice(1))-parseInt(b.slice(1)));

  const evo=semanas.map(s=>{
    const ts=bs[s]||[],csr=cs[s]||[];
    const ttrs=ts.filter(t=>t.ttr>0&&t.ttr<720).map(t=>t.ttr);
    return{s,tickets:ts.length,csat:csr.length?+avg(csr.map(c=>c.csat)).toFixed(2):null,ttr:ttrs.length?+avg(ttrs).toFixed(1):null};
  });

  const ult=evo[evo.length-1]||{};
  const abiertos=tickets.filter(t=>!isClosed(t.estado)).length;
  const ba=groupBy(tickets.filter(t=>t.agente),t=>t.agente);
  const agentes=Object.entries(ba).map(([a,ts])=>{
    const ab=ts.filter(t=>!isClosed(t.estado)).length;
    const ttrs=ts.filter(t=>t.ttr>0&&t.ttr<720).map(t=>t.ttr);
    return{a,total:ts.length,abiertos:ab,ttr:ttrs.length?+avg(ttrs).toFixed(1):null};
  }).sort((a,b)=>b.total-a.total);

  cards('o-cards',[
    {label:'Tickets esta semana',value:ult.tickets??'—'},
    {label:'Tickets abiertos',value:abiertos,sub:abiertos>20?'Revisión recomendada':'Nivel normal',cls:abiertos>20?'warn':'ok'},
    {label:'CSAT esta semana',value:ult.csat?`${ult.csat}/5`:'—'},
    {label:'TTR esta semana',value:ult.ttr?`${ult.ttr}h`:'—'},
    {label:'Agentes activos',value:agentes.length},
  ]);

  mkMixed('ch-sem-vol',semanas,evo.map(e=>e.tickets),evo.map(e=>e.csat),'Tickets','CSAT');

  const ttrSem=evo.filter(e=>e.ttr);
  mkBar('ch-sem-ttr',ttrSem.map(e=>e.s),[{label:'TTR (h)',data:ttrSem.map(e=>e.ttr),backgroundColor:'rgba(186,117,23,0.75)',borderRadius:4}]);

  document.getElementById('tbl-agentes').innerHTML=agentes.slice(0,15).map(a=>`
    <tr>
      <td>${a.a}</td><td>${a.total}</td>
      <td class="${a.abiertos>5?'warn':''}">${a.abiertos}</td>
      <td class="${a.ttr&&a.ttr>24?'bad':''}">${a.ttr?a.ttr+'h':'—'}</td>
    </tr>`).join('');

  const recientes=[...tickets].sort((a,b)=>(b.fc||0)-(a.fc||0)).slice(0,20);
  document.getElementById('tbl-tickets').innerHTML=recientes.map(t=>`
    <tr>
      <td style="font-family:monospace;font-size:11px;color:#2563eb">${String(t.ticket).slice(0,14)}</td>
      <td>${t.tipo||'—'}</td><td>${t.canal}</td>
      <td>${(t.agente||'').split(' ')[0]||'—'}</td>
      <td><span class="badge ${isClosed(t.estado)?'b-closed':'b-open'}">${t.estado||'—'}</span></td>
      <td>${t.fc?t.fc.toLocaleDateString('es-CO'):'—'}</td>
    </tr>`).join('');
}

function setView(v){
  currentView=v;
  document.getElementById('pane-g').className='pane'+(v==='g'?' show':'');
  document.getElementById('pane-o').className='pane'+(v==='o'?' show':'');
  document.querySelectorAll('.tab').forEach(t=>t.className='tab');
  const btn=document.querySelectorAll('.tab')[v==='g'?0:1];
  btn.className='tab '+(v==='g'?'g-active':'o-active');
}
</script>
</body>
</html>
