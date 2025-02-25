import math

def normal_cdf(x, mean, sd):
    return 0.5 * (1 + math.erf((x - mean) / (sd * math.sqrt(2))))

mean, sd = map(int, input().split())
a = int(input())
b = int(input())

prob1 = 1 - normal_cdf(a, mean, sd)
prob2 = 1 - normal_cdf(b, mean, sd)
prob3 = normal_cdf(b,mean,sd)

print(round(prob1*100, 2))
print(round(prob2*100, 2))
print(round(prob3*100, 2))