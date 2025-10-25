"""
Weather Data Collection Module for DC Bikeshare Analysis

This module provides functions to fetch historical weather data for the DC area.
Supports OpenWeather API and NOAA data sources.
"""

import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

DC_LAT = 38.9072
DC_LON = -77.0369


def fetch_historical_weather(start_date, end_date, api_key=None):
    """
    Fetch historical weather data for DC area using OpenWeather Time Machine API.
    
    Note: OpenWeather historical data beyond 5 days requires a paid subscription.
    For free alternatives, use NOAA Climate Data Online.
    
    Parameters:
    -----------
    start_date : datetime
        Start date for weather data collection
    end_date : datetime
        End date for weather data collection
    api_key : str, optional
        OpenWeather API key (uses env variable if not provided)
    
    Returns:
    --------
    pd.DataFrame
        Weather data with columns: date, temp, feels_like, humidity, clouds, 
        wind_speed, weather_main, weather_desc
    """
    if api_key is None:
        api_key = API_KEY
    
    if not api_key:
        raise ValueError("API key not found. Set OPENWEATHER_API_KEY in .env file")
    
    base_url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    
    weather_data = []
    current_date = start_date
    
    print(f"Fetching weather data from {start_date.date()} to {end_date.date()}...")
    
    while current_date <= end_date:
        timestamp = int(time.mktime(current_date.timetuple()))
        
        params = {
            'lat': DC_LAT,
            'lon': DC_LON,
            'dt': timestamp,
            'appid': api_key,
            'units': 'imperial'
        }
        
        try:
            response = requests.get(base_url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                daily_data = data['current']
                
                weather_data.append({
                    'date': current_date.date(),
                    'temp': daily_data['temp'],
                    'feels_like': daily_data['feels_like'],
                    'humidity': daily_data['humidity'],
                    'clouds': daily_data['clouds'],
                    'wind_speed': daily_data['wind_speed'],
                    'weather_main': daily_data['weather'][0]['main'],
                    'weather_desc': daily_data['weather'][0]['description']
                })
                
                print(f"✓ {current_date.date()}")
                
            elif response.status_code == 401:
                raise ValueError("Invalid API key")
            elif response.status_code == 429:
                print("Rate limit reached. Waiting 60 seconds...")
                time.sleep(60)
                continue
            else:
                print(f"✗ Error {response.status_code} for {current_date.date()}")
            
            time.sleep(1)
            
        except Exception as e:
            print(f"✗ Error fetching data for {current_date}: {e}")
        
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(weather_data)
    print(f"\nSuccessfully fetched {len(df)} days of weather data")
    
    return df


def fetch_current_weather(api_key=None):
    """
    Fetch current weather conditions for DC area.
    
    Parameters:
    -----------
    api_key : str, optional
        OpenWeather API key
    
    Returns:
    --------
    dict
        Current weather data
    """
    if api_key is None:
        api_key = API_KEY
    
    if not api_key:
        raise ValueError("API key not found")
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'lat': DC_LAT,
        'lon': DC_LON,
        'appid': api_key,
        'units': 'imperial'
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather: {response.status_code}")


def load_noaa_weather_data(file_path):
    """
    Load and process NOAA weather data from CSV file.
    
    NOAA Climate Data Online: https://www.ncdc.noaa.gov/cdo-web/
    Recommended station: Reagan National Airport (DCA)
    
    Parameters:
    -----------
    file_path : str
        Path to NOAA CSV file
    
    Returns:
    --------
    pd.DataFrame
        Processed weather data
    """
    df = pd.read_csv(file_path)
    
    df['date'] = pd.to_datetime(df['DATE']).dt.date
    
    column_mapping = {
        'TMAX': 'temp_max',
        'TMIN': 'temp_min',
        'PRCP': 'precipitation',
        'AWND': 'wind_speed',
        'SNOW': 'snow',
        'SNWD': 'snow_depth'
    }
    
    for old_col, new_col in column_mapping.items():
        if old_col in df.columns:
            df[new_col] = df[old_col]
    
    if 'temp_max' in df.columns and 'temp_min' in df.columns:
        df['temp_avg'] = (df['temp_max'] + df['temp_min']) / 2
    
    if 'precipitation' in df.columns:
        df['is_rainy'] = df['precipitation'] > 0
    
    return df


def create_weather_categories(weather_df):
    """
    Add categorical weather features to dataframe.
    
    Parameters:
    -----------
    weather_df : pd.DataFrame
        Weather dataframe with temp_avg column
    
    Returns:
    --------
    pd.DataFrame
        Weather dataframe with additional categorical columns
    """
    df = weather_df.copy()
    
    if 'temp_avg' in df.columns:
        def categorize_temp(temp):
            if temp < 32:
                return 'Freezing'
            elif temp < 50:
                return 'Cold'
            elif temp < 70:
                return 'Mild'
            elif temp < 85:
                return 'Warm'
            else:
                return 'Hot'
        
        df['temp_category'] = df['temp_avg'].apply(categorize_temp)
    
    if 'weather_main' in df.columns:
        df['is_clear'] = df['weather_main'] == 'Clear'
        df['is_rainy'] = df['weather_main'].isin(['Rain', 'Drizzle', 'Thunderstorm'])
        df['is_snowy'] = df['weather_main'].isin(['Snow', 'Sleet'])
    
    return df


def get_weather_summary(weather_df):
    """
    Generate summary statistics for weather data.
    
    Parameters:
    -----------
    weather_df : pd.DataFrame
        Weather dataframe
    
    Returns:
    --------
    dict
        Summary statistics
    """
    summary = {}
    
    if 'temp_avg' in weather_df.columns:
        summary['avg_temp'] = weather_df['temp_avg'].mean()
        summary['min_temp'] = weather_df['temp_avg'].min()
        summary['max_temp'] = weather_df['temp_avg'].max()
    
    if 'precipitation' in weather_df.columns:
        summary['total_precip'] = weather_df['precipitation'].sum()
        summary['rainy_days'] = (weather_df['precipitation'] > 0).sum()
    
    if 'weather_main' in weather_df.columns:
        summary['weather_distribution'] = weather_df['weather_main'].value_counts().to_dict()
    
    return summary


if __name__ == "__main__":
    print("DC Bikeshare Weather API Module")
    print("=" * 50)
    print(f"DC Coordinates: {DC_LAT}, {DC_LON}")
    print(f"API Key loaded: {'Yes' if API_KEY else 'No'}")
    
    try:
        current = fetch_current_weather()
        print(f"\nCurrent Weather in DC:")
        print(f"  Temperature: {current['main']['temp']:.1f}°F")
        print(f"  Conditions: {current['weather'][0]['description']}")
        print(f"  Humidity: {current['main']['humidity']}%")
        print(f"  Wind Speed: {current['wind']['speed']} mph")
    except Exception as e:
        print(f"\nCould not fetch current weather: {e}")

