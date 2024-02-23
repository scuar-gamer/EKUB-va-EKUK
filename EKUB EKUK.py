from math import gcd
#EKUK ni topish uchun

a,b=map(int,input().split())
print(a*b//gcd(a,b))

#EKUB ni topish uchun

print(gcd(a,b))
