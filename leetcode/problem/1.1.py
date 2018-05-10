class Solution:
    def twoSum(self, nums, target):
        """
        用 HashTable 存储结果和坐标,
        判断另一个数是否在 HashTable 中,
        不在的话就存储一个
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return None
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target-nums[i]] = i
solution = Solution()
