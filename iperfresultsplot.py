import numpy as np
import matplotlib.pyplot as plt

# Read the data from the text file using NumPy
data = np.genfromtxt('result.txt', skip_header=6, usecols=(4, 5, 6))

# Extract the columns into separate variables
transfer = data[:, 0]
bandwidth = data[:, 2]



print(bandwidth)
print(transfer)



# Plot the data
plt.plot( transfer, label='Transfer')
plt.plot( bandwidth, label='Bandwidth')
plt.xlabel('Time (sec)')
plt.ylabel('Data')
plt.legend()
plt.show()
