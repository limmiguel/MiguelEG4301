import serial
import csv
from datetime import datetime
import numpy as np
import threading
import pandas as pd
import time

fileTime = str(datetime.now().strftime('%H-%M-%S'))
arduino_port = 'COM6'
baud = 115200
fileName = f"data_log_{fileTime}.csv"
excelFileName = f"data_log_{fileTime}.xlsx"  # Add this line for the Excel file

sensor_data = []
rows = 3
cols = 3
global mean_raw_sum, std_raw_sum, mean_x_coord, std_x_coord, mean_y_coord, std_y_coord, thresholdObtained, fileName_ICM

icmcounter_raw_sum = 0
icmcounter_x_coord = 0
icmcounter_y_coord = 0

thresholdObtained = False

header = ['Date/Time','LL','ML','RL','LU','MU','RU','LB','MB','RB','AIR_RB','AIR_LU','AIR_LL','AIR_RL','AIR_RU','AIR_LB','RAW_SUM','X_COORD','Y_COORD']
with open(fileName,'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

ser = serial.Serial(arduino_port,baud)
print("Connected to arduino port: " + arduino_port)

def threshold_identify():
    global mean_raw_sum, std_raw_sum, mean_x_coord, std_x_coord, mean_y_coord, std_y_coord, thresholdObtained, fileName_ICM
    header = ['Time','Raw Sum','X Coord','Y Coord']
    fileTime = str(datetime.now().strftime('%H-%M-%S'))
    fileName_ICM = f"data_log_ICM_{fileTime}.csv"
    with open(fileName_ICM,'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    data = pd.read_csv(fileName)
    if not data.empty:  # Check if the DataFrame is not empty
        icm_raw_sum = data['RAW_SUM'].values

        if len(icm_raw_sum) > 0:
            mean_raw_sum = np.mean(icm_raw_sum)
            std_raw_sum = np.std(icm_raw_sum)
        else:
            print("Empty icm_raw_sum array")
            mean_raw_sum, std_raw_sum = 0, 1  # Assign default values to avoid division by zero

        mean_x_coord = np.mean(data['X_COORD'].values)
        std_x_coord = np.std(data['X_COORD'].values)

        mean_y_coord = np.mean(data['Y_COORD'].values)
        std_y_coord = np.std(data['Y_COORD'].values)

        thresholdObtained = True
    else:
        print("Data DataFrame is empty. Threshold identification skipped.")


def icm_identify(data):
    global mean_raw_sum, std_raw_sum, mean_x_coord, std_x_coord, mean_y_coord, std_y_coord, icmcounter_raw_sum, icmcounter_x_coord, icmcounter_y_coord

    raw_sum = data[0]
    x_coord = data[1]
    y_coord = data[2]

    raw_sum_Zscore = abs((raw_sum - mean_raw_sum) / std_raw_sum)
    x_coord_Zscore = abs((x_coord - mean_x_coord) / std_x_coord)
    y_coord_Zscore = abs((y_coord - mean_y_coord) / std_y_coord)

    print(f'{raw_sum_Zscore}, {x_coord_Zscore},{y_coord_Zscore} ')
    if raw_sum_Zscore > 2:
        icmcounter_raw_sum += 1
    if x_coord_Zscore > 2:
        icmcounter_x_coord += 1
    if y_coord_Zscore > 2:
        icmcounter_y_coord += 1

    return [icmcounter_raw_sum, icmcounter_x_coord, icmcounter_y_coord]

def write_to_file(data):
    fileTime = str(datetime.now().strftime('%H-%M-%S'))
    data.insert(0, fileTime)
    with open(fileName_ICM, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print(f'Written {data}')

threading.Timer(11, threshold_identify).start()
starting_time = time.time()

while True:
    data = ser.readline().decode().rstrip().split(',')
    airpressureData = data[9:]
    matpressureData = data[0:9]

    if len(matpressureData) != rows * cols:
        print("Invalid size of matpressureData:", len(matpressureData))
        continue

    currentTime = str(datetime.now().strftime('%H:%M:%S'))
    print(f'{currentTime}   Raw pressure readings: {matpressureData}')
    data.insert(0, currentTime)

    pressure = np.array(matpressureData, dtype=float).reshape(rows, cols)
    total_pressure = np.sum(pressure)
    weighted_row = np.sum(np.sum(pressure, axis=1) * np.arange(rows))
    weighted_col = np.sum(np.sum(pressure, axis=0) * np.arange(cols))

    centroid_row = weighted_row / total_pressure
    centroid_col = weighted_col / total_pressure

    data.insert(16, total_pressure)
    data.insert(17, centroid_col)
    data.insert(18, centroid_row)
    icm_data = [total_pressure, centroid_col, centroid_row]
    print(icm_data)

    with open(fileName, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if thresholdObtained:
        time_interval = 600
        identified_icm = icm_identify(icm_data)

        if time.time() - starting_time >= time_interval:
            write_to_file(identified_icm)
            icmcounter_raw_sum = 0
            icmcounter_x_coord = 0
            icmcounter_y_coord = 0
            starting_time = time.time()

        print(f'{identified_icm}')

    # Save data to Excel file
    data_df = pd.DataFrame([data])  # Create a DataFrame with a single row
    data_df.to_excel(excelFileName, index=False, mode='a', header=False)
