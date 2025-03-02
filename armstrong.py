n=int(input("enter the number:"))
num=n
rev=0

while(n>0):
    d=n%10
    rev=rev+d*d*d
    n=n//10

if(rev==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
