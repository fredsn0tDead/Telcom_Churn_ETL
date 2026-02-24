import streamlit as st
import plotly.express as px

# 1. Initialize connection
conn = st.connection("postgresql", type="sql")

# 2. Page Config
st.set_page_config(page_title="Telecom Churn Dashboard", layout="wide")
st.title("📊 Telecom Customer Churn Analysis")

# 3. Pull Data (Cached for 10 mins to stay within free tier limits)
@st.cache_data(ttl=600)
def get_data():
    return conn.query('SELECT * FROM stg_churn_data;', ttl="10m")

df = get_data()

# 4. KPI Row
total_cust = len(df)
churn_rate = (df['Churn'] == 'Yes').mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{total_cust:,}")
col2.metric("Churn Rate", f"{churn_rate:.1%}")
col3.metric("Avg Monthly Charges", f"${df['MonthlyCharges'].mean():.2f}")

# 5. Visualizations
st.divider()
left_col, right_col = st.columns(2)

with left_col:
    fig_contract = px.histogram(df, x="Contract", color="Churn", barmode="group", title="Churn by Contract Type")
    st.plotly_chart(fig_contract, use_container_width=True)

with right_col:
    fig_tenure = px.box(df, x="Churn", y="tenure", title="Tenure vs Churn", points="all")
    st.plotly_chart(fig_tenure, use_container_width=True)