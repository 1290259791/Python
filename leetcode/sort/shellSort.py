def shellSort(arr):
    """
    希尔排序
    插入排序的改进版本
    先将排序序列分成若干子序列,将每个子序列用插入排序进行排序,
    子序列中的记录"基本有序"时,对所有子序列进行一次插入排序
    :param arr:
    :return:
    """
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = gap // 3
    print(arr)
    return arr


arr = [3, 2, 4, 6, 1]
shellSort(arr)
