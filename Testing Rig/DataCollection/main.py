import csv
# changed to csv format for easier data processing
import serial

# Open the serial connection
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=25)  # Replace 'COM1' with the appropriate serial port

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
        label = input("Input test name, or q to end:")
        if label.strip() == "q":
            break
        print("Waiting for data")
        ser.write(b's')

        line = ser.readline().decode("ascii").strip()
        print(line)

        writer.writerow([label, line])

# Close the serial connection
ser.close()
