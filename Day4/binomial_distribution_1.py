import math

def binomial(X, N, P):
    return math.comb(N, X) * (P**X) * ((1 - P) ** (N - X))

if __name__ == '__main__':
    L, R = map(float, input().split())
    P = L / (L + R)
    
    probability = sum(binomial(i, 6, P) for i in range(3, 7))
    print(round(probability, 3))