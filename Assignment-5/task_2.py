# Task 2: Demonstrate List Slicing 
numbers = [x for x in range(1, 11)]
half = numbers[:len(numbers) // 2]
reverse = half[::-1]
print("Original list: ", numbers)
print("Extracted first five elements: ", half)
print("Reversed extracted elements: ", reverse)