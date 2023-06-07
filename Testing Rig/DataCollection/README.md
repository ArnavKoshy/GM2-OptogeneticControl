# Data collection documentation
Author: Arnav

## Description
---

This folder contains the files necessary to collect and store data from the Arduino when running light intensity measurements.

The `main.py` file does the following:

    - Establishes a connection with the Arduino over Serial.
    - Creates a new file in which to store data of a name of your choosing.
    - Requests the Arduino for data on command.
    - Stores the received data with an associated label.


## Instructions to run
---

### Requirements:
    - Python 3.10 or later
    - Python pip
    
### Running

Install necessary modules with `pip install -r requirements.txt`

Edit `main.py lines 5-6` with the serial port and baud rate (if you've changed it) of your Arduino (To find your serial port, try [this link](https://uk.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html)).

Then run `python main.py`

Enter a file name to store data
When prompted, enter a data label for the data point being collected. The python file will request data from the Arduino, wait until it responds (or times out) and then store that data under the label specified.


