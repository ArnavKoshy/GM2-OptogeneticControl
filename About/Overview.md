# Project Overview

## Problem Overview

In many developing countries, the gaps in terms of research and equipment is significant. One example is the accessibility to reagents for enzyme is very limited, and this cause troubles in their research and development. One effective solution is to use optogenetic device to boost the production of bacteria. This will help scientists in the Global South greatly, so they no longer limit the creativity, ambition and impacts. **In this project, our group coorperate with Jenny Molloy to improve the optogenetic device.**

## Technical Summary

<img width="350" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/ff8c2e23-a962-44b2-bfcb-e98c5cec0e04">  

Multiple optogenetics designs has already been built previously, and their literatures helped us greatly to start up the project. However, one main problem with these designs is a lack of experimental data on light intensity and quantitative analysis to help achieve more accurate monitor the optogenetics control.  
To solve this problem, we built a testing rig that measures the light intensity circumferentially to collect experimental data. We also came up with a numerical model, which is implemented in python and effectively simulate the light transmission behaviour through any cylinderial container. 
After data collection, we put the experimental data and analytic solution together and fit the parameters in the theoretical model, and evaluated its behaviour.

<img width="395" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/70f4ca4f-ded8-41fa-a62a-b4670c044252">

Above is the prototype of our testing rig and lighting rig. 


## Results and Further improvements
<img width="594" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/5dc54220-e126-4d3c-a4dd-f26d841aab45">


The testing rig and model has satisfactory behaviour considering the time scale and resources we're given, and they demonstrated the feasibility of our model. However, there are several possible improvements listed above.  
What's more, on the biology side of this project, it would be idea to have further data analysis and modelling relating the light intensity to the actual bacteria growth rate, which we cannot easily implement. Combining this to our current outcome will achieve more mature optogenetic control such as using PID control to boost the bacteria production even further.
