from math import comb

def binomial(X, N, P):
    return comb(N, X) * (P ** X) * ((1 - P) ** (N - X))

if __name__ == '__main__':
    reject, batch = map(int, input().split())
    prob = reject/100
    k=2

    prob_no_more_than_k = sum(binomial(x, batch, prob) for x in range(k+1))
    prob_at_least_k = 1 - sum(binomial(x, batch, prob) for x in range(k))

    print(f"{prob_no_more_than_k:.3f}")
    print(f"{prob_at_least_k:.3f}")