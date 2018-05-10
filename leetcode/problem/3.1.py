class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        无重复字符的最长子串
        """
        hashTable = {}
        max_len = 0  # 无重复的最长
        cur = 0  # 记录无重复的起始位置
        for i, c in enumerate(s):
            if c in hashTable and cur <= hashTable[c]:  # 字典序中存在字符,cur<hashTable[c]要大于重复的左边,不然又从重复的左边开始计算.
                cur = hashTable[c] + 1  # 更新无重复的起始位置
                print(cur, i, hashTable[c])
            else:
                max_len = max(max_len, i - cur + 1)
            hashTable[c] = i  # 记录从左到右每个字符的位置
        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring('tmmzuxt'))
