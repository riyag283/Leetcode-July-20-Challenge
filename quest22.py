class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def func(root):
    result = []
    if not root:
        return result
    level = [root]
    direction = 1
    while level:
        result.append([n.val for n in level][::direction])
        direction *= -1
        level = [child for node in level for child in (node.left, node.right) if child]
    return result
