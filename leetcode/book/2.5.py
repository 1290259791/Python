def fun(n):
    """
    跳台阶,n 阶,一次只能跳1或2,总共有几种
    递归方法
    :param n:
    :return:
    """
    result = [0, 1, 2]
    if n <= 2:
        return result[n]
    return fun(n - 1) + fun(n - 2)


def fun1(n):
    """
    递推方法
    递归方法有许多计算重复,可以从后往前推用递推方法
    :param n:
    :return:
    """
    result = [1, 1, 2]
    if n < 2:
        return result[n]
    for i in range(2, n + 1):
        result[2] = result[0] + result[1]
        result[0] = result[1]
        result[1] = result[2]
    return result[2]


print(fun1(5))
