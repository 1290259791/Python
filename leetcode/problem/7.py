class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        symbol = None
        if x == 0:
            return 0
        if x < 0:
            symbol = "-"
        x = abs(x)
        l = list(str(x))
        l.reverse()
        while l[0] == '0':
            l.pop(0)
        a = "".join(l)
        a = int(a)
        if a < -(2 ** 31) or a > (2 ** 31 - 1):
            return 0
        if symbol is None:
            return a
        else:
            return -a


solution = Solution()
print(solution.reverse(1534236469))