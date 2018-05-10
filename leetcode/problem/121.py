class Solution:
    def maxProfit(self, prices):
        """
        题目:买股票最佳时机
        解法:动态规划
        思路:
        从第一天开始遍历,
        设置一个最小值 min = prices[0]
        到遇到更小的则替换.
        设置一个最大利润,为0
        遇到 prices[i]-min > max 后替换
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        Max = 0
        Min = prices[0]
        for i in prices:
            Max = max(Max, i - Min)
            Min = min(Min, i)
        return Max


solution = Solution()
print(solution.maxProfit([]))
