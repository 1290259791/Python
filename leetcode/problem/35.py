class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        for i in range(len(nums)):
            if target < nums[0]:
                return 0
            if target > nums[len(nums)-1]:
                return len(nums)
            if nums[i] < target < nums[i+1]:
                return i+1

solution = Solution()
print(solution.searchInsert([1,3],0))



"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
"""