class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        判断三个数相加为0
        """
        nums.sort()
        Lists = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                List = []
                if sum == 0:
                    List.append(nums[i])
                    List.append(nums[l])
                    List.append(nums[r])
                    Lists.append(List)
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        print(Lists)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    solution.threeSum(nums)
