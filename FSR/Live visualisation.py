import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

import serial
import time
import csv

mat = 3
arduino = serial.Serial(port='/dev/cu.usbmodem1101', baudrate=115200, timeout=1)
time.sleep(2)  # Wait for the connection to initialize


# treat each grid point as a discrete mass and calculate the weighted average of their positions.
def centroid(matrix):
    if np.sum(matrix) != 0:
        x = np.sum(np.sum(matrix, axis=0) * np.arange(mat)) / np.sum(matrix)
        y = np.sum(np.sum(matrix, axis=1) * np.arange(mat)) / np.sum(matrix)
        return x, y
    else:
        return 1.5, 1.5


def read_arduino_data(arduino):
    """Read data from an Arduino and return it as a list."""
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        data = line.split(',')
        return data
    return None


X = np.arange(0, mat, step=1)  # X轴的坐标
Y = np.arange(0, mat, step=1)  # Y轴的坐标
calib = [0,0,0,0,0,0,0,0,0]

Z = np.zeros(shape=(mat, mat))
# centroid = np.zeros(shape=(1, 2))
xx, yy = np.meshgrid(X, Y)  # 网格化坐标
X, Y = xx.ravel(), yy.ravel()  # 矩阵扁平化
width = height = 1  # 每一个柱子的长和宽

# 绘图设置

plt.ion()
fig1 = plt.figure('3D Bar')
fig2 = plt.figure('2D Heatmap')
# fig3 = plt.figure('3D surface')
sns.set(font_scale=0.5)

count = 0

# Create a file name based on the current date and time
file_name = 'FSR/arduino_data_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.csv'

# Open the CSV file for writing
with open(file_name, 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile)

    # Write column headers
    headers = ['Time', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14',
               'A15']
    data_writer.writerow(headers)

    while True:
        try:
            # Read data from the Arduino board

            data = read_arduino_data(arduino)
            output = data[:9]
            pressure_m = np.array(output).reshape(3, 3)
            Z = pressure_m.astype(int)
            while count==0:
                calib = Z
                count = count+1
            while count<10:
                for i in range(3):
                    for j in range(3):
                        if calib[i][j] < Z[i][j]:
                            calib[i][j] = Z[i][j]
                count = count+1
            Z = Z - calib
            for i in range(3):
                for j in range(3):
                    if Z[i][j] < 0:
                        Z[i][j] = 0
            print(Z)

            if data:
                # Combine the data with the current time
                row = [time.strftime('%Y-%m-%d %H:%M:%S')] + data
                # Write the combined data to the CSV file
                data_writer.writerow(row)
                # Print the data to the console
                # print("Logged data:", row)

            # centroid_x1, centroid_y1 = cop(Z)
            # centroid_x = np.sum(np.sum(Z, axis=0) * np.arange(32)) / np.sum(Z)
            # centroid_y = np.sum(np.sum(Z, axis=1) * np.arange(32)) / np.sum(Z)
            centroid_x, centroid_y = centroid(Z)
            zz = Z.ravel()  # 扁平化矩阵

            colors = plt.cm.jet(zz / zz.max())
            ax = fig1.add_subplot(projection='3d')  # 三维坐标轴
            ax.bar3d(X, Y, np.zeros_like(zz), width, height, zz, color=colors, shade=True)
            # ax.bar3d(X, Y, np.zeros_like(zz), width, height, zz, shade=True)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('pressure')

            hm = fig2.add_subplot()
            sns.heatmap(Z, cmap="winter", annot=True, ax=hm)
            hm.scatter(x=centroid_x, y=centroid_y, marker='*', s=100, color='yellow')
            # hm.scatter(x=centroid_x1, y=centroid_y1, marker='*', s=100, color='red')
            print(centroid_x, centroid_y)
            #
            # surf = fig3.add_subplot(projection='3d')
            # surf.plot_surface(xx, yy, Z, cmap='viridis')

            plt.draw()
            plt.pause(1)
            plt.clf()

            # time.sleep(1)
        except KeyboardInterrupt:
            break
