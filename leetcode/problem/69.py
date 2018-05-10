class Solution:
    def mySqrt(self, x):
        """
        二分查找法
        求开根号之后的数
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        y = x//2
        while y:
            if y**2 < x:
                break
            else:
                y = int(y//2)
        for i in range(y, x+1):
            if i*i > x:
                return i-1
            elif i*i == x:
                return i



solution = Solution()
print(solution.mySqrt(1))