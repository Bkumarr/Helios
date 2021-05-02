class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def search(self, target):
    if self.data == target:
      print('Found the node')
      return self
    
    elif self.left and self.data > target:
    
      return self.left.search(target)

    elif self.right and self.data < target:
      return self.right.search(target)
    else:
      print('There are no such node')

  def traverse_preorder(self):
    print(self.data)
    if self.left:
      self.left.traverse_preorder()
  
    if self.right:
      self.right.traverse_preorder()
  def traverse_Inorder(self):
    if self.left:
      self.left.traverse_preorder()
    print(self.data)
    if self.right:
      self.right.traverse_preorder()
  def traverse_Postorder(self):
    if self.left:
      self.left.traverse_preorder()
  
    if self.right:
      return self.right.traverse_preorder()
    print(self.data)

class Tree:
  def __init__(self, root, name= ''):
    self.root = root
    self.name = name
    
  def search(self, target):
    return self.root.search(target)

  def traverse_Postorder(self):
    return self.root.Postorder()

  def traverse_preorder(self):
    return self.root.preorder()
  
  def traverse_Inorder(self):
    return self.root.Inorder()

node = Node(10)
node.left = Node(5)
node.right = Node(15)
my_tree = Tree(node, 'ryan root tree')

print(my_tree.name)
print(my_tree.root.left.data)

found = my_tree.search(15)
print(found.data)