# DC Bikeshare Demand & Peak Usage Analysis

A comprehensive data analysis project examining Capital Bikeshare usage patterns in Washington, DC, with a focus on identifying peak demand periods and weather impact on ridership.

##  Project Overview

This project analyzes DC Capital Bikeshare trip data to uncover:
- Peak usage patterns by hour, day, and season
- Top stations and routes
- Weather impact on ridership
- Member vs casual user behavior
- Geographic distribution of station usage

##  Project Structure

```
dc-bikeshare-analysis/
│
├── data/
│   ├── raw/                    # Raw CSV files from Capital Bikeshare
│   ├── processed/              # Cleaned and processed data
│   └── weather/                # Weather data
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
│   └── 04_visualizations.ipynb
├── src/
│   └── weather_api.py          # Weather data fetching utilities
├── outputs/
│   ├── figures/                # Visualizations
│   └── reports/                # Summary reports
├── .env                        # API keys (not tracked)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

##  Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- OpenWeather API key (optional, for weather data)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd DC-Bikeshare-Demand-Analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Configure API keys (optional):
```bash
# Create .env file with your OpenWeather API key
echo "OPENWEATHER_API_KEY=your_key_here" > .env
```

4. Download DC Bikeshare data:
   - Visit [Capital Bikeshare System Data](https://capitalbikeshare.com/system-data)
   - Download desired month(s) CSV files
   - Place in `data/raw/` directory

### Usage

Run the Jupyter notebooks in sequence:

```bash
jupyter lab
```

1. **01_data_collection.ipynb** - Load and inspect raw data
2. **02_data_cleaning.ipynb** - Clean data and engineer features
3. **03_analysis.ipynb** - Statistical analysis and insights
4. **04_visualizations.ipynb** - Generate interactive visualizations

##  Key Findings

Results will be available after running the analysis notebooks, including:
- Peak usage hours and days
- Seasonal demand variations
- Weather correlation analysis
- Top performing stations and routes
- Interactive maps and charts

## 🛠️ Technologies Used

- **Python** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Seaborn & Matplotlib** - Static visualizations
- **Plotly** - Interactive visualizations
- **SciPy** - Statistical analysis
- **Jupyter** - Interactive notebook environment

##  Data Sources

- **Bikeshare Data**: Capital Bikeshare System Data
- **Weather Data**: OpenWeather API or NOAA Climate Data Online

##  License

This project is for educational and analytical purposes.

##  Author

Daniel Berhane

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Last Updated**: October 2025

