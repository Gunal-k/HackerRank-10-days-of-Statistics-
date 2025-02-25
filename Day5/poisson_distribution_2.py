def poisson(lmbda):
    return 40 *(lmbda + lmbda ** 2)
    
lmbda1, lmbda2 = map(float,input().split())
c1 = 160 + poisson(lmbda1)
c2 = 128 + poisson(lmbda2)

print(round(c1,3))
print(round(c2,3))