# Arduino Code

The Arduino code is designed to collect and stream data to a laptop running the corresponding python file (See [Data Collection](Testing%20Rig/DataCollection))

The principal of operation is polling sensors with digital inputs. The sensors are selected by selecting corresponding connection on the analog multiplexer (See [Circuitry](Testing%20Rig/PhotodiodeAmplification))

The code is quite simple, and is documented internally. To run it, [Arduino IDE](https://www.arduino.cc/en/software) is required. Connect the Arduino, open code and select upload. Interfacing with the Arduino is done through Python.
