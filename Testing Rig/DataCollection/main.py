import csv
# changed to csv format for easier data processing
import serial

PORT = '/dev/ttyACM0'
BAUD = 9600


# Open the serial connection
ser = serial.Serial(PORT, BAUD, timeout=25)  # Replace 'COM1' with the appropriate serial port

file_name = input("Enter file name: ")

# Convert file name to csv
if(not file_name.endswith(".csv")):
    file_name = file_name.split(".")[0]
    file_name += ".csv"


# Create a new file
with open(file_name, 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Test Name", "Data"])

    while True:

        # Wait for label, quit if q
        label = input("Input test name, or q to end:")
        label = label.strip()
        if label == "q":
            break

        # Ping arduino and wait
        ser.write(b's')
        print("Waiting for data")

        # Collect data and write to file
        line = ser.readline().decode("ascii").strip().split(',')
        print(line)

        writer.writerow([label] + [line])

# Close the serial connection
ser.close()
