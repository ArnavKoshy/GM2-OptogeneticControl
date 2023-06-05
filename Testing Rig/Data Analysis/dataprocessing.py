import csv
import numpy as np
raw = {}

with open('DataCollection/1hr.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Get the header row
    
    for row in reader:
        if len(row) >= 9:
            key = row[0]
            values = list(map(float, row[1:]))
            if key not in raw:
                raw[key] = values
            else:
                print(f"Skipping duplicate entry for key: {key}")
        else:
            print(f"Skipping row with insufficient elements: {row}")

# Swap order
data = {key: [value[i] for i in [4, 2, 7, 3, 5, 0, 6, 1]] for key, value in raw.items()}
y = "y"
r = "r"
rgb = ["r", "g", "b"]
val1 = [0] #y index
val2 = [0,1,2] #rotation index
data_processed = {}
for i in val1:
    for j in rgb:
        key = "y{}{}".format(i,j)
        data_processed[key] = []
for i in val1:
    for j in rgb:
        for k in val2:
            key = "y{}r{}{}".format(i,k,j)#Crude data key
            calibration = "y{}r{}nolight".format(i,k)#Calibration key
            new_key = "y{}{}".format(i,j)#Processed data key
            data[key]=np.array(data[key])-np.array(data[calibration])#Calibration
            new_dict_value = data_processed[new_key] #Pre-load the value
            new_dict_value=np.append(data[key],new_dict_value) #Update the value
            data_processed[new_key] = new_dict_value#Load the uopdated value
            if j == "b":
                data_processed[new_key] = data_processed[new_key]/(0.3*2)
            if j == "g":
                data_processed[new_key] = data_processed[new_key]/(0.5*2)
            if j == "r":
                data_processed[new_key] = data_processed[new_key]/(0.79*2)
# put r0, r1, r2 together in one item
"""
combined_values = []
height = ["0", "1"]
set1 = ["y0r0b", "y0r1b", "y0r2b"]
set2 = ["y0r0g", "y0r1g", "y0r2g"]
set3 = ["y0r0r", "y0r1r", "y0r2r"]
set4 = ["y0r0nolight", "y0r1nolight", "y0r2nolight"]
red light: 660nm 79%
green light: 520nm 50%
blue light: 435nm 30%


"""



# print(combined_values)

import matplotlib.pyplot as plt

# Create a new figure and subplot
fig, ax = plt.subplots()
print(data_processed)
# Plot the 'r', 'g', and 'b' datasets on the same plot
for key, values in data_processed.items():
    if 'r' in key or 'g' in key or 'b' in key:
        if 'nolight' not in key:
            color = key[-1]  # Extract the color from the key
            label = f'{color.upper()} dataset'
            values_shift = np.roll(values, 7)# clockwise rotation by 7*15 = 105 degrees
            angular = np.linspace(0, 360, len(values))
            ax.scatter(angular, values_shift, label=label, color=color)
            ax.plot(angular, values_shift, color=color)

# Set the title and labels
ax.set_title("Variation in Light Intensity with Angular Position")

ax.set_xlabel("Angular Positions")
ax.set_ylabel("Value")

# Add a legend to the plot
handles, labels = ax.get_legend_handles_labels()
if handles and labels:
    ax.legend(handles, labels)

# Show the plot
plt.xticks(np.arange(min(angular), max(angular), 30))
plt.show()
