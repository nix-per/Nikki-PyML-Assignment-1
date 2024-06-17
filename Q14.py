# Q14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines

l1=[]
while (1):
    x=input("Enter a line of input: ")           # Adding lines in the list
    if(x==""):
        break
    else:
        l1.append(x)
        
for i in range(len(l1)):                         # Printing the lines
    print(l1[i])
