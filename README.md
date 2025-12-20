# 📊 BI Northwind Project - Complete Solution

## 🎯 Project Objective

This project presents a complete Business Intelligence (BI) solution based on the famous Northwind database. It demonstrates all stages of a modern ETL pipeline and the creation of an interactive analytical dashboard.

### Main Features:

- ✅ Data extraction from Access database and CSV files
- ✅ Data transformation and cleaning with Python/Pandas
- ✅ Creation of analytical metrics and KPIs
- ✅ Interactive dashboard with dynamic visualizations
- ✅ Generation of reports and exportable charts

---

## 📁 Project Structure

```
BI_Project/
│
├── data/
│   ├── Northwind 2012.accdb          # Source Access database
│   ├── extracted/                    # Extracted CSV files
│   │   ├── Access_Customers.csv
│   │   ├── Access_Employees.csv
│   │   ├── Access_Order_Details.csv
│   │   ├── Access_Orders.csv
│   │   └── Access_Products.csv
│   └── warehouse/
│       └── merged_northwind.csv      # Merged data warehouse
│
├── scripts/
│   ├── main.py                       # Main orchestrator
│   ├── etl_pipeline.py               # ETL pipeline
│   ├── extract_access.py             # Access database extraction
│   ├── extract_all.py                # Combined extraction
│   ├── transform_warehouse.py        # Data transformation
│   ├── database_manager.py           # Database operations
│   ├── dashboard.py                  # Dashboard generation
│   ├── generate_figures.py           # Static figures
│   ├── generate_interactive_figures.py # Interactive figures
│   ├── data_helpers.py               # Data utilities
│   ├── settings.py                   # Configuration
│   └── other scripts...              # Additional utilities
│
├── figures/                          # Generated figures (HTML/PNG)
│   ├── index.html                    # Main dashboard
│   ├── dashboard_interactive.html
│   ├── orders_by_country.html
│   └── other visualizations...
│
├── notebooks/                        # Jupyter notebooks
│   ├── visualization.ipynb
│   └── visualization_interactive.ipynb
│
├── reports/                          # Generated reports
├── video/                            # Presentation materials
│
├── start_pipeline.bat                # Batch file to start pipeline
├── README.md                         # This file
└── requirements.txt                  # Python dependencies (create if needed)
```

---

## 🚀 Installation and Configuration

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Microsoft Access database (Northwind 2012.accdb)
- Windows OS (for Access connectivity)

### 2. Dependency Installation

```bash
# Navigate to project directory
cd BI_Project

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly dash pyodbc sqlalchemy openpyxl
```

### 3. Data Source

The project uses the Northwind 2012 Access database as the primary data source. Ensure `data/Northwind 2012.accdb` is present.

---

## 🎬 Project Execution

### Quick Start

Use the batch file to run the complete pipeline:

```bash
start_pipeline.bat
```

Or run the main script:

```bash
python scripts/main.py
```

### Detailed Steps

#### Step 1: Data Extraction

```bash
# Extract from Access database
python scripts/extract_access.py

# Or extract all data
python scripts/extract_all.py
```

**What this does:**

- Connects to Northwind 2012.accdb
- Extracts tables to CSV files in `data/extracted/`
- Handles data type conversions and relationships

#### Step 2: Data Transformation

```bash
python scripts/transform_warehouse.py
```

**What this does:**

- Cleans and transforms extracted data
- Creates merged warehouse file `data/warehouse/merged_northwind.csv`
- Calculates derived metrics and KPIs

#### Step 3: Dashboard and Visualizations

```bash
# Generate static figures
python scripts/generate_figures.py

# Generate interactive figures
python scripts/generate_interactive_figures.py

# Run dashboard
python scripts/dashboard.py
```

**What this does:**

- Creates various charts and graphs
- Generates HTML dashboards in `figures/`
- Starts web server for interactive dashboard

---

## 📊 Key Indicators (KPIs)

The dashboard presents the following KPIs:

### Main KPIs

1. **💰 Total Revenue**: Sum of all sales
2. **📦 Number of Orders**: Total orders placed
3. **👥 Number of Customers**: Unique active customers
4. **📊 Average Order Value**: Average value per order
5. **🚚 Average Delivery Time**: In days

### Available Visualizations

1. **📈 Monthly Sales Trend**

   - Line chart showing temporal trends
   - Identifies seasonality

2. **🎯 Sales by Category**

   - Pie chart of sales by product category
   - Identifies most profitable categories

3. **🏆 Top Products**

   - Horizontal bar chart
   - Ranking of best-selling products

4. **🌍 Sales by Country**

   - Bar chart of geographical sales
   - Top countries by revenue

5. **👔 Employee Performance**

   - Comparison of sales by employee
   - Number of processed orders

6. **🚚 Delivery Statistics**
   - Delivery performance metrics
   - Country-wise delivery analysis

---

## 🛠️ Technical Choices

### Python Libraries Used

| Library        | Usage                  | Justification                              |
| -------------- | ---------------------- | ------------------------------------------ |
| **Pandas**     | Data manipulation      | Industry standard, performant, easy to use |
| **SQLAlchemy** | Database connection    | Compatible with multiple database types    |
| **Plotly**     | Visualizations         | Modern, interactive, elegant charts        |
| **Dash**       | Web dashboard          | Python framework for analytical web apps   |
| **PyODBC**     | Access connectivity    | Windows ODBC driver for Access databases   |
| **NumPy**      | Numerical calculations | Optimized for mathematical operations      |

### Chosen Architecture

**Modular ETL Pipeline**

- ✅ Clear separation of Extract / Transform / Load
- ✅ Each script can run independently
- ✅ Facilitates debugging and maintenance
- ✅ Enables code reuse

**CSV Storage**

- ✅ Universal and lightweight format
- ✅ Easy to inspect and debug
- ✅ Compatible with all analysis tools
- ✅ Versionable with Git

---

## 📈 Possible Analyses

This project allows answering business questions such as:

1. **Sales Analysis**

   - What is the sales trend over the period?
   - Which months are most profitable?
   - Is there seasonality?

2. **Product Analysis**

   - Which products generate the most revenue?
   - Which categories are most popular?
   - What is the repurchase rate?

3. **Geographical Analysis**

   - Which countries buy the most?
   - Where to focus commercial efforts?

4. **HR Analysis**

   - Which employees are most performant?
   - What is the workload per employee?

5. **Logistics Analysis**
   - What is the average delivery time?
   - Are there significant delays?

---

## 🎓 Going Further

### Possible Improvements

1. **Predictive Analysis**

   - Future sales forecasting (Machine Learning)
   - Anomaly detection

2. **Advanced Dashboard**

   - Interactive filters by period/category
   - Automated PDF report exports
   - Real-time alerts

3. **Optimization**

   - Use of NoSQL databases (MongoDB)
   - Result caching for better performance
   - Processing parallelization

4. **Deployment**
   - Cloud hosting (AWS, Azure, Heroku)
   - REST API setup
   - Automation with Airflow

---

## 🐛 Troubleshooting

### Problem: Access Database Connection Error

**Solution:**

- Ensure Microsoft Access is installed
- Verify the path to `Northwind 2012.accdb`
- Check user permissions for database access
- Try running as administrator

### Problem: Module Not Found

**Solution:** Ensure virtual environment is activated and dependencies are installed:

```bash
pip install pandas numpy matplotlib seaborn plotly dash pyodbc sqlalchemy openpyxl
```

### Problem: Dashboard Not Displaying

**Solution:** Check that port 8050 (default) is not in use. Change port if necessary:

```python
app.run_server(debug=True, port=8051)
```

### Problem: Data Extraction Fails

**Solution:**

- Verify Access database is not corrupted
- Check ODBC drivers are installed
- Ensure all required tables exist in the database

---

## 📚 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)
- [Dash Documentation](https://dash.plotly.com/)
- [Northwind Database](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs)

---

## 👤 Author

DAOUD OMAR RAYANE Cyber security student G4

---

## 📄 License

This project is provided for educational purposes. The Northwind database is property of Microsoft made publicly available.

---

## 🙏 Acknowledgments

- Microsoft for the Northwind database
- Python community for excellent open-source libraries
- All contributors and educators
