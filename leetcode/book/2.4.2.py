def MaxSum(array, n):
    """
    连续子数组的最大乘积
    动态规划    Max=Max{a[i],Max[i-1]*a[i],Min[i-1]*a[i]}Min=Min
    创建一维数组
    :param array:
    :param n:
    :return:
    """
    maxA = [0 for i in range(n)]
    minA = [0 for i in range(n)]
    maxA[0] = array[0]
    minA[0] = array[0]
    value = maxA[0]
    for i in range(1, n):
        maxA[i] = max(array[i], maxA[i - 1] * array[i], minA[i - 1] * array[i])
        minA[i] = min(array[i], maxA[i - 1] * array[i], minA[i - 1] * array[i])
        value = max(value, maxA[i])
    print(value)


List = [-2, -3, 8, -5, -2]
MaxSum(List, len(List))
