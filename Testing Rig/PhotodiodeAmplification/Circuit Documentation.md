### Circuit documentation
Author: Jasmine  
Co-contributor: Arnav  

This circuit is designed in order to read signals from photodiodes. We use multiplexers to select signals, and transimpedance amplifiers to convert current signals to voltage signals.  
##### For purchasing the components, reference to the parts list in the repository: [Link to Another File](another-file.md)  

The circuits included in the circuit design in hiecharchy order:
1. Arduino Nano
2. Transimpedance Amplifiers Circuits x 3
3. 8-1 Multiplexer x 3
4. Photodiodes x 24

Explanation of functionality
Arduino Nano:  
Arduino sends digital inputs at pin Dx to select multiplexer input, and reads from .  
Multiplexers:  
Multiplexers are used for selecting signals between different photodiodes. Each multiplexer is connected to 8 photodiodes, and it receives input from Arduino's digital input to select the photodiodes' input to read from.

### Implementing the circuit design
#### Stripboard
![git01](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/0fa82ac9-b2c0-477e-8fc9-ed57fae085e9)


##### PCB design
For PCB design, referrence to the kiCAD project -- PCB, which should be self-explanatory. PCB is recommanded if you stick to the o

##### Compatibility Notice:
If the listed cannot be purchased, here are some suggestions for replacements...
If any components are altered, remember to change the footprints in "" in kiCAD, however due to the poor compatibility of PCB, we recommand using stripboard to perform the design.


##### 
