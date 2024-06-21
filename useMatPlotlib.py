#!/usr/bin/env python3
import matplotlib.pyplot as plt

# Create a list of numbers from 0 to 10
x = list(range(11))

# Create a list of squares of the numbers from 0 to 10
y = [i**2 for i in x]

# Plot x and y
plt.plot(x, y)
# print(graph)
