import numpy as np
import matplotlib.pyplot as plt

#step 1: Generate random binary data

#change from 20 to 10000 to plot a smoother, theory alignegd NOISE_STD VS BER graph
num_bits = 10000
bits = np.random.randint(0, 2, num_bits)
print("Generated bits:", bits)

#step 2: Covert bits to digital signal

digital_signal = []
for bit in bits:
    if bit ==1:
        digital_signal.extend([1,1])
    else:
        digital_signal.extend([0,0])

#step 3: Plot the digital signal      
plt.figure(figsize=(10, 3))
plt.step(range(len(digital_signal)), digital_signal, where='post')
plt.ylim(-0.5, 1.5)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Digital Signal Representation')
plt.grid(True)
plt.savefig("plots/binary_signal.png", dpi=300, bbox_inches="tight")
plt.show()


# -------------------------------------------------------
# TRANSMITTER: BPSK(binary phase shift keying) MODULATION
# -------------------------------------------------------

# Convert binary bits to BPSK symbols
# Bit 1 -> +1
# Bit 0 -> -1

bpsk_signal = []

for bit in bits:
    if bit ==1:
        bpsk_signal.append(1)
    else:
        bpsk_signal.append(-1)

bpsk_signal = np.array(bpsk_signal)

#plot BPSK modulated signal

plt.figure(figsize=(10, 3))
plt.stem(bpsk_signal)
plt.xlabel('Symbol Index')
plt.ylabel('Amplitude')
plt.title('BPSK Modulated Signal')
plt.grid(True)
plt.savefig("plots/bpsk_modulated_signal.png", dpi=300, bbox_inches="tight")
plt.show()


# =====================================
# CHANNEL: ADDITIVE WHITE GAUSSIAN NOISE
# =====================================

noise_std = 1
#noise strength ^, change it to see diff in noise level
noise = np.random.normal(0,noise_std, size = len(bpsk_signal))
received_signal = bpsk_signal + noise


#plot Transmitted v/s Received signal
plt.figure(figsize=(10, 4))

# Plot original transmitted symbols
plt.stem(bpsk_signal, linefmt='b-', markerfmt='bo', basefmt='r-', label='Transmitted Signal')
# Plot noisy received signal
plt.stem(received_signal, linefmt='g--', markerfmt='go', basefmt='r-', label='Received Signal')

plt.xlabel('Symbol Index')
plt.ylabel('Amplitude')
plt.title('BPSK Signal Before and After Noise')
plt.legend()
plt.grid(True)
plt.savefig("plots/bpsk_signal_with_noise.png", dpi=300, bbox_inches="tight")
plt.show()


# ================================
# RECEIVER: BPSK DEMODULATION
# ================================

received_bits = []

for value in received_signal:
    if value > 0:
        received_bits.append(1)
    else:
        received_bits.append(0)

received_bits = np.array(received_bits)

print("received bits:", received_bits)



# ================================
# PERFORMANCE METRIC: BIT ERROR RATE (BER)
# ================================

bit_errors = np.sum(bits != received_bits)
total_bits = len(bits)

ber = bit_errors/total_bits

print("Number of bit errors:", bit_errors)
print("Bit Error Rate (BER):", ber)



# =====================================
# BER vs NOISE ANALYSIS
# =====================================

#USED WHEN num_bits = 20
'''
noise_std_values = np.linspace(0.1, 2.0, 10)
ber_values = []

for noise_std in noise_std_values:
    noise = np.random.normal(0, noise_std, size=len(bpsk_signal))
    received_signal = bpsk_signal + noise

    received_bits = []
    for value in received_signal:
        if value > 0:
            received_bits.append(1)
        else:
            received_bits.append(0)

    received_bits = np.array(received_bits)

    bit_errors = np.sum(bits != received_bits)
    ber = bit_errors / len(bits)

    ber_values.append(ber)    

    print(f"Noise STD = {noise_std:.2f}, BER = {ber:.3f}")

# Plot BER vs Noise Std Dev
plt.figure(figsize=(8,5))
plt.plot(noise_std_values, ber_values, marker='o')    
plt.xlabel('Noise Standard Deviation')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER vs Noise level for BPSK System')
plt.grid(True)
plt.show()
'''

#USED WHEN num_bits = 10000
noise_std_values = np.linspace(0.1, 2.0, 10)
ber_values = []

num_trials = 20  # Monte Carlo trials per noise level

for noise_std in noise_std_values:
    ber_sum = 0

    for _ in range(num_trials):
        noise = np.random.normal(0, noise_std, size=len(bpsk_signal))
        received_signal = bpsk_signal + noise

        received_bits = (received_signal > 0).astype(int)
        bit_errors = np.sum(bits != received_bits)

        ber_sum += bit_errors / len(bits)

    ber_avg = ber_sum / num_trials
    ber_values.append(ber_avg)

    print(f"Noise STD = {noise_std:.2f}, Avg BER = {ber_avg:.4f}")

# =====================================
# THEORETICAL BER FOR BPSK
# =====================================

from scipy.special import erfc

theoretical_ber = 0.5 * erfc(1 / (np.sqrt(2) * noise_std_values))

# Plot BER vs Noise Std Dev
plt.figure(figsize=(8,5))
plt.plot(noise_std_values, ber_values, 'o-', label='Simulated BER')
plt.plot(noise_std_values, theoretical_ber, 'r--', label='Theoretical BER')
plt.xlabel("Noise Standard Deviation")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs Noise for BPSK: Simulation vs Theory")
plt.legend()
plt.grid(True)
plt.savefig("plots/ber_vs_noise_bpsk.png", dpi=300, bbox_inches="tight")
plt.show()










