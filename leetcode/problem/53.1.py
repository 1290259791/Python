class Solution:
    def maxSubArray(self, nums):
        """
        题目:最大子序列和
        解法2:贪心算法
        思路:
        result = max(相加的和,下一个数)
        Max = max(Max,result)
        :type nums: List[int]
        :rtype: int
        """
        result = Max = nums[0]
        for i in nums[1:]:
            result = max(result+i,i)
            Max = max(Max,result)
        return Max

solution = Solution()
print(solution.maxSubArray([-2,1,-4,4,-1,2,1,-5,4]))