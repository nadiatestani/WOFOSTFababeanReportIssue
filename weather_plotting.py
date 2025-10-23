# weather_plotting.py
import pandas as pd
import matplotlib.pyplot as plt

#WOFOST weather data plotting module

# Define the units for each weather variable
units = {
    'TMAX': '°C',
    'TMIN': '°C',
    'VAP': 'kPa',
    'WIND': 'm/s',
    'RAIN': 'mm',
    'IRRAD': 'kJ/m²',
    'SNOWDEPTH': 'cm'
}
def plot_weather_variable(df, var, inidate, enddate):
    """
    Plot a weather variable from wofost weather DataFrame within a specified date range.
    
    Parameters:
    df (DataFrame): DataFrame containing weather data with a 'DAY' column.
    var (str): Variable to plot (e.g., 'TMAX').
    unit (str): Unit of the variable (e.g., '°C').
    inidate (str): Start date for filtering (format 'YYYY-MM-DD').
    enddate (str): End date for filtering (format 'YYYY-MM-DD').
    """
    plt.figure(figsize=(10, 5), dpi=150, facecolor='white')
    df_plot = df.copy()  # Create a copy of the DataFrame for plotting
    df_plot['DAY'] = pd.to_datetime(df_plot['DAY'], format='%Y%m%d')  # Convert to datetime\
    df_plot = df_plot.set_index('DAY')  # Set 'DAY' as index
    df_plot = df_plot.loc[inidate:enddate] # Filter the DataFrame for the specified date range
    unit = units[var]
    plt.plot(df_plot.index, df_plot[var], label=var, color='red', linewidth=2)
    plt.title(f"{var} from {inidate} to {enddate}")
    plt.xlabel('Date')
    plt.ylabel(f"{var} {unit}")
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_weather_variable_cum_sum(df, var, inidate, enddate):
    """
    Plot cumulative sum of a weather variable from WOFOST weather DataFrame within a specified date range.
    
    Parameters:
    df (DataFrame): DataFrame containing weather data with a 'DAY' column.
    var (str): Variable to plot (e.g., 'TMAX').
    inidate (str): Start date for filtering (format 'YYYY-MM-DD').
    enddate (str): End date for filtering (format 'YYYY-MM-DD').
    """
    plt.figure(figsize=(10, 5), dpi=150, facecolor='white')
    df_plot = df.copy()
    df_plot['DAY'] = pd.to_datetime(df_plot['DAY'], format='%Y%m%d')
    df_plot = df_plot.set_index('DAY')
    
    # Filtrar rango de fechas
    df_plot = df_plot.loc[inidate:enddate]
    
    # Calcular suma acumulada
    df_plot[f'{var}_cumsum'] = df_plot[var].cumsum()
    
    # Obtener unidades (opcional, si tenés un diccionario llamado units)
    unit = units[var]
    
    # Plot
    plt.plot(df_plot.index, df_plot[f'{var}_cumsum'], label=f'Cumulative {var}', color='red', linewidth=2)
    plt.title(f"Cumulative sum of {var} from {inidate} to {enddate}")
    plt.xlabel('Date')
    plt.ylabel(f"{var} cumulative sum {unit}")
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_gdd_cumsum(df, tmin_col, tmax_col, tbase, inidate, enddate):
    """
    Plot cumulative growing degree days (GDD) from WOFOST weather DataFrame within a date range.

    Parameters:
    df (DataFrame): Weather DataFrame with 'DAY', Tmin, Tmax columns.
    tmin_col (str): Column name for daily minimum temperature (e.g., 'TMIN').
    tmax_col (str): Column name for daily maximum temperature (e.g., 'TMAX').
    tbase (float): Base temperature for GDD calculation.
    inidate (str): Start date (e.g., 'YYYY-MM-DD').
    enddate (str): End date (e.g., 'YYYY-MM-DD').
    """
    plt.figure(figsize=(10, 5), dpi=150, facecolor='white')
    df_plot = df.copy()
    df_plot['DAY'] = pd.to_datetime(df_plot['DAY'], format='%Y%m%d')
    df_plot = df_plot.set_index('DAY')
    df_plot = df_plot.loc[inidate:enddate]

    # Calcular GDD diarios
    df_plot['GDD'] = ((df_plot[tmax_col] + df_plot[tmin_col]) / 2) - tbase
    df_plot['GDD'] = df_plot['GDD'].clip(lower=0)

    # Suma acumulada
    df_plot['GDD_cumsum'] = df_plot['GDD'].cumsum()

    # Plot
    plt.plot(df_plot.index, df_plot['GDD_cumsum'], label=f'Cumulative GDD (Tbase={tbase}°C)', color='green', linewidth=2)
    plt.legend()
    plt.title(f'Cumulative Growing Degree Days from {inidate} to {enddate}')
    plt.xlabel('Date')
    plt.ylabel('Cumulative GDD (°C days)')
    plt.grid()
    plt.tight_layout()
    plt.show()