List = []


def SumNumber(sum, n):
    """
    解法1:n 问题转换为 n-1问题
    :param sum:
    :param n:
    :return:
    """
    if n <= 0 or sum <= 0:
        return
    if sum == n:
        List.reverse()
        for i in List:
            print(i, end=' ')
        print("+",n)
        List.reverse()
    List.append(n)
    SumNumber(sum-n, n-1)
    List.pop()
    SumNumber(sum, n-1)


SumNumber(8, 7)