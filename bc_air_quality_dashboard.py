
import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="BC PM2.5 Air Quality Dashboard",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Customizing the UI slightly with CSS
st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    # Direct URL to the live dataset
    url = "https://catalogue.data.gov.bc.ca/dataset/699be99e-a9ba-403e-b0fe-3d13f84f45ab/resource/bfa3fdd8-2950-4d3a-b190-52fb39a5ffd4/download/pm25_stations_summary.csv"
    df = pd.read_csv(url)
    
    # Clean the data: Ensure numeric types for mapping
    df['metric_value_ambient'] = pd.to_numeric(df['metric_value_ambient'], errors='coerce')
    
    # Drop rows without geographical coordinates 
    df = df.dropna(subset=['latitude', 'longitude'])
    return df

df = load_data()

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.title("🌬️ Dashboard Controls")
st.sidebar.markdown("Filter the data to explore PM2.5 levels across British Columbia.")

# Year Filter
years = sorted(df['caaqs_year'].dropna().unique().astype(int).tolist())
selected_year = st.sidebar.slider("📅 Select Year", min_value=min(years), max_value=max(years), value=max(years))

# Metric Filter
metrics = df['metric'].dropna().unique().tolist()
selected_metric = st.sidebar.radio(
    "📊 Select PM2.5 Metric", 
    metrics, 
    format_func=lambda x: "24-Hour Average" if "24h" in x else "Annual Average"
)

# Airzone Filter
airzones = sorted(df['airzone'].dropna().unique().tolist())
selected_airzones = st.sidebar.multiselect("🗺️ Select Airzone(s)", airzones, default=airzones)

# --- 4. DATA FILTERING ---
filtered_df = df[
    (df['caaqs_year'] == selected_year) & 
    (df['metric'] == selected_metric) & 
    (df['airzone'].isin(selected_airzones))
].copy()

# --- 5. MAIN DASHBOARD CONTENT ---
st.title(f"🌲 British Columbia PM2.5 Air Quality ({selected_year})")
st.markdown("An interactive analysis of the **Canadian Ambient Air Quality Standards (CAAQS)** metrics for fine particulate matter (PM2.5) across BC.")

# Top Row: KPI Cards
col1, col2, col3, col4 = st.columns(4)

total_stations = filtered_df['station_name'].nunique()
achieved = len(filtered_df[filtered_df['caaqs_ambient'] == 'Achieved'])
not_achieved = len(filtered_df[filtered_df['caaqs_ambient'] == 'Not Achieved'])
avg_pm25 = filtered_df['metric_value_ambient'].mean()

col1.metric("Total Active Stations", total_stations)
col2.metric("✅ Achieved Standard", achieved, f"{(achieved/total_stations)*100 if total_stations else 0:.1f}%")
col3.metric("⚠️ Not Achieved", not_achieved, f"{(not_achieved/total_stations)*100 if total_stations else 0:.1f}%", delta_color="inverse")
col4.metric("📉 Avg PM2.5 Value", f"{avg_pm25:.2f} µg/m³" if pd.notnull(avg_pm25) else "N/A")

st.markdown("---")

# Middle Row: Interactive Map and Bar Chart
map_col, chart_col = st.columns([3, 2])

with map_col:
    st.subheader("📍 Station Locations & Status")
    
    # Handle map dot sizes dynamically
    filtered_df['map_size'] = filtered_df['metric_value_ambient'].fillna(2)
    filtered_df['map_size'] = filtered_df['map_size'].apply(lambda x: max(x, 2))
    
    # Custom color mapping for visual pop
    color_map = {
        "Achieved": "#28a745", 
        "Not Achieved": "#dc3545", 
        "Insufficient Data": "#6c757d", 
        "Unknown": "#6c757d"
    }
    
    # Plotly Mapbox
    fig_map = px.scatter_mapbox(
        filtered_df, 
        lat="latitude", 
        lon="longitude", 
        color="caaqs_ambient",
        color_discrete_map=color_map,
        size="map_size",
        size_max=15,
        hover_name="station_name",
        hover_data={
            "caaqs_ambient": True, 
            "metric_value_ambient": True, 
            "mgmt_level": True,
            "airzone": True, 
            "latitude": False, 
            "longitude": False,
            "map_size": False
        },
        zoom=4.5,
        center={"lat": 54.0, "lon": -125.0}, # Centered perfectly on British Columbia
        mapbox_style="carto-positron"
    )
    fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)

with chart_col:
    st.subheader("📊 Management Levels Required")
    mgmt_counts = filtered_df['mgmt_level'].value_counts().reset_index()
    mgmt_counts.columns = ['Management Level', 'Count']
    
    if not mgmt_counts.empty:
        fig_bar = px.bar(
            mgmt_counts, 
            y='Management Level', 
            x='Count', 
            orientation='h',
            color='Management Level',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_bar.update_layout(
            showlegend=False, 
            xaxis_title="Number of Stations", 
            yaxis_title="",
            yaxis={'categoryorder':'total ascending'},
            margin={"r":0,"t":0,"l":0,"b":0}
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("No management data available for current filters.")

st.markdown("---")

# Bottom Row: Time Series Trend
st.subheader("📈 PM2.5 Trends Over Time by Airzone")

# For the trendline, ignore the year filter but keep the metric and airzone filters
trend_df = df[(df['metric'] == selected_metric) & (df['airzone'].isin(selected_airzones))]
trend_grouped = trend_df.groupby(['caaqs_year', 'airzone'])['metric_value_ambient'].mean().reset_index()

if not trend_grouped.empty:
    fig_line = px.line(
        trend_grouped, 
        x="caaqs_year", 
        y="metric_value_ambient", 
        color="airzone",
        markers=True,
        labels={"caaqs_year": "Year", "metric_value_ambient": "Average PM2.5 Value (µg/m³)"}
    )
    fig_line.update_layout(hovermode="x unified", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.info("No trend data available for current filters.")

# Expandable Data Table
with st.expander("🔎 View Raw Station Data"):
    st.dataframe(
        filtered_df[['caaqs_year', 'airzone', 'station_name', 'metric', 'metric_value_ambient', 'caaqs_ambient', 'mgmt_level']]
        .sort_values(by='metric_value_ambient', ascending=False),
        use_container_width=True
    )

