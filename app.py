import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Title and project motivation
st.title("🎓 UC Admissions Equity & Representation Explorer")
st.markdown("""
This data tool evaluates **equity in action** across the University of California system. 
It analyzes how freshman acceptance rates vary across different ethnic demographics to identify 
where representation gaps exist for the **Fall 2025** cohort.
""")

# 2. Hardcoded Fall 2025 Dataset to bypass file uploading completely
@st.cache_data
def load_data():
    raw_data = {
        'campus': [
            'Berkeley', 'Berkeley', 'Davis', 'Davis', 'Irvine', 'Irvine', 
            'Los Angeles', 'Los Angeles', 'Merced', 'Merced', 'Riverside', 'Riverside', 
            'San Diego', 'San Diego', 'Santa Barbara', 'Santa Barbara', 'Santa Cruz', 'Santa Cruz'
        ],
        'ethnicity': [
            'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)',
            'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)',
            'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)', 'White', 'Hispanic/Latino(a)'
        ],
        'Total Applicants': [
            11300, 15400, 14200, 18600, 13100, 24300,
            12800, 19200, 2100, 11400, 5100, 18900,
            14500, 22100, 13900, 18200, 10200, 16400
        ],
        'Total Admits': [
            1358, 1818, 6395, 6671, 3599, 4527,
            1280, 1445, 2035, 10839, 4601, 15738,
            4051, 5726, 5308, 5614, 8068, 10154
        ]
    }
    pivoted = pd.DataFrame(raw_data)
    pivoted['Admit Rate (%)'] = (pivoted['Total Admits'] / pivoted['Total Applicants']) * 100
    return pivoted

df_clean = load_data()

# 3. Interactivity Settings
st.sidebar.header("🗺️ Filter Panel")

# Filter by Campus
campuses = sorted(df_clean['campus'].unique())
selected_campus = st.sidebar.selectbox("Select UC Campus:", campuses)

# Final localized data slice
final_data = df_clean[df_clean['campus'] == selected_campus].sort_values(by='Admit Rate (%)', ascending=False)

# 4. Dashboard Metrics Layout
st.subheader(f"📊 Admission Insights for {selected_campus} (Fall 2025)")

total_apps = int(final_data['Total Applicants'].sum())
total_adms = int(final_data['Total Admits'].sum())
overall_rate = (total_adms / total_apps) * 100 if total_apps > 0 else 0

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Pool Applicants", f"{total_apps:,}")
kpi2.metric("Total Pool Admits", f"{total_adms:,}")
kpi3.metric("Campus Baseline Admit Rate", f"{overall_rate:.2f}%")

st.markdown("---")

# 5. Interactive Data Visualization Layout
st.markdown("#### **Admit Rates by Ethnic Demographic**")
fig = px.bar(
    final_data, 
    x='ethnicity', 
    y='Admit Rate (%)',
    text=final_data['Admit Rate (%)'].apply(lambda x: f'{x:.1f}%'),
    color='ethnicity',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig.update_layout(showlegend=False, xaxis_title="Demographic Group", yaxis_title="Acceptance Percentage (%)")
st.plotly_chart(fig, use_container_width=True)

st.markdown("#### **Raw Data Audit View**")
st.dataframe(
    final_data[['ethnicity', 'Total Applicants', 'Total Admits', 'Admit Rate (%)']], 
    use_container_width=True,
    hide_index=True
)
