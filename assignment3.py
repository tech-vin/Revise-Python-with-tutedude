# Task 1: write a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("***Factorial***")
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

# Using the math module for calculations
import math

print("***Calculations using Math Module***")
num = int(input("Enter a number: "))
print("Square root: ", math.sqrt(num))
print("Logarithm: ", math.log(num))
print("Sine: ", math.sin(num))

