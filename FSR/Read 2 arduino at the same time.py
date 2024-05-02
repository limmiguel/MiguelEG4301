import serial
import time

# Open serial connections to both Arduinos
arduino1 = serial.Serial('COM4', 9600)  # Replace 'COM3' with the correct port for Arduino 1
arduino2 = serial.Serial('COM6', 9600)  # Replace 'COM4' with the correct port for Arduino 2

time.sleep(2)  # Wait for the serial connections to initialize

while True:
    if arduino1.in_waiting > 0:
        data1 = arduino1.readline().decode('utf-8').strip()
        print(f"Arduino 1: {data1}")

    if arduino2.in_waiting > 0:
        data2 = arduino2.readline().decode('utf-8').strip()
        print(f"Arduino 2: {data2}")

    time.sleep(0.1)
