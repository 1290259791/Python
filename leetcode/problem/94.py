class TreeNode:
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree:
    """数类"""

    def __init__(self):
        self.root = TreeNode()

    def add(self, elem):
        """加入节点"""
        node = TreeNode(elem)

        if self.root.elem == -1:
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.left is None:
                    treeNode.left = node
                    return
                elif treeNode.right is None:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_digui(root.left)
        print(root.elem)
        self.middle_digui(root.right)


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = Tree()
        for elem in root:
            tree.add(elem)
        tree.middle_digui(tree.root)
solution = Solution()
solution.inorderTraversal([1,None,2,3])
