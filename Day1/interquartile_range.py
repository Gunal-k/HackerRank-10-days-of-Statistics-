def interQuartile(values, freqs):
    dataset = []
    for i in range(len(values)):
        dataset.extend([values[i]] * freqs[i])

    dataset.sort()
    n = len(dataset)

    mid = n // 2
    if n % 2 == 0:
        lower_half = dataset[:mid]
        upper_half = dataset[mid:]
    else:
        lower_half = dataset[:mid]
        upper_half = dataset[mid + 1:]

    Q1 = median(lower_half)
    Q3 = median(upper_half)

    IQR = Q3 - Q1
    print(f"{IQR:.1f}")

def median(arr):
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

if __name__ == '__main__':
    n = int(input().strip()) 
    values = list(map(int, input().split()))  
    freqs = list(map(int, input().split()))  
    interQuartile(values, freqs)
