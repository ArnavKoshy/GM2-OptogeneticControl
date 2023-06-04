
# install Serial Monitor
import serial

# Open the serial connection
ser = serial.Serial('COM5', 9600, timeout=25)  # Replace 'COM1' with the appropriate serial port

# Wait for the start command from the Arduino
#while ser.read().decode() != 's':
#    pass
# python send to arduino to start

file_name = input("Enter file name: ")
# time = input("Enter time: ")
# y_position = input("Enter y-position: ")
# angle_rotations = input("Enter angle rotations: ")

# Create a new file
with open(file_name, 'w+') as file:
    # # Write additional information to the file
    # file.write(f"Time: {time}\n")
    # file.write(f"Y-Position: {y_position}\n")
    # file.write(f"Angle Rotations: {angle_rotations}\n\n")
    # i = 0
    # print("Opened file, written")
    # print("Starting")
    
    # ser.write(b's')
    # to_continue = True
    # Read and write the photodiode values until the stop command is received
    while True:
        label = input("Input test name, or q to end:")
        if(label.strip() == "q"):
            break
        print("Waiting for data")
        file.write(label)
        file.write("\n")
        ser.write(b's')
        # print(i)
        
        line = ser.readline().decode("ascii")
        print(line)
        file.write(f"{line}\n")
        # i = i+1
        # line = ser.read().decode()
        # print(line)
        # file.write(line)
# Close the serial connection
ser.close()