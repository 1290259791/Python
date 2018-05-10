import sys


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Min = sys.maxsize
        Max = 0
        for i in prices:
            if i < Min:
                Min = i
            elif i - Min > Max:
                Max = i - Min
        return Max