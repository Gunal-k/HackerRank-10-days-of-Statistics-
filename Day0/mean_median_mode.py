from collections import Counter

n = int(input())
val = list(map(int,input().split()))
val.sort()
mean = round(sum(val)/n,1)

count_val = Counter(val)
mode = max(count_val,key=count_val.get)
ind = round(n/2)
median = round((val[ind-1]+val[ind])/2,1)

print(mean)
print(median)
print(mode)