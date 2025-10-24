import re
import pandas as pd
import xlwings as xw
from TLM_EPOCH import DatoTLM
from datetime import datetime
from Ephemeris import Ephemeris

class EWSK_Single():
    def __init__(self):
        self.get_maneuver()
        self.get_manvRef()
        self.get_file_ManvRef()
        self.find_data_manvRef()
        self.get_torque()
        self.average_torque()
        self.get_requested_torques()
        self.get_new_values()
        self.make_a_decision()
        self.get_file_ManvPLAN()
        self.find_data_manv()
        self.control_thrusters()
        self.ephemeris_pre_load()
        self.ephemeris_post_load()
        
    def get_maneuver(self):
        self.manv= input("Maniobra a calcular: \n")#EWSK0812
        #return manv

    def get_manvRef(self):
        self.manv_ref= input("Maniobra de referencia: \n")#EWSK0810
        #return manv_ref
   
    def get_file_ManvRef(self):
        file = open(fr'V:\mx3\OASYS\Archivos_Mexsat3_2025\MNVR_Report\mx3_{self.manv_ref}_REC_Duty.rpt', 'r')
        self.content_manvRef = file.read()
        file.close()
        #print(content_manvRef)
        #return content_manvRef

    def find_data_manvRef(self): #, content_manvRef
        pattern_epoch="(\d{4})/(\d{2})/(\d{2})\s+(\d{2}):(\d{2}):(\d{2}).(\d{3})"
        pattern_ignition= r"Ignition:\s+"+ pattern_epoch
        self.Ignition_MR= re.findall(pattern_ignition ,self.content_manvRef)
        pattern_cutoff= r"Cutoff:\s+"+ pattern_epoch
        self.Cutoff_MR= re.findall(pattern_cutoff ,self.content_manvRef)
        #print(patternFinded_IgnitionMR)
        #print(patternFinded_CutoffMR)
        #return patternFinded_IgnitionMR, patternFinded_CutoffMR

    def get_torque(self): #<-------------------------------------------------
        self.torque_values=[]
        for i in range(1,4):
            self.datos_torque=DatoTLM("mx3","mx3_rt1@izopsfep3","ACS_ATC_TOTAL_TRQ_"+str(i))
            self.datos_torque.tipo="completo"
            self.datos_torque.inicio_TLM=datetime(int(self.Ignition_MR[0][0]),int(self.Ignition_MR[0][1]),int(self.Ignition_MR[0][2]),int(self.Ignition_MR[0][3]),int(self.Ignition_MR[0][4]),int(self.Ignition_MR[0][5]))
            self.datos_torque.final_TLM=datetime(int(self.Cutoff_MR[0][0]),int(self.Cutoff_MR[0][1]),int(self.Cutoff_MR[0][2]),int(self.Cutoff_MR[0][3]),int(self.Cutoff_MR[0][4]),int(self.Cutoff_MR[0][5]))
            self.datos_torque.obtener_TLM()
            self.datos_torque.xs
            self.torque_values.append(self.datos_torque.xs)
            #print(self.datos_torque.xs)
        #print(self.torque_values)
        #print(len(self.torque_values))
        #print(self.torque_values[0])
        #print(len(self.torque_values[0]))
        #print(self.torque_values[0][0])
        #print(dir(self.torque_values[0]))

    def average_torque(self): #, self.datos_torque
        self.average= list(range(len(self.torque_values)))
        self.list_addition= list(range(len(self.torque_values)))
        self.list_len= list(range(len(self.torque_values)))
        for i in range(len(self.torque_values)):
            self.list_addition[i]= sum(self.torque_values[i])
            #print(self.list_addition[i])
            self.list_len[i]= len(self.torque_values[i])
            #print(self.list_len[i])
            self.average[i]= self.list_addition[i] / self.list_len[i]
            #return average
        #print(self.average) 
 
    def get_requested_torques(self): #, manv_ref
        self.df_historic= pd.read_excel('SKMTool_dummy.xlsm', 'Historico')
        self.requested_torques= self.df_historic[self.df_historic.Maniobra== self.manv_ref]
        self.requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
        #print(self.df_historic)
        print(self.requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']])
        #return df_historic, requested_torques[['Maniobra', 'Torque 1', 'Torque 2', 'Torque 3']]
   
    def get_new_values(self): #, manv, average_torques, requested_torques
        self.new_values= []
        for i in range(3):
            #print(i)
            value= self.average[i]+self.requested_torques.iloc[0][i+1]
            self.new_values.append(value)

        #print(new_values)
        self.new_values.insert(0, self.manv)
        self.new_values
        #print(self.new_values) self.new_values.append(self.value)

    def make_a_decision(self): #, new_values, df_historic
        print("Do you want to overwrite these new values to Historico in SKMTool file?:") 
        print(str(self.new_values)[1:-1])
        answer= input("Yes/No:\n")
        if answer.lower().replace(' ','') == 'yes':
            #print('Dentro del if')
            new_row_data={'Maniobra':self.new_values[0],'Torque 1':self.new_values[1],'Torque 2':self.new_values[2],'Torque 3':self.new_values[3]}
            #print(new_row_data)
            df_new_values= pd.concat([self.df_historic, pd.DataFrame([new_row_data])], ignore_index= True)
            #print(df_new_values)
    
            wb= xw.Book('SKMTool_dummy.xlsm')
            #wb= wb.books.active
            sheet= wb.sheets['Historico']
            sheet.range('A'+str(len(df_new_values)+1)).value= self.new_values[0]
            sheet.range('B'+str(len(df_new_values)+1)).value= self.new_values[1]
            sheet.range('C'+str(len(df_new_values)+1)).value= self.new_values[2]
            sheet.range('D'+str(len(df_new_values)+1)).value= self.new_values[3]
            #sheet.range('A'+str(len(df_new_values)+1)+":D"+str(len(df_new_values)+1)).value= new_values

            wb.save()
            #wb.close()
      
    def get_file_ManvPLAN(self):
        file = open(fr'V:\mx3\OASYS\Archivos_Mexsat3_2025\MNVR_Report\mx3_{self.manv}_PLAN.rpt', 'r')
        self.content_manvPLAN = file.read()
        file.close()
        #print(self.content_manvPLAN)
        #return content_manvPLAN
   
    def find_data_manv(self): #, content_manvPLAN
    
        pattern_ThrusterCfg= r"Thruster Cfg:\s+(.+)\s"
        self.patternFinded_ThrusterCfgManv= re.findall(pattern_ThrusterCfg ,self.content_manvPLAN)
    
        pattern_epoch="(\d{4})/(\d{2})/(\d{2})\s+(\d{2}):(\d{2}):(\d{2}).(\d{3})"
        pattern_ignition= r"Ignition:\s+"+ pattern_epoch
        self.IgnitionManv= re.findall(pattern_ignition ,self.content_manvPLAN)
        pattern_cutoff= r"Cutoff:\s+"+ pattern_epoch
        self.CutoffManv= re.findall(pattern_cutoff ,self.content_manvPLAN)
    
        pattern_ThrusterSecsTotal= r"\n\s+Total:\s+(\d+.\d+)\ssecs\s*\n\s*\n\s+Duty Cycle:"   #SIEMPRE SON 4 REAS???????
        self.patternFinded_ThrusterSecsTotalManv= re.findall(pattern_ThrusterSecsTotal ,self.content_manvPLAN)
        #print(self.patternFinded_ThrusterCfgManv)
        #print(self.patternFinded_IgnitionManv)
        self.IgnitionManv_date= datetime(int(self.IgnitionManv[0][0]),int(self.IgnitionManv[0][1]),int(self.IgnitionManv[0][2]),int(self.IgnitionManv[0][3]),int(self.IgnitionManv[0][4]),int(self.IgnitionManv[0][5]))
        #print(self.patternFinded_CutoffManv)
        self.CutoffManv_date= datetime(int(self.CutoffManv[0][0]),int(self.CutoffManv[0][1]),int(self.CutoffManv[0][2]),int(self.CutoffManv[0][3]),int(self.CutoffManv[0][4]),int(self.CutoffManv[0][5])) 
        #print(self.patternFinded_ThrusterSecsTotalManv)
        #return patternFinded_ThrusterCfgManv, patternFinded_IgnitionManv, patternFinded_CutoffManv, patternFinded_ThrusterSecsTotalManv
    
    def control_thrusters(self):
        self.attitude_control_thruster=["E_ALL_NORTH_ALL", "W_ALL_NORTH_ALL", "E_W_N_EVEN"]
        print("The options for attitude_control_thruster are:") 
        print(str(self.attitude_control_thruster))
        self.attitude= input("Select: \t(1),\t\t(2)  \t\t(3): \n" )
        #print(attitude)
        self.attitude_control_thruster[int(self.attitude)-1]
        #print(self.attitude_control_thruster[int(self.attitude)-1])
        
    def ephemeris_pre_load(self):
        print("Ephemeris load Pre maneuver?")
        self.ans_pre=input("Yes/No\n")
        
    def ephemeris_post_load(self):
        print("Ephemeris load Post maneuver?")
        self.ans_post=input("Yes/No\n")
        
    def generate_file(self):
        text=f"""##              MANEUVER COMMAND ARGUMENT FILE
## ==========================================================
## Generated at:       {today}
## Spacecraft:         mx3
## Maneuver Number:    {self.manv}
## Maneuver Type:      EWSK_MNVR
## Maneuver Direction: EASTWEST
## Maneuver Mode:      REA
## Thruster Config:    {self.patternFinded_ThrusterCfgManv[0]}
## SOP Name:           OP31101
## Ignition Time:      {self.IgnitionManv_date.strftime("%Y-%j-%H:%M:%S")}
## Cutoff Time:        {self.CutoffManv_date.strftime("%Y-%j-%H:%M:%S")}
## Directory:          V:/mx3/ARES/Argument Files
## Filename:           OP31101_EASTWEST_{self.manv}.arg
## User Comment:       {comments}
## ==========================================================
##

#Maneuver Start Time
#YYYY-DOY-HH:MM:SS
#
man_T0_time={self.IgnitionManv_date.strftime("%Y-%j-%H:%M:%S")}

#Valid values for DV thruster sets
# DV_EAST_ODD DV_EAST_ALL DV_EAST_EVEN DV_WEST_ODD DV_WEST_ALL DV_WEST_EVEN
#
delta_v_thruster={self.patternFinded_ThrusterCfgManv[0]}

#Valid values for attitude control thrusters
# E_ALL_NORTH_ALL W_ALL_NORTH_ALL E_W_N_EVEN
#
attitude_control_thruster={self.attitude_control_thruster[int(self.attitude)-1]}

#Attitude parameters

ACS_roll_torque_bias={format(self.new_values[1],".4f")}
ACS_pitch_torque_bias={format(self.new_values[2],".4f")}
ACS_yaw_torque_bias={format(self.new_values[3],".4f")}

ACS_jet_pulse_period=4
ACS_jet_pulse_width=0.4
ACS_jet_seconds_duration={format(self.patternFinded_ThrusterSecsTotalManv[0],".2f")}
ACS_jet_seconds_ratio=1

#Ephemeris load Pre maneuver
#Yes or No
#
ephemeris_pre_load={self.ans_pre}

#Ephemeris load Post maneuver
#Yes or No
#
ephemeris_post_load={self.ans_post}
        """
        print(text)
       
    
        
        
    
manv_EWSK= EWSK_Single()
[today, YYYYDDD, time]= Ephemeris().current_date()
#print(today)
comments= Ephemeris().user_comments()
#print(comments)
manv_EWSK.generate_file()



#manv_EWSK.get_maneuver()
#manv_EWSK.get_manvRef()
#manv_EWSK.get_file_ManvRef()
#manv_EWSK.find_data_manvRef()
#manv_EWSK.get_torque()
#manv_EWSK.average_torque()
#manv_EWSK.get_requested_torques()
#manv_EWSK.get_new_values()
#manv_EWSK.make_a_decision()
#manv_EWSK.get_file_ManvPLAN()
#manv_EWSK.find_data_manv()
#manv_EWSK.control_thrusters()




