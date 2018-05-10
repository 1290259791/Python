class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = Max = Min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:  # 判断之后交换最大值和最小值
                Max, Min = Max, Min
            Max = max(nums[i], Max * nums[i])
            Min = min(nums[i], Min * nums[i])
            result = max(result, Max)
        return result
