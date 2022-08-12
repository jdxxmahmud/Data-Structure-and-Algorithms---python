def binarySearch(arr, key):

    lo, hi = 0, len(arr) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            lo = mid
        elif key < arr[mid]:
            hi = mid

    return -1


myList = [32, 4, 15, 6, 1, 7, 2, 0]

# The array must be sorted for a binary search
myList.sort()
print(binarySearch(myList, 6))
