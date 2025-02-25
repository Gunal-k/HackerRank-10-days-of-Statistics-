import math

# The function accepts INTEGER_ARRAY arr as parameter.

def stdDev(arr):
    n = len(arr)
    sum_val = sum(arr)/n
    total = math.sqrt(sum([(arr[i]-sum_val)**2 for i in range(n)])/n)
    print(round(total,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
