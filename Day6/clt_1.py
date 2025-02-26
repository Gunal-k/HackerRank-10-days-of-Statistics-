import math

def normal_cdf(x, mean, sd):
    return 0.5 * (1 + math.erf((x - mean) / (sd * math.sqrt(2))))

x_bar = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_total = n * mu
sigma_x = (n ** 0.5) * sigma

prob = normal_cdf(x_bar,mu_total, sigma_x)
print(f"{prob:.4f}")