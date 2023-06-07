# Circuit Documentation
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

### Ensemble notice
#### Stripboard

For stripboard design, referrence to the schematic and [this picture](git01.jpg). After building the circuit, check if there's any short circuit to avoid damaging any component. Protect the weak connections using tape or glue gun.

##### PCB design
For PCB design, referrence to the kiCAD project -- PCB, which should be self-explanatory.  

### Compatibility Notice:
If the listed cannot be purchased, here are some suggestions for replacements:
Arduino board:  
Multiplexers:  
Photodiodes:  
If any components are altered, remember to change the footprints in kiCAD, however due to the poor compatibility of PCB, we recommand using stripboard to reproduce the design if you'd like to change any components, otherwising there may be mismatch when soldering.

things to include:  
Testing and Results: Mention any testing procedures that were conducted on the circuit and provide a summary of the results. This can include performance measurements, signal quality assessments, or any issues encountered during testing.

Operating Instructions: Provide instructions on how to operate the circuit, including any specific configurations or settings that need to be adjusted. Mention any safety precautions or considerations that should be taken while using the circuit.

Troubleshooting Tips: Include a section on troubleshooting common issues that may arise while using the circuit. This can help the recipient of the handover note in identifying and resolving potential problems.

Maintenance and Support: Provide information about the expected maintenance requirements of the circuit. This can include details on periodic checks, component replacements, or any specific procedures that should be followed for proper maintenance. Also, mention the contact information or resources available for further support or clarification.

Future Enhancements: If there are any plans for future enhancements or improvements to the circuit, mention them briefly. This can help the recipient understand potential areas for further development or customization.

Acknowledgments: Give credit to any additional contributors, collaborators, or sources of inspiration that played a role in the circuit design. Acknowledge their contributions and express gratitude for their assistance.