# Task 1: Read a file and Handle Errors
import os

FILE_PATH="files/sample.txt"
try:
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):
        print(f'Line {i} :', line, end='')

except Exception as ep:
    print(f"Error: The file '{FILE_PATH}' was not found.")