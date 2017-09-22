def find_missing_number(arr, n):
    a = arr
    a.sort()
    for i in range(0, n-1):
        if a[i] != i + 1:
            return i + 1

print (find_missing_number([1, 2, 3, 5, 4, 7], 7))
