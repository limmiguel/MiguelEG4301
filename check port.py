import serial.tools.list_ports

def find_arduino_port():
    # Get a list of all available ports
    ports = list(serial.tools.list_ports.comports())

    if not ports:
        print("No serial ports found.")
    else:
        for port, desc, hwid in ports:
            print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")

            # Check if the description or hardware ID contains "Arduino"
            if "Arduino" in desc or "Arduino" in hwid:
                return port

    return None

arduino_port = find_arduino_port()

if arduino_port:
    print(f"Arduino found on port {arduino_port}")
else:
    print("Arduino not found.")
