import math

n = int(input())
mu = float(input())  
sigma = float(input())  
C = float(input())  
Z = float(input())  

SE = sigma / math.sqrt(n)

lower_bound = mu - Z * SE 
upper_bound = mu + Z * SE

print(f"{lower_bound:.2f}")
print(f"{upper_bound:.2f}")