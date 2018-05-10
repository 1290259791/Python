class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        left, rigth = 0, len(nums)-1
        while left <= rigth:
            mid = (left + rigth) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                rigth = mid - 1
            else:
                left = mid + 1
        return False

solution = Solution()
print(solution.search(nums = [2,5,6,0,0,1,2], target = 0))
