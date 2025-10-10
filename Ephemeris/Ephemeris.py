import re
from datetime import datetime


def current_date():
    now= datetime.now()
    today= str(now)[:-7]
    YYYYDDD= now.strftime("%Y-%j")
    time= now.time()
    time= now.strftime("%H%M%S")
    return today, YYYYDDD, time

def request_dateTime():
    date_requested= input("Introduce una fecha YYYY/MM/DD HH:mm: \n")
    date_requested= date_requested+":00.000"
    return date_requested

def user_comments():
    comments= input("Comentarios: ")
    return comments


def get_file():
    file = open(r'C:\Users\Joel\Documents\Python\Nave_Espacial\Ephemeris\mx3_NSSK0811_PLAN_EPHUP.rpt', 'r')
    content = file.read()
    file.close()
    return content

def find_date(date_requested, content):
    print(date_requested)
    #pattern= fr"{date_requested}\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)"
    pattern= date_requested+r"\s+(-?\d+.\d+)"*6
    pattern_finded_startDateTime= re.findall(pattern ,content)
    return pattern_finded_startDateTime


def convert_date_J2000(date_requested): 
    J2000=datetime(2000,1,1,12,00,0)

    year= date_requested[0:4]
    month= date_requested[5:7]
    day= date_requested[8:11]
    hour= date_requested[11:13]
    minute= date_requested[14:16]

    date_J2000=datetime(int(year),int(month),int(day),int(hour),int(minute)).timestamp()-J2000.timestamp()
    #print(ans.days*60*60*24+ans.seconds)
    return date_J2000


def generate_file(today, date_requested, YYYYDDD, time, comments, date_J2000, list_values):
    text=f"""
    ##           EPHEMERIS UPLOAD COMMAND ARGUMENT FILE
    ## ===============================================================
    ## Generated at:       {today}
    ## Spacecraft:         mx3
    ## SOP Name:           OP31102
    ## User Selected:      {date_requested}
    ## Found Epoch:        {date_requested}
    ## Directory:          V:/mx3/ARES/Argument Files
    ## Filename:           OP31102_{YYYYDDD[:-4]}_{YYYYDDD[-3:]}_{time}.arg
    ## User Comment:       {comments}
    ## ===============================================================
    ##

    #Ephemeris Epoch Time
    #J2000 seconds for {today}
    #
    load_update_time={date_J2000}

    #Ephemeris J2000.0 X Position
    #0
    #
    load_x_position={list_values[0][0]}

    #Ephemeris J2000.0 Y Position
    #0
    #
    load_y_position={list_values[0][1]}

    #Ephemeris J2000.0 Z Position
    #0
    #
    load_z_position={list_values[0][2]}

    #Ephemeris J2000.0 X Velocity
    #0
    #
    load_x_velocity={list_values[0][3]}

    #Ephemeris J2000.0 Y Velocity
    #0
    #
    load_y_velocity={list_values[0][4]}

    #Ephemeris J2000.0 Z Velocity
    #0
    #
    load_z_velocity={list_values[0][5]}

    """
    
    textfile= open(fr'C:\Users\Joel\Documents\Python\Nave_Espacial\Ephemeris\OP31102_{YYYYDDD[:-4]}_{YYYYDDD[-3:]}_{time}.arg', 'w')
    textfile.write(text)
    textfile.close()
    


today= current_date()[0]
YYYYDDD= current_date()[1]
time= current_date()[2]
date_requested= request_dateTime()
comments= user_comments()
content= get_file()

list_values= find_date(date_requested, content)
date_J2000= convert_date_J2000(date_requested)

generate_file(today, date_requested, YYYYDDD, time, comments, date_J2000, list_values)