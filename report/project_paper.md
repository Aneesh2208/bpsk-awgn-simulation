# Simulation and Theoretical Validation of a Binary Phase Shift Keying (BPSK) Digital Communication System over an Additive White Gaussian Noise (AWGN) Channel


## Abstract
This project presents the simulation and theoretical validation of a Binary Phase Shift Keying (BPSK) digital communication system operating over an Additive White Gaussian Noise (AWGN) channel. A complete end-to-end communication model was implemented, including binary data generation, BPSK modulation, noise addition, receiver demodulation, and Bit Error Rate (BER) analysis. Monte Carlo simulations were performed for different noise levels to study the statistical behavior of BER. The simulated results were compared with theoretical BER expressions for BPSK and showed close agreement as the number of transmitted bits increased. This project demonstrates the effect of noise on digital communication systems and validates theoretical concepts through practical simulation.



## 1. Introduction
Digital communication systems are a fundamental part of modern electronics, enabling reliable transmission of information in the presence of noise and channel imperfections. Such systems are widely used in wireless communication, data networks, and electronic devices. Despite differences in applications, the core challenge remains the same: accurately transmitting digital data over noisy channels.

The aim of this project is to design and simulate a complete digital communication system at the system level. The project focuses on understanding how binary data is represented as signals, how noise affects transmission, and how system performance can be evaluated using quantitative measures such as Bit Error Rate (BER).



## 2. System Overview
The digital communication system implemented in this project follows a standard block-based structure. The system consists of a binary data source, a transmitter, a communication channel, a receiver, and a performance evaluation block.

Binary data is first generated and represented as a digital signal. This signal is then modulated at the transmitter and passed through a noisy channel. At the receiver, the signal is detected and the transmitted data is recovered. Finally, the performance of the system is evaluated using error-based metrics.



## 3. Digital Data Generation
In the first stage of the system, random binary data is generated to model an information source. Each bit can take a value of either 0 or 1. This binary sequence is then converted into a discrete-time digital signal, where each bit is represented by a constant amplitude over a fixed duration.

This representation helps visualize how abstract binary information is mapped to physical signal levels. The resulting digital signal serves as the input to the transmitter stage of the communication system.



## 4. Transmitter Design
The transmitter converts the binary data into a modulated signal suitable for transmission over a noisy channel. In this project, Binary Phase Shift Keying (BPSK) modulation is used.

Each binary bit is mapped to a corresponding signal level. A bit value of 1 is represented by a positive amplitude (+1), while a bit value of 0 is represented by a negative amplitude (−1). This mapping corresponds to a phase shift of 0° and 180°, respectively.

The resulting sequence of BPSK symbols forms the discrete-time output of the transmitter and is used as the input to the channel. The modulated signal is visualized using stem plots to clearly show the symbol-level structure.



## 5. Channel Modeling
In real communication systems, transmitted signals are affected by noise introduced by electronic components and the transmission medium. To model this effect, an Additive White Gaussian Noise (AWGN) channel is used in this project.

Gaussian noise with zero mean is added to the transmitted BPSK symbols. The noise strength is controlled using the standard deviation parameter, allowing different channel conditions to be simulated. The received signal differs from the transmitted signal due to random noise fluctuations.

This channel model provides a realistic representation of signal corruption and enables analysis of receiver performance under noisy conditions.



## 6. Receiver Design
The receiver processes the noisy signal obtained from the channel and attempts to recover the original transmitted data. A simple hard-decision detection method is used for BPSK demodulation.

Each received symbol is compared against a zero-amplitude decision threshold. If the received value is greater than zero, the symbol is detected as a binary 1; otherwise, it is detected as a binary 0. This decision rule is based on the polarity of the BPSK symbols.

Due to the presence of noise, some received symbols may cross the decision boundary, resulting in incorrect bit decisions. This behavior directly affects system performance and leads to bit errors.



## 7. Performance Evaluation
System performance is evaluated using the Bit Error Rate (BER), which is defined as the ratio of incorrectly detected bits to the total number of transmitted bits.

After demodulation, the received bit sequence is compared with the original transmitted sequence to count the number of bit errors. The calculated BER provides a quantitative measure of the reliability of the communication system under noisy conditions.

Since noise is random in nature, BER values may vary across different simulation runs. This variation reflects real-world communication behavior and highlights the need for statistical analysis.



## 8. Results and Discussion
The performance of the communication system is analyzed by studying the variation of BER with respect to channel noise. BER is computed for multiple values of noise standard deviation to observe system behavior under different noise conditions.

The results show that BER increases as noise strength increases. At low noise levels, most symbols are correctly detected, resulting in very low BER. As noise increases, more symbols cross the decision threshold, leading to higher BER.

This observed trend matches theoretical expectations for BPSK systems and clearly demonstrates the trade-off between noise and system reliability.



## 9. Theoretical Validation
To validate the simulation results, the theoretical Bit Error Rate for BPSK over an AWGN channel is calculated using standard analytical expressions. Monte Carlo averaging is performed over multiple noise realizations to reduce statistical fluctuations in the simulated BER.

The simulated BER closely follows the theoretical BER curve, especially as the number of transmitted bits increases. At high noise levels, BER approaches 0.5, indicating random detection. This agreement confirms the correctness of the system model and simulation approach.



## 10. Conclusion
This project successfully demonstrated the simulation and theoretical validation of a Binary Phase Shift Keying (BPSK) digital communication system operating over an Additive White Gaussian Noise (AWGN) channel. A complete end-to-end system was implemented, covering data generation, modulation, noise modeling, receiver demodulation, and performance evaluation using Bit Error Rate (BER).

Monte Carlo simulations were used to analyze system performance under different noise conditions, and the simulated results showed close agreement with theoretical predictions. The results clearly illustrate how noise affects communication reliability and highlight the statistical nature of BER.

Overall, this project bridges theoretical concepts with practical simulation and provides a strong foundation for understanding digital modulation, noise effects, and receiver performance. The approach can be extended to more advanced modulation schemes, error-correcting codes, and hardware-level noise margin analysis, making it relevant for further study in digital communication and semiconductor-related applications.
