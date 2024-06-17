# Q23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input

print("Enter 1 for conversion from Celsius to Fahrenheit")
print("Enter 2 for conversion from Fahrenheit to Celsius")
c=int(input("Enter your choice: "))
if(c==1):
    x=int(input("Enter temparature in Celcius: "))
    y= (x*9/5) +32
    print("Temperature in Fahrenheit is:", y)
elif(c==2):
    x=int(input("Enter temparature in Fahrenheit: "))
    y= (x-32)*5/9
    print("Temperature in Celsius is:", y)
else:
    print("Invalid choice")
