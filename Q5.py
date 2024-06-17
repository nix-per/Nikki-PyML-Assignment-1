# Q5. Write a program that takes a string input from the user and writes it to a text file

x=input("Enter a string: ")
f=open("String.txt","w")
f.write(x)
f.close()
print("String written to file 'String.txt' Successfully")
