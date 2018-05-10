class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_handle():
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_Listnode(self, node):
        while node:
            print('node:',node,'val',node.val,'next',node.next)
            node = node.next

    def _reverse(self, nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_handle()
        for i in list:
            result = result_handle.add(i)
        return result


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()
        l3 = []
        count = 0
        if len(l1) <= len(l2):
            l0 = l1.copy()
            l1 = l2.copy()
            l2 = l0.copy()

        for i in range(len(l1)):
            n = l1[i]
            if i >= len(l2):
                m = 0
            else:
                m = l2[i]

            l3.append((n + m + count) % 10)
            count = (n + m + count)//10

        l3.reverse()
        return l3


l1 = [2, 4, 3]
l2 = [5, 6, 4]
solution = Solution()
solution.addTwoNumbers(l1,l2)
