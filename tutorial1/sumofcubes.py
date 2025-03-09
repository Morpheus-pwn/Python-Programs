l=[]
n=int(input("enter positive limit:"))
for i in range(1,n+1):
    l.append(i)
print("elements of the list are:",l)

sum=0
for i in l:
    sum=sum+i**3

print("the sum of the cubes of the numbers is:",sum)