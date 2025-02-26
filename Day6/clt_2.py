import math
def normal_cdf(x, mean, sd):
    return 0.5 * (1 + math.erf((x - mean) / (sd * math.sqrt(2))))
    
X = int(input())  
N = int(input())  
M = float(input())  
S = float(input())  

mu_total = N * M
sigma_total = math.sqrt(N) * S

probability = normal_cdf(X, mu_total, sigma_total)
print(round(probability,4))