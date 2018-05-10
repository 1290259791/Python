class Solution:
    def search(self, nums, target):
        """
        判断这个数在数组中的位置
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            for k, v in enumerate(nums):
                if v == target:
                    return k
        else:
            return -1


solution = Solution()
st = [15,16,19,20,25,1,3,4,5,7,10,14]
print(solution.search(st,25))