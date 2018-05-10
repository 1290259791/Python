def selectSort(arr):
    """
    选择排序
    A:先从未排序中找到最值元素放入到起始位置
    B:从未排序中继续寻找最值元素放到已排序末尾
    C: 重复 A B 操作
    :param arr:
    :return:
    """
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


arr = [4, 2, 1, 7, 5, 3, 9, 6, 7]
selectSort(arr)