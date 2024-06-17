# Q19. Write a python program that removes all punctuation from a given string

import string
x=input("Enter a string: ")
y=""
for i in x:
    if i not in string.punctuation:
        y+=i

print("Given string without punctuation is:",y)
