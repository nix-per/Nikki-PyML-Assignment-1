# Q26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix

x=input("Enter a string: ")
pre=input("Enter the prefix to be checked for: ")
su=input("Enter the suffix to be checked for: ")

if(x.startswith(pre)):
    print(pre,"is the prefix of",x)
else:
    print(pre,"is not the prefix of",x)

if(x.endswith(su)):
    print(su,"is the suffix of",x)
else:
    print(su,"is not the suffix of",x)
