# JK Cement Dashboard

This repository contains the source code for the **JK Cement Dashboard**, a Python Flask web application designed to track and visualize various business exceptions and insights across multiple domains (Supplier, Customer, Finance, etc.).

## 📁 Project Structure

The project follows a modular Monolith architecture using Flask Blueprints. It is organized into several domain-specific folders, promoting separation of concerns.

```text
JKcement/
├── app.py                      # Main entrypoint of the Flask application
├── requirements.txt            # Python dependencies
├── static/                     # Static assets (images, CSS, global JS)
│   ├── JK-logo.png
│   └── ajalabs-logo.png
├── templates/                  # Base HTML templates (e.g., home.html)
├── data_files/                 # Storage for generated CSV Exception Reports
├── Customer/                   # Customer Domain Blueprints
│   ├── c_invoice.py            # Customer Invoice Insights
│   ├── c_itac.py               # Customer ITAC Insights
│   ├── c_master_data.py        # Customer Master Data Insights
│   └── c_sales.py              # Customer Sales Insights
├── Supplier/                   # Supplier Domain Blueprints
│   ├── s_invoice.py            # Supplier Invoice Insights
│   ├── s_itac.py               # Supplier ITAC Insights
│   ├── s_master_data.py        # Supplier Master Data Insights
│   ├── s_payment.py            # Supplier Payment Insights
│   └── s_procurement.py        # Supplier Procurement Insights
├── Finance/                    # Finance Domain Scripts
├── Fixed_Asset/                # Fixed Assets Domain Scripts
├── ITcontrols/                 # IT Controls Domain Scripts
├── Manufacturing/              # Manufacturing Domain Scripts
├── Payroll/                    # Payroll Domain Scripts
└── Taxation/                   # Taxation Domain Scripts
```

## 🔗 How it is Linked (Architecture)

The application uses **Flask Blueprints** to keep the codebase maintainable and scalable.

1. **`app.py`**: Acts as the central hub. It imports individual Blueprints from the domain modules (e.g., `s_proc_bp` from `Supplier.s_procurement`) and registers them with specific URL prefixes (e.g., `/Supplier/procurement`).
2. **Domain Modules**: Each python file inside the domain folders (e.g., `Customer/c_invoice.py`) initializes its own `Blueprint` and contains its specific target views (HTML) and data API endpoints securely.
3. **Frontend Integration**: 
   - The user interface is driven by dynamic HTML templates (often returned via `render_template_string`).
   - The views pull in libraries like **Chart.js** for visualization, and **jQuery** for DOM manipulation.
4. **Data Access**: 
   - The frontend communicates with backend APIs (e.g., `/api/<oid>/<exc>`) defined within each blueprint.
   - The backend uses **Pandas** to read corresponding raw exception `.csv` files stored in the `data_files/` directory, formats them, and returns JSON payloads to the frontend.

## ⚙️ Application Workflow

1. **Initialization**: When you run `app.py`, the Flask server starts on `http://127.0.0.1:5000/`.
2. **Auto-Launch**: A threading timer wait 1.5 seconds and intelligently launches your default web browser sequentially, pointing directly to the dashboard's home page (`/`).
3. **Navigation**: From the landing view (`templates/home.html`), users click on an insight module they want to explore. This routes them to the corresponding blueprint endpoint (e.g., `/Customer/invoice`).
4. **Data Hydration**:
   - The blueprint responds with an interactive HTML framework.
   - Upon page load, a JavaScript fetch operation calls the backend API endpoint (`/api/<objective_id>/1`) with an objective ID.
   - The backend searches the `data_files/` directory for the relevant CSV exception file (e.g., `CJIN1_Exception01.csv`), processes it via Pandas handling `NaN` values, and sends a JSON dictionary.
5. **Dynamic Dashboard Interaction**:
   - The browser calculates all metrics (sums, averages, counts).
   - Data is dynamically bound to KPIs, Slicers (Filters), Tables, and Chart.js canvas elements.
   - When a user changes a filter (e.g., sliding the Date Range, or selecting a specific Document Type), the JavaScript `applyFilters()` function triggers immediately to re-process the cached JSON data client-side. This architecture entirely circumvents the need for heavy, synchronous backend database queries for interactive slicing.

## 🚀 Running the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Make sure the generated CSV output reports are placed within the `data_files/` folder to securely populate the dashboards.
3. Run the application:
   ```bash
   python app.py
   ```
