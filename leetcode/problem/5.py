class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        题目:最长回文字符串
        思路:枚举回文字符中心位置,在该位置上扩展
        """
        if s is None:
            return 0
        Max = 0
        List = []
        #   i 是回文字符的中心位置
        for i in range(len(s)):

            #   回文字符长度奇数
            j = 1
            n = 0
            while i - j >= 0 and i + j < len(s):
                if s[i-j] != s[i+j]:
                    break
                n = j*2 + 1
                j += 1
            if n >= Max:
                List = s[i-j-1:i+j-1]
            #   回文字符为偶数
            k = 1
            m = 0
            while i - k >= 0 and i+k+1 < len(s):
                if s[i-k] != s[i+k+1]:
                    break
                m = k*2+2
                k += 1
            if m >= Max:
                print(i-k+1)
                List = s[i-k+1:i+k]
        print(List)
        return Max


solution = Solution()
s = 'wabcddcbaw'
solution.longestPalindrome(s)
