a,b = map(int,input().split())
k = int(input())
p = a/b

def geometric(p, k):
    return ((1-p)**(k-1))* p
    
print(round(geometric(p,k),3))