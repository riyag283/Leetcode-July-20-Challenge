class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def preorder(root, level, dict1):
    if root is None:
        return

    if root.key != None:
        dict1.setdefault(level, []).append(root.key)

    preorder(root.left, level+1, dict1)
    preorder(root.right, level+1, dict1)

def traverse(root):
    dict1 = {}
    preorder(root, 1, dict1)

    list1 = []
    for i in range(len(dict1),0,-1):
        list1.append(dict1.get(i))

    return list1

if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(None)
    root.left.right = Node(None)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(traverse(root))
