# Q20. Write a python program that takes a list of numbers and returns their sum

x=input("Enter numbers separated by spaces: ").split()
sum=0
for i in x:
    sum+=int(i)
print("Sum of elements in the list is:",sum)
