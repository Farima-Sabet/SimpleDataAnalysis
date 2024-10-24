# Import necessary libraries
import pandas as pd

# Load the dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [23, 35, 45, 25, 35],
    'Salary': [60000, 80000, 90000, 75000, 68000]
}

df = pd.DataFrame(data)

# Print the dataset
print("Dataset:")
print(df)

# Calculate and print basic statistics
print("\nStatistics:")
print("Mean Age:", df['Age'].mean())
print("Median Salary:", df['Salary'].median())
print("Age Range:", df['Age'].max() - df['Age'].min())
