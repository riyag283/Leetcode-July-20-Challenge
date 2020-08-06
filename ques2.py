class Node: 
    def __init__(self, data): 
	    self.data = data 
            self.left = None
	    self.right = None


# Given a binary tree, print its nodes in reverse level order 
def reverseLevelOrder(root): 
	S = [] 
	Q = [] 
	Q.append(root) 

	# Do something like normal level order traversal order. 
	# Following are the differences with normal level order 
	# traversal: 
	# 1) Instead of printing a node, we push the node to stack 
	# 2) Right subtree is visited before left subtree 
	while(len(Q) > 0 ): 

		# Dequeue node and make it root
		root = Q.pop(0) 
		S.append(root) 

		# Enqueue right child 
		if (root.right): 
			Q.append(root.right) 

		# Enqueue left child 
		if (root.left): 
			Q.append(root.left) 

	# Now pop all items from stack one by one and print them 
	while(len(S) > 0): 
		root = S.pop() 
		print(root.data) 

# Driver program to test above function 
root = Node(3) 
root.left = Node(9) 
root.right = Node(20) 
root.left.left = Node(None) 
root.left.right = Node(None) 
root.right.left = Node(15) 
root.right.right = Node(7) 

print("Level Order traversal of binary tree is")
reverseLevelOrder(root) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
