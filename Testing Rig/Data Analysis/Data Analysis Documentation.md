# Guide to Data Analysis
Author: Jasmine

This is a brief guide that will explain the process and testing result of data analysis. It is based on the circuit design and datalogging program that is explained detailedly in the other files in Testing Rig folder.  
After data logging, you should have .csv files loading all the data you have. Here are the steps needed to calibrate the raw data to something we can use directly to build empirical formulars of the model, or for other purpurses:
1. Zero Reading Calibration
2. Position Calibration
3. Wavelength  Sensitivity Calibration

### Zero Reading Calibration
The data you have already logged should each include a set of reading with no light. Subtracting the raw data with this set helps remove background noises, which are inevitable in most of the cases.

### Position Calibration
For simplicity in ensembling, the apparatus we used in the testing have photodiodes randomly fitted in the testing rig, therefore before the test we covered the sensors one by one. This data is then used to remap the sensors in correct order aroung the circumference. This may not be the case in real application, as you'd probably like to label and fix photodiodes' position for simplicity. However if there's a need to do so, remap can be done as it was shown in the python code.

### Wavelength Sensitivity Calibration
The photodiodes normally have a relative sensitivity curve showing its different sensitivity corresponding to different wavelength. For SFH 203 P, which we used in our design, the sensitivity curve is ![here]. If another type of photodiode is used, check the datasheet for its own sensitivity curve. The code we used simply divide the corresponding datasets with red, blue and green light by their sensitivity to calibrate their light intensity reading.

## Sample results
[light_intensity_sample.jpg]
Explanation of the curve.
