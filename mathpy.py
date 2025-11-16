import numpy as np
import matplotlib.pyplot as plt

# Define theta values
theta = np.linspace(0, 2*np.pi, 1000)

# Define r based on the given equation
r = 3 * np.cos(5 * theta)

# Plot the polar graph
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Plot the curve
ax.plot(theta, r, label=r'$r = 3 \cos(5\theta)$')

# Mark the specific points
points_theta = [0, np.pi/10, 2*np.pi/10, 3*np.pi/10, 4*np.pi/10, 5*np.pi/10]
points_r = [3 * np.cos(5 * t) for t in points_theta]
ax.scatter(points_theta, points_r, color='red', label='Points')

# Add labels and title
ax.set_title(r'Polar plot of $r = 3 \cos(5\theta)$')
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$r$')

# Display the legend
ax.legend()

# Show the plot
plt.show()
