import serial
import csv
from datetime import datetime

#fileTime = str(datetime.now().strftime('%H-%M-%S'))
current_time = datetime.now()
date_str = current_time.strftime('%Y-%m-%d')
hour_minute_str = current_time.strftime('%H-%M')

# Construct the file name
fileName = f"data_log_{date_str}_{hour_minute_str}.csv"


arduino_port = "COM4"
baud = 115200
#fileName = f"data_log_{fileTime}.csv"
sensor_data = []

header = ['Date/Time','LL','ML','RL','LU','MU','RU','LB','MB','RB','AIR_RB','AIR_LU','AIR_LL','AIR_RL','AIR_RU','AIR_LB']
with open(fileName,'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

ser = serial.Serial(arduino_port,baud)
print("Connected to arduino port: " + arduino_port)
#file = open(fileName,"a")
#print("created file")

#Data Display


while (True):
    data = ser.readline().decode().rstrip().split(',')
    airpressureData = data[9:]
    matpressureData = data[0:9]
    #print(airpressureData)
    #print(matpressureData)
    currentTime = str(datetime.now().strftime('%H:%M:%S'))
    data.insert(0,currentTime)
    print(airpressureData)
    print(matpressureData)

    with open(fileName,'a', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    
