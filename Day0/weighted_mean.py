def weightedMean(X, W):
    sum_val1 = sum([ W[i] * X[i] for i in range(len(W))])
    sum_val2 = sum(W)
    
    print(round(sum_val1/sum_val2,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
