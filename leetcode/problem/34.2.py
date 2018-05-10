class Solution:
    def searchRange(self, nums, target):
        """
        查找出现的位置
        进行二分查找,然后 while 循环找到最小和最大的位置
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                min = mid
                while min >= 0 and nums[min] == target:
                    min -= 1
                max = mid
                while max <= end and nums[max] == target:
                    max += 1
                result.append(min+1)
                result.append(max-1)
                return result
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1,-1]

solution = Solution()
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 8))