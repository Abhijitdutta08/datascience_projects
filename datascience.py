import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 8, 6, 4, 2])

# Plot the data
plt.plot(x, y)

# Display the plot
plt.show()
# Fit a polynomial curve of degree 1 (linear regression) to the data
coefficients = np.polyfit(x, y, 1)
# Print the coefficients
print('Coefficients:', coefficients)
# Create a function to calculate the predicted y-values for any given x-value
predict = np.poly1d(coefficients)

# Print the equation of the line
print('Equation:', predict)