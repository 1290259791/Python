def Sort(arr):
    """
    冒泡排序
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [4, 2, 1, 7, 5, 3, 9, 6, 7]
arr = Sort(arr)
print(arr)
