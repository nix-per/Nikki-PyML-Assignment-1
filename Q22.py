# Q22. Write a python program that returns the minimum and maximum values in a list of numbers

x=input("Enter list elements separated by spaces: ").split()
mi=int(x[0])
ma=int(x[0])
for i in range (1,len(x)):
    mi=min(mi,int(x[i]))
    ma=max(ma,int(x[i]))

print("Minimum value in the list is:",mi)
print("Maximum value in the list is:",ma)
