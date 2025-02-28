def LSRL(X,Y):
    n = 5
    mean_X = sum(X)/n
    mean_Y = sum(Y)/n
    
    numerator = sum((X[i] - mean_X)*(Y[i]-mean_Y) for i in range(n))
    denominator = sum((X[i] - mean_X)** 2 for i in range(n))
    
    b = numerator/denominator
    a = mean_Y- b* mean_X
    
    return a,b

X,Y=[],[]
for _ in range(5):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

a, b =LSRL(X,Y)

x_pred = 80
y_pred = a + b*x_pred

print(round(y_pred,3))