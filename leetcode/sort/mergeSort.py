"""
归并排序
"""


def merge(left, right):
    """
    将左右两个列表进行比较添加
    :param left:
    :param right:
    :return:
    """
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
    else:
        result.extend(right)
    print(result)
    return result


def mergeSort(arr):
    """
    将列表分成最小的每个为1
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


lst = [111, 333, 555, 666, 77, 777, 1, 11, 4, 6, 7, 9]
print(mergeSort(lst))
