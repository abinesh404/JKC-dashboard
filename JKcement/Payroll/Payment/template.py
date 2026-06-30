# Auto-generated template
def get_html():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg: #FAF5FF;
            --sidebar: #31004A;
            --sidebar-hover: #4A0070;
            --card-bg: #FFFFFF;
            --accent: #D000FF;
            --text-main: #000000;
            --text-light: #8E6CA8;
            --kpi-bg: #31004A;
        }
        body { font-family:'Plus Jakarta Sans',sans-serif; margin:0; display:flex; height:100vh; background:var(--bg); overflow:hidden; color:var(--text-main); }
        .sidebar { width:280px; background:var(--sidebar); color:#fff; display:flex; flex-direction:column; flex-shrink:0; z-index:100; overflow:hidden; }
        .side-header { padding:20px 15px; display:flex; align-items:center; gap:10px; cursor:pointer; width:100%; box-sizing:border-box; }
        .side-header i { font-size:18px; color:var(--accent); flex-shrink:0; }
        .logo-container { display:flex; align-items:center; justify-content:center; gap:12px; background:rgba(255,255,255,0.9); padding:8px 12px; border-radius:12px; flex-grow:1; max-width:210px; }
        .logo-container img { height:20px; width:auto; object-fit:contain; }
        .obj-list { flex-grow:1; overflow-y:auto; padding-left:15px; scrollbar-width:none; }
        .obj-list::-webkit-scrollbar { display:none; }
        .side-item { position:relative; padding:12px 20px; margin:4px 0; border-radius:30px 0 0 30px; cursor:pointer; font-size:11px; color:#CC80FF; transition:all 0.2s ease; font-weight:600; }
        .side-item:hover { color:#fff; background:var(--sidebar-hover); }
        .side-item.active { background:var(--bg); color:#000; font-weight:800; }
        .side-item.active::before { content:""; position:absolute; background:transparent; top:-20px; right:0; height:20px; width:20px; border-bottom-right-radius:20px; box-shadow:5px 5px 0 5px var(--bg); }
        .side-item.active::after { content:""; position:absolute; background:transparent; bottom:-20px; right:0; height:20px; width:20px; border-top-right-radius:20px; box-shadow:5px -5px 0 5px var(--bg); }
        .main { flex-grow:1; overflow-y:auto; padding:25px 40px; }
        .top-nav { display:flex; justify-content:space-between; align-items:center; margin-bottom:25px; }
        #disp-name { margin:0; font-size:24px; font-weight:900; color:#000; text-transform:uppercase; letter-spacing:1.5px; }
        .exc-btns { display:flex; gap:8px; }
        .exc-btns button { padding:8px 18px; border-radius:8px; border:1px solid var(--accent); background:var(--card-bg); font-size:11px; font-weight:700; cursor:pointer; color:var(--sidebar); transition:all 0.2s; }
        .exc-btns button.active { background:var(--sidebar); color:#fff; border-color:var(--sidebar); }
        #kpi-row { display:grid; grid-template-columns:repeat(6,1fr); gap:15px; margin-bottom:25px; }
        .kpi-card { background:var(--kpi-bg); padding:25px 10px; border-radius:25px; text-align:center; color:#fff; min-height:80px; display:flex; flex-direction:column; justify-content:center; transition:transform 0.2s; }
        .kpi-card:hover { transform: translateY(-3px); box-shadow: inset 0 0 25px var(--accent), 0 0 15px var(--accent); }
        .kpi-val { font-size:20px; font-weight:800; color:#FFF; }
        .kpi-lbl { font-size:10px; color:#CC80FF; text-transform:uppercase; font-weight:700; margin-top:8px; opacity:0.9; }
        #slicer-row { display:grid; grid-template-columns:1fr 1fr 1fr 1.6fr 0.8fr; gap:15px; margin-bottom:25px; align-items:end; }
        .slicer-card { background:var(--card-bg); padding:12px 15px; border-radius:15px; border:2px solid var(--accent); height:60px; display:flex; flex-direction:column; justify-content:center; }
        .slicer-lbl { font-size:9px; color:#000; text-transform:uppercase; font-weight:800; margin-bottom:5px; }
        select { width:100%; border:none; font-size:11px; padding:5px 0; background:transparent; outline:none; color:#000; font-weight:600; cursor:pointer; }
        .date-display { font-size:10px; font-weight:800; color:#000; }
        .btn-reset { height:40px; background:var(--sidebar); color:#fff; border:none; font-size:10px; font-weight:800; border-radius:15px; cursor:pointer; text-transform:uppercase; transition:opacity 0.2s; }
        .btn-reset:hover { opacity:0.9; }
        #chart-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:30px; }
        .chart-box { background:#fff; padding:15px; border-radius:25px; height:380px; position:relative; display:flex; flex-direction:column; border:4px solid var(--sidebar); overflow:hidden; box-shadow: 0 12px 30px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.05); }
        .full { grid-column:span 2; }
        .no-data-msg { position:absolute; inset:0; background:var(--bg); display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:20px; z-index:10; }
        .empty-state-icon { font-size:32px; color:var(--sidebar); opacity:0.2; margin-bottom:10px; }
        .empty-state-title { font-size:14px; font-weight:800; color:var(--sidebar); margin-bottom:5px; }
        .empty-state-desc { font-size:11px; color:var(--text-light); max-width:250px; }
        .table-box { background:var(--card-bg); padding:25px; border-radius:15px; margin-bottom:50px; border:2px solid var(--accent); }
        .table-header-flex { display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; }
        .btn-download { background:var(--sidebar); color:#fff; border:none; padding:8px 15px; border-radius:8px; cursor:pointer; font-size:11px; font-weight:700; display:flex; align-items:center; gap:8px; transition:0.2s; }
        .btn-download:hover { background:var(--accent); color:var(--sidebar); }
        .table-wrapper { max-height:500px; overflow-y:auto; border-radius:8px; border:1px solid #E5E7EB; }
        table { width:100%; border-collapse:collapse; font-size:11px; }
        th { background:#F9FAFB; color:#000; padding:12px; text-align:left; position:sticky; top:0; z-index:10; font-weight:800; border-bottom:2px solid #E5E7EB; }
        td { padding:10px 12px; border-bottom:1px solid #F3F4F6; color:#333; }
        tr:hover { background:#F9FAFB; }
        .date-slider-wrapper .slider-container { background:#E8C8F8!important; border-radius:10px; }
        #slider-track { background:var(--sidebar)!important; height:100%; border-radius:10px; }
        input[type=range] { pointer-events:none; -webkit-appearance:none; background:transparent; width:100%; }
        input[type=range]::-webkit-slider-thumb { pointer-events:auto; -webkit-appearance:none; width:14px; height:14px; border-radius:50%; background:var(--sidebar); border:2px solid var(--accent); cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.2); }
    </style>
</head>
<body>
    <div class="sidebar">
        <div class="side-header" onclick="window.location.href='/'">
            <i class="fa-solid fa-house"></i>
            <div class="logo-container">
                <img src="/static/JK-logo.png" alt="JK Logo">
                <img src="/static/ajalabs-logo.png" alt="Ajalabs Logo">
            </div>
        </div>
        <div class="obj-list">
            {% for obj in objectives %}
            <div class="side-item" data-id="{{ obj.id }}" data-name="{{ obj.o }}" onclick="selObj('{{ obj.id }}','{{ obj.o }}',this)">
                {{ obj.id }} - {{ obj.o }}
            </div>
            {% endfor %}
        </div>
    </div>
    <div class="main">
        <div class="top-nav">
            <div>
                <h2 id="disp-name">{{ page_title }}</h2>
                <h4 id="exc-title" style="margin: 5px 0 0 0; font-size: 13px; color: #8E6CA8; font-weight: 700; text-transform: uppercase; opacity: 0.8;"></h4>
            </div>
            <div class="exc-btns" id="exc-btns"></div>
        </div>
        <div id="kpi-row"></div>
        <div id="slicer-row"></div>
        <div id="chart-grid"></div>
        <div class="table-box">
            <div class="table-header-flex">
                <h3 style="font-size:14px;margin:0;font-weight:800;color:#000;">Detailed Log</h3>
                <button class="btn-download" onclick="downloadCSV()">
                    <i class="fa-solid fa-file-csv"></i> Download Data
                </button>
            </div>
            <div class="table-wrapper" id="table-container"></div>
        </div>
    </div>
<script>
const CONFIGS = {{ configs|safe }};
const CC = ['#31004A','#D000FF','#8E6CA8','#B300D9','#4A0070','#E580FF','#9B59B6'];
let rawD=[],rawC=[],filteredD=[];
let cInst={},colCache={};
let curID='',curExc=1,dateList=[];
let bStats=null,aCfg=null,curExcFilters=[],curExcCards=[],curExcCharts=[];
function rCol(source){if(!aCfg?.columns?.[source])return null;if(colCache[source])return colCache[source];const candidates=aCfg.columns[source];const nh=rawC.map(c=>c.trim().toLowerCase());for(const cand of candidates){const idx=nh.indexOf(cand.trim().toLowerCase());if(idx!==-1){colCache[source]=rawC[idx];return rawC[idx];}}return null;}
function parseNum(val){if(val===null||val===undefined||val==='')return 0;if(typeof val==='number')return val;const clean=String(val).replace(/[^\d.-]/g,'');const num=parseFloat(clean);return isNaN(num)?0:num;}
function fmt(n,cur){if(n===0)return cur?'\u20b90':'0';let s='',v=Math.abs(n);if(v>=1e7){v=n/1e7;s='Cr';}else if(v>=1e5){v=n/1e5;s='L';}else{v=n;}let r=parseFloat(v.toFixed(2))+s;return cur?'\u20b9'+r:r;}
function applyFilters(){if(!aCfg)return;const dC=rCol('date');const minD=dateList.length>0?new Date(dateList[+$('#rng-min').val()]):null;const maxD=dateList.length>0?new Date(dateList[+$('#rng-max').val()]):null;const af=(curExcFilters||[]).map(f=>({col:rCol(f.source),val:$('#'+f.id).val()})).filter(f=>f.col&&f.val!=='ALL');filteredD=rawD.filter(r=>{for(const f of af){if(String(r[f.col])!==f.val)return false;}if(dC&&minD&&maxD){const d=new Date(r[dC]);if(isNaN(d)||d<minD||d>maxD)return false;}return true;});updateKPIs();updateCharts();renderTable("No data available for this Exception");}
function updateKPIs(){const allFilt=isAllFilters();(curExcCards||[]).forEach(card=>{let val=0;if(!filteredD||filteredD.length===0){$('#'+card.id).text(card.format==='currency'?'\u20b90':'0');return;}const sourceCol=card.source?rCol(card.source):null;if(card.agg==='row_count')val=filteredD.length;else if(card.agg==='total_rows')val=(bStats&&allFilt)?bStats.total_rows:filteredD.length;else if(card.agg==='total_value'){if(bStats&&allFilt)val=bStats.total_value;else if(sourceCol)val=filteredD.reduce((a,b)=>a+parseNum(b[sourceCol]),0);}else if(card.agg==='unique'){val=sourceCol?new Set(filteredD.map(r=>r[sourceCol]).filter(v=>v!=='')).size:0;}$('#'+card.id).text(card.format==='currency'?fmt(val,true):val.toLocaleString('en-IN'));});}
function updateCharts(){if(!curExcCharts||curExcCharts.length===0)return;curExcCharts.forEach(cfg=>{const box=$('#box-'+cfg.id);box.find('.no-data-msg').remove();if(cInst[cfg.id])cInst[cfg.id].destroy();const xCol=rCol(cfg.x),yCol=rCol(cfg.y);if(!xCol||!filteredD.length){handleChartError(cfg.id,box);return;}let data={};if(cfg.time_group==='month'){filteredD.forEach(r=>{const o=new Date(r[xCol]);if(!isNaN(o)){const k=o.toLocaleString('default',{month:'short',year:'numeric'});data[k]=(data[k]||0)+(yCol?parseNum(r[yCol]):1);}});const sk=Object.keys(data).sort((a,b)=>new Date(a)-new Date(b));data=Object.fromEntries(sk.map(k=>[k,data[k]]));}else{filteredD.forEach(r=>{const k=r[xCol]||'N/A';data[k]=(data[k]||0)+(cfg.agg==='count'?1:parseNum(r[yCol]));});if(cfg.top_n)data=Object.fromEntries(Object.entries(data).sort((a,b)=>b[1]-a[1]).slice(0,cfg.top_n));}const labels=Object.keys(data),values=Object.values(data);if(!labels.length){handleChartError(cfg.id,box);return;}$('#'+cfg.id).show();renderChartJS(cfg,labels,values);});}
function handleChartError(id,box){$('#'+id).hide();box.find('.no-data-msg').remove();box.append(`<div class="no-data-msg"><i class="fa-solid fa-chart-bar empty-state-icon"></i><div class="empty-state-title">No data available</div><div class="empty-state-desc">Try adjusting filters or select another exception</div></div>`);}
function renderChartJS(cfg,labels,values){const ctx=document.getElementById(cfg.id).getContext('2d');const type=cfg.type||'bar';let chartConfig={type:type,data:{labels:labels,datasets:[{data:values,backgroundColor: type === 'line' ? CC[1] + '40' : CC,borderRadius:5,borderColor:CC[0],borderWidth:type==='line'?2:0,fill:type==='line'?{target:'origin',above:'rgba(0,0,0,0.05)'}: false,tension:0.4}]},options:{responsive: true,maintainAspectRatio: false,plugins:{title:{display: true,text:cfg.title,font:{size:13,weight:'800'},color:'#000'},legend:{display:!!cfg.legend,position:'bottom',labels:{boxWidth:10,font:{size:9}}}}}};if(type==='bar'||type==='line'){chartConfig.options.scales={x:{grid:{display: false},ticks:{font:{size:9}}},y:{grid:{color:'#f0f0f0'},ticks:{font:{size:9},callback:v=>fmt(v,false)}}};if(cfg.horizontal)chartConfig.options.indexAxis='y';}cInst[cfg.id]=new Chart(ctx,chartConfig);}
async function load(){if(!curID)return;colCache={};$('#table-container').html('<div class="no-data-msg">Fetching data...</div>');try{const r=await fetch(`./api/${curID}/${curExc}?t=${Date.now()}`);const d=await r.json();if(d.success){rawD=d.rows||[];rawC=d.cols||[];bStats=d.full_stats||null;setupSlider();popSlicers();applyFilters();}else{handleEmptyState(d.msg);}}catch(e){console.error(e);handleEmptyState("Server Error");}}
function handleEmptyState(msg="No data available for this Exception"){rawD=[];rawC=[];filteredD=[];updateKPIs();updateCharts();renderTable(msg);}
function setupSlider(){const dc=rCol('date');if(!dc){$('#lbl-min').text('-');$('#lbl-max').text('-');$('#slider-track').css({width:'0%'});return;}dateList=[...new Set(rawD.map(r=>r[dc]))].filter(x=>x&&!isNaN(new Date(x))).sort((a,b)=>new Date(a)-new Date(b));if(dateList.length>0){$('#rng-min').attr({min:0,max:dateList.length-1}).val(0);$('#rng-max').attr({min:0,max:dateList.length-1}).val(dateList.length-1);updSliderUI();}else{$('#lbl-min').text('-');$('#lbl-max').text('-');$('#slider-track').css({width:'0%'});}}
function popSlicers(){(curExcFilters||[]).forEach(f=>{const col=rCol(f.source),sel=$('#'+f.id);sel.html(`<option value="ALL">${f.all_label}</option>`);if(col&&rawD.length>0){[...new Set(rawD.map(r=>r[col]))].filter(x=>x).sort().forEach(v=>sel.append(`<option value="${v}">${v}</option>`));}});}
function renderTable(msg){if(!filteredD.length){$('#table-container').html(`<div class="no-data-msg" style="position:relative;min-height:200px;background:transparent;"><i class="fa-solid fa-circle-info empty-state-icon"></i><div class="empty-state-title">${msg||"No data available for this Exception"}</div></div>`);return;}let h='<table><thead><tr>';rawC.forEach(c=>h+=`<th>${c}</th>`);h+='</tr></thead><tbody>';filteredD.slice(0,100).forEach(r=>{h+='<tr>';rawC.forEach(c=>h+=`<td>${r[c]!==null&&r[c]!==undefined?r[c]:''}</td>`);h+='</tr>';});h+='</tbody></table>';$('#table-container').html(h);}
function selObj(id, name, el) {
    if (history.pushState) history.pushState(null, "", "?oid=" + id);
    $('.side-item').removeClass('active'); $(el).addClass('active');
    curID = id; aCfg = CONFIGS[id] || {};
    curExc = aCfg.active_exceptions?.[0]?.id || 1;
    $('#disp-name').text(`${id} | ${name}`);
    buildExcBtns(); 
    const eObj = aCfg.active_exceptions?.[0] || {};
    curExcFilters = eObj.filters || aCfg.filters || [];
    curExcCards = eObj.cards || aCfg.cards || [];
    curExcCharts = eObj.charts || aCfg.charts || [];
    buildKPIs(curExcCards); 
    buildSlicers(curExcFilters); 
    buildChartBoxes(curExcCharts);
    load();
}
function selExc(ex) { 
    curExc = ex; 
    $('.exc-btns button').removeClass('active'); 
    $(`#btn-exc${ex}`).addClass('active'); 
    const eObj = (aCfg.active_exceptions || []).find(e => e.id == ex);
    if (eObj) {
        $('#exc-title').text(eObj.title || '');
        curExcFilters = eObj.filters || aCfg.filters || [];
        curExcCards = eObj.cards || aCfg.cards || [];
        curExcCharts = eObj.charts || aCfg.charts || [];
        buildKPIs(curExcCards); 
        buildSlicers(curExcFilters); 
        buildChartBoxes(curExcCharts);
    }
    load(); 
}

function buildExcBtns(){let h='';(aCfg.active_exceptions||[]).forEach(e=>h+=`<button id="btn-exc${e.id}" class="${e.id==curExc?'active':''}" onclick="selExc('${e.id}')">${e.label}</button>`);$('#exc-btns').html(h);}
function buildKPIs(cards){const arr=cards||aCfg.cards||[];let h='';arr.forEach(c=>h+=`<div class="kpi-card"><div id="${c.id}" class="kpi-val">0</div><div class="kpi-lbl">${c.label}</div></div>`);$('#kpi-row').html(h);}
function buildSlicers(filters){const arr=filters||aCfg.filters||[];let h='';arr.forEach(f=>h+=`<div class="slicer-card"><span class="slicer-lbl">${f.label}</span><select id="${f.id}" onchange="applyFilters()"></select></div>`);h+=`<div class="slicer-card"><div style="display:flex;justify-content:space-between"><span class="slicer-lbl">Date Range</span><div class="date-display"><span id="lbl-min">-</span> to <span id="lbl-max">-</span></div></div><div class="date-slider-wrapper"><div class="slider-container" style="position:relative;width:100%;height:6px;top:6px"><div id="slider-track" style="position:absolute;height:100%;z-index:1"></div><input type="range" id="rng-min" oninput="handleSlider()" style="position:absolute;width:100%;z-index:2;margin:0"><input type="range" id="rng-max" oninput="handleSlider()" style="position:absolute;width:100%;z-index:2;margin:0"></div></div></div><button class="btn-reset" onclick="resetFilters()">Reset</button>`;$('#slicer-row').html(h);}
function buildChartBoxes(charts){const arr=charts||aCfg.charts||[];Object.values(cInst).forEach(c=>c?.destroy());cInst={};let h='';arr.forEach(c=>h+=`<div class="${(c.full_width || c.type === 'line') ? 'chart-box full' : 'chart-box'}" id="box-${c.id}"><canvas id="${c.id}"></canvas></div>`);$('#chart-grid').html(h);}
function handleSlider(){let v1=+$('#rng-min').val(),v2=+$('#rng-max').val();if(v1>v2)$('#rng-min').val(v2);updSliderUI();applyFilters();}
function updSliderUI(){let v1=+$('#rng-min').val(),v2=+$('#rng-max').val(),mx=dateList.length-1;$('#lbl-min').text(dateList[v1]||'-');$('#lbl-max').text(dateList[v2]||'-');if(mx>0)$('#slider-track').css({left:(v1/mx)*100+'%',width:((v2-v1)/mx)*100+'%'});}
function resetFilters(){(curExcFilters||[]).forEach(f=>$('#'+f.id).val('ALL'));setupSlider();applyFilters();}
function isAllFilters(){return(curExcFilters||[]).every(f=>$('#'+f.id).val()==='ALL');}
function downloadCSV(){if(!filteredD.length)return;let csv=rawC.join(',')+\'\\n\';filteredD.forEach(r=>csv+=rawC.map(c=>`"${String(r[c]||'').replace(/"/g,'""')}"`).join(',')+\'\\n\');const b=new Blob([csv],{type:'text/csv'}),l=document.createElement('a');l.href=URL.createObjectURL(b);l.download=`${curID}_Export.csv`;l.click();}
$(document).ready(()=>{const p=new URLSearchParams(window.location.search),o=p.get('oid');if(o){const t=$(`.side-item[data-id="${o}"]`);if(t.length)selObj(o,t.data('name'),t[0]);}else $('.side-item').first().click();});
</script>
</body>
</html>
    """

def get_chart_title(x, y=None, type='bar', top_n=None):
    """Generates a standardized chart title."""
    title = f"{y} by {x}" if y else f"{x} Distribution"
    if top_n:
        title = f"Top {top_n} {title}"
    return title.upper()

def get_exception_title(label):
    """Generates a standardized exception definition title."""
    return f"{label}".upper()
