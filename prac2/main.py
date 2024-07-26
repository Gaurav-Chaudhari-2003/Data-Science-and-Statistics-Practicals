# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Variable Creation and Data Types
x = 10
y = 3.14
name = "Alice"
is_student = True

# Logical Operators
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

# Sequence Data Types and Operations
# String
greeting = "Hello, World!"
print(greeting[0])  # Indexing
print(greeting[7:12])  # Slicing

# List
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
print(numbers[2:5])

# Tuple
coordinates = (10, 20)
print(coordinates[0])

# Dictionary
person = {'name': 'Alice', 'age': 25}
print(person['name'])

# Set
unique_numbers = {1, 2, 3, 3, 4, 5}
print(unique_numbers)

# Range
for i in range(5):
    print(i)

# Loops and Conditional Statements
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Basic Linear Regression
# Create a simple dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5],
    'Scores': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Prepare the data
X = df[['Hours_Studied']].values
y = df['Scores'].values

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.title('Linear Regression')
plt.show()
