import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('provided_data.csv')
                 
# Display the first 5 rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Calculate and print summary statistics
print(df.describe())

# Calculate the derivative of the first column
derivative = np.diff(df.iloc[:, 1])

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Plot original data
ax1.plot(df.iloc[:, 0], df.iloc[:, 1])
ax1.set_ylabel('Value')
ax1.set_title('Second Column vs Frame Number')
ax1.grid(True)

# Plot derivative
ax2.plot(df.iloc[1:, 0], derivative)
ax2.set_xlabel('Frame Number')
ax2.set_ylabel('Derivative')
ax2.set_title('Derivative of Second Column vs Frame Number')
ax2.grid(True)

plt.tight_layout()
plt.savefig('plot.png')
plt.show()

# Assignment 1
# Plotting second column vs frame number
'''
plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:, 0], df.iloc[:, 1])
plt.xlabel('Frame Number')
plt.ylabel('Value')
plt.title('Second Columns vs Frame Number')
plt.savefig('plot.png')
plt.show()
'''

# Create a scatter plot
'''
plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], alpha=0.5)
plt.xlabel('Frame Number')
plt.ylabel('Value')
plt.title('Second Column vs Frame Number (Scatter Plot)')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()
'''

# Create a box plot
'''
plt.figure(figsize=(12, 6))
df.iloc[:, 1:5].boxplot()
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title('Box Plot of Columns 2-5')
plt.grid(True)
plt.savefig('boxplot.png')
plt.show()
'''