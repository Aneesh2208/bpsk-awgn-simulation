# Simulation and Theoretical Validation of a Binary Phase Shift Keying (BPSK) Digital Communication System over an Additive White Gaussian Noise (AWGN) Channel

## Abstract
(To be written last)

## 1. Introduction
Digital communication systems form the backbone of modern electronics, enabling reliable transfer of information in the presence of noise and distortion. From wireless communication to on-chip interconnects, the fundamental challenge remains the same: transmitting digital data accurately over imperfect channels.

This project aims to design and simulate a complete digital communication system at the system level. The objective is to understand how binary data is represented as signals, how noise affects transmission, and how system performance can be evaluated using quantitative metrics.

## 2. System Overview
The digital communication system implemented in this project follows a standard block-based architecture. The system consists of a binary data source, a transmitter, a communication channel, a receiver, and a performance evaluation block.

Binary data is first generated and represented as a time-domain digital signal. This signal is then processed by the transmitter for transmission over a noisy channel. At the receiver, the signal is detected and the original data is recovered. Finally, system performance is analyzed using error metrics.

## 3. Digital Data Generation
In the first stage of the system, random binary data is generated to model an information source. Each bit takes a value of either 0 or 1. This binary data is then converted into a discrete-time digital signal, where each bit is represented by a constant amplitude level over a fixed duration.

This representation allows visualization of how abstract digital information is mapped into physical signal levels. Such a digital baseband signal forms the input to the transmitter stage of the communication system.

## 4. Transmitter Design
The transmitter converts binary data into a modulated signal suitable for transmission. In this project, Binary Phase Shift Keying (BPSK) modulation is implemented at baseband.

Each binary bit is mapped to a corresponding signal symbol. A bit value of 1 is represented by a positive amplitude (+1), while a bit value of 0 is represented by a negative amplitude (−1). This polarity-based mapping corresponds to a phase shift of 0° and 180°, respectively.
 
The resulting sequence of BPSK symbols represents the discrete-time output of the transmitter. These symbols form the input to the communication channel and are visualized using a stem plot to highlight the symbol-level structure of the modulated signal.

## 5. Channel Modeling
In practical communication systems, transmitted signals are affected by noise introduced by electronic components and the transmission medium. To model this behavior, an Additive White Gaussian Noise (AWGN) channel is implemented.

Gaussian noise with zero mean is added to the transmitted BPSK symbols. The noise strength is controlled using the standard deviation parameter, allowing simulation of different channel conditions. The resulting received signal differs from the ideal transmitted signal due to random noise fluctuations.

This channel model provides a realistic representation of signal corruption and serves as the basis for analyzing receiver performance and error behavior in subsequent stages.

## 6. Receiver Design
The receiver processes the noisy signal obtained from the channel and attempts to recover the transmitted binary data. A simple hard-decision detection method is employed for BPSK demodulation.

Each received symbol is compared against a zero-amplitude decision boundary. Symbols with positive amplitude are detected as binary 1, while symbols with negative amplitude are detected as binary 0. This decision rule exploits the polarity-based representation of BPSK modulation.

Due to the presence of noise, some received symbols may cross the decision boundary, resulting in incorrect bit decisions. This behavior forms the basis for performance evaluation in terms of error rates.


## 7. Performance Evaluation
To quantitatively evaluate system performance, the Bit Error Rate (BER) is calculated. BER is defined as the ratio of incorrectly detected bits to the total number of transmitted bits.

After demodulation, the received bit sequence is compared with the original transmitted data to count bit errors. The resulting BER provides a direct measure of the reliability of the communication system under noisy conditions.

As expected, the presence of additive Gaussian noise introduces bit errors, leading to a non-zero BER. The observed BER varies across runs due to the random nature of noise, reflecting real-world communication behavior.


## 8. Results and Discussion
The performance of the digital communication system is evaluated by analyzing the Bit Error Rate (BER) as a function of channel noise. BER is computed for multiple noise standard deviation values to observe system behavior under varying channel conditions.

The results show a clear increasing trend in BER as noise strength increases. At low noise levels, most symbols remain correctly detected, resulting in near-zero BER. As noise increases, a larger number of received symbols cross the decision boundary, leading to higher BER.

This behavior aligns with theoretical expectations for BPSK systems and highlights the trade-off between noise robustness and system reliability in practical communication environments.

## 9. Theoretical Validation
To validate the simulated results, the theoretical Bit Error Rate (BER) for BPSK over an AWGN channel is computed using the Q-function formulation. Monte Carlo averaging is performed over multiple noise realizations to reduce statistical variance.

The simulated BER closely follows the theoretical curve, confirming correct system implementation. As the noise standard deviation increases, BER approaches 0.5, indicating random detection in high-noise conditions. This convergence demonstrates agreement between theory and simulation.

## 10. Conclusion
This project presented the simulation and theoretical validation of a Binary Phase Shift Keying (BPSK) digital communication system operating over an Additive White Gaussian Noise (AWGN) channel. An end-to-end communication chain was implemented, including binary data generation, BPSK modulation, noisy channel modeling, receiver demodulation using hard decision detection, and performance evaluation using Bit Error Rate (BER).

Monte Carlo simulations were conducted over a range of noise standard deviation values to estimate the BER under different channel conditions. The simulated BER results closely matched the theoretical BER derived from the Q-function, demonstrating convergence as the number of transmitted bits and averaging trials increased. This agreement confirms the correctness of the system model, noise representation, and receiver decision logic.

The results clearly illustrate the fundamental trade-off between noise strength and system reliability, showing that BER increases monotonically with increasing noise and approaches 0.5 under high-noise conditions, where symbol decisions become random. The observed behavior aligns with established communication theory and validates the effectiveness of Monte Carlo methods for performance analysis.

Overall, this project successfully bridges theoretical communication concepts with practical simulation, providing a strong foundation for understanding digital modulation, noise effects, and receiver performance. The methodology and framework developed here can be extended to higher-order modulation schemes, channel coding techniques, and hardware-level noise margin analysis, making it relevant for advanced communication system design and semiconductor validation applications.

