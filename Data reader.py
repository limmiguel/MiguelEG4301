import serial
import time

# Set up the serial connections for both Arduino boards
arduino1 = serial.Serial(port='COM13', baudrate=115200, timeout=1)
arduino2 = serial.Serial(port='COM14', baudrate=115200, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

def read_arduino_data(arduino):
    """Read data from an Arduino and return it as a list."""
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        data = line.split(',')
        return data
    return None

while True:
    try:
        data1 = read_arduino_data(arduino1)
        data2 = read_arduino_data(arduino2)

        if data1:
            print("Arduino 1:", data1)
        if data2:
            print("Arduino 2:", data2)

        time.sleep(1)  # Read every second
    except KeyboardInterrupt:
        break

# Close the serial connections
arduino1.close()
arduino2.close()
