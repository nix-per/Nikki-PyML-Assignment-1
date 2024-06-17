# Q16. Write a program in python that counts the frequency of each character in a string

x=input("Enter a string: ")
d={}
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for i in d.keys():
    print("Frequency of",i,"is:",d[i])
