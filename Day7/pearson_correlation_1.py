import math
def pearson_correlation(n,X, Y):
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n

    num = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
    den_X = math.sqrt(sum((X[i] - mean_X) ** 2 for i in range(n)))
    den_Y = math.sqrt(sum((Y[i] - mean_Y) ** 2 for i in range(n)))

    return num / (den_X * den_Y)

n = int(input())
mean_X = list(map(float,input().split()))
mean_Y = list(map(float,input().split()))

print(round(pearson_correlation(n,mean_X,mean_Y),3))