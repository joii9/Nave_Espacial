import re
import pandas as pd
import xlwings as xw
from TLM_EPOCH import DatoTLM
from datetime import datetime

def get_maneuver():
    manv= input("Maniobra a calcular: \n")#NSSK0812
    return manv

def get_manRef():
    manv_ref= input("Maniobra de referencia: \n")#NSSK0811
    return manv_ref
   
def get_file():
    file = open(fr'V:\mx3\OASYS\Archivos_Mexsat3_2025\MNVR_Report\mx3_{manv_ref}_REC_Duty.rpt', 'r')
    content = file.read()
    file.close()
    #print(content)
    return content

def find_data():
    pattern_epoch="(\d{4})/(\d{2})/(\d{2})\s+(\d{2}):(\d{2}):(\d{2}).(\d{3})"
    pattern_ignition= r"Ignition:\s+"+ pattern_epoch
    pattern_findedIgnition= re.findall(pattern_ignition ,content)
    pattern_cutoff= r"Cutoff:\s+"+ pattern_epoch
    pattern_findedCutoff= re.findall(pattern_cutoff ,content)
    #print(pattern_findedIgnition)
    #print(pattern_findedCutoff)
    return pattern_findedIgnition, pattern_findedCutoff

def get_torque(n):
    datos_torque=DatoTLM("mx3","mx3_rt1@izopsfep3","ACS_ATC_TOTAL_TRQ_"+str(n))
    datos_torque.tipo="completo"
    datos_torque.inicio_TLM=datetime(int(Ignition[0][0]),int(Ignition[0][1]),int(Ignition[0][2]),int(Ignition[0][3]),int(Ignition[0][4]),int(Ignition[0][5]))
    datos_torque.final_TLM=datetime(int(Cutoff[0][0]),int(Cutoff[0][1]),int(Cutoff[0][2]),int(Cutoff[0][3]),int(Cutoff[0][4]),int(Cutoff[0][5]))
    datos_torque.obtener_TLM()
    return datos_torque.xs

def average_torque(datos_torque):
    #print(datos_torque)
    list_addition= sum(datos_torque)
    #print(list_sum)
    list_len= len(datos_torque)
    #print(list_len)
    average= list_addition / list_len
    return average
 
def get_requested_torques(manv_ref):
    df_historic= pd.read_excel('SKMTool_dummy.xlsm', 'Historico')
    requested_torques= df_historic[df_historic.Maniobra== manv_ref]
    requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
    #print(df)
    return df_historic, requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
   
def get_new_values(manv, average_torques, requested_torques):
    new_values= []
    for i in range(3):
        #print(i)
        value= average_torques[i]+requested_torques.iloc[0][i+1]
        new_values.append(value)

    #print(new_values)
    new_values.insert(0, manv)
    return new_values

def make_a_decision(new_values, df_historic):
    answer= input("Quieres agregar estos nuevos valores al Historico del SKMTool?: (si/no)\n" +str(new_values)[1:-1]+ "\n")
    if answer.lower().replace(' ','') == 'si':
        #print('Dentro del if')
        new_row_data={'Maniobra':new_values[0],'Torque 1':new_values[1],'Torque 2':new_values[2],'Torque 3':new_values[3]}
        #print(new_row_data)
        df_new_values= pd.concat([df_historic, pd.DataFrame([new_row_data])], ignore_index= True)
        #print(df_new_values)
    
        wb= xw.Book('SKMTool_dummy.xlsm')
        #wb= wb.books.active
        sheet= wb.sheets['Historico']
        sheet.range('A'+str(len(df_new_values)+1)).value= new_values[0]
        sheet.range('B'+str(len(df_new_values)+1)).value= new_values[1]
        sheet.range('C'+str(len(df_new_values)+1)).value= new_values[2]
        sheet.range('D'+str(len(df_new_values)+1)).value= new_values[3]
        #sheet.range('A'+str(len(df_new_values)+1)+":D"+str(len(df_new_values)+1)).value= new_values

        wb.save()
        wb.close()
    


manv= get_maneuver()
manv_ref=get_manRef()
content= get_file()
[Ignition, Cutoff]=find_data()
average_torques=[average_torque(get_torque(i)) for i in range(1,4)]
#print(average_torques)
[df_historic, requested_torques]= get_requested_torques(manv_ref)
#print(requested_torques)
#print(df_historic)
new_values= get_new_values(manv, average_torques, requested_torques)
make_a_decision(new_values, df_historic)


