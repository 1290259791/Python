class Solution:
    def searchRange(self, nums, target):
        """
        查找出现的位置
        利用 List 添加位置,用 if 判断是否为空
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = []
        for k, v in enumerate(nums):
            if v == target:
                flag.append(k)
            elif flag:
                break
        if flag:
            return [flag[0], flag[-1]]
        else:
            return [-1, -1]


solution = Solution()
print(solution.searchRange(nums = [5,7,7,8,8,10], target = 5))
