class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [0]    # dp[i]表示s[ dp[i-1] : i ]的子串在wordDict中
        for i in range(1,len(s)+1):
            for j in range(len(dp)-1, -1, -1):    # dp[j]：已匹配的最后一个字符的后一个字符 到 s[i]:正在匹配的最后一个字符
                if s[dp[j]:i] in wordDict:
                    dp.append(i)
                    break
        if dp[-1] == len(s):
            return True
        else:
            return False