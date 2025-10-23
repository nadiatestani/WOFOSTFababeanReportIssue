
import matplotlib
matplotlib.style.use("ggplot")
import matplotlib.pyplot as plt
import pandas as pd

def plot_N_rates(df_outputs, nfix_fr, sowingdate):
    """Calculate N rates based on WOFOST outputs and a given N fixation fraction.
    
    Parameters
    ----------
    df_outputs : pd.DataFrame
        DataFrame containing WOFOST simulation outputs.
    nfix_fr : float
        Fraction of nitrogen fixation (between 0 and 1).
    
    Returns
    -------
    plt.plot with calculated N rates.
    """
    plt.figure(figsize = (10,5), dpi = 150)
    plt.plot(df_outputs["day"], df_outputs["Ndemand"], label="Ndemand", alpha = 0.8) 
    plt.plot(df_outputs["day"], df_outputs["RNuptake"], label="RNUptake", linestyle='--', alpha = 0.8) 
    plt.plot(df_outputs['day'], df_outputs['RNfixation'], label=f'RNfixation') 
    plt.plot(df_outputs['day'], df_outputs["RNuptake"] + df_outputs['RNfixation'], linestyle=':', c = 'k', label=f'RNuptake + RNfixation') 

    plt.xlabel('Date')
    plt.ylabel('kg N ha-1 d-1')
    plt.title(f'Wofost81_NWLP_MLWB_SNOMIN NFIX_FR {nfix_fr}')
    plt.axvline(pd.to_datetime(sowingdate), color='red', linestyle='--', label='Sowing date')
    legend = plt.legend(loc='upper left')
    plt.show()

def plot_N_rates_cumsum(df_outputs, nfix_fr, sowingdate):
    """Calculate N rates based on WOFOST outputs and a given N fixation fraction.
    
    Parameters
    ----------
    df_outputs : pd.DataFrame
        DataFrame containing WOFOST simulation outputs.
    nfix_fr : float
        Fraction of nitrogen fixation (between 0 and 1).
    
    Returns
    -------
    plt.plot with calculated N rates.
    """
    plt.figure(figsize = (10,5), dpi = 150)
    plt.plot(df_outputs["day"], df_outputs["Ndemand"].cumsum(), label="Ndemand.cumsum()", alpha = 0.8) 
    plt.plot(df_outputs["day"], df_outputs["RNuptake"].cumsum(), label="RNUptake.cumsum()", linestyle='--', alpha = 0.8) 
    plt.plot(df_outputs['day'], df_outputs['RNfixation'].cumsum(), label=f'RNfixation.cumsum()') 
    plt.plot(df_outputs['day'], df_outputs["RNuptake"].cumsum() + df_outputs['RNfixation'].cumsum(), linestyle=':', c = 'k', label=f'RNuptake.cumsum() + RNfixation.cumsum()') 

    plt.xlabel('Date')
    plt.ylabel('kg N ha-1')
    plt.title(f'Wofost81_NWLP_MLWB_SNOMIN NFIX_FR {nfix_fr}')
    plt.axvline(pd.to_datetime(sowingdate), color='red', linestyle='--', label='Sowing date')
    legend = plt.legend(loc='upper left')
    plt.show()

def plot_root_depth(df_outputs, nfix_fr, sowingdate):
    """Plot root depth based on WOFOST outputs and a given N fixation fraction.
    
    Parameters
    ----------
    df_outputs : pd.DataFrame
        DataFrame containing WOFOST simulation outputs.
    nfix_fr : float
        Fraction of nitrogen fixation (between 0 and 1).
    
    Returns
    -------
    plt.plot with root depth.
    """
    plt.figure(figsize = (10,5), dpi = 150)
    plt.plot(df_outputs["day"], df_outputs["RD"], label="RD", alpha = 0.8) 
    plt.xlabel('Date')
    plt.ylabel('cm')
    plt.title(f'Wofost81_NWLP_MLWB_SNOMIN NFIX_FR {nfix_fr}')
    plt.axvline(pd.to_datetime(sowingdate), color='red', linestyle='--', label='Sowing date')
    legend = plt.legend(loc='upper left')
    plt.show()

def plot_NH4_NO3(df_outputs, nfix_fr, sowingdate):
    """Plot soil NH4 and NO3 based on WOFOST outputs and a given N fixation fraction.
    
    Parameters
    ----------
    df_outputs : pd.DataFrame
        DataFrame containing WOFOST simulation outputs.
    nfix_fr : float
        Fraction of nitrogen fixation (between 0 and 1).
    
    Returns
    -------
    plt.plot with soil NH4 and NO3.
    """
    plt.figure(figsize = (10,5), dpi = 150)
    for i in range(3):
        plt.plot(df_outputs['day'], df_outputs['NH4'].apply(lambda x: x[i]), label=f'NH4 in {i} soil layer')
    for i in range(3):
        plt.plot(df_outputs['day'], df_outputs['NO3'].apply(lambda x: x[i]), label=f'NO3 in {i} soil layer')
    plt.xlabel('Date')
    plt.ylabel('kg N ha-1 d-1')
    plt.title(f'Wofost81_NWLP_MLWB_SNOMIN NFIX_FR {nfix_fr}')
    plt.axvline(pd.to_datetime(sowingdate), color='red', linestyle='--', label='Sowing date')
    legend = plt.legend(loc='upper left')
    plt.show()

def plot_TAGB(df_outputs, nfix_fr, sowingdate):
    """Plot total above-ground biomass based on WOFOST outputs and a given N fixation fraction.
    
    Parameters
    ----------
    df_outputs : pd.DataFrame
        DataFrame containing WOFOST simulation outputs.
    nfix_fr : float
        Fraction of nitrogen fixation (between 0 and 1).
    
    Returns
    -------
    plt.plot with total above-ground biomass.
    """
    plt.figure(figsize = (10,5), dpi = 150)
    plt.plot(df_outputs['day'], df_outputs['TAGP'], label='TAGP')
    plt.xlabel('Date')
    plt.ylabel('kg ha-1')
    plt.title(f'Wofost81_NWLP_MLWB_SNOMIN NFIX_FR {nfix_fr}')
    plt.axvline(pd.to_datetime(sowingdate), color='red', linestyle='--', label='Sowing date')
    legend = plt.legend(loc='upper left')
    plt.show()