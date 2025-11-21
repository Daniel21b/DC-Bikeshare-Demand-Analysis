<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,22,30&height=180&section=header&text=DC%20Bikeshare%20Analytics&fontSize=40&fontColor=fff&animation=fadeIn&fontAlignY=38" alt="Header Banner" width="100%">
</div>

<h1>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Bicycle.png" alt="Bicycle Emoji" width="40px"/> 
  Capital Bikeshare Demand Analysis
</h1>

<div align="center">
  <h3>
    <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" width="25px" align="center" alt="Chart Emoji"/> 
    Unlocking Urban Mobility Insights through Data
  </h3>
  
  <p>
    <em>A comprehensive data engineering and analytics pipeline analyzing 2M+ trips to optimize fleet operations and understand commuter behavior in Washington, DC.</em>
  </p>

  <br>

  <a href="https://dc-bikeshare-demand-analysis-ycklasmcgsozwy87bsdgzr.streamlit.app/">
    <img src="https://img.shields.io/badge/Streamlit-Launch_Live_Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" height="40" alt="Launch Streamlit App"/>
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://daniel21b.github.io/DC-Bikeshare-Demand-Analysis/">
    <img src="https://img.shields.io/badge/GitHub_Pages-View_Hypothesis_Docs-222222?style=for-the-badge&logo=githubpages&logoColor=white" height="40" alt="View Documentation"/>
  </a>
</div>

<br>

---

## <div><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Right.png" width="30px" align="center" alt="Magnifying Glass"/> Project Overview</div>

This project implements a full-stack data analysis pipeline to decode the usage patterns of the **Capital Bikeshare** system. By processing over **2 million trip records**, this application provides actionable intelligence for fleet rebalancing, peak demand forecasting, and user segmentation.

The solution features a robust **Streamlit Dashboard** for interactive exploration and a detailed **GitHub Pages** documentation site that breaks down the statistical hypothesis testing.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" width="25px" align="center"/> Key Insights
<ul>
  <li>
    <strong>Commuter Dominance:</strong> Identified a rigid bi-modal distribution in weekday usage, confirming the system is primarily a commuter utility.
  </li>
  <li>
    <strong>Operational Peaks:</strong> Pinpointed critical demand windows at <strong>8:00 AM</strong> and <strong>5:00 PM</strong>, necessitating targeted station rebalancing.
  </li>
  <li>
    <strong>User Segmentation:</strong> Revealed distinct behavioral differences between <em>Members</em> (efficiency-focused) and <em>Casual Users</em> (leisure-focused).
  </li>
</ul>

<br>

## <div><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Laptop.png" width="30px" align="center" alt="Laptop Emoji" /> Tech Stack</div>

<div align="left">

### Core Infrastructure
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

### Data Engineering & Analysis
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

### Visualization
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=python&logoColor=white)

</div>

<br>

## <div><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Map%20of%20Japan.png" width="30px" align="center" alt="Map Emoji" /> Dashboard Features</div>

The deployed application includes four specialized analytics views:

| View | Description |
| :--- | :--- |
| **📊 Executive Summary** | High-level KPIs, 7-day trend analysis, and system health metrics for stakeholders. |
| **⏰ Temporal Patterns** | Hourly heatmaps and rush-hour analysis separating weekday vs. weekend behaviors. |
| **🗺️ Station Analysis** | Geospatial mapping of the top 15 start/end stations and route popularity rankings. |
| **👥 User Behavior** | Deep dive into Member vs. Casual rider duration, trip frequency, and bike type preference. |

<br>

## <div><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Books.png" width="30px" align="center" alt="Books Emoji" /> Project Structure</div>

```bash
├── 📁 data/                  # Processed parquet files (optimized for speed)
├── 📁 notebooks/             # Jupyter notebooks for data pipeline
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
│   └── 04_visualizations.ipynb
├── 📁 src/                   # Helper scripts (Weather API integration)
├── 📄 app.py                 # Main Streamlit application entry point
└── 📄 requirements.txt       # Project dependencies
