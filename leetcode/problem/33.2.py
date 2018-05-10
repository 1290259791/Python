class Solution:
    def search(self, nums, target):
        """
        判断这个数在数组中的位置
        复杂度为 O(log(n))
        二分查找,判断范围之间,在范围间继续判断
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] > target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


List = [4, 5, 6, 7, 8, 0, 1, 2, 3]
solution = Solution()
print(solution.search(List, 3))
