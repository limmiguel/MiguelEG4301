import serial
import csv
from datetime import datetime

arduino_port = "/dev/cu.usbmodem1101"
baud = 9600
fileName = "COM4"
sensor_data = []
header = ['Date/Time','LU','MU','RU','LM','MM','RM','LB','MB','RB']
with open(fileName,'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

ser = serial.Serial(arduino_port,baud)
print("Connected to arduino port: " + arduino_port)
#file = open(fileName,"a")
#print("created file")

#Data Display


while (True):
    getData = ser.readline()
    dataString = getData.decode('utf-8')
    parsedData = dataString[0:][:-2]
    reading = parsedData.split(",")
    currentTime = str(datetime.now())
    reading.insert(0,currentTime)
    #sensor_data.append(reading)
    print(reading)

    
    with open(fileName,'a', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(reading)
    
    
