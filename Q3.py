# Q3. Write a python program that calculates the factorial of a given number

x=int(input("Enter the number: "))
fac=1
if(x==0 or x==1):
    print("Factorial of", x, "is:", fac)
elif(x<0):
    print("Factorial of a negative number does not exist")
else:
    for i in range (1,x+1):
        fac*=i
    print("Factorial of", x, "is:", fac)
