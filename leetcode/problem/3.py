class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        无重复字符的最长子串
        设定两个指向表,并且利用 dict 的特性
        """
        length = len(s)
        l = 0   # 左边的指向
        r = 0   # 右边的指向
        maxlength = 0
        Dict = {}
        while r != length:
            if s[r] in Dict and l <= Dict[s[r]]:    # 是否存在字典序,并且存在的位置大于左边的指向
                l = Dict[s[r]] + 1  # 右边的指向更新加1
            else:
                maxlength = max(maxlength, r - l + 1)
            Dict[s[r]] = r
            r += 1
        return maxlength


solution = Solution()
print(solution.lengthOfLongestSubstring('asdzxdfs'))
