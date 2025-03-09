l=[]
sum=0
n=int(input("enter the limit:"))
for i in range(1,n+1):
    a=int(input("enter positive numbers:"))
    if a%2==0:
        l.append(a)
print("elements of the list are:",l)

for i in l:
    sum=sum+i

print("the sum of the even numbers is:",sum)