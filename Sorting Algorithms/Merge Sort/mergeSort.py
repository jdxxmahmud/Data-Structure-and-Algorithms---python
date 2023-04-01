from merge import merge

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    
    left = nums[:mid]
    right = nums[mid:]
    
    return merge(merge_sort(left), merge_sort(right))

if __name__ == "__main__":
    
    myList = [0, 92, 18, 4, 6, 1, 25, -1]
    print(f'The unsorted list is: {myList}')
    print("The sorted list is: => ", end= " ")
    print(merge_sort(myList))