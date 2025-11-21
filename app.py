import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# -----------------------------------------------------------------------------
# Page Config
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="DC Bikeshare Analytics",
    page_icon=":material/pedal_bike:",
    layout="wide",
)

# -----------------------------------------------------------------------------
# Data Loading
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    """Load and cache the cleaned bikeshare data"""
    df = pd.read_parquet('data/processed/bikeshare_cleaned.parquet')
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    df['date'] = pd.to_datetime(df['date'])
    return df

# -----------------------------------------------------------------------------
# Helper: Clean Plotly Layout
# -----------------------------------------------------------------------------
def clean_plot(fig):
    """Applies a cleaner layout to match the dashboard aesthetic"""
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_family="sans-serif",
    )
    return fig

# -----------------------------------------------------------------------------
# View Functions
# -----------------------------------------------------------------------------

def view_executive_summary(df):
    """Executive Summary View"""
    
    # Top Metrics Row
    cols = st.columns(4)
    metrics = [
        ("Total Trips", f"{len(df):,}", "July 2025"),
        ("Avg Duration", f"{df['duration_min'].mean():.1f} min", None),
        ("Member Share", f"{(df['member_casual'] == 'member').sum() / len(df) * 100:.1f}%", None),
        ("Peak Hour", f"{df.groupby('hour').size().idxmax()}:00", None),
    ]
    
    for col, (label, value, delta) in zip(cols, metrics):
        with col.container(border=True):
            st.metric(label, value, delta)

    st.write("") # Spacer

    # Charts Row 1
    c1, c2 = st.columns([2, 1])
    
    with c1.container(border=True):
        st.markdown("##### :material/timeline: Daily Trip Volume")
        daily_trips = df.groupby(df['date']).size().reset_index(name='trips')
        fig = px.line(daily_trips, x='date', y='trips', labels={'date': '', 'trips': ''})
        fig.update_traces(line_color='#1f77b4', line_width=2)
        st.plotly_chart(clean_plot(fig), use_container_width=True)

    with c2.container(border=True):
        st.markdown("##### :material/pie_chart: User Distribution")
        user_counts = df['member_casual'].value_counts()
        fig = px.pie(
            values=user_counts.values, 
            names=user_counts.index,
            color_discrete_sequence=['#2ecc71', '#e74c3c'],
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent')
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

    # Charts Row 2
    with st.container(border=True):
        st.markdown("##### :material/directions_bike: Bike Type Preference")
        bike_by_user = pd.crosstab(df['rideable_type'], df['member_casual'], normalize='columns') * 100
        fig = px.bar(
            bike_by_user,
            barmode='group',
            color_discrete_sequence=['#3498db', '#e67e22']
        )
        fig.update_layout(xaxis_title=None, yaxis_title="Percentage (%)")
        st.plotly_chart(clean_plot(fig), use_container_width=True)

def view_temporal_patterns(df):
    """Temporal Analysis View"""
    
    # Sub-navigation
    period = st.pills("Time Scale", ["Hourly", "Daily", "Categories"], default="Hourly")
    st.write("")

    if period == "Hourly":
        c1, c2 = st.columns(2)
        with c1.container(border=True):
            st.markdown("##### Total Trips by Hour")
            hourly_trips = df.groupby('hour').size().reset_index(name='trips')
            fig = px.bar(hourly_trips, x='hour', y='trips', color='trips', color_continuous_scale='Blues')
            fig.update_layout(showlegend=False)
            st.plotly_chart(clean_plot(fig), use_container_width=True)

        with c2.container(border=True):
            st.markdown("##### Hourly by User Type")
            hourly_by_user = df.groupby(['hour', 'member_casual']).size().reset_index(name='trips')
            fig = px.line(
                hourly_by_user, x='hour', y='trips', color='member_casual',
                color_discrete_map={'member': '#2ecc71', 'casual': '#e74c3c'}
            )
            st.plotly_chart(clean_plot(fig), use_container_width=True)
            
        with st.container(border=True):
            st.markdown("##### :material/traffic: Rush Hour Analysis")
            rush_hour_df = df.groupby(['hour', 'is_rush_hour']).size().reset_index(name='trips')
            rush_hour_df['category'] = rush_hour_df['is_rush_hour'].map({True: 'Rush Hour', False: 'Off-Peak'})
            fig = px.bar(
                rush_hour_df, x='hour', y='trips', color='category',
                color_discrete_map={'Rush Hour': '#e74c3c', 'Off-Peak': '#95a5a6'}
            )
            st.plotly_chart(clean_plot(fig), use_container_width=True)

    elif period == "Daily":
        with st.container(border=True):
            st.markdown("##### Weekly Patterns")
            day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            daily_trips = df.groupby('day_name').size().reindex(day_order).reset_index(name='trips')
            fig = px.bar(daily_trips, x='day_name', y='trips', color='trips', color_continuous_scale='Viridis')
            st.plotly_chart(clean_plot(fig), use_container_width=True)

        with st.container(border=True):
            st.markdown("##### Heatmap: Hour vs Day")
            heatmap_data = df.groupby(['day_name', 'hour']).size().reset_index(name='trips')
            heatmap_pivot = heatmap_data.pivot(index='day_name', columns='hour', values='trips')
            heatmap_pivot = heatmap_pivot.reindex(day_order)
            fig = px.imshow(heatmap_pivot, color_continuous_scale='YlOrRd', aspect='auto')
            st.plotly_chart(clean_plot(fig), use_container_width=True)

    else: # Categories
        with st.container(border=True):
            st.markdown("##### Usage by Time Category")
            time_cat_trips = df['time_category'].value_counts().reset_index()
            time_cat_trips.columns = ['time_category', 'trips']
            fig = px.bar(time_cat_trips, x='time_category', y='trips', color='trips', color_continuous_scale='Plasma')
            st.plotly_chart(clean_plot(fig), use_container_width=True)

def view_station_analysis(df):
    """Station Analysis View"""
    
    # Sub-nav
    view_type = st.pills("View", ["Rankings", "Map", "Routes"], default="Rankings")
    st.write("")

    if view_type == "Rankings":
        c1, c2 = st.columns(2)
        with c1.container(border=True):
            st.markdown("##### :material/arrow_upward: Top Start Stations")
            top_start = df['start_station_name'].value_counts().head(15).reset_index()
            top_start.columns = ['station', 'trips']
            fig = px.bar(top_start, y='station', x='trips', orientation='h', color='trips', color_continuous_scale='Blues')
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(clean_plot(fig), use_container_width=True)
            
        with c2.container(border=True):
            st.markdown("##### :material/arrow_downward: Top End Stations")
            top_end = df['end_station_name'].value_counts().head(15).reset_index()
            top_end.columns = ['station', 'trips']
            fig = px.bar(top_end, y='station', x='trips', orientation='h', color='trips', color_continuous_scale='Greens')
            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(clean_plot(fig), use_container_width=True)

    elif view_type == "Map":
        with st.container(border=True):
            st.markdown("##### :material/map: Station Heatmap")
            station_usage = df.groupby(['start_station_name', 'start_lat', 'start_lng']).size().reset_index(name='trips')
            fig = px.scatter_mapbox(
                station_usage, lat='start_lat', lon='start_lng', size='trips',
                color='trips', zoom=11, height=600, mapbox_style='open-street-map'
            )
            st.plotly_chart(clean_plot(fig), use_container_width=True)

    else: # Routes
        with st.container(border=True):
            st.markdown("##### :material/route: Popular Routes")
            top_routes = df['route'].value_counts().head(20).reset_index()
            top_routes.columns = ['route', 'trips']
            fig = px.bar(top_routes, y='route', x='trips', orientation='h', color='trips', color_continuous_scale='Oranges')
            fig.update_layout(yaxis={'categoryorder': 'total ascending'}, height=600)
            st.plotly_chart(clean_plot(fig), use_container_width=True)

def view_user_behavior(df):
    """User Behavior View"""
    
    c1, c2 = st.columns([1, 1])
    
    with c1.container(border=True):
        st.markdown("##### Member vs Casual: Daily Usage")
        user_by_day = df.groupby(['day_name', 'member_casual']).size().reset_index(name='trips')
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        user_by_day['day_name'] = pd.Categorical(user_by_day['day_name'], categories=day_order, ordered=True)
        user_by_day = user_by_day.sort_values('day_name')
        
        fig = px.line(
            user_by_day, x='day_name', y='trips', color='member_casual',
            color_discrete_map={'member': '#2ecc71', 'casual': '#e74c3c'}
        )
        st.plotly_chart(clean_plot(fig), use_container_width=True)
        
    with c2.container(border=True):
        st.markdown("##### Trip Duration Distribution")
        fig = px.box(
            df, x='member_casual', y='duration_min', color='member_casual',
            color_discrete_map={'member': '#2ecc71', 'casual': '#e74c3c'}
        )
        fig.update_yaxis(range=[0, 60])
        st.plotly_chart(clean_plot(fig), use_container_width=True)

def view_peak_demand(df):
    """Peak Demand View"""
    
    # Hypothesis Box
    with st.container(border=True):
        st.markdown("""
        **Hypothesis:** DC Capital Bikeshare exhibits a commuter-driven usage pattern, with peak demand 
        concentrated during weekday rush hours (7-9 AM and 5-7 PM).
        """)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Rush Hour Trips", f"{(df['is_rush_hour'].sum()/len(df)*100):.1f}%")
        c2.metric("Weekday Trips", f"{((~df['is_weekend']).sum()/len(df)*100):.1f}%")
        c3.metric("Member Usage", f"{((df['member_casual'] == 'member').sum()/len(df)*100):.1f}%")

    st.write("")

    c1, c2 = st.columns(2)
    with c1.container(border=True):
        st.markdown("##### :material/access_time: Peak Hours")
        hourly_trips = df.groupby('hour').size().reset_index(name='trips')
        hourly_trips['is_peak'] = hourly_trips['hour'].isin([7, 8, 9, 17, 18, 19])
        fig = px.bar(
            hourly_trips, x='hour', y='trips', color='is_peak',
            color_discrete_map={True: '#e74c3c', False: '#95a5a6'}
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(clean_plot(fig), use_container_width=True)

    with c2.container(border=True):
        st.markdown("##### Weekday vs Weekend")
        weekday_hour = df[~df['is_weekend']].groupby('hour').size().reset_index(name='trips')
        weekend_hour = df[df['is_weekend']].groupby('hour').size().reset_index(name='trips')
        weekday_hour['type'] = 'Weekday'
        weekend_hour['type'] = 'Weekend'
        combined = pd.concat([weekday_hour, weekend_hour])
        
        fig = px.line(
            combined, x='hour', y='trips', color='type',
            color_discrete_map={'Weekday': '#3498db', 'Weekend': '#f39c12'}
        )
        st.plotly_chart(clean_plot(fig), use_container_width=True)

# -----------------------------------------------------------------------------
# Main Application Layout
# -----------------------------------------------------------------------------

def main():
    """
    Main layout using the 'Stock Peer Analysis' dashboard structure:
    - Split Layout: Left Control Panel (1), Right Content Panel (3)
    - Card-like containers for all distinct visual elements
    - Material icons instead of emojis
    """
    
    # Header
    st.markdown("""
    # :material/pedal_bike: DC Bikeshare Analysis
    Comprehensive analysis of Capital Bikeshare usage patterns.
    """)
    st.write("") # Spacer

    # Load Data
    try:
        with st.spinner("Loading dataset..."):
            df = load_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

    # Main Grid Layout
    cols = st.columns([1, 3])
    
    # -------------------------------------------------------------------------
    # Left Panel: Controls & Global Stats
    # -------------------------------------------------------------------------
    left_panel = cols[0].container(border=True, height=600)
    
    with left_panel:
        st.markdown("### :material/settings: Controls")
        
        # Navigation
        analysis_view = st.radio(
            "Select Analysis View",
            ["Executive Summary", "Temporal Patterns", "Station Analysis", "User Behavior", "Peak Demand Insights"],
            index=0
        )
        
        st.divider()
        
        st.markdown("### :material/dataset: Dataset Stats")
        
        # Dataset Metrics in a clean vertical layout
        st.metric("Total Trips", f"{len(df):,}")
        st.metric("Unique Stations", f"{df['start_station_name'].nunique():,}")
        st.metric("Routes", f"{df['route'].nunique():,}")
        
        st.caption(f"Range: {df['started_at'].min().strftime('%b %d')} - {df['started_at'].max().strftime('%b %d, %Y')}")
        
        st.divider()
        
        st.markdown("""
        **About**
        This dashboard visualizes demand, user behavior, and operational insights for the DC Capital Bikeshare system.
        """)

    # -------------------------------------------------------------------------
    # Right Panel: Main Visualization Area
    # -------------------------------------------------------------------------
    right_panel = cols[1].container(border=True)
    
    with right_panel:
        if analysis_view == "Executive Summary":
            st.markdown("## Executive Summary")
            view_executive_summary(df)
            
        elif analysis_view == "Temporal Patterns":
            st.markdown("## Temporal Usage Patterns")
            view_temporal_patterns(df)
            
        elif analysis_view == "Station Analysis":
            st.markdown("## Station Usage Analysis")
            view_station_analysis(df)
            
        elif analysis_view == "User Behavior":
            st.markdown("## User Behavior")
            view_user_behavior(df)
            
        elif analysis_view == "Peak Demand Insights":
            st.markdown("## Peak Demand & Hypotheses")
            view_peak_demand(df)

if __name__ == "__main__":
    main()