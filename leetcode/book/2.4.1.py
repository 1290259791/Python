def MaxSum(a, n):
    """
    最大连续子数组,同时输出数组开始和结束位置
    currSum = max{0,currSum[j-1]} + a[j]
    :param a:
    :param n:
    :return:
    """
    currSum = 0
    maxSum = 0
    begin = 0   # 最大数组开始位置
    end = 0     #最大数组结束位置
    for i in range(n):
        if currSum >= 0:
            currSum += a[i]
        else:
            begin = i
            currSum = a[i]
        if currSum > maxSum:
            end = i
            maxSum = currSum
    return maxSum, begin, end


List = [1, -2, 3, 10, -4, 7, 2, -5]
print(MaxSum(List, len(List)))
