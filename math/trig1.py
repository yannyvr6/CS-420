import numpy as np
import matplotlib.pyplot as plt

# Define the function: y = -7 * sin(8x - π/4) - 6
def f(x):
    return -7 * np.sin(8 * x - np.pi / 4) - 6

# Create x values to cover a few periods
x = np.linspace(0, np.pi, 1000)
y = f(x)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r"$y = -7\sin(8x - \frac{\pi}{4}) - 6$", color='purple')

# Add a horizontal line at y = -6 to show vertical shift
plt.axhline(y=-6, color='gray', linestyle='--', label='Vertical shift: $-6$')

# Formatting
plt.title("Graph of $y = -7\sin(8x - \frac{\pi}{4}) - 6$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.ylim(-14, 2)

plt.show()
