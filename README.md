# 🌲 BC Air Quality PM2.5 Interactive Dashboard

An interactive web application built with Python to visualize and analyze fine particulate matter ($PM_{2.5}$) levels across British Columbia. This tool pulls live data from Environmental Reporting BC to provide insights into air quality trends, management levels, and station-specific metrics.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.0+-red.svg)
![Plotly](https://img.shields.io/badge/plotly-v5.0+-orange.svg)

## 🚀 Features
- **Live Data Integration:** Fetches the latest PM2.5 station summary directly from the British Columbia Data Catalogue.
- **Interactive Mapping:** Geographic visualization of air quality stations using Plotly Mapbox, with markers scaled and colored by pollution levels.
- **Trend Analysis:** Time-series charts to track air quality changes by Air Zone over the last decade.
- **Dynamic Filtering:** 
    - Filter by **Metric Type** (24h vs. Annual).
    - Filter by **Air Zone** (e.g., Lower Fraser Valley, Southern Interior, etc.).
    - Filter by **Year Range** using a slider.
- **Management Level Stats:** Visual breakdown of stations meeting or exceeding air quality objectives.

## 🛠️ Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone https://github.com/your-username/bc-air-quality-dashboard.git
   cd bc-air-quality-dashboard
   ```

2. **Install the required dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install streamlit pandas plotly
   ```

## 💻 Usage

To launch the dashboard, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser (usually at `http://localhost:8501`).

## 📊 Data Source
The data used in this dashboard is provided by the **Government of British Columbia** via the [Open Government Portal](https://open.canada.ca/data/en/dataset/699be99e-a9ba-403e-b0fe-3d13f84f45ab). 

- **Dataset:** [Fine Particulate Matter CAAQS Station Results](https://catalogue.data.gov.bc.ca/dataset/699be99e-a9ba-403e-b0fe-3d13f84f45ab/resource/bfa3fdd8-2950-4d3a-b190-52fb39a5ffd4/download/pm25_stations_summary.csv)
- **License:** [Open Government License - British Columbia](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-license-bc)

## 🛠️ Python Libraries Used
- **Pandas**: Data manipulation and cleaning.
- **Streamlit**: Framework for building the web interface.
- **Plotly Express**: Interactive charts and geographic maps.

## 📝 License
This project is open-source and available under the Apache 2.0 License.

---

### Author
Developed by [Frankie Chan](https://github.com/chanfrankie) 


