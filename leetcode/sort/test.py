def mergeSort(arr):
    if(len(arr)<2):
        return arr
    middle = int(len(arr)/2)
    left,right = arr[:middle],arr[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0]<=right[0]:
        #为了不用具体的索引，我们直接把它pop出来
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))
    return result
lst = [111,333,555,666,77,777,1,11,4,6,7,9]
print(mergeSort(lst))