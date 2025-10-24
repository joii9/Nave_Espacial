import re
from datetime import datetime


class Ephemeris():
    def current_date(self):
        now= datetime.now()
        self.today= str(now)[:-7]
        self.YYYYDDD= now.strftime("%Y-%j")
        time= now.time()
        self.time= now.strftime("%H%M%S")
        return self.today, self.YYYYDDD, self.time

    def request_dateTime(self):
        date_requested= input("Introduce una fecha YYYY/MM/DD HH:mm: \n")
        self.date_requested= date_requested+":00.000"
        #return date_requested

    def user_comments(self):
        self.comments= input("Comentarios: ")
        return self.comments

    def get_file(self):
        file = open(r'C:\Users\epochtc\Documents\Joel\python\Spacecraft_projects\Generators\mx3_NSSK0811_PLAN_EPHUP.rpt', 'r')
        self.content = file.read()
        file.close()
        #return content

    def find_date(self): #, date_requested, content
        #print(self.date_requested)
        #pattern= fr"{date_requested}\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)"
        pattern= self.date_requested+r"\s+(-?\d+.\d+)"*6
        self.list_values= re.findall(pattern ,self.content)
        #return pattern_finded_startDateTime

    def convert_date_J2000(self): #, date_requested
        J2000=datetime(2000,1,1,12,00,0)

        year= self.date_requested[0:4]
        month= self.date_requested[5:7]
        day= self.date_requested[8:11]
        hour= self.date_requested[11:13]
        minute= self.date_requested[14:16]

        self.date_J2000=datetime(int(year),int(month),int(day),int(hour),int(minute)).timestamp()-J2000.timestamp()
        #print(ans.days*60*60*24+ans.seconds)
        #return date_J2000


    def generate_file(self):
        text=f"""##           EPHEMERIS UPLOAD COMMAND ARGUMENT FILE
## ===============================================================
## Generated at:       {self.today}
## Spacecraft:         mx3
## SOP Name:           OP31102
## User Selected:      {self.date_requested}
## Found Epoch:        {self.date_requested}
## Directory:          V:/mx3/ARES/Argument Files
## Filename:           OP31102_{self.YYYYDDD[:-4]}_{self.YYYYDDD[-3:]}_{self.time}.arg
## User Comment:       {self.comments}
## ===============================================================
##

#Ephemeris Epoch Time
#J2000 seconds for {self.today}
#
load_update_time={self.date_J2000}

#Ephemeris J2000.0 X Position
#0
#
load_x_position={self.list_values[0][0]}

#Ephemeris J2000.0 Y Position
#0
#
load_y_position={self.list_values[0][1]}

#Ephemeris J2000.0 Z Position
#0
#
load_z_position={self.list_values[0][2]}

#Ephemeris J2000.0 X Velocity
#0
#
load_x_velocity={self.list_values[0][3]}

#Ephemeris J2000.0 Y Velocity
#0
#
load_y_velocity={self.list_values[0][4]}

#Ephemeris J2000.0 Z Velocity
#0
#
load_z_velocity={self.list_values[0][5]}

"""
    
        textfile= open(fr'C:\Users\epochtc\Documents\Joel\python\Spacecraft_projects\Generators\output_ephemeris\OP31102_{self.YYYYDDD[:-4]}_{self.YYYYDDD[-3:]}_{self.time}.arg', 'w')
        textfile.write(text)
        textfile.close()
    