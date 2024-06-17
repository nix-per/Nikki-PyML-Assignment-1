# Q21. Write a python program that counts the occurrences of a specific element in a list

x=input("Enter list elements separated by spaces: ").split()
y=input("Enter the element whose occurance is to be found: ")
o=0
for i in x:
    if(i==y):
        o+=1
print(y, "occurs in the list", o, "times")
