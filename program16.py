# Write a Python program to find the value for sin(x) up to n terms using the
# series: sin(x)=1-x^3/3!+x^5/5!..... ( sin(x) = ((-1)^n/(2n+1)!)x^(2n+1) )

import math
def sin_series(x, n):
  sin_x = 0
  for i in range(n):
    term = (-1)**i * (x**(2*i+1)) / math.factorial(2*i+1) 
    sin_x += term
  return sin_x

x = math.pi / 4  
n = int(input("enter the value of n: "))  

sin_value = sin_series(x, n)
print(f"sin({x}) using {n} terms: {sin_value}")  