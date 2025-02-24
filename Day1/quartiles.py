 #!/bin/python3
import os

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr.sort()
    n = len(arr)
    
    Q2 = median(arr)
    
    lower = arr[:n//2]
    Q1 = median(lower)
    
    if n%2!=0:
        val = n//2 +1
    else:
        val = n//2
    
    upper = arr[val:]
    Q3 = median(upper)
    
    return [Q1,Q2,Q3]
    
    
def median(arr):
    n = len(arr)
    mid = n//2
    return arr[mid] if n%2!=0 else (arr[mid-1]+arr[mid])//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
