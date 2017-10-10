def subsum(arr, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += arr[i]
    return sum