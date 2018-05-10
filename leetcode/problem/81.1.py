class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] is target:
                return True
            while left < mid and nums[left] == nums[mid]:
                left += 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return False

solution = Solution()
print(solution.search(nums = [1,3,1,1,1], target = 3))
