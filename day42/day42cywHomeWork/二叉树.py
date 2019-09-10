# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/9/10 23:06
# 文件名称 : 二叉树.PY
# 开发工具 : PyCharm

class TreeNode:
    def __init__(self,left = None,right = None,data = None):
        self.data = data
        self.left = left
        self.right = right

    # 前序
    def preorder(self,root):
        if root is None:
            return
        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    #中序
    def inorder(self,root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    #后序
    def postorder(self,root):
        if root is None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)