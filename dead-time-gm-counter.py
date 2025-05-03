import numpy as np
import matplotlib.pyplot as plt

# Counts for multiple events
C1 = np.array([138840, 139365, 45448, 145027])
C2 = np.array([111808, 110945, 37591, 113844])
C12 = np.array([240785, 241604, 80196, 253974])
CB = np.array([625, 615, 191, 1162])
T = np.array([1800, 1800, 600, 3600])  # Time in seconds

# Count rates
M1 = C1 / T
M2 = C2 / T
M12 = C12 / T
MB = CB / T

# Relaxation time calculation
numerator = M1 + M2 - MB - M12
denominator = 2 * (M1 * M2 - MB * M12)
tau = numerator / denominator  # in seconds

# Error in count rates (Poisson)
sigma_M1 = np.sqrt(C1) / T
sigma_M2 = np.sqrt(C2) / T
sigma_M12 = np.sqrt(C12) / T
sigma_MB = np.sqrt(CB) / T

# Partial derivatives of tau
d_tau_M1 = (denominator - numerator * (2 * M2)) / (denominator ** 2)
d_tau_M2 = (denominator - numerator * (2 * M1)) / (denominator ** 2)
d_tau_MB = (-denominator + numerator * (2 * M12)) / (denominator ** 2)
d_tau_M12 = (-denominator + numerator * (2 * MB)) / (denominator ** 2)

# Error propagation
sigma_tau_squared = (
    (d_tau_M1 * sigma_M1) ** 2 +
    (d_tau_M2 * sigma_M2) ** 2 +
    (d_tau_MB * sigma_MB) ** 2 +
    (d_tau_M12 * sigma_M12) ** 2
)
sigma_tau = np.sqrt(sigma_tau_squared)  # in seconds

# Convert to microseconds for plotting normalized PDFs
tau_us = tau * 1e6
sigma_us = sigma_tau * 1e6

# Weighted average calculation (using seconds)
weights = 1 / (sigma_tau ** 2)
tau_weighted = np.sum(weights * tau) / np.sum(weights)
tau_weighted_us = tau_weighted * 1e6

# Define x-axis in microseconds domain with ±4σ range
x_min = np.min(tau_us - 4 * sigma_us)
x_max = np.max(tau_us + 4 * sigma_us)
x = np.linspace(x_min, x_max, 1000)

# Plot individual normalized Gaussian PDFs
plt.figure()
for i in range(len(tau_us)):
    y = (1 / (sigma_us[i] * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - tau_us[i]) / sigma_us[i]) ** 2)
    plt.plot(x, y, label=f'Event {i+1}')

# Plot weighted average as vertical line
plt.axvline(tau_weighted_us, linestyle='--', label=f'Weighted Avg = {tau_weighted_us:.2f} µs')

# Labels and legend
plt.xlabel('Relaxation Time τ (µs)')
plt.ylabel('Probability Density (normalized)')
plt.title('Normalized Gaussian Fits for Each Event with Weighted Average')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
