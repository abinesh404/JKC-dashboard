# Supplier/ITAC/template.py
# -------------------------------------------------------------
# TEMPLATE ENGINE — ITAC Egyptian Blue Theme
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
            --bg: #C1E8FF;
            --sidebar: #021024;
            --sidebar-hover: #052659;
            --card-bg: #f8fdff;
            --accent: #5483B3;
            --text-main: #021024;
            --text-light: #FFFFFF;
            --kpi-bg: #052659;
            --slider-track: #021024;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin: 0;
            display: flex;
            height: 100vh;
            background: var(--bg);
            overflow: hidden;
            color: var(--text-main);
        }
        
        /* Sidebar Navigation */
        .sidebar {
            width: 280px;
            background: var(--sidebar);
            color: #fff;
            display: flex;
            flex-direction: column;
            flex-shrink: 0;
            z-index: 100;
            overflow: hidden;
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
        .side-header i { font-size: 18px; color: var(--accent); flex-shrink: 0; }
        
        .logo-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            background: rgba(255,255,255,0.9);
            padding: 8px 12px;
            border-radius: 12px;
            flex-grow: 1;
            max-width: 210px;
        }
        .logo-container img { height: 20px; width: auto; object-fit: contain; }
        
        .obj-list {
            flex-grow: 1;
            overflow-y: auto;
            padding-left: 15px;
            scrollbar-width: none;
        }
        .obj-list::-webkit-scrollbar { display: none; }
        .side-item {
            position: relative;
            padding: 12px 20px;
            margin: 4px 0;
            border-radius: 30px 0 0 30px;
            cursor: pointer;
            font-size: 11px;
            color: #7DA0CA;
            transition: all 0.2s ease;
            font-weight: 600;
        }
        .side-item:hover { color: #fff; background: var(--sidebar-hover); }
        .side-item.active {
            background: var(--bg);
            color: var(--sidebar);
            font-weight: 800;
        }
        .side-item.active::before {
            content: ""; position: absolute; background: transparent;
            top: -20px; right: 0; height: 20px; width: 20px;
            border-bottom-right-radius: 20px; box-shadow: 5px 5px 0 5px var(--bg);
        }
        .side-item.active::after {
            content: ""; position: absolute; background: transparent;
            bottom: -20px; right: 0; height: 20px; width: 20px;
            border-top-right-radius: 20px; box-shadow: 5px -5px 0 5px var(--bg);
        }

        /* Main Content Area */
        .main {
            flex-grow: 1;
            overflow-y: auto;
            padding: 25px 40px;
        }
        .top-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
        }
        #disp-name {
            margin: 0;
            font-size: 24px;
            font-weight: 900;
            color: var(--text-main);
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }
        
        /* Buttons & Exceptions */
        .exc-btns { display: flex; gap: 8px; }
        .exc-btns button {
            padding: 8px 18px;
            border-radius: 8px;
            border: 1px solid var(--accent);
            background: var(--card-bg);
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            color: var(--sidebar);
            transition: all 0.2s;
        }
        .exc-btns button.active {
            background: var(--sidebar);
            color: #fff;
            border-color: var(--sidebar);
        }

        /* KPI Cards */
        #kpi-row {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 15px;
            margin-bottom: 25px;
        }
        .kpi-card {
            background: var(--kpi-bg);
            padding: 25px 10px;
            border-radius: 25px;
            text-align: center;
            color: #fff;
            min-height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            transition: transform 0.2s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border: none;
        }
        .kpi-card:hover { transform: translateY(-3px); box-shadow: inset 0 0 25px var(--accent), 0 0 15px var(--accent); cursor: pointer; }
        .kpi-val { font-size: 20px; font-weight: 800; color: #FFF; }
        .kpi-lbl {
            font-size: 10px;
            color: #BBDEFB;
            text-transform: uppercase;
            font-weight: 700;
            margin-top: 8px;
            opacity: 0.9;
        }

        /* Slicers */
        #slicer-row {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1.6fr 0.8fr;
            gap: 15px;
            margin-bottom: 25px;
            align-items: end;
        }
        .slicer-card {
            background: var(--card-bg);
            padding: 12px 15px;
            border-radius: 12px;
            border: 1px solid var(--accent);
            height: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(60, 51, 42, 0.05);
            transition: all 0.2s ease;
        }
        .slicer-card:hover { 
            border-color: var(--sidebar);
            box-shadow: 0 6px 15px rgba(60, 51, 42, 0.1);
        }
        .slicer-lbl {
            font-size: 9px;
            color: var(--text-main);
            text-transform: uppercase;
            font-weight: 800;
            margin-bottom: 5px;
        }
        select {
            width: 100%;
            border: none;
            font-size: 11px;
            padding: 5px 0;
            background: transparent;
            outline: none;
            color: var(--text-main);
            font-weight: 600;
            cursor: pointer;
        }
        .date-display { font-size: 10px; font-weight: 800; color: var(--sidebar); }
        .btn-reset {
            height: 40px;
            background: var(--sidebar);
            color: #fff;
            border: none;
            font-size: 10px;
            font-weight: 800;
            border-radius: 12px;
            cursor: pointer;
            text-transform: uppercase;
            transition: opacity 0.2s;
        }
        .btn-reset:hover { opacity: 0.9; }

        /* Charts */
        #chart-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        .chart-box {
            background: #fff;
            padding: 15px;
            border-radius: 20px;
            height: 380px;
            position: relative;
            display: flex;
            flex-direction: column;
            border: 4px solid var(--sidebar);
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(60, 51, 42, 0.08), 0 4px 15px rgba(60, 51, 42, 0.04);
            transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .chart-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 50px rgba(60, 51, 42, 0.15), 0 8px 25px rgba(212, 175, 55, 0.1);
        }
        .full { grid-column: span 2; }
        .no-data-msg {
            position: absolute;
            inset: 0;
            background: var(--bg);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
            z-index: 10;
        }
        .empty-state-icon {
            font-size: 32px;
            color: var(--sidebar);
            opacity: 0.2;
            margin-bottom: 10px;
        }
        .empty-state-title {
            font-size: 14px;
            font-weight: 800;
            color: var(--sidebar);
            margin-bottom: 5px;
        }
        .empty-state-desc {
            font-size: 11px;
            color: var(--text-main);
            max-width: 250px;
            opacity: 0.7;
        }

        /* Table */
        .table-box {
            background: var(--card-bg);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 50px;
            border: 2px solid var(--accent);
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }
        .table-box:hover {
            box-shadow: 0 15px 50px rgba(0,0,0,0.08);
        }
        .table-header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        .btn-download {
            background: var(--sidebar);
            color: #fff;
            border: none;
            padding: 8px 15px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 11px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: 0.2s;
        }
        .btn-download:hover { background: var(--accent); color: white; }
        .table-wrapper { max-height: 500px; overflow-y: auto; border-radius: 8px; border: 1px solid #BBDEFB; }
        table { width: 100%; border-collapse: collapse; font-size: 11px; }
        th { background: var(--sidebar); color: #fff; padding: 12px; text-align: left; position: sticky; top: 0; z-index: 10; font-weight: 800; border-bottom: 2px solid var(--accent); }
        td { padding: 10px 12px; border-bottom: 1px solid #F3F4F6; color: #333; }
        tr:hover { background: #F0F4FF; }

        /* Sliders */
        .date-slider-wrapper .slider-container { background: #BBDEFB!important; border-radius: 10px; }
        #slider-track { background: var(--slider-track)!important; height: 100%; border-radius: 10px; }
        input[type=range] { pointer-events: none; -webkit-appearance: none; background: transparent; width: 100%; }
        input[type=range]::-webkit-slider-thumb {
            pointer-events: auto; -webkit-appearance: none;
            width: 14px; height: 14px; border-radius: 50%;
            background: var(--sidebar); border: 2px solid var(--accent);
            cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
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
                <h4 id="exc-title" style="margin: 5px 0 0 0; font-size: 13px; color: var(--accent); font-weight: 700; text-transform: uppercase; opacity: 0.8;"></h4>
            </div>
            <div class="exc-btns" id="exc-btns"></div>
        </div>

        <div id="kpi-row"></div>
        <div id="slicer-row"></div>
        <div id="chart-grid"></div>

        <div class="table-box">
            <div class="table-header-flex">
                <h3 style="font-size:15px;margin:0;font-weight:800;color:var(--sidebar);">Detailed Configuration Log</h3>
                <button class="btn-download" onclick="downloadCSV()">
                    <i class="fa-solid fa-file-csv"></i> Download Data
                </button>
            </div>
            <div class="table-wrapper" id="table-container"></div>
        </div>
    </div>

<script>
        const EXC_NAMES = {
    'CJIT3': {
        'All Exceptions': 'Receivables exceeding minimum credit limit',
        'Exception 01': 'Receivables exceeding minimum credit limit',
        'Exception 1': 'Receivables exceeding minimum credit limit'
    },
    'CJIT03': {
        'All Exceptions': 'Receivables exceeding minimum credit limit',
        'Exception 01': 'Receivables exceeding minimum credit limit',
        'Exception 1': 'Receivables exceeding minimum credit limit'
    },
    'CJMA11': {
        'Exception 01': 'Payment term issues',
        'Exception 1': 'Payment term issues'
    },
    'CJMA15': {
        'Exception 01': 'Customer to Vendor balances are set off',
        'Exception 1': 'Customer to Vendor balances are set off',
        'Exception 02': 'Vendor to Customer balances are set off',
        'Exception 2': 'Vendor to Customer balances are set off'
    },
    'CJSA24': {
        'Exception 01': 'Delay between LR Date and Invoice Date (more than 7 days)',
        'Exception 1': 'Delay between LR Date and Invoice Date (more than 7 days)',
        'Exception 02': 'Delay between LR Date and Invoice Date (negative days)',
        'Exception 2': 'Delay between LR Date and Invoice Date (negative days)'
    },
    'CJSA30': {
        'All Exceptions': 'Scrap price is lower than the price at other location',
        'Exception 01': 'Scrap price is lower than the price at other location',
        'Exception 1': 'Scrap price is lower than the price at other location'
    },
    'FJAC6': {
        'Exception 01': 'Missing Date Invoicing',
        'Exception 1': 'Missing Date Invoicing',
        'Exception 02': 'Backdated Invoicing',
        'Exception 2': 'Backdated Invoicing'
    },
    'MJIT4': {
        'All Exceptions': 'Message Configuration check for Validity period',
        'Exception 01': 'Message Configuration check for Validity period',
        'Exception 1': 'Message Configuration check for Validity period'
    },
    'MJOT11': {
        'All Exceptions': 'Same plant with Scrap Sales',
        'Exception 01': 'Same plant with Scrap Sales',
        'Exception 1': 'Same plant with Scrap Sales',
        'Exception 02': 'Across all plants with Scrap Sales',
        'Exception 2': 'Across all plants with Scrap Sales'
    },
    'SJIN37': {
        'Exception 01': 'Vendors with same PAN having same reference number / doc date',
        'Exception 1': 'Vendors with same PAN having same reference number / doc date',
        'Exception 02': 'Vendors with same PAN having same reference number / doc date / amount',
        'Exception 2': 'Vendors with same PAN having same reference number / doc date / amount',
        'Exception 03': 'Vendors with same PAN having same reference number / amount',
        'Exception 3': 'Vendors with same PAN having same reference number / amount',
        'Exception 04': 'Vendors with same PAN having same amount / doc date',
        'Exception 4': 'Vendors with same PAN having same amount / doc date',
        'Exception 05': 'Vendor Reference Document Date',
        'Exception 5': 'Vendor Reference Document Date',
        'Exception 06': 'Vendor Reference Document Date & Amount in LC',
        'Exception 6': 'Vendor Reference Document Date & Amount in LC',
        'Exception 07': 'Vendor Reference Amount in LC',
        'Exception 7': 'Vendor Reference Amount in LC',
        'Exception 08': 'Vendor Document Date & Amount in LC',
        'Exception 8': 'Vendor Document Date & Amount in LC'
    },
    'SJIT31': {
        'Exception 01': 'GR & IR configurations over Item Category Type configured inappropriately',
        'Exception 1': 'GR & IR configurations over Item Category Type configured inappropriately',
        'Exception 02': 'GR & IR configurations over Account Assignment Categories configured inappropriately',
        'Exception 2': 'GR & IR configurations over Account Assignment Categories configured inappropriately',
        'Exception 03': 'Purchase docs under exception with no GR check in PO',
        'Exception 3': 'Purchase docs under exception with no GR check in PO'
    },
    'SJPR1': {
        'Exception 01': 'PR to PO delay is more than 30 days',
        'Exception 1': 'PR to PO delay is more than 30 days',
        'Exception 02': 'PR to PO delay is negative',
        'Exception 2': 'PR to PO delay is negative'
    },
    'SJPR25': {
        'Exception 01': 'Invoice Creator and PO Creator are same',
        'Exception 1': 'Invoice Creator and PO Creator are same',
        'Exception 02': 'Entry Date before PO Date or equal to Invoice Date',
        'Exception 2': 'Entry Date before PO Date or equal to Invoice Date',
        'Exception 03': 'Posting Date before PO Date or equal to Invoice Date',
        'Exception 3': 'Posting Date before PO Date or equal to Invoice Date'
    },
    'SJPR28': {
        'Exception 01': 'Group accounts with PO & Non PO Invoices raised',
        'Exception 1': 'Group accounts with PO & Non PO Invoices raised',
        'Exception 02': 'Same Group account with PO & Non PO Invoices',
        'Exception 2': 'Same Group account with PO & Non PO Invoices',
        'Exception 03': 'GL & Group accounts with PO & Non PO Invoices raised',
        'Exception 3': 'GL & Group accounts with PO & Non PO Invoices raised'
    },
    'SJPR53': {
        'Exception 01': 'GL accounts with PO & Non PO Invoices raised',
        'Exception 1': 'GL accounts with PO & Non PO Invoices raised',
        'Exception 02': 'Same GL with PO & Non PO Invoices',
        'Exception 2': 'Same GL with PO & Non PO Invoices'
    },
    'SJPR5': {
        'Exception 01': 'Single Source Vendor - Plant level',
        'Exception 1': 'Single Source Vendor - Plant level',
        'Exception 02': 'Single Source Vendor - Company level',
        'Exception 2': 'Single Source Vendor - Company level'
    },
    'SJPR9': {
        'Exception 01': 'PR split within 10 days',
        'Exception 1': 'PR split within 10 days',
        'Exception 02': 'PR split within 30 days',
        'Exception 2': 'PR split within 30 days'
    }
};
        const MERGED_INSIGHTS = ['CJIT3', 'CJIT03', 'CJMA15', 'CJSA24', 'FJAC6', 'MJOT11', 'SJPR1', 'SJPR53', 'SJPR5', 'SJPR9', 'SJPR28', 'SJIT31', 'CJMA11', 'CJSA30', 'MJIT4', 'SJPR25', 'SJIN37'];
        
        function handleMergedInsightsUI(id) {
            if (MERGED_INSIGHTS.includes(id)) {
                $('#exc-btns').hide();
                if (!curExcFilters.some(f => f.source === 'exception_type')) {
                    curExcFilters.unshift({ id: 'sel-extype', label: 'Exception Type', source: 'exception_type', all_label: 'All Exceptions' });
                }
            } else {
                $('#exc-btns').show();
                curExcFilters = curExcFilters.filter(f => f.source !== 'exception_type');
            }
        }

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

const CONFIGS = {{ configs|safe }};
/* Procurement Blue Palette for Charts */
const CC = ['#052659', '#315C8E', '#5483B3', '#7DA0CA', '#9BBCE0', '#C1E8FF', '#A0C4FF'];
let rawD = [], rawC = [], filteredD = [];
let cInst = {}, colCache = {};
let curID = '', curExc = 1, dateList = [];
let bStats = null, aCfg = null, curExcFilters = [], curExcCards = [], curExcCharts = [];

function rCol(source) {
    if (!aCfg?.columns?.[source]) return null;
    if (colCache[source]) return colCache[source];
    const candidates = aCfg.columns[source];
    const normalizedHeaders = rawC.map(c => c.trim().toLowerCase());
    for (const cand of candidates) {
        const idx = normalizedHeaders.indexOf(cand.trim().toLowerCase());
        if (idx !== -1) { colCache[source] = rawC[idx]; return rawC[idx]; }
    }
    return null;
}

function parseNum(val) {
    if (val === null || val === undefined || val === '') return 0;
    if (typeof val === 'number') return val;
    const clean = String(val).replace(/[^0-9.-]/g, '');
    const num = parseFloat(clean);
    return isNaN(num) ? 0 : num;
}

function fmt(n, cur) {
    if (n === 0) return cur ? '₹0' : '0';
    let s = '', v = Math.abs(n);
    if (v >= 1e7) { v = n / 1e7; s = 'Cr'; }
    else if (v >= 1e5) { v = n / 1e5; s = 'L'; }
    else { v = n; }
    let r = parseFloat(v.toFixed(2)) + s;
    return cur ? '₹' + r : r;
}

function applyFilters() {
    if (!aCfg) return;
    const dC = rCol('date');
    const minD = dateList.length > 0 ? new Date(dateList[+$('#rng-min').val()]) : null;
    const maxD = dateList.length > 0 ? new Date(dateList[+$('#rng-max').val()]) : null;
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

    updateKPIs();
    updateCharts();
    renderTable("No records match your filters");
}

function updateKPIs() {
    const allFilt = isAllFilters();
    (curExcCards || []).forEach(card => {
        let val = 0;
        if (!filteredD || filteredD.length === 0) {
            $('#' + card.id).text(card.format === 'currency' ? '₹0' : '0');
            return;
        }
        const sourceCol = card.source ? rCol(card.source) : null;
        if (card.agg === 'row_count') val = filteredD.length;
        else if (card.agg === 'total_rows') val = (bStats && allFilt && !card.source) ? bStats.total_rows : filteredD.length;
        else if (card.agg === 'total_value') {
            if (bStats && allFilt && card.source === 'amount') val = bStats.total_value;
            else if (sourceCol) val = filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0);
        }
        else if (card.agg === 'sum') {
            val = sourceCol ? filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0) : 0;
        }
        else if (card.agg === 'unique') {
            val = sourceCol ? new Set(filteredD.map(r => r[sourceCol]).filter(v => v !== '')).size : 0;
        }
        else if (card.agg === 'percentage') {
            if (filteredD.length === 0) val = 0;
            else {
                let sum = sourceCol ? filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0) : 0;
                val = (sum / filteredD.length) * 100;
            }
        }
        else if (card.agg === 'avg') {
            if (filteredD.length === 0) val = 0;
            else {
                let sum = sourceCol ? filteredD.reduce((a, b) => a + parseNum(b[sourceCol]), 0) : 0;
                val = sum / filteredD.length;
            }
        }
        else if (card.agg === 'max') {
            if (filteredD.length === 0) val = 0;
            else {
                val = sourceCol ? Math.max(...filteredD.map(r => parseNum(r[sourceCol]))) : 0;
            }
        }
        $('#' + card.id).text(card.format === 'currency' ? fmt(val, true) : (card.agg === 'percentage' ? val.toFixed(2) + '%' : (card.agg === 'avg' || card.agg === 'max' ? val.toFixed(1) : val.toLocaleString('en-IN'))));
    });
}

function updateCharts() {
    if (!curExcCharts || curExcCharts.length === 0) return;
    curExcCharts.forEach(cfg => {
        const box = $('#box-' + cfg.id);
        box.find('.no-data-msg').remove();
        box.find('.chart-total-label').remove();
        if (cInst[cfg.id]) cInst[cfg.id].destroy();

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
        box.append(`<div class="chart-total-label" style="position: absolute; bottom: 15px; left: 15px; font-weight: 800; font-size: 11px; color: var(--sidebar); z-index: 5; background: rgba(255,255,255,0.8); padding: 2px 6px; border-radius: 4px;">Total: ${fmt(totalChartVal, false)}</div>`);
        renderChartJS(cfg, labels, values);
    });
}

function handleChartError(id, box, msg = "No data available") {
    const cfg = (curExcCharts || []).find(c => c.id === id);
    const title = cfg ? cfg.title : '';
    $('#' + id).hide();
    box.find('.no-data-msg').remove();
    box.find('.chart-total-label').remove();
    box.append(`
        <div class="no-data-msg">
            <div class="empty-state-title" style="margin-bottom:10px; font-size:12px; opacity:0.8;">${title}</div>
            <i class="fa-solid fa-chart-bar empty-state-icon"></i>
            <div class="empty-state-title">${msg}</div>
            <div class="empty-state-desc">Check if CSV has required data</div>
        </div>
    `);
}

function renderChartJS(cfg, labels, values) {
    const ctx = document.getElementById(cfg.id).getContext('2d');
    const type = cfg.type || 'bar';
    let chartConfig = {
        type: type,
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: type === 'line' ? CC[1] + '40' : CC,
                borderRadius: 5,
                borderColor: CC[0],
                borderWidth: type === 'line' ? 2 : 0,
                fill: type === 'line' ? {target: 'origin', above: 'rgba(2,16,36,0.08)'} : false,
                tension: 0.4
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: {
                title: { display: true, text: cfg.title || (cfg.y ? `${cfg.y} by ${cfg.x}` : `${cfg.x} Distribution`).toUpperCase(), font: { size: 13, weight: '800', family: "'Plus Jakarta Sans', sans-serif" }, color: '#000' },
                legend: { display: !!cfg.legend, position: 'bottom', labels: { boxWidth: 10, font: { size: 9 } } }
            }
        }
    };
    if (type === 'bar' || type === 'line') {
        chartConfig.options.scales = {
            x: { grid: { display: false }, ticks: { font: { size: 9 } } },
            y: { grid: { color: '#f0f0f0' }, ticks: { font: { size: 9 }, callback: v => fmt(v, false) } }
        };
        if (cfg.horizontal) chartConfig.options.indexAxis = 'y';
    }
    cInst[cfg.id] = new Chart(ctx, chartConfig);
}

async function load() {
    if (!curID) return;
    colCache = {};
    $('#table-container').html('<div class="no-data-msg">Fetching data...</div>');
    try {
        const r = await fetch(`api/${curID}/${curExc}?t=${Date.now()}`);
        const d = await r.json();
        if (d.success) {
            rawD = d.rows || []; rawC = d.cols || []; bStats = d.full_stats || null;
            setupSlider(); popSlicers(); applyFilters();
        } else { handleEmptyState(d.msg); }
    } catch (e) { 
        console.error(e); handleEmptyState("Server Error"); 
    }
}

function handleEmptyState(msg = "No data available for this Exception") {
    rawD = []; rawC = []; filteredD = [];
    updateKPIs(); updateCharts(); renderTable(msg);
}

function setupSlider() {
    const dc = rCol('date');
    if (!dc) { $('#lbl-min').text('-'); $('#lbl-max').text('-'); $('#slider-track').css({ width: '0%' }); return; }
    dateList = [...new Set(rawD.map(r => r[dc]))].filter(x => x && !isNaN(new Date(x))).sort((a, b) => new Date(a) - new Date(b));
    if (dateList.length > 0) {
        $('#rng-min').attr({ min: 0, max: dateList.length - 1 }).val(0);
        $('#rng-max').attr({ min: 0, max: dateList.length - 1 }).val(dateList.length - 1);
        updSliderUI();
    } else { $('#lbl-min').text('-'); $('#lbl-max').text('-'); $('#slider-track').css({ width: '0%' }); }
}

function popSlicers() {
    (curExcFilters || []).forEach(f => {
        const col = rCol(f.source), sel = $('#' + f.id);
        let allLbl = f.all_label || ('All ' + f.label);
                if (allLbl.toLowerCase() === 'all exception type' || allLbl.toLowerCase() === 'all exception types') {
                    allLbl = 'All Exceptions';
                }
                allLbl = allLbl.replace(/"/g, '');
                sel.html('<option value="ALL">' + allLbl + '</option>');
        if (f.id === 'sel-extype') { (aCfg.active_exceptions || []).forEach(e => { const label = e.label; const mappedName = (typeof EXC_NAMES !== 'undefined' && EXC_NAMES[curID] && EXC_NAMES[curID][label]) || label; sel.append('<option value="' + label + '">' + mappedName + '</option>'); }); } else if (col && rawD.length > 0) { [...new Set(rawD.map(r => r[col]))].filter(x => x).sort().forEach(v => sel.append(`<option value="${v}">${v}</option>`)); }
    });
}

function renderTable(msg) {
    if (!filteredD.length) {
        $('#table-container').html(`<div class="no-data-msg" style="position:relative; min-height: 200px; background: transparent;">
            <i class="fa-solid fa-circle-info empty-state-icon"></i>
            <div class="empty-state-title">${msg || "No records match your filters"}</div>
        </div>`);
        return;
    }
    let h = '<table><thead><tr>'; rawC.forEach(c => h += `<th>${c}</th>`); h += '</tr></thead><tbody>';
    filteredD.slice(0, 100).forEach(r => {
        h += '<tr>'; rawC.forEach(c => h += `<td>${r[c] !== null && r[c] !== undefined ? r[c] : ''}</td>`); h += '</tr>';
    });
    h += '</tbody></table>'; $('#table-container').html(h);
}

function selObj(id, name, el) {
    if (history.pushState) history.pushState(null, "", "?oid=" + id);
    $('.side-item').removeClass('active'); $(el).addClass('active');
    curID = id; aCfg = CONFIGS[id] || {};
    curExc = aCfg.active_exceptions?.[0]?.id || 1;
    $('#disp-name').text(`${id} | ${name}`);
    buildExcBtns(); 
    
    const eObj = aCfg.active_exceptions?.[0] || {};
    curExcFilters = eObj.filters || aCfg.filters || defaultFilters;
    curExcCards = eObj.cards || aCfg.cards || defaultCards;
    curExcCharts = eObj.charts || aCfg.charts || defaultCharts;
    handleMergedInsightsUI(id); buildKPIs(curExcCards); 
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
        curExcFilters = eObj.filters || aCfg.filters || defaultFilters;
        curExcCards = eObj.cards || aCfg.cards || defaultCards;
        curExcCharts = eObj.charts || aCfg.charts || defaultCharts;
        handleMergedInsightsUI(curID); buildKPIs(curExcCards); 
        buildSlicers(curExcFilters); 
        buildChartBoxes(curExcCharts);
    }
    load(); 
}
function buildExcBtns() {
    let h = ''; (aCfg.active_exceptions || []).forEach(e => h += `<button id="btn-exc${e.id}" class="${e.id == curExc ? 'active' : ''}" onclick="selExc('${e.id}')">${e.label}</button>`);
    $('#exc-btns').html(h);
}
function buildKPIs(cards) {
    const arr = cards || aCfg.cards || [];
    let h = ''; arr.forEach(c => h += `<div class="kpi-card"><div id="${c.id}" class="kpi-val">0</div><div class="kpi-lbl">${c.label}</div></div>`);
    $('#kpi-row').html(h);
}
function buildSlicers(filters) {
    const arr = filters || curExcFilters || [];
    let h = ''; arr.forEach(f => h += `<div class="slicer-card"><span class="slicer-lbl">${f.label}</span><select id="${f.id}" onchange="applyFilters()"></select></div>`);
    h += `<div class="slicer-card"><div style="display:flex;justify-content:space-between"><span class="slicer-lbl">Date Range</span><div class="date-display"><span id="lbl-min">-</span> to <span id="lbl-max">-</span></div></div>
          <div class="date-slider-wrapper"><div class="slider-container" style="position:relative;width:100%;height:6px;top:6px"><div id="slider-track" style="position:absolute;height:100%;z-index:1"></div>
          <input type="range" id="rng-min" oninput="handleSlider()" style="position:absolute;width:100%;z-index:2;margin:0"><input type="range" id="rng-max" oninput="handleSlider()" style="position:absolute;width:100%;z-index:2;margin:0"></div></div></div>
          <button class="btn-reset" onclick="resetFilters()">Reset</button>`;
    $('#slicer-row').html(h);
}
function buildChartBoxes(charts) { 
    const arr = charts || aCfg.charts || [];
    Object.values(cInst).forEach(c => c?.destroy()); cInst = {}; 
    let h = ''; arr.forEach(c => h += `<div class="${(c.full_width || c.type === 'line') ? 'chart-box full' : 'chart-box'}" id="box-${c.id}"><canvas id="${c.id}"></canvas></div>`);
    $('#chart-grid').html(h);
}

function handleSlider() { 
    let v1 = +$('#rng-min').val(), v2 = +$('#rng-max').val(); 
    if (v1 > v2) $('#rng-min').val(v2); 
    updSliderUI(); applyFilters(); 
}
function updSliderUI() {
    let v1 = +$('#rng-min').val(), v2 = +$('#rng-max').val(), mx = dateList.length - 1;
    $('#lbl-min').text(dateList[v1] || '-'); $('#lbl-max').text(dateList[v2] || '-');
    if (mx > 0) $('#slider-track').css({ left: (v1 / mx) * 100 + '%', width: ((v2 - v1) / mx) * 100 + '%' });
}
function resetFilters() { (curExcFilters || []).forEach(f => $('#' + f.id).val('ALL')); setupSlider(); applyFilters(); }
function isAllFilters() { return (curExcFilters || []).every(f => $('#' + f.id).val() === 'ALL'); }

// Corrected download csv for Excel compatibility and file name
function downloadCSV() {
    if (!filteredD.length) return;
    let csv = rawC.join(',') + '\n';
    filteredD.forEach(r => csv += rawC.map(c => `"${String(r[c] !== null && r[c] !== undefined ? r[c] : '').replace(/"/g, '""')}"`).join(',') + '\n');
    const b = new Blob([csv], { type: 'text/csv;charset=utf-8;' }), l = document.createElement('a'); l.href = URL.createObjectURL(b); l.download = `${curID}_Export.csv`; l.click();
}

$(document).ready(() => {
    const p = new URLSearchParams(window.location.search), o = p.get('oid');
    if (o) { const t = $(`.side-item[data-id="${o}"]`); if (t.length) selObj(o, t.data('name'), t[0]); }
    else $('.side-item').first().click();
});
</script>
</body>
</html>
"""
