# Additional testing Rig Documentation
---
Author: Alban Wales

## Description
---
This folder contains the files which will allow for more extensive testing of light intensity within the bioreactor, as our measurements were only made outside of the bioreactor, which has issues with internal reflection for instance.

In order to test internally the intensity of the light without contaminating the bacterial environment, we designed a lid that enabled us to insert a test tube with a light sensor in it, as Jenny advised this was the most effective way to conduct measurements inside the jar. Indeed, test tube are transparent and their reflective/refraction are very similar to the air's. Furthermore, they are very easy to source in lab environment. 


This lid clips on a pre-existing jar that Jenny and her team use in their experiments. 

The constraints design-wise are:
  - It has to fit on the lid base
  - A test tube has to be able to fit in the middle of it.
 
With these constraints in mind, we started to design the testing lid.


## Testing rig design
---
After a couple of unsuccessful iterations due to 3D-printing issues (gcode file issues) and wrong dimensions, we printed the following lid.


![IMG_2966](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/a1311748-f724-4ec4-8907-7b22cbc55b27)
![IMG_2967](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/634f0c6a-2f8e-4a59-8c0c-170bfaad6b5e)
![IMG_2965](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/24c02c67-ae47-4299-a565-09b996b5b249)


## Cad file and design specifications
---
The lid is a lid that clips on top of a pre-existing lid.

-	`internal_testing_lid.SLDPRT`

It has a hole of 8.1mm radius in its, to accomodate for a test tube when measuring light in the center of the jar. We chose to have 2mm of extra room for the test tube (16mm diameter) as 3D print can sometimes not be as accurate as expected, and to also account for the tolerance on the test tube diameter.

It features a 19 mm tube in order to guide the test tube down, and the lid is 4mm thick.

There are four clicking-on extensions, which click on into place on 4 pre-installed screws on the lid base.


