n=int(input("enter a number:"))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
print("reverse of the number is:",rev)