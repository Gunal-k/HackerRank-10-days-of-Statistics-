from math import e, factorial

def poisson_distribution(lmbda,k):
    return ((e ** (-lmbda))* (lmbda ** k))/factorial(k)
    
lmbda = float(input())
k = int(input())
print(round(poisson_distribution(lmbda,k),3))