class Solution:
    def reverse(self, x):
        """
        56ms 操作
        :type x: int
        :rtype: int
        """
        flag = 0
        if x > 0:
            flag = 1
        else:
            flag = -1
        s = str(abs(x))[::-1]
        n = int(s) * flag
        return n if n.bit_length() < 32 else 0

