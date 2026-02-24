# 📊 Telecom Customer Churn ETL & Analytics Pipeline

A comprehensive Data Engineering project that automates the extraction, transformation, and loading (ETL) of telecom customer data to predict and visualize churn patterns.

## 🚀 Live Demo
[View the Deployed Web App](https://telcomchurnetl-csrpsgct7tf33opxtktv4m.streamlit.app/)

## 🛠️ Project Architecture
The pipeline follows a modern data stack approach:
1. **Extraction**: Raw data fetched from Supabase Storage.
2. **Orchestration**: Managed by **Apache Airflow (Astro CLI)** to handle task dependencies.
3. **Storage**: Data is cleaned and loaded into a **Supabase (PostgreSQL)** data warehouse.
4. **Analytics**: A **Streamlit** dashboard visualizes churn rates and patterns.
5. **Insights**: Preliminary churn analysis based on tenure, contract type, and monthly charges.

![Dashboard Preview](dashboard_preview.png)

## 🏗️ Tech Stack
* **Orchestrator**: Apache Airflow
* **Database**: PostgreSQL (Supabase)
* **Language**: Python (Pandas, SQLAlchemy)
* **Visualization**: Streamlit & Plotly
* **Environment**: Docker (Astro)

## 📊 Key Insights
* **Contract Impact**: Month-to-month contracts show the highest churn velocity.
* **Financial Correlation**: High monthly charges correlate strongly with increased churn probability.
* **Tenure**: Retention rates significantly improve after the first 12 months of service.

## ⚙️ Setup & Installation
1. Clone the repo: `git clone https://github.com/fredsn0tDead/Telcom_Churn_ETL.git`
2. Install requirements: `pip install -r requirements.txt`
3. Configure your `.streamlit/secrets.toml` (see `secrets.toml.example`).
4. Run the dashboard: `streamlit run dashboard.py`
