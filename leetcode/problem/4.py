class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        两个排序数组的中位数
        """
        # nums1.sort()
        # nums2.sort()
        leng1 = len(nums1)
        leng2 = len(nums2)

        nums1.extend(nums2)
        nums1.sort()
        if (leng1+leng2)%2==0:
            n = (leng2+leng1)//2
            return (nums1[n]+nums1[n-1])/2
        else:
            n = (leng1+leng2)//2
            return nums1[n]


solution = Solution()
a = [1,3]
b = [2]
en = solution.findMedianSortedArrays(a,b)
print(en)
