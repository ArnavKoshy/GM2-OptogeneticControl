# Project Overview

## Problem Overview

In many developing countries, the gaps in terms of research and equipment is significant. An example of this is the limited access to reagents for enzyme synthesis. This limits the efficacy of research and development in developing countries. One proposed solution is to use optogenetics to induce the production of enzymes without needing reagents. This allows researchers with limited access to inducing agents to synthesis enzymes by illuminating bacteria. See [this paper](https://pubmed.ncbi.nlm.nih.gov/33255280/) for more information **In this project, our group cooperates with Jenny Molloy to improve the optogenetic device.**

<img width="350" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/137b9f05-121b-4fb2-870a-3a7d2c8b628c"> 

## Technical Summary

<img width="350" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/ff8c2e23-a962-44b2-bfcb-e98c5cec0e04">  

Multiple optogenetics designs has already been built previously, and their literatures helped us greatly to start up the project. However, one main problem with these designs is a lack of experimental data on light intensity and quantitative analysis to inform the design of an effective illumination system for a bioreactor with optically sensitive bacteria.
To solve this problem, we built a testing rig that measures the light intensity circumferentially to collect experimental data. We also came up with a numerical model, which is implemented in python and effectively simulate the light transmission behaviour through any cylindrical container. 
After data collection, we put the experimental data and analytic solution together and fit the parameters in the theoretical model, and evaluated its behaviour.

<img width="395" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/70f4ca4f-ded8-41fa-a62a-b4670c044252">

Above is the prototype of our testing rig and lighting rig.  


## Results and Further improvements
<img width="594" alt="image" src="https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/71087503/5dc54220-e126-4d3c-a4dd-f26d841aab45">


The testing rig and model has satisfactory behaviour considering the time scale and resources we're given, and they demonstrated the feasibility of our model. However, there are several possible improvements listed above.  
What's more, on the biology side of this project, it would be idea to have further data analysis and modelling relating the light intensity to the actual bacteria growth rate, which we cannot easily implement. Combining this to our current outcome will achieve allow more advanced solutions such as using PID control to control bacterial activity.

### Compatibility
We're aware that in developing countries the availability of components can be quite limited. Also, depending on the type of bacteria there may be different setups. For example, the wavelength of LED may be changed in different scenario. Our electrical design documentation had taken this into account and gave suggestions for substituting components. However, the modelling also require modification in that case, which would be feasible by changing model parameters.
