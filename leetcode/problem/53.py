class Solution:
    def maxSubArray(self, nums):
        """
        题目:最大子序列和
        解法:贪心算法
        思路:
        先求结果,与 Max 比较,比较之后若结果小于0,则从新累加
        将子串和为负数的子串丢掉，只留和为正的子串。
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return sum(nums)
        n = len(nums)
        Max = -2**31
        result = 0
        for i in range(n):
            result += nums[i]
            if result >= Max:
                Max = result
            if result < 0:
                result = 0
        return Max

solution = Solution()
print(solution.maxSubArray([-1,-2,-3]))