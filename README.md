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
│   ├── processed/              # Cleaned and processed data (bikeshare_cleaned.parquet)
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
├── .streamlit/
│   └── config.toml             # Streamlit configuration
├── app.py                      # Streamlit web dashboard
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

#### Option 1: Interactive Streamlit Dashboard (Recommended)

Launch the interactive web dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501` with:
- Executive summary with key metrics
- Temporal pattern analysis
- Station usage maps
- User behavior comparisons
- Peak demand insights

#### Option 2: Jupyter Notebooks

Run the analysis notebooks in sequence:

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
- **Streamlit** - Interactive web dashboard
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Seaborn & Matplotlib** - Static visualizations
- **Plotly** - Interactive visualizations
- **SciPy** - Statistical analysis
- **Jupyter** - Interactive notebook environment
- **PyArrow** - Efficient parquet file handling

##  Data Sources

- **Bikeshare Data**: Capital Bikeshare System Data
- **Weather Data**: OpenWeather API or NOAA Climate Data Online

## 🚀 Deployment

### Streamlit Cloud Deployment

This project is configured for easy deployment on Streamlit Cloud:

1. **Push to GitHub**: Ensure `app.py`, `requirements.txt`, and `data/processed/bikeshare_cleaned.parquet` are committed
   ```bash
   git add app.py requirements.txt .streamlit/ data/processed/bikeshare_cleaned.parquet
   git commit -m "Add Streamlit dashboard"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Select your repository
   - Streamlit will automatically detect `app.py` and deploy

3. **Your app will be live** at: `https://dc-bikeshare-[your-username].streamlit.app`

**Requirements for Streamlit Cloud:**
- ✅ `app.py` - Main application file
- ✅ `requirements.txt` - Including streamlit, pandas, plotly, pyarrow
- ✅ `data/processed/bikeshare_cleaned.parquet` - Cleaned dataset (30MB)

##  License

This project is for educational and analytical purposes.

##  Author

Daniel Berhane

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Last Updated**: October 2025

