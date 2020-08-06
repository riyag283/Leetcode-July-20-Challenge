# Data structure to store a Binary Tree node
class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right


# traverse the tree in pre-order fashion and store nodes into the dict
# corresponding to their level
def preorder(root, level, dict):

	# base case: empty tree
	if root is None:
		return

	# insert current node and its level into the dict
	dict.setdefault(level, []).append(root.key)

	# recur for left and right subtree by increasing level by 1
	preorder(root.left, level + 1, dict)
	preorder(root.right, level + 1, dict)


# Recursive function to do reverse level order traversal of given binary tree
def levelOrderTraversal(root):

	# create an empty dict to store nodes between given levels
	dict = {}

	# traverse the tree and insert its nodes into the dict
	# corresponding to the their level
	preorder(root, 1, dict)

	# iterate through the dict in reverse order and
    # print all nodes present in very level
	for i in range(len(dict), 0, -1):
		print("Level", i, ":", dict.get(i))


if __name__ == '__main__':

	root = Node(3)
	root.left = Node(9)
	root.right = Node(20)
	root.left.left = Node(None)
	root.left.right = Node(None)
	root.right.left = Node(15)
	root.right.right = Node(7)
#	root.right.right.right = Node(30)

	levelOrderTraversal(root)
