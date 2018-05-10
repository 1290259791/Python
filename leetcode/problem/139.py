class Solution:
    def wordBreak(self, s, wordDict):
        """
        题目:单词拆分
        解法:动态规划
        思路:
        将 s 字符串遍历
        对 wordDict 中的单词进行遍历
        当遍历 s 字符串的长度大于 word 中单词长度时,
        比较 s 中遍历字符组成的字符串,来进行word 的比较.
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for word in wordDict:
                if len(word) <= i and dp[i - len(word)]:  # 判断i大于word长度防止越界,判断上个单词是否存在,
                    if s[i - len(word):i] == word:
                        dp[i] = 1
                        break
        return True if dp[-1] else False


solution = Solution()
print(solution.wordBreak(s="leetcode", wordDict=["leet", "code"]))
