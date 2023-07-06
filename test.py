import numpy as np
import matplotlib.pyplot as plt

filename = "ue2.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

# Delete the last 5 lines
updated_lines = lines[:-5]

with open(filename, 'w') as file:
    file.writelines(updated_lines)


# Read the data from the text file using NumPy
data = np.genfromtxt(filename, skip_header=6, usecols=(4, 5, 6))






# Extract the columns into separate variables
transfer = data[:, 0]
bandwidth = data[:, 2]

for i in range(len(transfer)):
    if transfer[i] > 100:
        transfer[i] /= 1024

#print(bandwidth)
#print(transfer)



# Plot the data
plt.plot( transfer, label='Transfer')
plt.plot( bandwidth, label='Bandwidth')
plt.ylim(0, 80)
plt.xlabel('Time (sec)')
plt.ylabel('Data')
plt.legend()
plt.show()
