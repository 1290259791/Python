class Solution:
    def search(self, nums, target):
        """
        判断这个数在数组中的位置

        二分查找,当数组为空的时候,修改18 20/22
        少去一个判断
        时间复杂度大于 Olog(n)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = -1  # 判断是否排序了
        for i in range(len(nums) - 1):  # 判断旋转的位置
            if nums[i] > nums[i + 1]:
                nums[:] = nums[i + 1:] + nums[:i + 1]
                flag = i
                break
        start, end = 0, len(nums)-1
        print(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid if flag == -1 else (mid + flag + 1) % len(nums)  # 当没有排序直接返回,排序的话后移动 flag
        return -1


List = [4,5,6,7,8,0,1,2,3]
solution = Solution()
print(solution.search(List,3))
