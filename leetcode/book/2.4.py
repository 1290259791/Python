def MaxSum(a, n):
    """
    最大连续子数组和
    currSum = max{0,currSum[j-1]} + a[j]
    :param a:
    :param n:
    :return:
    """
    currSum = 0
    maxSum = 0
    for i in range(n):
        if currSum >= 0:
            currSum += a[i]
        else:
            currSum = a[i]
        if currSum > maxSum:
            maxSum = currSum
    return maxSum


List = [1, -2, 3, 10, -4, 7, 2, -5]
print(MaxSum(List, len(List)))
