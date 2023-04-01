'''
This function is going to merge two sorted list
into one sorted list. 
'''

def merge(list1, list2):
    combined = []
    
    i = 0
    j = 0
    
    '''
    This loop will run when both the lists have elements
    to put in the combined list'''
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
        
    ''' 
    This loop will run when list2 does not 
    have any element to put in the combined list
    '''
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    '''
    This loop will run when list1 is done entering
    elements in combined list
    '''    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined

if __name__ == "__main__":
    # Please enter two sorted lists
    print("Please enter two sorted lists to merge")
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    
    print("The merged list is: ", end= " => ")
    print(merge(list1, list2))
    