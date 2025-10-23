import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def f_SMcurves(soil):
    PFFieldCapacity = soil['SoilProfileDescription']['PFFieldCapacity']
    SMcurves = dict()
    for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers']))):
        pFs = soil['SoilProfileDescription']['SoilLayers'][i]['SMfromPF']
        pFs_vect = [None] * int(len(pFs)/2)
        SMs_vect = [None] * int(len(pFs)/2)
        for j in range(0, int(len(pFs)/2)):
            pFs_vect[j] = pFs[int(j * 2)]
            SMs_vect[j] = pFs[int(j * 2 + 1)]
        SMcurves_i = pd.DataFrame([pFs_vect, SMs_vect]).transpose()
        SMcurves_i.columns = ['PF', 'SM']
        SMcurves[i] = SMcurves_i
    return(SMcurves)

def SMprofileplot(soil, output_df, time):
    '''
    Plot the SM profile at diff times (int)
    '''
    sm_0 = output_df["SM"][time] 
    SMcurves = f_SMcurves(soil)
    layers = [soil['SoilProfileDescription']['SoilLayers'][i]['Thickness'] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_fieldcapacity = [SMcurves[i][SMcurves[i]['PF'] == 2.0]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_wiltingpoint = [SMcurves[i][SMcurves[i]['PF'] == 4.2]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_saturation = [SMcurves[i][SMcurves[i]['PF'] == -1]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_air = [sm_wiltingpoint[i] - 0.02 for i in range(0,len(sm_wiltingpoint))]

    # Mid points of each layer
    midpoints = [sum(layers[:i]) + layers[i] / 2 for i in range(len(layers))] + [sum(layers)]
    sm_0 =  [sm_0[i] for i in range(len(sm_0))]  + [sm_0[len(sm_0)-1]] # Convertir a lista para el gráfico
    sm_fieldcapacity = sm_fieldcapacity + [sm_fieldcapacity[-1]]
    sm_wiltingpoint = sm_wiltingpoint + [sm_wiltingpoint[-1]]
    sm_saturation = sm_saturation + [sm_saturation[-1]]
    sm_air = sm_air + [sm_air[-1]]

    # Plot
    plt.figure(figsize=(8, 6), dpi = 150)
    plt.plot(sm_fieldcapacity, midpoints, marker='.', linestyle='--', label='Soil Moisture at field capacity', color='red')
    plt.plot(sm_wiltingpoint, midpoints, marker='.', linestyle='--', label='Soil Moisture at wilting point', color='blue')
    plt.plot(sm_saturation, midpoints, marker='.', linestyle='--', label='Soil Moisture at saturation', color='green')
    plt.plot(sm_air, midpoints, marker='.', linestyle='--', label='Soil Air Content', color='orange')
    # Fill the area between field capacity and wilting point
    plt.fill_betweenx(midpoints, sm_fieldcapacity, sm_wiltingpoint, color='lightblue', alpha=0.5, label='Plant-Available Water')
    plt.plot(sm_0, midpoints, marker='.', linestyle='-', label= f'Soil Moisture Profile - Time {time}', color ='black')
    plt.gca().invert_yaxis() # Invert Y 
    
    # Title and tags
    plt.xlabel('Soil Moisture (cm³/cm³)')
    plt.ylabel('Depth (cm)')
    plt.title(f'Soil Moisture Profile - Time {time}')
    plt.grid(True)
    plt.ylim((100, 0))  
    plt.legend()

    # Show plot
    plt.show()

def SMdynamicplot(soil, output_df, layer, soiltype):
    '''
    Plot the SM dynamic per layer (int)
    '''
    SMcurves = f_SMcurves(soil)
    layers = [soil['SoilProfileDescription']['SoilLayers'][i]['Thickness'] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_fieldcapacity = [SMcurves[i][SMcurves[i]['PF'] == 2.0]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_wiltingpoint = [SMcurves[i][SMcurves[i]['PF'] == 4.2]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_saturation = [SMcurves[i][SMcurves[i]['PF'] == -1]['SM'].values[0] for i in list(np.arange(0, len(soil['SoilProfileDescription']['SoilLayers'])))]
    sm_air = [sm_wiltingpoint[i] - 0.02 for i in range(0,len(sm_wiltingpoint))]

    plt.figure(figsize=(10, 5), dpi=150)
    #plt.title(f"Volumetric Soil Moisture Content in Layer {i+1} ({soil['SoilProfileDescription']['SoilLayers'][i]['Name']})")
    plt.axhline(y = sm_fieldcapacity[layer], label="SM field capacity", color='red' , linestyle='--')
    plt.axhline(y = sm_wiltingpoint[layer], label="SM wilting point", color='blue', linestyle='--')
    plt.axhline(y = sm_saturation[layer], label="SM saturation", color='green', linestyle='--')
    plt.axhline(y = sm_air[layer], label="SM air content", color='orange', linestyle='--')
    # Fill the area between field capacity and wilting point
    
    # Fill the area between wilting point and field capacity
    plt.axhspan(sm_wiltingpoint[layer], sm_fieldcapacity[layer], color='lightblue', alpha=0.5, label='Plant-Available Water')

    plt.plot(output_df["date_col"], output_df["SM"].apply(lambda x: x[layer]), label=f"SM layer {layer}", color='black')

    plt.xlabel('Date')
    plt.ylabel('Soil Moisture (cm³/cm³)')
    plt.legend()
    plt.grid(True)
    plt.ylim((0, 1))  
    plt.legend()
    plt.title(f'Soil Moisture Dynamic in Layer {layer} ({soiltype})')

    # Show plot
    plt.show()