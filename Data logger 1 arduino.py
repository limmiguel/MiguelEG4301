import serial
import time
import csv

# Set up the serial connection for the Arduino board on COM14
arduino = serial.Serial(port='COM15', baudrate=115200, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

def read_arduino_data(arduino):
    """Read data from an Arduino and return it as a list."""
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        data = line.split(',')
        return data
    return None

# Create a file name based on the current date and time
file_name = 'arduino_data_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.csv'

# Open the CSV file for writing
with open(file_name, 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile)
    
    # Write column headers
    headers = ['Time', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
    data_writer.writerow(headers)

    while True:
        try:
            # Read data from the Arduino board
            data = read_arduino_data(arduino)
            
            if data:
                # Combine the data with the current time
                row = [time.strftime('%Y-%m-%d %H:%M:%S')] + data
                # Write the combined data to the CSV file
                data_writer.writerow(row)
                # Print the data to the console
                print("Logged data:", row)
            
            time.sleep(1)  # Read every second
        except KeyboardInterrupt:
            break

# Close the serial connection
arduino.close()
