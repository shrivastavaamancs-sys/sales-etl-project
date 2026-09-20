# End-to-End Sales ETL & Analytics Pipeline

## 📌 Project Overview
An end-to-end **Sales Data ETL Pipeline** designed to ingest raw sales transactional data, perform automated cleaning and transformations, load structured datasets into a SQL database, and visualize key performance indicators in **Power BI**.

---

## 🏗️ Architecture & Data Flow
1. **Data Extraction:** Ingesting raw sales data through automated Python scripts (`src/`).
2. **Data Transformation (ETL):** Processing, cleaning, and validating records using custom Python transformations (`etl/`).
3. **Database Loading:** Storing structured tables into SQL databases using optimized schema scripts (`sql/`).
4. **Business Intelligence:** Reporting revenue trends, sales dynamics, and KPI metrics in **Power BI** (`powerbi/`).

---

## 🛠️ Tech Stack & Tools
* **Programming Language:** Python
* **Data Transformation:** Pandas, NumPy
* **Database & Querying:** SQL
* **Visualization & BI:** Power BI
* **Version Control:** Git, GitHub

---

## 📂 Repository Structure
```text
sales-etl-project/
├── etl/        # ETL processing and pipeline logic
├── powerbi/    # Power BI dashboard files (.pbix) and reports
├── sql/        # SQL schema DDLs and analytical queries
├── src/        # Core source code and utility functions
├── .gitignore  # Git ignore rules
└── README.md   # Project documentation
