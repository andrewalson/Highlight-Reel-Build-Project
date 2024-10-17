import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('provided_data.csv')
                 
# Display the first 5 rows
print(df.head())

# Display basic information about the dataset
print(df.info())

# Calculate and print summary statistics
print(df.describe())

# Plotting
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
plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], alpha=0.5)
plt.xlabel('Frame Number')
plt.ylabel('Value')
plt.title('Second Column vs Frame Number (Scatter Plot)')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

plt.figure(figsize=(12, 6))
df.iloc[:, 1:5].boxplot()
plt.xlabel('Columns')
plt.ylabel('Values')
plt.title('Box Plot of Columns 2-5')
plt.grid(True)
plt.savefig('boxplot.png')
plt.show()