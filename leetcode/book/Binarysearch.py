def binary_search(find, List):
    """
    二分查找元素
    时间复杂度O(log(n)),最坏的情况 O(n)
    :param find:
    :param List:
    :return:
    """
    low = 0
    high = len(List) - 1    #防止下标越界
    while low <= high:
        mid = (low + high) // 2
        if List[mid] == find:
            return mid
        # 左半边
        elif List[mid] > find:
            high = mid - 1
        # 右半边
        else:
            low = mid + 1
    # 未查找到
    return -1


List = [1, 2, 3, 4, 4, 7, 5, 8]
List.sort()

print("原序列为:", List)
try:
    find = int(input('输入查找的数:'))
except:
    print('请输入整数!')
    exit()

result = binary_search(find, List)
if result != -1:
    print("查找的元素%d序号为%d" % (find, result))
else:
    print("未找到")
