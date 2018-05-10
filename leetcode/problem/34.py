class Solution:
    def searchRange(self, nums, target):
        """
        查找出现的文职
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = -1
        end = -1
        flag = 0
        for k, v in enumerate(nums):
            if v == target and flag == 0:   # 出现的位置并且是第一次出现, begin 记录第一次
                begin = k
                flag = 1
            if nums[begin] == v and flag == 1:  # begin已经记录过位置,记录最后出现的位置
                end = k

        return [begin,end]


solution = Solution()
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 6))

"""
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""
