#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
print("How many terms of the fibonacci sequence do you want?")
num = input()
if(num <= 0 ):
   print("please enter a positive number)
else:
   a, b = 0, 1
   print("Fibonacci Sequence: ")
   for _ in range(num): 
       print(a, end=" ")
       a, b = b, a + b
       print()
       
   
