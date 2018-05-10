def insertionSort(arr):
    """
    插入排序
    第二层循环在找到插入位置后可提前终止
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        p = i - 1
        current = arr[i]
        while p >= 0 and arr[p] > current:
            arr[p + 1] = arr[p]
            p -= 1
        arr[p + 1] = current
    print(arr)
    return arr


arr = [3, 2, 4, 6, 1]
insertionSort(arr)
