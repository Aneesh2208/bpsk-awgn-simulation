# BPSK Communication System Simulation over AWGN

## 📌 What is this project?
This project is a hands-on simulation of a **digital communication system** built using  
**Binary Phase Shift Keying (BPSK)** over an  
**Additive White Gaussian Noise (AWGN)** channel.

The goal of this project is to understand how digital data is transmitted, how noise affects the signal, and how errors occur in real-world communication systems. Instead of only studying theory, this project focuses on **actually building and validating the system through simulation**.

---

## 🎯 Why I built this
I built this project to strengthen my fundamentals in digital communication and signal processing. It helped me move from theoretical formulas to practical understanding by visualizing signals, adding noise, measuring errors, and validating results against theory.

This project also serves as a foundation for more advanced topics such as higher-order modulation, error correction, and hardware-level signal integrity analysis.

---

## ⚙️ How the system works (step by step)

1. **Binary data generation**  
   Random binary bits (0s and 1s) are generated to represent digital information.

2. **Digital signal visualization**  
   The binary data is visualized as a digital waveform to better understand how information is represented.

3. **BPSK modulation**  
   Each bit is mapped to a signal level:
   - Bit `1` → `+1`
   - Bit `0` → `-1`

4. **AWGN channel**  
   Gaussian noise is added to the transmitted signal to model real-world channel effects.

5. **Receiver (demodulation)**  
   The receiver makes a simple decision:
   - If the received value is greater than 0 → bit `1`
   - Otherwise → bit `0`

6. **Performance evaluation**  
   - Bit Error Rate (BER) is calculated
   - BER vs noise is analyzed using Monte Carlo simulation
   - Simulated results are compared with theoretical BER

---

## 📊 Results and observations
- As noise increases, the Bit Error Rate (BER) increases
- With fewer transmitted bits, BER fluctuates due to randomness
- Increasing the number of bits reduces these fluctuations
- For large sample sizes, the simulated BER closely matches the theoretical curve
- At very high noise levels, BER approaches **0.5**, meaning the receiver is effectively guessing

---

## 📁 Project structure

```
Digital_Comm_Project/
├── README.md
├── src/
│   └── main.py
├── plots/
│   ├── ber_N100
│   ├── ber_N500
│   ├── ber_N1000
│   ├── ber_N10000
├── report/
│   └── project_paper.md
```

---

## 🛠 Tools used
- Python
- NumPy (numerical computation)
- Matplotlib (signal and performance visualization)
- SciPy (theoretical BER calculation)

---

## 🧠 Key takeaways
- Noise introduces unavoidable errors in communication systems
- BER is a statistical measure and requires large sample sizes for accuracy
- Monte Carlo simulation is essential for reliable performance analysis
- Practical simulations can effectively validate communication theory

---

## 🚀 Future improvements
- Extend the system to higher-order modulation schemes (QPSK, QAM)
- Add error-correcting codes
- Explore soft-decision receivers
- Relate simulation results to hardware noise margins and semiconductor design

---

## 👤 Author
**Aneesh Sridhar**

This project was created as a step toward building strong fundamentals in digital communication, signal processing, and hardware-oriented system analysis.
