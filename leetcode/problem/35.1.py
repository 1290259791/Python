class Solution:
    def searchInsert(self, nums, target):
        """
        判断左边大于右边的时候
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:   # 当nums[mid] 和 target 相等或大于的时候, right-1,
                right = mid - 1
        print(left,right)
        return left


solution = Solution()
print(solution.searchInsert([1,2,3,4,7,8],6))