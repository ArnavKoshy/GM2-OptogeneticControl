# Circuit Design Documentation
Author: Jasmine  
Contributor: Arnav  

This circuit is designed in order to read signals from photodiodes. We use multiplexers to select signals, and transimpedance amplifiers to convert current signals to voltage signals.  
##### For purchasing the components, reference to the parts list in the repository: [Parts List For Referrence](https://github.com/ArnavKoshy/GM2-OptogeneticControl/blob/main/Testing%20Rig/PhotodiodeAmplification/parts_list.xlsx)  

## Table of Components
The circuits included in the circuit design in hiecharchy order:
1. Arduino Nano
2. Transimpedance Amplifiers Circuits x 3
3. 8-1 Multiplexer x 3
4. Photodiodes x 24


## Ensemble Notice
### Stripboard

For stripboard design, referrence to the schematic. Here is a picture of the prototype we made: [Stripboard Prototype](git01.jpg). After building the circuit, check if there's any short circuit to avoid damaging any component. Protect the weak connections using tape or glue gun.

#### PCB design
For PCB design, referrence to the kiCAD project -- PCB, which should be self-explanatory.  

### Troubleshooting
Check the following aspects when the circuit don't work properly:
1. Powering: Is the power enough to drive the circuit
2. Short Circuits: Are there any bare wires in contact? Are the components soldered properly? 
3. 

## Compatibility Notice:
If the listed cannot be purchased, here are some suggestions for replacements:
Arduino board: 
1. Arduino Uno
2. Arduino Pro Mini
3. ESP8266 NodeMCU  

Photodiodes: 
1. BPW34
2. TEMT6000
3. TSL2561  

Multiplexers:
1. 74HC4051
2. 74HC4067  

If any components are altered, remember to change the footprints in kiCAD, however due to the poor compatibility of PCB, we recommand using stripboard to reproduce the design if you'd like to change any components, otherwising there may be mismatch when soldering.


## Our testing and results

We've done a breadboard and a stripboard prototype. The breadboard testing functioned properly, but it seems it needs mounting to maintain the stability of positions of photodiodes. The stripboard passed the testing, but before data collection the arduino board malfunctioned and cannot function correctly.

## Future Enhancements

After testing, we find out the amplification factor for the circuit can be increased further to achieve better signal-to-noise ratio. It might be helpful to use a gain resistor of larger value. The capacitor value should be adjusted as well to maintain same level of filtering.  
For powering circuits with larger power than our prototype, we may need voltage regulation to maintain the voltage supply.

