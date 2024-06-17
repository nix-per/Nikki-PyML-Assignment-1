# Q18. Write a python program that checks if two strings are anagrams of each other

x=input("Enter first string: ")
y=input("Enter second string: ")

l1=list(x)
l2=list(y)
l1.sort()
l2.sort()

if(l1==l2):
    print(x,"and",y,"are anagrams of each other")
else:
    print(x,"and",y,"are not the anagrams of each other")
