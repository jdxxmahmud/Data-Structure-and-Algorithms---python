'''
This function finds the index from which
all the elements of the array will be greater than 
or equal to target.
'''
def idxGreaterThanOrEqual(target, arr):
    lo, hi = 0, len(arr) - 1
    
    ans = -1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if arr[mid] < target:
            lo = mid + 1
        else:
            ans = mid
            hi = mid - 1
            
    return ans

if __name__ == "__main__":
    arr = [1, 5, 7, 9, 12, 17, 18, 21, 23]
    target = 10
    
    idx = idxGreaterThanOrEqual(target, arr)
    print(f'Index to find elements >= target is: {idx}')
    print(f'{target} < {arr[idx:]}')