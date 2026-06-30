# Supplier/master_data/template.py
# -------------------------------------------------------------
# TEMPLATE ENGINE — Aegean Sea Theme for Master Data Insights
# -------------------------------------------------------------

def get_chart_title(x, y=None, type='bar', top_n=None):
    """Generates a standardized chart title."""
    title = f"{y} by {x}" if y else f"{x} Distribution"
    if top_n:
        title = f"Top {top_n} {title}"
    return title.upper()

def get_exception_title(label):
    """Generates a standardized exception definition title."""
    return f"{label}".upper()

def get_html():
    return r"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            /* Aegean Sea Palette Mapping */
            --bg-main: #F4F9FB;           /* Very Light background */
            --side-bg: #1E4D6B;           /* Deep Navy (First Swatch) */
            --side-hover: #2A6183;        /* Dark Blue (Second Swatch) */
            --card-bg: #ffffff;
            --accent: #36759B;            /* Steel Blue (Third Swatch) */
            --text-main: #000000;         /* Changed to Black as requested */
            --text-light: #FFFFFF;
            --kpi-blue: #2A6183;          /* Dark Blue */
            --slider-track: #4E9DCB;      /* Bright Blue (Last Swatch) */
            --border-light: #4289B3;      /* Mid Blue (Fourth Swatch) */
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin: 0; display: flex; height: 100vh;
            background: var(--bg-main);
            overflow: hidden; color: var(--text-main);
        }

        .sidebar {
            width: 280px; background: var(--side-bg); color: var(--text-light);
            display: flex; flex-direction: column; flex-shrink: 0; z-index: 100;
            overflow: hidden; /* Removed sidebar scrollbar */
        }

        .side-header {
            padding: 20px 15px;
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box;
        }

        .side-header i { font-size: 18px; color: var(--text-light); flex-shrink: 0; }

        .logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            background: rgba(255, 255, 255, 0.9);
            padding: 8px 12px;
            border-radius: 12px;
            flex-grow: 1;
            max-width: 210px;
        }

        .logo-container img {
            height: 20px;
            width: auto;
            object-fit: contain;
        }

        .obj-list { flex-grow: 1; overflow-y: auto; padding-left: 15px; }
        
        /* Hide scrollbar for Chrome, Safari and Opera */
        .obj-list::-webkit-scrollbar { display: none; }
        /* Hide scrollbar for IE, Edge and Firefox */
        .obj-list { -ms-overflow-style: none; scrollbar-width: none; }

        .side-item {
            position: relative; padding: 12px 20px; margin: 4px 0;
            border-radius: 30px 0 0 30px; cursor: pointer; font-size: 11px;
            color: #C1E1F5; transition: all 0.2s ease; font-weight: 600;
        }
        .side-item:hover { color: #fff; background: var(--side-hover); }

        .side-item.active { background: var(--bg-main); color: var(--side-bg); font-weight: 800; }

        .side-item.active::before {
            content: ""; position: absolute; background: transparent; top: -20px; right: 0; height: 20px; width: 20px;
            border-bottom-right-radius: 20px; box-shadow: 5px 5px 0 5px var(--bg-main);
        }
        .side-item.active::after {
            content: ""; position: absolute; background: transparent; bottom: -20px; right: 0; height: 20px; width: 20px;
            border-top-right-radius: 20px; box-shadow: 5px -5px 0 5px var(--bg-main);
        }

        .main { flex-grow: 1; overflow-y: auto; padding: 25px 40px; }
        .top-nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; }

        #disp-name {
            margin:0;
            font-size: 24px;
            font-weight: 900;
            color: #000000; /* Set to Black */
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        .exc-btns { display: flex; gap: 8px; }
        .exc-btns button {
            padding: 8px 18px; border-radius: 8px; border: 1px solid var(--border-light);
            background: var(--card-bg); font-size: 11px; font-weight: 700; cursor: pointer; color: var(--side-bg);
        }
        .exc-btns button.active { background: var(--side-bg); color: white; border-color: var(--side-bg); }

        .kpi-row { display: grid; grid-template-columns: repeat(6, 1fr); gap: 15px; margin-bottom: 25px; }
        .kpi-card:hover { transform: translateY(-3px); box-shadow: 0 0 15px var(--accent); cursor: pointer; }
        .kpi-card { box-shadow: inset 0 0 15px rgba(255,255,255,0.1); 
            background: var(--kpi-blue); padding: 25px 10px; border-radius: 25px;
            text-align: center; color: white; border: none;
            min-height: 80px; display: flex; flex-direction: column; justify-content: center;
        }
        .kpi-val { font-size: 20px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.5px; }
        .kpi-lbl { font-size: 10px; color: #BDEFFF; text-transform: uppercase; font-weight: 700; margin-top: 8px; opacity: 0.9; }

        .slicer-row { display: grid; grid-template-columns: 1fr 1fr 1fr 1.6fr 0.8fr; gap: 15px; margin-bottom: 25px; align-items: end; }
        .slicer-card {
            background: var(--card-bg); padding: 12px 15px; border-radius: 10px;
            border: 1px solid var(--border-light); height: 60px; display: flex; flex-direction: column; justify-content: center;
        }
        .slicer-lbl { font-size: 9px; color: var(--side-bg); text-transform: uppercase; font-weight: 800; margin-bottom: 5px; }

        select {
            width: 100%; border: none; font-size: 11px; padding: 5px 0;
            background: transparent; outline: none; color: #000; font-weight: 600; cursor: pointer;
        }

        .date-display { font-size: 10px; font-weight: 800; color: var(--side-bg); }

        .btn-reset {
            height: 40px; background: var(--side-bg); color: var(--text-light); border: none;
            font-size: 10px; font-weight: 800; border-radius: 10px; cursor: pointer; text-transform: uppercase;
        }

        .chart-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 30px; }
        .chart-box {
            background: white; padding: 15px; border-radius: 15px; height: 360px;
            position: relative; display: flex; flex-direction: column;
            border: 4px solid var(--side-bg);
            overflow: hidden;
        }
        .full { grid-column: span 2; }

        .no-data-msg {
            position: absolute; inset: 4px; background: #F0FBFF;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            font-size: 13px; font-weight: 700; color: var(--side-bg);
            border-radius: 11px;
            text-align: center;
            padding: 20px;
        }

        .table-box { background: var(--card-bg); padding: 25px; border-radius: 15px; margin-bottom: 50px; border: 2px solid var(--border-light);}
        .table-header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .btn-download {
            background: var(--side-bg); color: white; border: none; padding: 8px 15px;
            border-radius: 8px; cursor: pointer; font-size: 11px; font-weight: 700;
            display: flex; align-items: center; gap: 8px; transition: 0.2s;
        }
        .btn-download:hover { background: var(--slider-track); }

        .table-wrapper { max-height: 500px; overflow-y: auto; border-radius: 8px; background: white; }
        table { width: 100%; border-collapse: collapse; font-size: 12px; }
        th { background: var(--side-bg); color: var(--text-light); padding: 15px; text-align: left; position: sticky; top: 0; }
        td { padding: 12px 15px; border-bottom: 1px solid #e1f5f9; color: #000; }

        .date-slider-wrapper .slider-container { background: #D1E9F6 !important; }
        #slider-track { background: var(--slider-track) !important; }
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
            <div class="side-item" data-id="{{ obj.id }}" data-name="{{ obj.o }}" onclick="selObj('{{ obj.id }}', '{{ obj.o }}', this)">{{ obj.id }} - {{ obj.o }}</div>
            {% endfor %}
        </div>
    </div>
    <div class="main">
        <div class="top-nav">
            <div>
                <h2 id="disp-name">{{ page_title }}</h2>
                <h4 id="exc-title" style="margin: 5px 0 0 0; font-size: 13px; color: var(--accent); font-weight: 700; text-transform: uppercase; opacity: 0.8;"></h4>
            </div>
            <div class="exc-btns" id="exc-btns"></div>
        </div>

        <div class="kpi-row" id="kpi-row"></div>
        <div class="slicer-row" id="slicer-row"></div>
        <div class="chart-grid" id="chart-grid"></div>

        <div class="table-box">
            <div class="table-header-flex">
                <h3 style="font-size: 15px; margin: 0; font-weight: 800; color: var(--side-bg);">Detailed Master Data Log</h3>
                <button class="btn-download" onclick="downloadCSV()"><i class="fa-solid fa-file-csv"></i> Download Data</button>
            </div>
            <div class="table-wrapper" id="table-container"></div>
        </div>
    </div>

    <script>
        const CONFIGS = {{ configs|safe }};
        let rawD = [], rawC = [], filteredD = [], charts = {}, curID = '', curExc = 1, dateList = [];
        let backendStats = null;
        let aCfg = null, colCache = {};
        let curExcFilters = [], curExcCards = [], curExcCharts = [];

        /* Aegean Sea Chart Palette */
        const CHART_COLORS = ['#1E4D6B', '#2A6183', '#36759B', '#4289B3', '#4E9DCB', '#7FBADC', '#A3D1E9'];

        const MAP = {
            amount: ['amount','Amount in Local Currency','Invoice Amount Paid', 'amount in lc', 'amount in local currency', 'amount in document currency', 'net value', 
            'total value', 'sum(amount_lc)', 'debit', 'credit', 'total debit', 'total credit', 'net outstanding', 'open_balance', 'total_amount', 'total unadjusted advance amount'],
            vendor: ['vendor name', 'vendor_name', 'name1', 'vendor', 'name 1', 'vendor code', 'vendor number', 'account number vendor', 'name1_ven', 'name1_vendor', 'offacc_name', 'vendor code', 'Vendor Code'],
            date: ['posting date','Creation date of the change document (Change 2)','Date the Payment was Made', 'posting date in the document', 'posting_date', 'document date', 'document date in document',
            'created on','Created On', 'date on which the record was created', 'Creation date of the change document', 'clearing date', 'last_posting_date', 'invoice date','Employee Created on','Vendor Created on'],
            city: ['city', 'company city', 'vendor city', 'district', 'region', 'vendor region', 'vendor district'],
            company: ['company name', 'company_name', 'name of company', 'company code', 'Company Code','company description','Company Code_ven','Company Code_Cus', 'company description'],
            record: ['document number', 'accounting document number', 'document_number', 'fiscal year', 'transaction_count'],
            days: ['difference', 'days difference', 'days_difference', 'diff_days', 'months_inactive', 'overdue_days'],
            account_group: ['account group', 'vendor account group', 'account_group', 'cust account group', 'offacc_grp','Employee Account group'],
            plant: ['plant', 'plant code', 'plant name'],
            customer: ['customer name', 'customer name1', 'customer code', 'customer number', 'Customer Number'],
            country: ['country', 'vendor country', 'vendor_country', 'country key'],
            fiscal: ['fiscal year', 'gjahr']
        };

        const defaultCards = [
            { id: 'k-comp', label: 'Companies', agg: 'unique', source: 'company' },
            { id: 'k-vend', label: 'Vendors', agg: 'unique', source: 'vendor' },
            { id: 'k-rec', label: 'Records', agg: 'row_count' },
            { id: 'k-val', label: 'Total Value', agg: 'total_value', source: 'amount', format: 'currency' },
            { id: 'k-days', label: 'Avg Days', agg: 'avg', source: 'days' },
            { id: 'k-issues', label: 'Critical Issues', agg: 'row_count' }
        ];

        const defaultFilters = [
            { id: 'sel-comp', label: 'Company', source: 'company' },
            { id: 'sel-vend', label: 'Vendor', source: 'vendor' },
            { id: 'sel-city', label: 'City', source: 'city' }
        ];

        const defaultCharts = [
            { id: 'chartPie', type: 'pie', x: 'vendor', agg: 'count', top_n: 5, title: 'TOP 5 VENDORS (RECORD COUNT)', legend: true },
            { id: 'chartBar', type: 'bar', x: 'company', agg: 'count', top_n: 10, horizontal: true, title: 'TOP 10 COMPANIES (RECORD COUNT)' },
            { id: 'chartLine', type: 'line', x: 'date', agg: 'count', time_group: 'month', title: 'MONTHLY ACTIVITY TREND' },
            { id: 'chartDonut', type: 'doughnut', x: 'account_group', agg: 'count', title: 'ACCOUNT GROUP DISTRIBUTION', legend: true },
            { id: 'chartCol', type: 'bar', x: 'city', agg: 'count', top_n: 10, title: 'TOP 10 CITIES (RECORD COUNT)' }
        ];

        function parseNum(val) {
            if (val === null || val === undefined || val === '') return 0;
            if (typeof val === 'number') return val;
            const clean = String(val).replace(/[^0-9.-]/g, '');
            const num = parseFloat(clean);
            return isNaN(num) ? 0 : num;
        }

        function formatCompact(num, isCurrency = false) {
            if (num === 0) return isCurrency ? '₹0' : '0';
            let suffix = ''; let val = Math.abs(num);
            if (val >= 10000000) { val = num / 10000000; suffix = 'Cr'; }
            else if (val >= 100000) { val = num / 100000; suffix = 'L'; }
            else { val = num; }
            let res = parseFloat(val.toFixed(2)).toString() + suffix;
            if (num < 0) res = '-' + res;
            return isCurrency ? '₹' + res : res;
        }

        function rCol(source) {
            if (colCache[source]) return colCache[source];
            const candidates = aCfg?.columns?.[source] || MAP[source];
            if (!candidates) return null;
            const normalizedHeaders = rawC.map(c => c.trim().toLowerCase());
            for (const cand of candidates) {
                const idx = normalizedHeaders.indexOf(cand.trim().toLowerCase());
                if (idx !== -1) { colCache[source] = rawC[idx]; return rawC[idx]; }
            }
            return null;
        }

        function buildExcBtns() {
            let h = '';
            (aCfg.active_exceptions || []).forEach(e => {
                h += `<button id="btn-exc${e.id}" class="${e.id == curExc ? 'active' : ''}" onclick="selExc('${e.id}')">${e.label}</button>`;
            });
            $('#exc-btns').html(h);
        }

        function buildExcBtnsStatic() {
            let h = '';
            for (let i = 1; i <= 7; i++) {
                h += `<button id="btn-exc${i}" class="${i == curExc ? 'active' : ''}" onclick="selExc(${i})">Exception 0${i}</button>`;
            }
            $('#exc-btns').html(h);
        }

        function buildKPIs(cards) {
            let h = '';
            cards.forEach(c => {
                h += `<div class="kpi-card"><div id="${c.id}" class="kpi-val">0</div><div class="kpi-lbl">${c.label}</div></div>`;
            });
            $('#kpi-row').html(h);
        }

        function buildSlicers(filters) {
            let h = '';
            filters.forEach(f => {
                h += `<div class="slicer-card"><span class="slicer-lbl">${f.label}</span><select id="${f.id}" onchange="applyFilters()"></select></div>`;
            });
            h += `<div class="slicer-card">
                    <div style="display:flex; justify-content: space-between;">
                        <span class="slicer-lbl">Date Range</span>
                        <div class="date-display"><span id="lbl-min">-</span> to <span id="lbl-max">-</span></div>
                    </div>
                    <div class="date-slider-wrapper">
                        <div class="slider-container" style="position: relative; width: 100%; height: 6px; background: #C1E8FF; border-radius: 10px; top: 6px;">
                            <div id="slider-track" style="position: absolute; height: 100%; background: var(--side-bg); border-radius: 10px; z-index: 1;"></div>
                            <input type="range" id="rng-min" step="1" oninput="handleSlider()" style="position: absolute; width: 100%; pointer-events: none; -webkit-appearance: none; background: none; top: -3px; z-index: 2; margin: 0;">
                            <input type="range" id="rng-max" step="1" oninput="handleSlider()" style="position: absolute; width: 100%; pointer-events: none; -webkit-appearance: none; background: none; top: -3px; z-index: 2; margin: 0;">
                        </div>
                    </div>
                  </div>
                  <button class="btn-reset" onclick="resetFilters()">Reset Filters</button>`;
            $('#slicer-row').html(h);
        }

        function buildChartBoxes(chartsList) {
            Object.values(charts).forEach(c => c?.destroy());
            charts = {};
            let h = '';
            chartsList.forEach(c => {
                h += `<div class="${(c.full_width || c.type === 'line') ? 'chart-box full' : 'chart-box'}" id="box-${c.id}"><canvas id="${c.id}"></canvas></div>`;
            });
            $('#chart-grid').html(h);
        }

        function selObj(id, name, el) {
            if (history.pushState) history.pushState(null, "", "?oid=" + id);
            $('.side-item').removeClass('active'); $(el).addClass('active');
            curID = id; 
            $('#disp-name').text(id + ' | ' + name);

            aCfg = CONFIGS[id] || {};
            colCache = {};

            if (aCfg && Object.keys(aCfg).length > 0) {
                curExc = aCfg.active_exceptions?.[0]?.id || 1;
                const eObj = aCfg.active_exceptions?.[0] || {};
                $('#exc-title').text(eObj.title || '');
                curExcFilters = eObj.filters || aCfg.filters || [];
                curExcCards = eObj.cards || aCfg.cards || [];
                curExcCharts = eObj.charts || aCfg.charts || [];
                
                buildExcBtns();
                buildKPIs(curExcCards);
                buildSlicers(curExcFilters);
                buildChartBoxes(curExcCharts);
            } else {
                curExc = 1;
                $('#exc-title').text('');
                curExcFilters = defaultFilters;
                curExcCards = defaultCards;
                curExcCharts = defaultCharts;

                buildExcBtnsStatic();
                buildKPIs(defaultCards);
                buildSlicers(defaultFilters);
                buildChartBoxes(defaultCharts);
            }
            load();
        }

        function selExc(ex) {
            curExc = ex;
            $('.exc-btns button').removeClass('active');
            $('#btn-exc' + ex).addClass('active');

            if (aCfg && Object.keys(aCfg).length > 0) {
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
            } else {
                $('#exc-title').text('');
                buildKPIs(defaultCards);
                buildSlicers(defaultFilters);
                buildChartBoxes(defaultCharts);
            }
            load();
        }

        async function load() {
            if(!curID) return;
            $('#table-container').html('<p style="padding:20px;">Loading data...</p>');
            try {
                const r = await fetch(`./api/${curID}/${curExc}?t=${new Date().getTime()}`);
                const d = await r.json();
                if(d.success) {
                    rawD = d.rows || []; rawC = d.cols || [];
                    backendStats = d.full_stats || null;
                    setupSlider(); populateSlicers(); applyFilters();
                } else { 
                    rawD = []; rawC = []; filteredD = [];
                    updateKPIs(); updateCharts(); renderTable();
                }
            } catch(e) { console.error(e); }
        }

        function setupSlider() {
            let dc = rCol('date');
            if(!dc) {
                $('#lbl-min').text('-'); $('#lbl-max').text('-');
                $('#slider-track').css({ width: '0%' });
                return;
            }
            dateList = [...new Set(rawD.map(r => r[dc]))].filter(x => x && !isNaN(new Date(x))).sort((a,b) => new Date(a) - new Date(b));
            if(dateList.length > 0) {
                $('#rng-min').attr({min:0, max:dateList.length-1}).val(0);
                $('#rng-max').attr({min:0, max:dateList.length-1}).val(dateList.length-1);
                updSliderUI();
            } else {
                $('#lbl-min').text('-'); $('#lbl-max').text('-');
                $('#slider-track').css({ width: '0%' });
            }
        }

        function handleSlider() {
            let v1 = parseInt($('#rng-min').val()), v2 = parseInt($('#rng-max').val());
            if(v1 > v2) { $('#rng-min').val(v2); }
            updSliderUI(); applyFilters();
        }

        function updSliderUI() {
            let v1 = parseInt($('#rng-min').val()), v2 = parseInt($('#rng-max').val()), max = dateList.length - 1;
            $('#lbl-min').text(dateList[v1] || '-'); $('#lbl-max').text(dateList[v2] || '-');
            if (max > 0) {
                let p1 = (v1/max)*100, p2 = (v2/max)*100;
                $('#slider-track').css({left: p1+'%', width: (p2-p1)+'%'});
            } else {
                $('#slider-track').css({left: '0%', width: '0%'});
            }
        }

        function populateSlicers() {
            curExcFilters.forEach(f => {
                let col = rCol(f.source), sel = $('#' + f.id);
                sel.html(`<option value="ALL">All ${f.label}s</option>`);
                if (col && rawD.length > 0) {
                    let u = [...new Set(rawD.map(r => r[col]))].filter(x => x).sort();
                    u.forEach(v => sel.append(`<option value="${v}">${v}</option>`));
                }
            });
        }

        function applyFilters() {
            if (aCfg && Object.keys(aCfg).length > 0) {
                const dC = rCol('date');
                const minD = dateList.length > 0 ? new Date(dateList[parseInt($('#rng-min').val())]) : null;
                const maxD = dateList.length > 0 ? new Date(dateList[parseInt($('#rng-max').val())]) : null;
                const activeFilters = (curExcFilters || [])
                    .map(f => ({ col: rCol(f.source), val: $('#' + f.id).val() }))
                    .filter(f => f.col && f.val !== 'ALL');

                filteredD = rawD.filter(r => {
                    for (const f of activeFilters) { if (String(r[f.col]) !== f.val) return false; }
                    if (dC && minD && maxD) {
                        const d = new Date(r[dC]);
                        if (isNaN(d) || d < minD || d > maxD) return false;
                    }
                    return true;
                });
            } else {
                const cC = rCol('company'), vC = rCol('vendor'), cityC = rCol('city'), dC = rCol('date');
                const sC = $('#sel-comp').val(), sV = $('#sel-vend').val(), sCity = $('#sel-city').val();
                const minD = dateList.length > 0 ? new Date(dateList[parseInt($('#rng-min').val())]) : null;
                const maxD = dateList.length > 0 ? new Date(dateList[parseInt($('#rng-max').val())]) : null;

                filteredD = rawD.filter(r => {
                    let d = new Date(r[dC]);
                    return (sC === 'ALL' || r[cC] == sC) && 
                           (sV === 'ALL' || r[vC] == sV) && 
                           (sCity === 'ALL' || r[cityC] == sCity) && 
                           (!dC || !minD || (d >= minD && d <= maxD));
                });
            }

            updateKPIs();
            updateCharts();
            renderTable();
        }

        function updateKPIs() {
            if (aCfg && Object.keys(aCfg).length > 0) {
                const isAllSelected = (curExcFilters || []).every(f => $('#' + f.id).val() === 'ALL');
                (curExcCards || []).forEach(card => {
                    let val = 0;
                    if (!filteredD || filteredD.length === 0) {
                        $('#' + card.id).text(card.format === 'currency' ? '₹0' : '0');
                        return;
                    }
                    const sourceCol = card.source ? rCol(card.source) : null;
                    if (card.agg === 'row_count') val = filteredD.length;
                    else if (card.agg === 'total_rows') val = (backendStats && isAllSelected && !card.source) ? backendStats.total_rows : filteredD.length;
                    else if (card.agg === 'total_value') {
                        if (backendStats && isAllSelected && card.source === 'amount') val = backendStats.total_value;
                        else if (sourceCol) val = filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0);
                    }
                    else if (card.agg === 'sum') {
                        val = sourceCol ? filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0) : 0;
                    }
                    else if (card.agg === 'unique') {
                        val = sourceCol ? new Set(filteredD.map(r => r[sourceCol]).filter(v => v !== '')).size : 0;
                    }
                    else if (card.agg === 'avg') {
                        if (filteredD.length === 0) val = 0;
                        else {
                            let sum = sourceCol ? filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0) : 0;
                            val = sum / filteredD.length;
                        }
                    }
                    $('#' + card.id).text(card.format === 'currency' ? formatCompact(val, true) : (card.agg === 'avg' ? val.toFixed(1) : val.toLocaleString('en-IN')));
                });
            } else {
                const sum = (k) => {
                    let c = rCol(k); if (!c) return 0;
                    return filteredD.reduce((a, b) => a + (parseFloat(String(b[c]).replace(/[^0-9.-]/g, '')) || 0), 0);
                };
                const avg = (k) => {
                    let c = rCol(k); if (!c) return 0;
                    let vals = filteredD.map(r => parseFloat(String(r[c]).replace(/[^0-9.-]/g, '')) || 0).filter(v => v > 0);
                    return vals.length > 0 ? vals.reduce((a,b) => a+b, 0) / vals.length : 0;
                };
                const unq = (k) => { let c=rCol(k); return c ? [...new Set(filteredD.map(r=>r[c]))].length : 0; };

                let isAllSelected = ($('#sel-comp').val() === 'ALL' && $('#sel-vend').val() === 'ALL' && $('#sel-city').val() === 'ALL');

                if (backendStats && isAllSelected) {
                    $('#k-val').text(formatCompact(backendStats.total_value, true));
                    $('#k-rec').text(backendStats.total_rows);
                } else {
                    $('#k-val').text(formatCompact(sum('amount'), true));
                    $('#k-rec').text(filteredD.length);
                }

                $('#k-comp').text(unq('company'));
                $('#k-vend').text(unq('vendor'));
                $('#k-days').text(Math.round(avg('days')));
                $('#k-issues').text(filteredD.length);
            }
        }

        function renderChartOrMessage(canvasId, config, condition) {
            const box = $(`#box-${canvasId}`);
            box.find('.no-data-msg').remove();
            box.find('.chart-total-label').remove();
            if (charts[canvasId]) charts[canvasId].destroy();

            if (!condition) {
                $(`#${canvasId}`).hide();
                box.append('<div class="no-data-msg">No data available for this exception</div>');
                return null;
            } else {
                $(`#${canvasId}`).show();
                charts[canvasId] = new Chart(document.getElementById(canvasId), config);
                return charts[canvasId];
            }
        }

        function handleChartError(canvasId, box, msg = "No data available") {
            $(`#${canvasId}`).hide();
            box.append(`<div class="no-data-msg">${msg}</div>`);
        }

        function renderChartJS(cfg, labels, values) {
            const ctx = document.getElementById(cfg.id);
            const isHorizontal = cfg.horizontal === true;
            const config = {
                type: cfg.type === 'doughnut' ? 'doughnut' : 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: cfg.y ? cfg.y.toUpperCase() : 'COUNT',
                        data: values,
                        backgroundColor: cfg.type === 'doughnut' ? CHART_COLORS : '#36759B',
                        borderWidth: cfg.type === 'doughnut' ? 0.5 : 0,
                        borderRadius: cfg.type === 'doughnut' ? 0 : 5
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    indexAxis: isHorizontal ? 'y' : 'x',
                    plugins: {
                        title: {
                            display: true,
                            text: cfg.title ? cfg.title.toUpperCase() : 'CHART',
                            color: '#000000',
                            font: { size: 14, weight: '800', family: "'Plus Jakarta Sans', sans-serif" }
                        },
                        legend: {
                            display: cfg.legend === true,
                            position: 'bottom',
                            labels: { color: '#1E4D6B', font: { size: 8, weight: '600' }, boxWidth: 10, padding: 10 }
                        }
                    },
                    scales: cfg.type === 'doughnut' ? {} : {
                        x: {
                            grid: { display: false },
                            ticks: {
                                color: '#1E4D6B',
                                font: { size: 8, weight: '600' },
                                maxRotation: isHorizontal ? 0 : 45,
                                minRotation: isHorizontal ? 0 : 45,
                                callback: function(value) {
                                    let label = this.getLabelForValue(value);
                                    if (!isHorizontal && label.length > 12) return label.substring(0, 10) + '...';
                                    return label;
                                }
                            }
                        },
                        y: {
                            grid: { display: false },
                            ticks: { color: '#1E4D6B', font: { size: 8 } }
                        }
                    }
                }
            };
            if (cfg.type === 'line') {
                config.type = 'line';
                config.data.datasets[0].borderColor = '#1E4D6B';
                config.data.datasets[0].tension = 0.4;
                config.data.datasets[0].fill = true;
                config.data.datasets[0].backgroundColor = 'rgba(78, 157, 203, 0.1)';
                config.data.datasets[0].pointRadius = 4;
            }
            charts[cfg.id] = new Chart(ctx, config);
        }

        function updateCharts() {
            if (aCfg && Object.keys(aCfg).length > 0) {
                if (!curExcCharts || curExcCharts.length === 0) return;
                curExcCharts.forEach(cfg => {
                    const box = $('#box-' + cfg.id);
                    box.find('.no-data-msg').remove();
                    box.find('.chart-total-label').remove();
                    if (charts[cfg.id]) charts[cfg.id].destroy();

                    const xCol = rCol(cfg.x), yCol = rCol(cfg.y);
                    
                    if (!xCol) { handleChartError(cfg.id, box, `Column '${cfg.x}' not found`); return; }
                    if (!filteredD.length) { handleChartError(cfg.id, box, "No data matching filters"); return; }

                    let data = {};
                    if (cfg.time_group === 'month') {
                        filteredD.forEach(r => {
                            const o = new Date(r[xCol]);
                            if (!isNaN(o)) {
                                const k = o.toLocaleString('default', { month: 'short', year: 'numeric' });
                                data[k] = (data[k] || 0) + (yCol ? parseNum(r[yCol]) : 1);
                            }
                        });
                        const sk = Object.keys(data).sort((a, b) => new Date(a) - new Date(b));
                        data = Object.fromEntries(sk.map(k => [k, data[k]]));
                    } else {
                        filteredD.forEach(r => {
                            const k = r[xCol] || 'N/A';
                            data[k] = (data[k] || 0) + (cfg.agg === 'count' ? 1 : parseNum(r[yCol]));
                        });
                        if (cfg.top_n) data = Object.fromEntries(Object.entries(data).sort((a, b) => b[1] - a[1]).slice(0, cfg.top_n));
                    }
                    const labels = Object.keys(data), values = Object.values(data);
                    if (!labels.length) { handleChartError(cfg.id, box); return; }
                    $('#' + cfg.id).show();
                    let totalChartVal = values.reduce((a,b)=>a+Number(b),0);
                    box.append(`<div class="chart-total-label" style="position: absolute; bottom: 15px; left: 15px; font-weight: 800; font-size: 11px; color: var(--side-bg); z-index: 5; background: rgba(255,255,255,0.8); padding: 2px 6px; border-radius: 4px;">Total: ${formatCompact(totalChartVal, false)}</div>`);
                    
                    renderChartJS(cfg, labels, values);
                });
            } else {
                const mC = rCol('amount');
                const getAgg = (col, isVal=true) => {
                    let res = {}; filteredD.forEach(r => {
                        let k = r[col] || 'Other';
                        let v = isVal && mC ? (parseFloat(String(r[mC]).replace(/[^0-9.-]/g,""))||0) : 1;
                        res[k] = (res[k]||0)+v;
                    });
                    return res;
                };

                const opt = (title) => ({
                    responsive: true, maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: title, color: '#000000', font: {size: 15, weight: '800', family: "'Plus Jakarta Sans', sans-serif"}},
                        legend: { display: false }
                    },
                    scales: {
                        x: {
                            display: true, grid: { display: false },
                            ticks: {
                                color: '#1E4D6B', font: {size: 9, weight: '600'},
                                callback: function(value) {
                                    let label = this.getLabelForValue(value);
                                    if (label.length > 12) return label.substring(0, 10) + '...';
                                    return label;
                                }
                            }
                        },
                        y: { display: true, grid: { display: false }, ticks: { color: '#1E4D6B', font: {size: 9} } }
                    }
                });

                let vCol = rCol('vendor');
                let topValData = vCol ? getAgg(vCol, false) : {};
                let topVal = Object.entries(topValData).sort((a,b)=>b[1]-a[1]).slice(0,5);
                let hasVData = topVal.length > 0 && topVal.some(x => x[1] > 0);
                renderChartOrMessage('chartPie', {
                    type:'pie',
                    data:{ labels:topVal.map(x=>x[0]), datasets:[{data:topVal.map(x=>x[1]), backgroundColor:CHART_COLORS, borderWidth: 0.5}] },
                    options: {
                        responsive: true, maintainAspectRatio: false,
                        plugins: {
                            title: { display: true, text: 'TOP 5 VENDORS (RECORD COUNT)', color: '#000000', font: {size: 15, weight: '800', family: "'Plus Jakarta Sans', sans-serif"}},
                            legend: { display: true, position: 'bottom', labels: { color: '#1E4D6B', font: {size: 8, weight: '600'}, boxWidth: 10, padding: 10 } }
                        }
                    }
                }, hasVData);

                let cpC = rCol('company');
                let topComp = cpC ? getAgg(cpC, false) : {};
                let topCompData = Object.entries(topComp).sort((a,b)=>b[1]-a[1]).slice(0,10);
                let hasCompData = topCompData.length > 0 && topCompData.some(x => x[1] > 0);
                renderChartOrMessage('chartBar', {
                    type:'bar',
                    data:{ labels: topCompData.map(x => x[0]), datasets:[{label:'Count', data: topCompData.map(x => x[1]), backgroundColor: '#4289B3', borderRadius: 5}] },
                    options: {
                        ...opt('TOP 10 COMPANIES (RECORD COUNT)'),
                        indexAxis: 'y',
                        scales: {
                            x: { display: true, grid: { display: false }, ticks: { display: false } },
                            y: { display: true, grid: { display: false }, ticks: { font: {size: 8}, color: '#1E4D6B', callback: function(value) { let label = this.getLabelForValue(value); if (label.length > 15) return label.substring(0, 13) + '..'; return label; } } }
                        }
                    }
                }, hasCompData);

                let dtC = rCol('date');
                let trendData = {};
                if(dtC) {
                    filteredD.forEach(r => {
                        let dStr = r[dtC];
                        if(dStr) {
                            let dateObj = new Date(dStr);
                            if(!isNaN(dateObj)) {
                                let key = dateObj.toLocaleString('default', { month: 'short', year: 'numeric' });
                                trendData[key] = (trendData[key]||0) + 1;
                            }
                        }
                    });
                }
                let sortedKeys = Object.keys(trendData).sort((a,b) => new Date(a) - new Date(b));
                let hasTrendData = sortedKeys.length > 0 && Object.values(trendData).some(v => v > 0);
                renderChartOrMessage('chartLine', {
                    type:'line',
                    data:{ labels: sortedKeys, datasets:[{label:'Activity', data:sortedKeys.map(k=>trendData[k]), borderColor: '#1E4D6B', tension:0.4, fill: true, backgroundColor:'rgba(78, 157, 203, 0.1)', pointRadius: 4}] },
                    options: opt('MONTHLY ACTIVITY TREND')
                }, hasTrendData);

                let acctGrpC = rCol('account_group');
                let acctGrpData = acctGrpC ? getAgg(acctGrpC, false) : {};
                let hasAcctGrpData = Object.keys(acctGrpData).length > 0 && Object.values(acctGrpData).some(v => v > 0);
                renderChartOrMessage('chartDonut', {
                    type:'doughnut',
                    data:{ labels:Object.keys(acctGrpData), datasets:[{data:Object.values(acctGrpData), backgroundColor:CHART_COLORS, borderWidth: 0.5}] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { title: { display: true, text: 'ACCOUNT GROUP DISTRIBUTION', color: '#000000', font: {size: 15, weight: '800'}}, legend: { display: true, position: 'bottom', labels: { color: '#1E4D6B', font: {size: 8, weight: '600'}, boxWidth: 10, padding: 10 } } } }
                }, hasAcctGrpData);

                let cityCol = rCol('city');
                let cityDataRaw = cityCol ? getAgg(cityCol, false) : {};
                let topCity = Object.entries(cityDataRaw).sort((a,b)=>b[1]-a[1]).slice(0,10);
                let hasCityData = topCity.length > 0 && topCity.some(x => x[1] > 0);
                renderChartOrMessage('chartCol', {
                    type:'bar', data:{ labels:topCity.map(x=>x[0]), datasets:[{label:'Count', data:topCity.map(x=>x[1]), backgroundColor: '#4E9DCB', borderRadius: 5}] },
                    options: { ...opt('TOP 10 CITIES (RECORD COUNT)'), scales: { x: { grid: { display: false }, ticks: { maxRotation: 45, minRotation: 45, color: '#1E4D6B', font: {size: 8}, callback: function(value) { let label = this.getLabelForValue(value); if (label.length > 12) return label.substring(0, 10) + '..'; return label; } } }, y: { grid: { display: false }, ticks: { font: {size: 8}, color: '#1E4D6B' } } } }
                }, hasCityData);
            }
        }

        function renderTable() {
            let html = '<table><thead><tr>';
            rawC.forEach(c => html += `<th>${c}</th>`);
            html += '</tr></thead><tbody>';
            filteredD.slice(0, 100).forEach(r => {
                html += '<tr>'; rawC.forEach(c => html += `<td>${r[c] !== null && r[c] !== undefined ? r[c] : ''}</td>`); html += '</tr>';
            });
            html += '</tbody></table>';
            $('#table-container').html(html);
        }

        function downloadCSV() {
            if (filteredD.length === 0) { alert("No data to download"); return; }
            let csv = rawC.join(',') + '\n';
            filteredD.forEach(row => {
                csv += rawC.map(c => {
                    let cell = String(row[c] !== null && row[c] !== undefined ? row[c] : '').replace(/"/g, '""');
                    return cell.includes(',') ? `"${cell}"` : cell;
                }).join(',') + '\n';
            });
            let blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            let link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.setAttribute("download", `${curID}_Data.csv`);
            document.body.appendChild(link); link.click(); document.body.removeChild(link);
        }

        function resetFilters() {
            curExcFilters.forEach(f => $('#' + f.id).val('ALL'));
            setupSlider(); applyFilters();
        }

        $(document).ready(function() {
            const urlParams = new URLSearchParams(window.location.search);
            const oid = urlParams.get('oid');
            if (oid) {
                const target = $(`.side-item[data-id="${oid}"]`);
                if (target.length > 0) selObj(oid, target.data('name'), target[0]);
            } else {
                $('.side-item').first().click();
            }
        });
    </script>
</body>
</html>
"""
