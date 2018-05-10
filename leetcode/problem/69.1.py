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
        left = 0
        right = x //2 + 1
        while left <= right:
            mid = (left+right) // 2
            if mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
            else:
                return mid
        return right

solution = Solution()
print(solution.mySqrt(300000))