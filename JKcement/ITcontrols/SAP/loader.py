# ITcontrols loader.py
from flask import Blueprint, render_template_string, jsonify
import pandas as pd
import importlib
import glob
import json
import os
import sys
import re

from . import template

def get_live_configs(category_folder):
    cat_dir = os.path.dirname(__file__)
    insight_files = sorted(glob.glob(os.path.join(cat_dir, 'IJ*.py')))
    insight_configs = {}
    insight_modules = {}
    objectives = []
    for fpath in insight_files:
        module_name = os.path.splitext(os.path.basename(fpath))[0]
        full_module = f"ITcontrols.{category_folder}.{module_name}"
        try:
            if full_module in sys.modules:
                mod = importlib.reload(sys.modules[full_module])
            else:
                mod = importlib.import_module(full_module)
            cfg = getattr(mod, 'CONFIG', None)
            m = mod.meta()
            if cfg:
                insight_configs[m["id"]] = cfg
                insight_modules[m["id"]] = mod
                objectives.append({"id": m["id"], "o": m["name"]})
        except Exception as e:
            print(f"    [ERR] {full_module}: {e}")
    objectives.sort(key=lambda x: int(re.search(r'\d+', x["id"]).group()) if re.search(r'\d+', x["id"]) else 0)
    return insight_configs, insight_modules, objectives

def create_blueprint(bp_name, page_title, url_prefix, category_folder):
    bp = Blueprint(bp_name, __name__)

    @bp.route('/')
    def dashboard():
        importlib.reload(template)
        insight_configs, _, objectives = get_live_configs(category_folder)
        configs_json = json.dumps(insight_configs)
        html = template.get_html()
        return render_template_string(html, objectives=objectives, page_title=page_title, configs=configs_json)

    @bp.route('/api/<oid>/<exc>')
    def api(oid, exc):
        insight_configs, insight_modules, _ = get_live_configs(category_folder)
        config = insight_configs.get(oid, {})
        mod = insight_modules.get(oid)
        if not mod:
            return jsonify({"success": False, "msg": "Insight module not found"})
        try:
            df = mod.get_data(exc)
            if df is None:
                return jsonify({"success": True, "cols": [], "rows": [], "is_large": False, "full_stats": {"total_rows": 0, "total_value": 0}, "msg": "Exception CSV file not found"})
            if df.empty:
                return jsonify({"success": True, "cols": list(df.columns), "rows": [], "is_large": False, "full_stats": {"total_rows": 0, "total_value": 0}, "msg": "No data found in CSV"})
            df.columns = [str(c).strip() for c in df.columns]
            amt_candidates = config.get('columns', {}).get('amount', [])
            amt_col = None
            for name in amt_candidates:
                match = [c for c in df.columns if c.lower().strip() == name.lower().strip()]
                if match: amt_col = match[0]; break
            total_val = 0
            if amt_col:
                temp = pd.to_numeric(df[amt_col].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce').fillna(0)
                total_val = float(temp.sum())
            return jsonify({"success": True, "cols": list(df.columns), "rows": df.head(100).to_dict(orient='records'), "is_large": len(df) > 100, "full_stats": {"total_rows": len(df), "total_value": total_val}})
        except Exception as e:
            return jsonify({"success": False, "msg": str(e)})
    return bp, url_prefix
