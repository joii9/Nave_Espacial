# Argument File Generator

# Torque Bias

## RECONSTRUCTION
Maniobra de referencia 


```python
def get_maneuver():
    manv= input("Maniobra a calcular: \n")#NSSK0812
    return manv
```


```python
manv= get_maneuver()
```

    Maniobra a calcular: 
    NSSK0812
    


```python
def get_manRef():
    manv_ref= input("Maniobra de referencia: \n")#NSSK0811
    return manv_ref
```


```python
manv_ref=get_manRef()
```

    Maniobra de referencia: 
    NSSK0811
    


```python
def get_file():
    file = open(fr'V:\mx3\OASYS\Archivos_Mexsat3_2025\MNVR_Report\mx3_{manv_ref}_REC_Duty.rpt', 'r') #referencia
    content = file.read()
    file.close()
    print(content)
    return content
```


```python
content= get_file()
```

    
    
                         Maneuver Service Report
    
                Version: OASYS v10.3.3 (September 26, 2012), Kratos Integral Systems International
            Description: 
                   Date: 2025/10/14 17:05:50
                   Path: /V=/mx3/OASYS/Archivos_Mexsat3_2025/MNVR_Report/mx3_NSSK0811_REC_Duty.rpt
             Spacecraft: [mx3] Mexsat 3
              Ephemeris: /V=/mx3/OASYS/Archivos_Mexsat3_2025/MNVR_Ephemeris/mx3_NSSK0811_REC_pTUpdate.eph
                Equinox: True of Date FK5
               Attitude: AttitudeReference
    
            Maneuver[s]:         NSSK896
                 Status:         Success
                   Type:  Reconstruction
        Command Antenna:            None
           Thruster Cfg:      DV_EHT_ODD
            Thruster[s]:           EHT13
                                   EHT15
    
            Firing Mode:      Continuous
    Thrust Profile Type:      Continuous
               Ignition:      2025/10/14
                            11:33:51.000 UTC.YmdHMs3
               Centroid:      2025/10/14
                            11:57:25.121 UTC.YmdHMs3
               Duration:       2828.0030 secs
                 Cutoff:      2025/10/14
                            12:20:59.003 UTC.YmdHMs3
    
          Thruster Secs: 
                  EHT13:       2789.5700 secs
                  EHT15:       2789.5700 secs
                  Total:       5579.1400 secs
    
             Duty Cycle: 
                  EHT13:      0.98640984 ones
                  EHT15:      0.98640984 ones
    
      Thrust Efficiency: 
                  EHT13:       1.0000000 ones
                  EHT15:       1.0000000 ones
    
        Flow Efficiency: 
    
    Thrust Coefficients:          Static
                   Ct.x:     0.019761530 ones
                   Ct.y:     -0.13486757 ones
                   Ct.z:    0.0094265600 ones
                   Ct.m:       1.0176132 ones
    
        Net Performance: 
                    Isp:       268.78583 secs
                 Thrust:      0.67190355 Nt
              Fuel Flow:  -0.00025490591 kg/sec
          Oxidizer Flow: 
          Mixture Ratio: 
                     dM:     -0.72087467 kg
    
                     dV:       1.3318046 m/sec
    
               SCB dV.x:     0.030658153 m/sec
               SCB dV.y:       1.3313669 m/sec
               SCB dV.z:     0.015024717 m/sec
    
            SCB dV.x/dV:     0.023020009 ones
            SCB dV.y/dV:      0.99967135 ones
            SCB dV.z/dV:     0.011281473 ones
    
            Along-Track:     0.030658153 m/sec
            Cross-Track:      -1.3313669 m/sec
                 Radial:    -0.015024717 m/sec
    
              Right Asc:      -155.61629 degs
                   Decl:      -88.504984 degs
                    Yaw:       88.680850 degs
                  Pitch:     -0.64639449 degs
    
                     dH:       0.0000000 Nt-m-s
    
               SCB dH.x:       0.0000000 Nt-m-s
               SCB dH.y:       0.0000000 Nt-m-s
               SCB dH.z:       0.0000000 Nt-m-s
    
            SCB dH.x/dH:       0.0000000 ones
            SCB dH.y/dH:       0.0000000 ones
            SCB dH.z/dH:       0.0000000 ones
    
    
                                Pre-Mnvr          Delta      Post-Mnvr
    
               Dry Mass:       1159.0200      0.0000000      1159.0200 kg
    
             Pressurant: 
            Fuel System:       1.7330000      0.0000000      1.7330000 kg
        Oxidizer System:       4.7470000      0.0000000      4.7470000 kg
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                  Total:       6.4800000      0.0000000      6.4800000 kg
    
                   Fuel: 
            Fuel System:       242.07625    -0.72087467      241.35538 kg
                               92.534936      100.00000      92.514308 %
        Oxidizer System:       19.529000      0.0000000      19.529000 kg
                               7.4650642      0.0000000      7.4856917 %
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                               0.0000000      0.0000000      0.0000000 %
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                               0.0000000      0.0000000      0.0000000 %
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                               0.0000000      0.0000000      0.0000000 %
                 Unused:       0.0000000      0.0000000      0.0000000 kg
                               0.0000000      0.0000000      0.0000000 %
                  Total:       261.60525    -0.72087467      260.88438 kg
    
             Total Mass:       1427.1053    -0.72087467      1426.3844 kg
    
               Pressure: 
            Fuel System:       1447.4542     -1.4250252      1446.0291 kPa
        Oxidizer System:       1792.6369      0.0000000      1792.6369 kPa
                 Unused:       0.0000000      0.0000000      0.0000000 kPa
                 Unused:       0.0000000      0.0000000      0.0000000 kPa
                 Unused:       0.0000000      0.0000000      0.0000000 kPa
                 Unused:       0.0000000      0.0000000      0.0000000 kPa
    
            Temperature: 
            Fuel System:       18.573781      0.0000000      18.573781 degC
        Oxidizer System:       20.000000      0.0000000      20.000000 degC
                 Unused:       0.0000000      0.0000000      0.0000000 degC
                 Unused:       0.0000000      0.0000000      0.0000000 degC
                 Unused:       0.0000000      0.0000000      0.0000000 degC
                 Unused:       0.0000000      0.0000000      0.0000000 degC
    
         Center Of Mass: 
                      x:   -0.0048768000      0.0000000  -0.0048768000 meters
                      y:   -0.0081788000      0.0000000  -0.0081788000 meters
                      z:       1.4012418      0.0000000      1.4012418 meters
    
     Center Of Pressure: 
                      x:       0.0000000      0.0000000      0.0000000 meters
                      y:       0.0000000      0.0000000      0.0000000 meters
                      z:       0.0000000      0.0000000      0.0000000 meters
    
               Attitude: 
                  Frame: AttitudeReference
                   Type: Fixed
              Attd Repn: 323_Euler
              Rate Repn: VectorRate
    
               Euler[3]:       0.0000000      0.0000000      0.0000000 degs
               Euler[2]:       0.0000000      0.0000000      0.0000000 degs
               Euler[3]:       0.0000000      0.0000000      0.0000000 degs
                Spin[1]:       0.0000000      0.0000000      0.0000000 deg/day
                Spin[2]:       0.0000000      0.0000000      0.0000000 deg/day
                Spin[3]:       0.0000000      0.0000000      0.0000000 deg/day
    
                  Orbit: 
                  Frame: Kepler
          Mnvr Centroid:      2025/10/14      0.0000000     2025/10/14
                            11:57:25.121      0.0000000   11:57:25.121 UTC.YmdHMs3
        Time of Perigee:      2025/10/14      0.0000000     2025/10/14
                            19:15:53.094      0.0000000   18:45:26.241 UTC.YmdHMs3
        Semi-Major Axis:       42165.231     0.84092576      42166.072 km
           Eccentricity:       154.49470    -0.84002849      153.65467 micros
            Inclination:     0.028403146  -0.0057222781    0.022680868 degs
            RA Asc Node:       137.73315      56.795909      194.52906 degs
            Arg Perigee:       60.032549      295.56916      355.60171 degs
            Lon Perigee:       197.76570     -7.6349346      190.13077 degs
            LST Perigee:       11.631941    -0.50899564      11.122945 hrs
           Mean Anomaly:       250.08747      7.6354993      257.72297 degs
           True Anomaly:       250.07083      7.6349394      257.70577 degs
           Arg Latitude:       310.10338     -56.795905      253.30747 degs
                 Period:       1436.1224    0.042962352      1436.1654 mins
            Mean Motion:       1.0027000 -2.9995399e-05      1.0026701 revs/day
        Longitude Drift:       6.3129385     -10.769995     -4.4570563 mdeg/rev
                               6.3299837     -10.798941     -4.4689569 mdeg/day
         Perigee Radius:       42158.717     0.87621654      42159.593 km
                 Radius:       42167.451  7.2759576e-12      42167.451 km
          Apogee Radius:       42171.745     0.80563498      42172.551 km
               Velocity:       3074.4596    0.030660332      3074.4902 m/sec
              Longitude:       245.19526 -2.8421709e-14      245.19526 degE
         Mean Longitude:       245.21191  0.00056464738      245.21247 degE
               Latitude:    -0.021747116 -1.0408341e-17   -0.021747116 degs
               Altitude:       35789.314  1.4551915e-11      35789.314 km
       Local Solar Time:       4.5375696 -6.2172489e-15      4.5375696 hrs
     Local Time Perigee:       11.631941    -0.50899564      11.122945 hrs
    
                                Pre-Mnvr       Mid-Mnvr      Post-Mnvr
          Orbit Normals: 
        Right Ascension:       47.733154      72.657836      104.52906 degs
            Declination:       89.971597      89.977490      89.977319 degs
    
    


```python
import re

def find_data():
    pattern_epoch="(\d{4})/(\d{2})/(\d{2})\s+(\d{2}):(\d{2}):(\d{2}).(\d{3})"
    pattern_ignition= r"Ignition:\s+"+ pattern_epoch
    pattern_findedIgnition= re.findall(pattern_ignition ,content)
    pattern_cutoff= r"Cutoff:\s+"+ pattern_epoch
    pattern_findedCutoff= re.findall(pattern_cutoff ,content)
    print(type(pattern_findedIgnition))
    print(type(pattern_findedCutoff))
    print(pattern_findedIgnition)
    print(pattern_findedCutoff)
    return pattern_findedIgnition, pattern_findedCutoff
```


```python
[Ignition, Cutoff]=find_data()
```

    <class 'list'>
    <class 'list'>
    [('2025', '10', '14', '11', '33', '51', '000')]
    [('2025', '10', '14', '12', '20', '59', '003')]
    

## Get telemetry with library TLM_EPOCH


```python
from TLM_EPOCH import DatoTLM
from datetime import datetime

def get_torque(n):
    datos_torque=DatoTLM("mx3","mx3_rt1@izopsfep3","ACS_ATC_TOTAL_TRQ_"+str(n))
    datos_torque.tipo="completo"
    datos_torque.inicio_TLM=datetime(int(Ignition[0][0]),int(Ignition[0][1]),int(Ignition[0][2]),int(Ignition[0][3]),int(Ignition[0][4]),int(Ignition[0][5]))
    datos_torque.final_TLM=datetime(int(Cutoff[0][0]),int(Cutoff[0][1]),int(Cutoff[0][2]),int(Cutoff[0][3]),int(Cutoff[0][4]),int(Cutoff[0][5]))
    datos_torque.obtener_TLM()
    return datos_torque.xs
```


```python
#datos_torque=get_torque(1)
#print(datos_torque)
#print(id(datos_torque))
#print(id(get_torque(3)))
```


```python
def average_torque(datos_torque):
    #print(id(datos_torque))
    list_addition= sum(datos_torque)
    #print(list_sum)

    list_len= len(datos_torque)
    #print(list_len)

    average= list_addition / list_len
    return average
```


```python
#average_torque(datos_torque)
```


```python
average_torques=[average_torque(get_torque(i)) for i in range(1,4)]
```

    Mnemonico Valido
    Obtencion de telemetria exitosa :)
    Mnemonico Valido
    Obtencion de telemetria exitosa :)
    Mnemonico Valido
    Obtencion de telemetria exitosa :)
    


```python
average_torques
```




    [0.0015112709446428551, -0.001275171920053749, 0.005914713588734078]



## Get SKMTool to get the historic data (Pandas)


```python
import pandas as pd
```


```python
#df= pd.read_excel('SKMTool_dummy.xlsm', sheet_name= 'Historico') This way is incompatible with this pandas ver
df= pd.read_excel('SKMTool_dummy.xlsm', 'Historico')
print(df)
#print(df[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']])
```

         Maniobra  Torque 1  Torque 2  Torque 3 Unnamed: 4       Unnamed: 5  \
    0     EWSK260  0.000800  0.026800 -0.000600        NaN              NaN   
    1    NSSK0261 -0.133300 -0.008300 -0.026800        NaN              NaN   
    2    EWSK0262  0.005000 -0.006000 -0.001000        NaN              NaN   
    3    NSSK0263 -0.108300 -0.007200 -0.016600        NaN              NaN   
    4    EWSK0264  0.000800  0.026800  0.000600        NaN              NaN   
    5    NSSK0265 -0.103300 -0.007200 -0.018600        NaN              NaN   
    6    NSSK0266 -0.098200  0.005400  0.049700        NaN              NaN   
    7    EWSK0267 -0.001000  0.025300 -0.000300        NaN              NaN   
    8    NSSK0268 -0.123000  0.003400  0.064700        NaN              NaN   
    9    EWSK0269 -0.001000  0.021300 -0.000800        NaN              NaN   
    10   NSSK0270 -0.129000  0.005900  0.062500        NaN              NaN   
    11   EWSK0271  0.000500  0.022900 -0.000700        NaN              NaN   
    12   NSSK0272 -0.134000  0.010900  0.044000        NaN              NaN   
    13   EWSK0273  0.004500  0.019900 -0.001700        NaN              NaN   
    14   NSSK0274 -0.133100  0.012300  0.021300        NaN              NaN   
    15   EWSK0275  0.001800  0.026900 -0.000500        NaN              NaN   
    16   EWSK0276 -0.010200 -0.021900 -0.006000        NaN              NaN   
    17   NSSK0277 -0.123100  0.016300  0.013300        NaN              NaN   
    18   EWSK0278 -0.000700  0.021900  0.022400        NaN              NaN   
    19   NSSK0279 -0.110200  0.015600  0.018100        NaN              NaN   
    20   EWSK0280 -0.002400  0.028800  0.004000        NaN              NaN   
    21   NSSK0281 -0.100200  0.016600  0.024100        NaN              NaN   
    22   EWSK0282 -0.007400  0.023800  0.001000        NaN              NaN   
    23   NSSK0283 -0.098100  0.014400  0.031000        NaN              NaN   
    24   EWSK0284 -0.001900  0.028700 -0.001100        NaN              NaN   
    25   NSSK0285 -0.100100  0.011400  0.030000        NaN              NaN   
    26   EWSK0286  0.001100  0.024700  0.002900        NaN              NaN   
    27   NSSK0287 -0.099700  0.011100  0.032700        NaN              NaN   
    28   EWSK0288  0.000200  0.029200  0.001000        NaN              NaN   
    29   NSSK0289 -0.099700  0.009100  0.033700        NaN              NaN   
    ..        ...       ...       ...       ...        ...              ...   
    525  NSSK0782 -0.125004 -0.008699  0.003671       JPM3              500   
    526  EWSK0783 -0.003476  0.031213 -0.002466        NaN              NaN   
    527  NSSK0784 -0.124924 -0.009597  0.006817       JPM3              520   
    528  EWSK0785 -0.005005  0.037670 -0.001151        NaN              NaN   
    529  NSSK0786 -0.125054 -0.010774  0.009877       JPM3              540   
    530  EWSK0787 -0.004303  0.032109 -0.002250        NaN              NaN   
    531  NSSK0788 -0.126759 -0.011097  0.017367       JPM3              520   
    532  NSSK0789 -0.129692 -0.010612  0.020745       JPM3              520   
    533  EWSK0790 -0.004677  0.030823 -0.001524        NaN              NaN   
    534  NSSK0791 -0.133742 -0.009534  0.025500       JPM3              560   
    535  EWSK0792 -0.000135 -0.027713 -0.000225        NaN              NaN   
    536  NSSK0793 -0.148681 -0.010513  0.042423       JPM3              540   
    537  EWSK0794 -0.000872 -0.016219 -0.001139        NaN              NaN   
    538  NSSK0795 -0.151820 -0.008151  0.037254        NaN  JPM'S Suspended   
    539  EWSK0796 -0.000502 -0.014170 -0.000298        NaN              NaN   
    540  NSSK0797 -0.153733 -0.005332  0.031327        NaN              NaN   
    541  EWSK0798 -0.006721 -0.037776  0.004944        NaN              NaN   
    542  NSSK0799 -0.155029 -0.001094  0.014565        NaN              NaN   
    543  EWSK0800 -0.001408 -0.019345 -0.000756        NaN              NaN   
    544  NSSK0801 -0.153458  0.000607  0.014499        NaN              NaN   
    545  EWSK0802 -0.003823 -0.022645 -0.000750        NaN              NaN   
    546  NSSK0803 -0.144847 -0.000456  0.023256        NaN              NaN   
    547  EWSK0804 -0.006473 -0.030176  0.001547        NaN              NaN   
    548  NSSK0805 -0.146353 -0.001591  0.032238        NaN              NaN   
    549  EWSK0806 -0.003697 -0.024262 -0.003558        NaN              NaN   
    550  NSSK0807 -0.143986 -0.003998  0.040984        NaN              NaN   
    551  EWSK0808 -0.000950 -0.021087 -0.005850        NaN              NaN   
    552  NSSK0809 -0.141242 -0.008020  0.048082        NaN              NaN   
    553  EWSK0810 -0.004414 -0.019994 -0.004163        NaN              NaN   
    554  NSSK0811 -0.142286 -0.012945  0.056209        NaN              NaN   
    
                  Unnamed: 6        Unnamed: 7  Unnamed: 8  Unnamed: 9  
    0                    NaN               NaN         NaN         NaN  
    1                    NaN               NaN         NaN         NaN  
    2                    NaN               NaN         NaN         NaN  
    3                    NaN               NaN         NaN         NaN  
    4                    NaN               NaN         NaN         NaN  
    5                    NaN               NaN         NaN         NaN  
    6                    NaN               NaN         NaN         NaN  
    7                    NaN               NaN         NaN         NaN  
    8                    NaN               NaN         NaN         NaN  
    9                    NaN               NaN         NaN         NaN  
    10                   NaN               NaN         NaN         NaN  
    11                   NaN               NaN         NaN         NaN  
    12                   NaN               NaN         NaN         NaN  
    13                   NaN               NaN         NaN         NaN  
    14                   NaN               NaN         NaN         NaN  
    15                   NaN               NaN         NaN         NaN  
    16                   NaN               NaN         NaN         NaN  
    17                   NaN               NaN         NaN         NaN  
    18                   NaN               NaN         NaN         NaN  
    19                   NaN               NaN         NaN         NaN  
    20                   NaN               NaN         NaN         NaN  
    21                   NaN               NaN         NaN         NaN  
    22                   NaN               NaN         NaN         NaN  
    23                   NaN               NaN         NaN         NaN  
    24                   NaN               NaN         NaN         NaN  
    25                   NaN               NaN         NaN         NaN  
    26                   NaN               NaN         NaN         NaN  
    27                   NaN               NaN         NaN         NaN  
    28                   NaN               NaN         NaN         NaN  
    29                   NaN               NaN         NaN         NaN  
    ..                   ...               ...         ...         ...  
    525           20/05/2025               NaN         NaN         NaN  
    526                  NaN               NaN         NaN         NaN  
    527           27/05/2025               NaN         NaN         NaN  
    528                  NaN               NaN         NaN         NaN  
    529  2025-10-06 00:00:00               NaN         NaN         NaN  
    530                  NaN               NaN         NaN         NaN  
    531            17/6/2025               NaN         NaN         NaN  
    532            24/6/2025               NaN         NaN         NaN  
    533                  NaN               NaN         NaN         NaN  
    534  2025-07-08 00:00:00  Segundo semestre         NaN         NaN  
    535                  NaN               NaN         NaN         NaN  
    536              15/7/25               NaN         NaN         NaN  
    537                  NaN               NaN         NaN         NaN  
    538                  NaN               NaN         NaN         NaN  
    539                  NaN               NaN         NaN         NaN  
    540                  NaN               NaN         NaN         NaN  
    541                  NaN               NaN         NaN         NaN  
    542                  NaN               NaN         NaN         NaN  
    543                  NaN               NaN         NaN         NaN  
    544                  NaN               NaN         NaN         NaN  
    545                  NaN               NaN         NaN         NaN  
    546                  NaN               NaN         NaN         NaN  
    547                  NaN               NaN         NaN         NaN  
    548                  NaN               NaN         NaN         NaN  
    549                  NaN               NaN         NaN         NaN  
    550                  NaN               NaN         NaN         NaN  
    551                  NaN               NaN         NaN         NaN  
    552                  NaN               NaN         NaN         NaN  
    553                  NaN               NaN         NaN         NaN  
    554                  NaN               NaN         NaN         NaN  
    
    [555 rows x 10 columns]
    


```python
import pandas as pd

def get_requested_torques(manv_ref):
    df_historic= pd.read_excel('SKMTool_dummy.xlsm', 'Historico')
    requested_torques= df_historic[df.Maniobra== manv_ref]
    requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
    #print(df)
    return df_historic, requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
```


```python
[df_historic,requested_torques]= get_requested_torques(manv_ref)
```


```python
print(requested_torques)
```

         Maniobra  Torque 1  Torque 2  Torque 3
    554  NSSK0811 -0.142286 -0.012945  0.056209
    


```python
average_torques
```




    [0.0015112709446428551, -0.001275171920053749, 0.005914713588734078]




```python
#print(df.iloc[-1])
```


```python
requested_torques= df[df.Maniobra== manv_ref]
requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
```


```python
requested_torques.iloc[0][0]
```

## Another way to get info of an excel file


```python
import xlwings
SA=xlwings.Book("SKMTool_dummy.xlsm")
sht=xlwings.Sheet("Historico")
Epoch=sht.range("A25:d50").value
print(Epoch)
SA.close()
```

## Continue


```python
dir(requested_torques)
```


```python
requested_torques.values[0][1:4]
```


```python
average_torques[0]+float(requested_torques.values[0][1])
```


```python
new_values= average_torques[0]+requested_torques.iloc[0][1]
print(new_values)
```


```python
new_values=[average_torques[i]+requested_torques.iloc[0][i+1] for i in range(3)]

print(new_values)
```

## Suma


```python
new_values= []
for i in range(3):
    #print(i)
    value= average_torques[i]+requested_torques.iloc[0][i+1]
    new_values.append(value)

#print(new_values)
new_values.insert(0, manv)
print(new_values)

    
```

    ['NSSK0812', -0.14077427694943861, -0.014219976805559776, 0.062123980702140473]
    


```python
def get_new_values(manv, average_torques, requested_torques):
    new_values= []
    for i in range(3):
        #print(i)
        value= average_torques[i]+requested_torques.iloc[0][i+1]
        new_values.append(value)

    #print(new_values)
    new_values.insert(0, manv)
    return new_values
    
```


```python
new_values= get_new_values(manv, average_torques, requested_torques)
```


```python
answer= input("Quieres agregar estos nuevos valores al Historico del SKMTool?: \n" +str(new_values)[1:-1]+ "\n")
```

    Quieres agregar estos nuevos valores al Historico del SKMTool?: 
    'NSSK0812', -0.14077427694943861, -0.014219976805559776, 0.062123980702140473
    n
    


```python
import xlwings as xw

def make_a_decision(new_values, df_historic):
    answer= input("Quieres agregar estos nuevos valores al Historico del SKMTool?: (si/no)\n" +str(new_values)[1:-1]+ "\n")
    if answer.lower().replace(' ','') == 'si':
        #print('Dentro del if')
        new_row_data={'Maniobra':new_values[0],'Torque 1':new_values[1],'Torque 2':new_values[2],'Torque 3':new_values[3]}
        #print(new_row_data)
        df_new_values= pd.concat([df_historic, pd.DataFrame([new_row_data])], ignore_index= True)
        print(df_new_values)
    
        wb= xw.Book('SKMTool_dummy - Copy.xlsm')
        #wb= wb.books.active
        sheet= wb.sheets['Historico']
        sheet.range('A'+str(len(df_new_values)+1)).value= new_values[0]
        sheet.range('B'+str(len(df_new_values)+1)).value= new_values[1]
        sheet.range('C'+str(len(df_new_values)+1)).value= new_values[2]
        sheet.range('D'+str(len(df_new_values)+1)).value= new_values[3]
        #sheet.range('A'+str(len(df_new_values)+1)+":D"+str(len(df_new_values)+1)).value= new_values

        wb.save()
        wb.close()
        
```


```python
make_a_decision(new_values, df_historic)
```

    Quieres agregar estos nuevos valores al Historico del SKMTool?: (si/no)
    'NSSK0812', -0.14077427694943861, -0.014219976805559776, 0.062123980702140473
    si
         Maniobra  Torque 1  Torque 2  Torque 3 Unnamed: 4       Unnamed: 5  \
    0     EWSK260  0.000800  0.026800 -0.000600        NaN              NaN   
    1    NSSK0261 -0.133300 -0.008300 -0.026800        NaN              NaN   
    2    EWSK0262  0.005000 -0.006000 -0.001000        NaN              NaN   
    3    NSSK0263 -0.108300 -0.007200 -0.016600        NaN              NaN   
    4    EWSK0264  0.000800  0.026800  0.000600        NaN              NaN   
    5    NSSK0265 -0.103300 -0.007200 -0.018600        NaN              NaN   
    6    NSSK0266 -0.098200  0.005400  0.049700        NaN              NaN   
    7    EWSK0267 -0.001000  0.025300 -0.000300        NaN              NaN   
    8    NSSK0268 -0.123000  0.003400  0.064700        NaN              NaN   
    9    EWSK0269 -0.001000  0.021300 -0.000800        NaN              NaN   
    10   NSSK0270 -0.129000  0.005900  0.062500        NaN              NaN   
    11   EWSK0271  0.000500  0.022900 -0.000700        NaN              NaN   
    12   NSSK0272 -0.134000  0.010900  0.044000        NaN              NaN   
    13   EWSK0273  0.004500  0.019900 -0.001700        NaN              NaN   
    14   NSSK0274 -0.133100  0.012300  0.021300        NaN              NaN   
    15   EWSK0275  0.001800  0.026900 -0.000500        NaN              NaN   
    16   EWSK0276 -0.010200 -0.021900 -0.006000        NaN              NaN   
    17   NSSK0277 -0.123100  0.016300  0.013300        NaN              NaN   
    18   EWSK0278 -0.000700  0.021900  0.022400        NaN              NaN   
    19   NSSK0279 -0.110200  0.015600  0.018100        NaN              NaN   
    20   EWSK0280 -0.002400  0.028800  0.004000        NaN              NaN   
    21   NSSK0281 -0.100200  0.016600  0.024100        NaN              NaN   
    22   EWSK0282 -0.007400  0.023800  0.001000        NaN              NaN   
    23   NSSK0283 -0.098100  0.014400  0.031000        NaN              NaN   
    24   EWSK0284 -0.001900  0.028700 -0.001100        NaN              NaN   
    25   NSSK0285 -0.100100  0.011400  0.030000        NaN              NaN   
    26   EWSK0286  0.001100  0.024700  0.002900        NaN              NaN   
    27   NSSK0287 -0.099700  0.011100  0.032700        NaN              NaN   
    28   EWSK0288  0.000200  0.029200  0.001000        NaN              NaN   
    29   NSSK0289 -0.099700  0.009100  0.033700        NaN              NaN   
    ..        ...       ...       ...       ...        ...              ...   
    526  EWSK0783 -0.003476  0.031213 -0.002466        NaN              NaN   
    527  NSSK0784 -0.124924 -0.009597  0.006817       JPM3              520   
    528  EWSK0785 -0.005005  0.037670 -0.001151        NaN              NaN   
    529  NSSK0786 -0.125054 -0.010774  0.009877       JPM3              540   
    530  EWSK0787 -0.004303  0.032109 -0.002250        NaN              NaN   
    531  NSSK0788 -0.126759 -0.011097  0.017367       JPM3              520   
    532  NSSK0789 -0.129692 -0.010612  0.020745       JPM3              520   
    533  EWSK0790 -0.004677  0.030823 -0.001524        NaN              NaN   
    534  NSSK0791 -0.133742 -0.009534  0.025500       JPM3              560   
    535  EWSK0792 -0.000135 -0.027713 -0.000225        NaN              NaN   
    536  NSSK0793 -0.148681 -0.010513  0.042423       JPM3              540   
    537  EWSK0794 -0.000872 -0.016219 -0.001139        NaN              NaN   
    538  NSSK0795 -0.151820 -0.008151  0.037254        NaN  JPM'S Suspended   
    539  EWSK0796 -0.000502 -0.014170 -0.000298        NaN              NaN   
    540  NSSK0797 -0.153733 -0.005332  0.031327        NaN              NaN   
    541  EWSK0798 -0.006721 -0.037776  0.004944        NaN              NaN   
    542  NSSK0799 -0.155029 -0.001094  0.014565        NaN              NaN   
    543  EWSK0800 -0.001408 -0.019345 -0.000756        NaN              NaN   
    544  NSSK0801 -0.153458  0.000607  0.014499        NaN              NaN   
    545  EWSK0802 -0.003823 -0.022645 -0.000750        NaN              NaN   
    546  NSSK0803 -0.144847 -0.000456  0.023256        NaN              NaN   
    547  EWSK0804 -0.006473 -0.030176  0.001547        NaN              NaN   
    548  NSSK0805 -0.146353 -0.001591  0.032238        NaN              NaN   
    549  EWSK0806 -0.003697 -0.024262 -0.003558        NaN              NaN   
    550  NSSK0807 -0.143986 -0.003998  0.040984        NaN              NaN   
    551  EWSK0808 -0.000950 -0.021087 -0.005850        NaN              NaN   
    552  NSSK0809 -0.141242 -0.008020  0.048082        NaN              NaN   
    553  EWSK0810 -0.004414 -0.019994 -0.004163        NaN              NaN   
    554  NSSK0811 -0.142286 -0.012945  0.056209        NaN              NaN   
    555  NSSK0812 -0.140774 -0.014220  0.062124        NaN              NaN   
    
                  Unnamed: 6        Unnamed: 7  Unnamed: 8  Unnamed: 9  
    0                    NaN               NaN         NaN         NaN  
    1                    NaN               NaN         NaN         NaN  
    2                    NaN               NaN         NaN         NaN  
    3                    NaN               NaN         NaN         NaN  
    4                    NaN               NaN         NaN         NaN  
    5                    NaN               NaN         NaN         NaN  
    6                    NaN               NaN         NaN         NaN  
    7                    NaN               NaN         NaN         NaN  
    8                    NaN               NaN         NaN         NaN  
    9                    NaN               NaN         NaN         NaN  
    10                   NaN               NaN         NaN         NaN  
    11                   NaN               NaN         NaN         NaN  
    12                   NaN               NaN         NaN         NaN  
    13                   NaN               NaN         NaN         NaN  
    14                   NaN               NaN         NaN         NaN  
    15                   NaN               NaN         NaN         NaN  
    16                   NaN               NaN         NaN         NaN  
    17                   NaN               NaN         NaN         NaN  
    18                   NaN               NaN         NaN         NaN  
    19                   NaN               NaN         NaN         NaN  
    20                   NaN               NaN         NaN         NaN  
    21                   NaN               NaN         NaN         NaN  
    22                   NaN               NaN         NaN         NaN  
    23                   NaN               NaN         NaN         NaN  
    24                   NaN               NaN         NaN         NaN  
    25                   NaN               NaN         NaN         NaN  
    26                   NaN               NaN         NaN         NaN  
    27                   NaN               NaN         NaN         NaN  
    28                   NaN               NaN         NaN         NaN  
    29                   NaN               NaN         NaN         NaN  
    ..                   ...               ...         ...         ...  
    526                  NaN               NaN         NaN         NaN  
    527           27/05/2025               NaN         NaN         NaN  
    528                  NaN               NaN         NaN         NaN  
    529  2025-10-06 00:00:00               NaN         NaN         NaN  
    530                  NaN               NaN         NaN         NaN  
    531            17/6/2025               NaN         NaN         NaN  
    532            24/6/2025               NaN         NaN         NaN  
    533                  NaN               NaN         NaN         NaN  
    534  2025-07-08 00:00:00  Segundo semestre         NaN         NaN  
    535                  NaN               NaN         NaN         NaN  
    536              15/7/25               NaN         NaN         NaN  
    537                  NaN               NaN         NaN         NaN  
    538                  NaN               NaN         NaN         NaN  
    539                  NaN               NaN         NaN         NaN  
    540                  NaN               NaN         NaN         NaN  
    541                  NaN               NaN         NaN         NaN  
    542                  NaN               NaN         NaN         NaN  
    543                  NaN               NaN         NaN         NaN  
    544                  NaN               NaN         NaN         NaN  
    545                  NaN               NaN         NaN         NaN  
    546                  NaN               NaN         NaN         NaN  
    547                  NaN               NaN         NaN         NaN  
    548                  NaN               NaN         NaN         NaN  
    549                  NaN               NaN         NaN         NaN  
    550                  NaN               NaN         NaN         NaN  
    551                  NaN               NaN         NaN         NaN  
    552                  NaN               NaN         NaN         NaN  
    553                  NaN               NaN         NaN         NaN  
    554                  NaN               NaN         NaN         NaN  
    555                  NaN               NaN         NaN         NaN  
    
    [556 rows x 10 columns]
    


```python
#print(dir(answer))
print(answer.lower().replace(' ',''))

if answer == 'si':
    print('Dentro del if')
```


```python
new_row_data={'Maniobra':new_values[0],'Torque 1':new_values[1],'Torque 2':new_values[2],'Torque 3':new_values[3]}
print(new_row_data)
```

    {'Maniobra': 'NSSK0812', 'Torque 1': -0.14077427694943861, 'Torque 2': -0.014219976805559776, 'Torque 3': 0.062123980702140473}
    


```python
df_new_values= pd.concat([df, pd.DataFrame([new_row_data])], ignore_index= True)
print(df_new_values)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-98-7f3813308001> in <module>()
    ----> 1 df_new_values= pd.concat([df, pd.DataFrame([new_row_data])], ignore_index= True)
          2 print(df_new_values)
    

    NameError: name 'new_row_data' is not defined



```python
from openpyxl import load_workbook

try:
    book= load_workbook("SKMTool_dummy - Copy.xlsm")
except FileNotFoundError:
    print("File not found")

with pd.ExcelWriter("SKMTool_dummy - Copy.xlsm", engine="openpyxl", keep_vba= True) as writer:
    writer.book= book
    writer.vba_archive= book.vba_archive
    writer.sheets= dict((ws.title, ws) for ws in book.worksheets)
    df_new_values.to_excel(writer, sheet_name= "Historico", index=False)
    writer.close()
```


```python
with pd.ExcelWriter(
    "SKMTool_dummy - Copy.xlsm",
    engine="openpyxl",
    mode= "a",
    engine_kwargs={"keep_vba": True}
)as writer:
    df_new_values.to_excel(writer, sheet_name= "Historico")
```


```python
#import xlsxwriter, xlwings
import openpyxl
df_new_values.to_excel(excel_writer, 'SKMTool_dummy - Copy.xlsm', 'Historico', index=False)
```


```python
import xlsxwriter
import os

excel_file= 'test.xlsx'

if os.path.exists(excel_file):
    os.remove(excel_file)
    
workbook= xlsxwriter.Workbook(excel_file)
worksheet= workbook.add_worksheet()

worksheet.write('A1', 'Hello')
worksheet.write('B1', 'Puto')

workbook.close()
```


```python
import xlwings as xw

wob= xw.Book('SKMTool_dummy - Copy.xlsm')

#wb= wb.books.active

sheet= wob.sheets['Historico']

sheet.range('A'+str(len(df_new_values)+1)).value= new_values[0]
sheet.range('B'+str(len(df_new_values)+1)).value= new_values[1]
sheet.range('C'+str(len(df_new_values)+1)).value= new_values[2]
sheet.range('D'+str(len(df_new_values)+1)).value= new_values[3]
#sheet.range('A'+str(len(df_new_values)+1)+":D"+str(len(df_new_values)+1)).value= new_values

wob.save()
wob.close()


```


```python
mx3_EWSK0812_PLAN.rpt #Plan (manv - a calcular)

IGNITION
CUTOFF
tHRUSTER CFG
Thrusters sec TOTAL


```


```python
SET DE IMPULSORES (LISTA)

SKMTool ... ATTITUDE_CONTROL_THRUSTER 
Las opciones para los thrusters de control son los siguientes
```


```python
manv= "EWSK0812"
manvRef= "EWSK0810"
```


```python
def get_file(option):
    if option == "EWSK0812":
        print(manv)
        #return manv
    elif option == "EWSK0810":
        print(manvRef)
        #return manvRef
        
```


```python
get_file(manv)
```

    EWSK0812
    


```python
get_file(manvRef)
```

    EWSK0810
    


```python
respuesta=input("Test")
print(type(respuesta))
```

    Test1
    <class 'str'>
    


```python
type(str(1))
```




    str




```python
a=[1,2,4]

for i in range(0, len(a)):
    print(a[i])
```

    1
    2
    4
    


```python
b=list(range(len(a)))
print(b)
```

    [0, 1, 2]
    


```python
ignition=[('2025', '10', '17', '13', '38', '10', '003')]
#print('-'.join(ignition[0]))
date_='-'.join(ignition[0])
print(date_)
```

    2025-10-17-13-38-10-003
    


```python
from datetime import datetime

print(dir(datetime))
print(datetime.now().weekday())
```

    ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
    3
    


```python
my_date= datetime.strptime(date_, "%Y-%m-%d-%H-%M-%S-%f")
print(my_date)
print(my_date.strftime("%Y-%j-%H-%M-%S"))
```

    2025-10-17 13:38:10.003000
    2025-290-13-38-10
    


```python
my_date= datetime(int(ignition[0][0]),int(ignition[0][1]),int(ignition[0][2]),int(ignition[0][3]),int(ignition[0][4]),int(ignition[0][5]))
print(my_date)
print(my_date.strftime("%Y-%j-%H-%M-%S"))
```

    2025-10-17 13:38:10.003000
    2025-290-13-38-10
    


```python
ignition[0][1]
```




    '10'




```python
a=0.123456789
```


```python
a.format("%.4f")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-242-020583424bc1> in <module>()
    ----> 1 a.format("%.4f")
    

    AttributeError: 'float' object has no attribute 'format'



```python
format(a,".4f")
```




    '0.1235'




```python

```
