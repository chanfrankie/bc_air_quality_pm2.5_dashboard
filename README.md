# 🌲 British Columbia PM2.5 Air Quality Dashboard

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Data](https://img.shields.io/badge/Data-BC_Gov_Catalogue-success)

An interactive web dashboard built with **Streamlit** and **Plotly** to visualize the Canadian Ambient Air Quality Standards (CAAQS) metrics for fine particulate matter (PM2.5) across British Columbia.

## ✨ Features

- **Live Data Ingestion:** Fetches and caches data directly from the BC Government Data Catalogue.
- **Dynamic KPI Metrics:** Real-time summary cards showing total active stations, standard achievement percentages, and average PM2.5 values based on your filters.
- **Interactive Mapbox:** A geographical map of BC. Station markers are sized dynamically by PM2.5 concentration and color-coded by their achievement status (Achieved / Not Achieved).
- **Historical Trend Analysis:** A time-series line chart that compares PM2.5 trends across different airzones over multiple years.
- **Deep Filtering:** Sidebar controls allow you to instantly slice the data by Year, Metric Type (24-Hour vs Annual), and specific Airzones.
- **Raw Data Explorer:** An expandable section to view, sort, and analyze the raw tabular data behind the visualizations.

## 💾 Data Source
The data used in this dashboard is provided by the Government of British Columbia under the Open Government License - British Columbia. 
* **Dataset:** [CAAQS metrics for fine particulate matter (PM2.5)](https://catalogue.data.gov.bc.ca/dataset/699be99e-a9ba-403e-b0fe-3d13f84f45ab/resource/bfa3fdd8-2950-4d3a-b190-52fb39a5ffd4/download/pm25_stations_summary.csv)

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.7 or higher installed on your machine. 

### Installation
1. Clone this repository or download the source code to your local machine.
2. Open your terminal or command prompt and navigate to the project directory.
3. Install the required Python dependencies:

```bash
pip install streamlit pandas plotly
```

*(Optional but recommended: Create a virtual environment before installing dependencies)*

### Running the Application
Once the requirements are installed, you can launch the dashboard by running:

```bash
streamlit run bc_air_quality_dashboard.py
```

A new tab will automatically open in your default web browser (usually at `http://localhost:8501`) displaying the interactive dashboard.

## 🛠️ Built With
* [Streamlit](https://streamlit.io/) - The web framework used for building the interactive UI.
* [Plotly](https://plotly.com/python/) - Used for the interactive mapping and charting.
* [Pandas](https://pandas.pydata.org/) - Used for data manipulation, cleaning, and aggregation.

## 📝 License
This project is open-source and free to use. Please ensure you comply with the [Open Government License - British Columbia](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-license-bc) when using the underlying dataset.
```
