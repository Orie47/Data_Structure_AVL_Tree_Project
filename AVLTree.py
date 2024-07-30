#name - Orie Shaked 

"""A class representing a node in an AVL tree (updated version)"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		if key != None: 
			self.height= 0
			self.left = AVLNode(None,None)
			self.right = AVLNode(None,None)
		
			
	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	@time complexity: O(1)
	"""
	def get_left(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	@time complexity: O(1)
	"""
	def get_right(self):
		return self.right 

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	@time complexity: O(1)
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	@time complexity: O(1)
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	@time complexity: O(1)
	
	"""
	def get_value(self):
		return self.value 


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	@time complexity: O(1)
	"""
	def get_height(self):
		return self.height
	

	"""sets the left child

	@rtype: None
	@type node: AVLNode
	@param node: a node in a tree 
	@time complexity: O(1)
	"""
	def set_left(self, node):
		self.left = node


	"""sets the right child
	@type node: AVLNode
	@rtype: None
	@param node: a node in a tree
	@time complexity: O(1)
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent of node
	@type node: AVLNode
	@rtype: None
	@param node: node from tree
	@time complexity: O(1)
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key for a node

	@rtype: None
	@type key: int or None
	@param key: the key of a node
	@time complexity: O(1)
	"""
	def set_key(self, key):
		self.key = key


	"""sets value to a node
	@rtype: None
	@type value: any
	@param value: data
	@time complexity: O(1)
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@rtype: None
	@param h: the height of a node
	@time complexity: O(1)
	"""
	def set_height(self, h):
		self.height = h

	
	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	@time complexity: O(1)
	"""
	def is_real_node(self):
		return True if self.key is not None else False


	"""calculates the height of a node in a AVL tree
 	@type AVLNode
  	@param node: a node of a tree
   	@rType: int
    @returns: the height of a node
	@time complexity: O(1)
	"""		
	def calc_height(self):
			return max(self.left.height, self.right.height) + 1

	"""calculates the balance factor of a node in a Tree
 	@type AVLNode
  	@param node: a node of a tree
   	@rType: int
    @returns: the balance factor of a node
	@time complexity: O(1)
	"""
	def balance_factor(self):
		return self.left.height - self.right.height

 
	"""calculates the minimum of a subtree where the root
        is our given node
 	@type AVLNode
  	@param node: a node of a tree
   	@rType: AVLNode
    @returns: the minimum of a node
	@time complexity: O(log(n))
	"""
	def min(self):
		node = self
		while node.left.is_real_node():
			node = node.left
		return node

	"""calculates the successor of a given node
 	@type AVLNode
  	@param node: a node of a tree
   	@rType: AVLNode
    @returns: the successor of a node
	@time complexity: O(log(n))
	"""
	def successor(self):
		if self.right.is_real_node():
			return self.right.min()  # Find the minimum node in the right subtree
		parent = self.parent
		current = self
		#the next node in the order will be the node that we must go up and right to
		while parent.is_real_node() and current == parent.right:
			current = parent
			parent = parent.get_parent()
		return parent
	

	"""manually adds to a node a right virtual child
 	@type AVLNode
  	@param self: a node of a tree
   	@rType: None
    @returns: Nothing
	@time complexity: O(1)
	"""
	def add_right_virtual_node(self):
		self.right = AVLNode(None, None) 
		self.right.set_parent(self)
	

	"""manually adds to a node a left virtual child
 	@type AVLNode
  	@param self: a node of a tree
   	@rType: None
    @returns: None
	@time complexity: O(1)
	"""
	def add_left_virtual_node(self):
		self.left = AVLNode(None, None) 
		self.left.set_parent(self)

	
	""" 
	gives a node two virtual children
	@type AVLNode
	@rType: None
	@returns: returns nothing
	@time complexity: O(1)
	"""
	def add_virtual_nodes(self):
		self.add_right_virtual_node()
		self.add_left_virtual_node()
		self.height = 0
  

"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):
	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.tree_size = 0


	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	@time complexity: O(log(n))
	"""
	def search(self, key):
		current_node = self.root
		while current_node.is_real_node():
			#if keys match then return current node
			if current_node.get_key() == key:
				return current_node
			elif key < current_node.get_key():
				current_node = current_node.get_left()
			else:
				current_node = current_node.get_right()
		#node was not found:(
		return None

	"""returns the would-be parent of a node we want to insert
 	@type key: int
  	@param key: a key of a node
   	@rType: AVLNode
    @returns: the would-be parent of a node we want to insert
	@time complexity: O(log(n))
	"""
	def tree_position(self,key):
		if self.root is None:
			return None
		current_node = self.root
		parent = current_node
		while current_node.is_real_node():
			parent = current_node 
			if key == current_node.get_key():
				return current_node
			elif key < current_node.get_key():
				current_node = current_node.get_left()
			else:
				current_node = current_node.get_right()
		return parent
		
	"""performs regular bst insertion without rebalancing
	@type node: AVLNode
	@rtype: None
	@returns: Nothing
	@time complexity: O(log(n))
	"""
	def tree_insert(self, node):
		if self.root == None:
			self.root = node
		else:
			#gets the position of the parent-to-be
			parent = self.tree_position(node.get_key())
			#if node already existed in the tree do nothing
			if node.get_key() == parent.get_key():
				return
			#set the parent of the new node accordingly 
			node.set_parent(parent)
			#set the kid of the parent accordingly 
			if node.get_key() < parent.get_key():
				parent.set_left(node)
			else: 
				parent.set_right(node)
		
  
	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@time complexity: O(log(n))
	"""
	
	def insert(self, key, val):
		#we create a new node with key and val
		node = AVLNode(key, val)
		self.tree_insert(node)
		#we add virtual nodes as the children of the new leaf
		node.add_virtual_nodes()
		if key is not None:
			self.tree_size += 1
		return self.insert_maintain(node.get_parent())

	"""Maintains AVL rules and node/tree fields for insert operations

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations
	@time Complexity: O(log(n)) 
	"""
	def insert_maintain(self, node):
		count_re_balance = 0
		while node is not None:
			bFactor = node.balance_factor()
			if node.calc_height() == node.get_height() and abs(bFactor) < 2:
				if node.get_parent() is None:
					self.root = node
				break
			# need to fix height after deletion even if there is no current rotate:
			elif node.calc_height() != node.get_height() and abs(bFactor) < 2:
				node.set_height(node.calc_height())
				count_re_balance += 1
			else:
				count_re_balance += self.rotate(node)
				if node.get_parent() is None:
					self.root = node
				break
			if node.get_parent() is None:
				self.root = node
			node = node.get_parent()
		return count_re_balance
	
	"""Does a right rotation

	   @type node: AVLNode
	   @pre: 0 <= search(node) < self.length()
	   @param node: node in the tree
	   @rtype: int
	   @time complexity: O(1)
	   """
	def right_rotation(self, node):
		#performing the neccessary changes to the pointers of the nodes in rotation
		new_parent = node.get_left()
		node.set_left(new_parent.get_right())
		node.get_left().set_parent(node)
		new_parent.set_right(node)
		new_parent.set_parent(node.get_parent())
		node.set_parent(new_parent)
		if new_parent.get_parent() is None:
			self.root = new_parent
		else:
			if new_parent.get_parent().get_left() == node:
				new_parent.get_parent().set_left(new_parent)
			if new_parent.get_parent().get_right() == node:
				new_parent.get_parent().set_right(new_parent)
		#updating the height and fields of the nodes in rotation
		node.set_height(node.calc_height())
		new_parent.set_height(new_parent.calc_height())
		return 1

	"""Does a left rotation

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations - 1
	@time complexity: O(1)
	"""
	def left_rotation(self, node):
		#performing the neccessary changes to the pointers of the nodes in rotation
		new_parent = node.get_right()
		node.set_right(new_parent.get_left())
		node.get_right().set_parent(node)
		new_parent.set_left(node)
		new_parent.set_parent(node.get_parent())
		node.set_parent(new_parent)
		if new_parent.get_parent() is None:
			self.root = new_parent
		else:
			if new_parent.get_parent().get_left() == node:
				new_parent.get_parent().set_left(new_parent)
			if new_parent.get_parent().get_right() == node:
				new_parent.get_parent().set_right(new_parent)
		#updating the height and fields of the nodes in rotation	
		node.set_height(node.calc_height())
		new_parent.set_height(new_parent.calc_height())
		return 1

	"""
	performs a left rotation followed by a right rotation

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations, which is 2
	@time complexity: O(1)
	"""
	def left_right_rotation(self, node):
		return self.left_rotation(node.get_left()) + self.right_rotation(node)

	
	"""
	performs a right rotation rotation followed by a left rotation

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations, which is 2
	@time complexity: O(1)
	"""
	def right_left_rotation(self, node):
		return self.right_rotation(node.get_right()) + self.left_rotation(node)

	"""
	Determines which rotation is needed (if needed) and does that

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations, 0 if there were not any rotations
	@time complexity: O(1)
	"""
	def rotate(self, node):
		if node.balance_factor() < -1:
			if node.get_right().balance_factor() >= 1:
				return self.right_left_rotation(node)
			else:
				return self.left_rotation(node)
		if node.balance_factor() > 1:
			if node.get_left().balance_factor() <= -1:
				return self.left_right_rotation(node)
			else:
				return self.right_rotation(node)
		return 0


	"""Maintains AVL rules and node/tree fields for delete operations

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations
	@time Complexity: O(log(n)) 
	"""
	def delete_maintain(self, node):
		count_re_balance = 0
		while node is not None:
			original_parent = node.get_parent()
			bFactor = node.balance_factor()
			if node.calc_height() == node.get_height() and abs(bFactor) < 2:
				if node.get_parent() is None:
					self.root = node
				break
			# need to fix height after deletion even if there is no current rotate:
			elif node.calc_height() != node.get_height() and abs(bFactor) < 2:
				node.set_height(node.calc_height())
				count_re_balance += 1
			else:
				count_re_balance += self.rotate(node)
			if node.get_parent() is None:
				self.root = node
			node = original_parent
		return count_re_balance


	"""deletes a node that is a leaf
	@type node: AVLNodes
	@pre: height of node is 0
	@rtype: int
	@returns: number of rebalancing operations
	time complexity: O(log(n))
	"""
	def delete_leaf(self, node):
		parent = node.get_parent()
		#the leaf was also the root
		if parent is None:
			self.root = None
		#the leaf wasnt the root
		else: 
			if parent.get_left() == node:
				parent.add_left_virtual_node()
				node = None
			else:
				parent.add_right_virtual_node()
				node = None
		return self.delete_maintain(parent)


	"""deletes a node that has or child
	@type node: AVLNodes
	@rtype: int
	@returns: number of rebalancing operations
	time complexity: O(log(n))
	"""
	def delete_branch(self, node):
		parent = node.get_parent()
		#if parent exists
		if parent:
			#if node is left child
			if parent.get_left() == node:
				#if node has left child
				if node.get_left().is_real_node():
					parent.set_left(node.get_left())
					node.get_left().set_parent(parent)
		
				else: 
					parent.set_left(node.get_right())
					node.get_right().set_parent(parent)
				node = None
			#if node is right child
			if parent.get_right() == node:
				if node.get_left().is_real_node():
					parent.set_right(node.get_left())
					node.get_left().set_parent(parent)
				else: 
					parent.set_right(node.get_right())
					node.get_right().set_parent(parent)
				node = None
		return self.delete_maintain(parent)
		

	"""swaps nodes while dealing with all relevant pointers
	@type node, successor: AVLNodes
	@pre: height of node is higher than successor's height, and as a result 
	successor doesnt have a real left child
	@rtype: None
	@returns: None
	time complexity: O(1)
	"""
	def swap_nodes(self, node, successor):
		parent_of_node= node.get_parent()
		node_left_child = node.get_left()
		node_right_child = node.get_right()
		parent_of_successor= successor.get_parent()
		successor_right_child = successor.get_right()
		
		#swapping heights:
		temp_height = node.get_height()
		node.set_height(successor.get_height())
		successor.set_height(temp_height)


		#if node had a parent, we then need to update the child of parent
		if parent_of_node is not None:
			#node is left child of parent
			if node.get_parent().get_left() == node:
				parent_of_node.set_left(successor) 
			#node is right child of parent
			else: 
				parent_of_node.set_right(successor)
			successor.set_parent(parent_of_node)
		#if node was root:
		else: 
			self.root = successor
			successor.set_parent(None)
		
		#swapping children 
		successor.set_left(node_left_child)
		node_left_child.set_parent(successor)
		node.add_left_virtual_node()
		node.set_right(successor_right_child)
		successor_right_child.set_parent(node)

		#resetting the parent of node
		if parent_of_successor == node:
			successor.set_right(node)
			node.set_parent(successor)
		else: 
			successor.set_right(node_right_child)
			node_right_child.set_parent(successor)
			parent_of_successor.set_left(node)
			node.set_parent(parent_of_successor)
		

	"""deletes node from the tree that has two children
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@time complexity: O(log(n))
	"""
	def delete_with_two_children(self, node):
		#finds the next node in ascending order
		successor = node.successor()
		#swithces between the node 
		self.swap_nodes(node, successor)
		if node.get_height() == 0:
			return self.delete_leaf(node)
		else:
			return self.delete_branch(node)


	"""deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	@time complexity: O(log(n))
	"""
	def delete(self, node):
		self.tree_size -= 1
		#if node is leaf
		if node.get_left().is_real_node() == False and node.get_right().is_real_node() == False:
			return self.delete_leaf(node)
		#if the node only has one child
		elif node.get_left().is_real_node() == False or node.get_right().is_real_node() == False:
			return self.delete_branch(node)
		#node to delete has two children
		else:
			return self.delete_with_two_children(node)


	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	@time complexity: O(n)
	"""
	def avl_to_array(self):
		def node_to_array(node):
			left_array = node_to_array(node.left) if node.left.is_real_node() else []
			self_array = [(node.key, node.value)] if node.is_real_node() else []
			right_array = node_to_array(node.right) if node.right.is_real_node() else []
			return left_array + self_array + right_array
		if self.root is None:
			return []
		return node_to_array(self.root)


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	time complexity: O(1)
	"""
	def size(self):
		return self.tree_size


	"""implements the split method down below
	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: tuple
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	@time complexity: O(log(n))
	"""
 	
	def split_helper(self, node):
		if self.tree_size == 1:
			return (AVLTree(),AVLTree())
		#creating two sub-trees 
		ltree,rtree = AVLTree(),AVLTree()
		ltree.root = self.root.get_left()
		rtree.root = self.root.get_right()
		#our root is the node we want to separate
		if (node.get_key() == self.root.get_key()):
			left = self.root.get_left()
			right = self.root.get_right()
			left.set_parent(None)
			right.set_parent(None)
			return (ltree, rtree)
		#our root is bigger than node we want to separate
		if (node.get_key() < self.root.get_key()):
			l_sub_tree, r_sub_tree = ltree.split_helper(node)
			r_sub_tree.join(rtree, self.root.get_key(), self.root.get_value())
			return (l_sub_tree, r_sub_tree)
		#our root is smaller than node we want to separate
		if (node.get_key() > self.root.get_key()):
			l_sub_tree, r_sub_tree = rtree.split_helper(node)
			ltree.join(l_sub_tree, self.root.get_key(), self.root.get_value())
			return (ltree, r_sub_tree)
		

			
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	@time complexity: O(log(n))
	"""
	def split(self, node):
		return list(self.split_helper(node))
		


	"""Maintains AVL rules and node/tree fields for join operations

	@type node: AVLNode
	@pre: 0 <= search(node) < self.length()
	@param node: node in the tree
	@rtype: int
	@returns: The number of rotations
	@time Complexity: O(log(n)) 
	"""
	def join_maintain(self, node):
		count_re_balance = 0
		while node is not None:
			original_parent = node.get_parent()
			bFactor = node.balance_factor()
			if node.calc_height() == node.get_height() and abs(bFactor) < 2:
				if node.get_parent() is None:
					self.root = node
				break
			# need to fix height after deletion even if there is no current rotate:
			elif node.calc_height() != node.get_height() and abs(bFactor) < 2:
				node.set_height(node.calc_height())
				count_re_balance += 1
			else:
				count_re_balance += self.rotate(node)
			if node.get_parent() is None:
				self.root = node
			node = original_parent
		return count_re_balance

	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: key is bigger than all keys in a tree and smaller than all keys in another tree
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	@ time complexity: O(log(n))
	"""
	def join(self, tree2, key, val):
		new_node = AVLNode(key, val)
		#if tree number one is empty:
		if self.root is None or self.root.get_key() is None:
			#if both trees are empty:
			if tree2.root is None or tree2.root.get_key() is None:
				self.root = new_node
				self.tree_size = 1
				return 1
			else:
				height_T2 = tree2.root.get_height()
				self.root = tree2.root
				self.insert(key, val)
				self.tree_size += tree2.tree_size
				# +2 cause the height of an empty tree is -1 
				return height_T2 + 2
		else:
			if tree2.root is None or tree2.root.get_key() is None:
				height_T1 = self.get_root().get_height()
				self.insert(key, val)
				return height_T1 + 2


		height_T1 = self.root.get_height() 
		height_T2 = tree2.root.get_height() 
		#keys in self are smaller than keys in tree2
		if self.root.get_key() < key:
			self.join_self_keys_smaller(tree2, new_node)
		#keys of left tree are bigger
		else: 
			self.join_self_keys_bigger(tree2, new_node)
		self.tree_size += tree2.tree_size + 1
		return abs(height_T1 - height_T2) + 1

	"""joins self with key thats bigger and another AVLTree whose keys are bigger

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type new_node:AVLNode
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: None
	@returns: nothing
	@ time complexity: O(log(n))
	"""
	def join_self_keys_smaller(self, tree2, new_node):
		height_T1 = self.root.get_height()
		height_T2 = tree2.root.get_height()
		if height_T1 > height_T2:
			current_node = self.root
			# find the first node that has a height smaller than tree 2 (at most smaller by 1)
			while current_node.get_height() > height_T2:
				current_node = current_node.get_right()
			#fix pointers and connect the trees
			parent = current_node.get_parent()
			parent.set_right(new_node)
			new_node.set_parent(parent)
			new_node.set_left(current_node)
			new_node.set_right(tree2.get_root())
			tree2.get_root().set_parent(new_node)
			current_node.set_parent(new_node)
			self.join_maintain(new_node)

		if height_T1 < height_T2:
			current_node = tree2.get_root()
			# find the first node that has a height smaller than tree 1 (at most smaller by 1)
			while current_node.get_height() > height_T1:
				current_node = current_node.get_left()
			#fix pointers and connect the trees
			parent = current_node.get_parent()
			parent.set_left(new_node)
			new_node.set_parent(parent)
			new_node.set_right(current_node)
			new_node.set_left(self.root)
			self.root.set_parent(new_node)
			current_node.set_parent(new_node)
			self.join_maintain(new_node)
		if 	height_T1 == height_T2:
			new_node.set_left(self.root)
			self.root.set_parent(new_node)
			new_node.set_right(tree2.get_root())
			tree2.get_root().set_parent(new_node)
			new_node.set_parent(None)
			self.root = new_node
			self.join_maintain(new_node)

	"""joins self with key thats smaller and another AVLTree whose keys are smaller

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type new_node:AVLNode
	@pre: all keys in self are bigger than key and all keys in tree2 are smaller than key
	@rtype: None
	@returns: nothing
	@ time complexity: O(log(n))
	"""
	def join_self_keys_bigger(self, tree2, new_node):
		height_T1 = self.root.get_height()
		height_T2 = tree2.root.get_height()
		if height_T1 > height_T2:
			current_node = self.root
			# find the first node that has a height smaller than tree 2 (at most smaller by 1)
			while current_node.get_height() > height_T2:
				current_node = current_node.get_left()
			#fix pointers and connect the trees
			parent = current_node.get_parent()
			parent.set_left(new_node)
			new_node.set_parent(parent)
			new_node.set_right(current_node)
			new_node.set_left(tree2.get_root())
			tree2.get_root().set_parent(new_node)
			current_node.set_parent(new_node)
			self.join_maintain(new_node)

		if height_T1 < height_T2:
			current_node = tree2.get_root()
			# find the first node that has a height smaller than tree 1 (at most smaller by 1)
			while current_node.get_height() > height_T1:
				current_node = current_node.get_right()
			#fix pointers and connect the trees
			parent = current_node.get_parent()
			parent.set_right(new_node)
			new_node.set_parent(parent)
			new_node.set_left(current_node)
			new_node.set_right(self.root)
			self.root.set_parent(new_node)
			current_node.set_parent(new_node)
			self.join_maintain(new_node)

		if 	height_T1 == height_T2:
			new_node.set_right(self.root)
			self.root.set_parent(new_node)
			new_node.set_left(tree2.get_root())
			tree2.get_root().set_parent(new_node)
			new_node.set_parent(None)
			self.root = new_node
			self.join_maintain(new_node)

		return   


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	@time complexity: O(1)
	"""
	def get_root(self):
		return self.root
