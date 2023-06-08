# Simulation and circuit design

This document outlines the initial design process for the amplification circuit elements, in case a ground-up redesign is considered.


## Amplifier Stage Design

###### Overview
The amplification circuit uses trans-impedance amplifiers (TIAs) to amplify the minute photodiode currents caused due to incident light. For the photodiode chosen, this current varies from $10nA$ to $50\mu A$.

The gain of the TIA is set by a single gain resistor. The output voltage is given by $I_d R_g + V_{off}$ where $I_d$ is the current through the diode, $R_g$ is the gain resistance and $V_{off}$ is the offset voltage applied to the non-inverting input. An additional capacitor is included to reduce noise.

The value of $R_g$ was chosen to allow the full range of currents through the diode to be measured. (See [Improvements](#improvements-for-redesign))

The choice to multiplex photodiodes before the amplifiers was made due to the significant cost and complexity benefits it provides. Only 3 amplifiers were needed, which amounted to a single chip, as opposed to the potential 6 ICs that would be needed without multiplexing.


###### Inclusion of Offset voltage
The amplifiers used are advertised as rail-to-rail, but actually can only drive outputs $25mV$ above $V_{ss}$ or below $V_{dd}$. 

In order to stay out of this region, a $50mV$ offset voltage was applied, so that the lowest output voltage of the TIA would always be $50mV$


###### Effect of multiplexer on resistance

When using a multiplexer before the inverting input of the amplifier, the resistance of the multiplexer was considered to confirm it had no impact on amplified reading. This was clear from a back-of-the-envelope circuit analysis, and was further verified in simulation.

## Simulation

[PhotodiodeStage.asc](PhotodiodeStage.asc) is an [LTSpice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) simulation of a single amplifier and photodiode. 

Photodiodes are not a standard part in the LTSpice library, so a phototransistor was used. This has a very similar working principle so was considered to be a usable substitute. 

The multiplexer resistance was taken into account with R3 - a $100 \Omega$ series resistance between the phototransistor and the inverting input of the amplifier.

A transient simulation has been set up for steadily increasing incident light on the phototransistor.

## Improvements for redesign

The photodiodes and amplifiers worked well in broad daylight, but were not sensitive enough for the low light intensities of bioreactor illumination. A different choice of photodiode would be beneficial, with a steeper current-light relationship. 

The gain resistance could also be changed to achieve the same effect.