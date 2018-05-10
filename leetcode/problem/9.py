class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        strx_bax = strx[::-1]
        for i in range(len(strx)):
            if strx[i] != strx_bax[i]:
                return False
        return True

solution = Solution()
print(solution.isPalindrome(121))