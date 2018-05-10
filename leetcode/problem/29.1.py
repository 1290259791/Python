class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        marker = (dividend > 0) == (divisor > 0)    # 符号判断调价
        dividend, divisor = abs(dividend), abs(divisor)     # 取两个数的绝对值
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp    # 减去除数的倍数2,4,8,16,如果减去的过大,就从第一个while 继续开始从1,2,4减
                ret += i
                i <<= 1     # 左移动放大两倍
                temp <<= 1
        if not marker:
            ret = -ret
        return max(min(ret, 2 ** 31 - 1), -2 ** 31)
