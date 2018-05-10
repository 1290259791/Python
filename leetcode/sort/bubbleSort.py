def Sort(Str):
    """
    冒泡排序算法
    时间复杂度 最好O(n),最坏 O(n^2)
    ^来进行交换
    :param Str:
    :return:
    """
    for i in range(len(Str) - 1):  # 第一轮循环
        no_sort = True  # 定义变量,判断第二轮循环是否有交换
        j = i + 1
        while j < len(Str):  # 第二轮循环,比较
            if Str[j] < Str[i]:
                Str[j] = Str[j] ^ Str[i]
                Str[i] = Str[j] ^ Str[i]
                Str[j] = Str[j] ^ Str[i]
                no_sort = False
            j += 1
        if no_sort:  # 第二轮循环没有交换,直接结束
            break
    return Str


s = [9, 8, 2, 4, 2, 6, 8]
s = Sort(s)
print(s)
