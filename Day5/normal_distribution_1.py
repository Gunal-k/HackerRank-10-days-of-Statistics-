import math

def normal_cdf(x, mean, sd):
    return 0.5 * (1 + math.erf((x - mean) / (sd * math.sqrt(2))))

mean, sd = map(float, input().split())
a = float(input())
b, c = map(float, input().split())

prob_less_than_a = normal_cdf(a, mean, sd)
prob_between_b_c = normal_cdf(c, mean, sd) - normal_cdf(b, mean, sd)

print(round(prob_less_than_a, 3))
print(round(prob_between_b_c, 3))