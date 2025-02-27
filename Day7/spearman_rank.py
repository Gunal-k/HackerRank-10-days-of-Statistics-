def rank(data):
    sorted_data = sorted((x, i) for i, x in enumerate(data))
    ranks = [0] * len(data)
    for rank, (_, i) in enumerate(sorted_data, start=1):
        ranks[i] = rank
    return ranks

def spearman_rank_correlation(X, Y):
    n = len(X)
    rank_X = rank(X)
    rank_Y = rank(Y)
    d_squared = [(rank_X[i] - rank_Y[i]) ** 2 for i in range(n)]
    
    rho = 1 - (6 * sum(d_squared)) / (n * (n**2 - 1))
    return rho

_ = int(input())
X = list(map(float,input().split()))
Y = list(map(float,input().split()))

print(round(spearman_rank_correlation(X,Y),3))