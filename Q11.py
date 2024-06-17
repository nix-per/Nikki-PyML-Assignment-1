# Q11. Write a python program that generates the first n numbers in the Fibonacci sequence

x=int(input("Enter number of elements in the sequence: "))
a=0
b=1
for i in range(x):
    print(a)
    s=a+b
    a=b
    b=s
