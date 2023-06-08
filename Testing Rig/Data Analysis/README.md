# Data analysis and comparison to the model
---
Author: Alban Wales

## Variable parameters in the model
---

In the model we developed, we had two major parameters we could play with to alter the model simulation results.
1. The turbidity of the solution. Using Beer-Lambert's law, we could play with the turbidity factor to increase or decrease the attenuation of light. Attenuation is an inverted exponential of the distance to the light source multiplied by the turbidity index mu
2. The light source itself, whether it is a point source or a expanded light source.


## Comparison between the model and the experimental results
---
As shown in :
- `light_intensity_sample_plot.png`

We obtained a uniform light distribution on the circumference for all the points that were at an angle between 90 degrees and 270 degrees. On the other hand, all the other points received close to not light at all.


When running our model with a standard value of mu=0.15, we obtained the following light distribution around the circumference of the jar.

![mu0 15](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/406707c6-1b1e-4608-ae0a-43dfe3599639)

As the turbidity doesn't seem to be high enough, we kept increasing the turbidity, with mu=0.25 and mu=1.

![mu0 25](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/f417c61f-ad01-4f5c-a01e-b9cbb9862915)
![mu=1](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/09ead089-eb72-4266-b022-f0de332a5d70)

---

As we can see, we are starting have a curve that is flattened in the middle, which is what we want to able to model.

## Finding the right turbidity value
---
After a bit of playing around with the model, we came to the conclusion that the best mu value we could find was mu=1.38 .
![mu1 38](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/53e5ce31-1f0c-4613-a069-6c3956033ed8)

However, we still have differences with our experimental as we don't experience as massive a drop in light intensity as in our experiments.

![exp](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/6582188f-5e63-41d4-b880-5dc3c8e1f66d)

## Limits of our experimental data
---

It is important for us to not only be critical of our theoretical model, which is a simplified version of the phenonemon, but also of our experimental data.
Indeed, such a drop in light intensity when going past a certain angle doesn't appear very physically intuitive.

We came up with two reasons that can explain this observation:
1. Our sensors have a deadzone, which prevents them from receiving light at certain angles, in our case when the angle to light source is less than 90 degrees.
![deadzone](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/a84c3107-f2ea-4ac4-8121-655246cfccf1)

2. We have total internal reflection: in very low angles of approach, this phenomenon is very common. Light is reflected against the inner circumference of the bioreactor, and is therefore not transmitted outside to the sensors.
![internal](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/e8bed5fa-5d3f-4cf0-9172-dfcfa44f3391)
Total internal reflection can be calculated and predicted using the Descartes-Snell law.
![descartes](https://github.com/ArnavKoshy/GM2-OptogeneticControl/assets/135922158/028ef37b-f264-4712-af75-0dbc17187ee4)

---
## Conclusion
---
We have been able to get our model to match somewhat closely our data by increasing the turbidity index of the media in the bioreactor.
However, it would be very interesting to further study the reasons explaining the differences between the model and the results.

