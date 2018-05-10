def quickSort(a, start, end):
    """
    快速排序
    https://blog.csdn.net/ljr257816/article/details/52374022
    :param a:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return
    i, j = start, end
    tmp = a[start]
    while True:
        while i < j and a[j] >= tmp:
            j -= 1
        if i < j:
            a[i] = a[j]
            i += 1
        while i < j and a[i] < tmp:
            i += 1
        if i < j:
            a[j] = a[i]
            j -= 1
        else:
            break
    a[i] = tmp
    quickSort(a, start, i-1)
    quickSort(a, i+1, end)


def quickrank(a):
    quickSort(a, 0, len(a)-1)
    return a


a = [1,3,6,4,3,2]
print(quickrank(a))