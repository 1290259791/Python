class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        首先排序然后进行两个数相加,当大于的时候,进行左右的判断
        """
        nums_bak = nums.copy()
        nums.sort()
        i = 0
        j = 0
        for k in range(0, len(nums)-1):
            if nums[k] + nums[k+1] >= target:
                i = k
                j = k + 1
                break
        while i >= 0 and j < len(nums):
            if nums[i] + nums[j] < target:
                j += 1
            elif nums[i] + nums[j] > target:
                i -= 1
            else:
                if nums[i] == nums[j]:
                    return [nums_bak.index(nums[i]), nums_bak.index(nums[i], i+1)]
                else:
                    return [nums_bak.index(nums[i]), nums_bak.index(nums[j])]


if __name__ == '__main__':
    nums = [1,2,3,4]
    target = 3
    solution = Solution()
    print(solution.twoSum(nums,target))