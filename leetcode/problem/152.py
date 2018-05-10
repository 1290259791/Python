class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        Min = Max = nums[0]
        sum = nums[0]
        for i in range(1,n):
            tempMax = Max
            tempMin = Min
            Max = max(tempMin*nums[i],nums[i],tempMax*nums[i])
            Min = min(tempMin*nums[i],nums[i],tempMax*nums[i])
            sum = max(sum,Max)
        return sum
solution = Solution()
print(solution.maxProduct([-1,-2,-3]))