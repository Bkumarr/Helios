class Node:
  
  left = None
  right = None

  def __init__(self, data, left, right):
    self.left = left
    self.right = right
    self.data = data

class Binary_Tree:
  __root = None
  @property
  def root(self):
    return self.__root


  def in_order(self, root):
    # smallest to largest
    if root ==  None:
      return 
    self.in_order(root.left) #Traversing left subtree
    print(root.data, ",", end='')
    self.in_order(root.right) #Traversing right subtree

    #Inserting new node
  def insert(self, node, new_data):
    if self.__root == None:
      self.__root = Node(new_data, None, None)
      return
    compare_value = new_data-node.data
    #Recursive left subtree, continue to find the insertion position
    if compare_value < 0:
      if node.left == None:
        node.left = Node(new_data, None, None)
      else:
        self.insert(node.left, new_data)
    #Recursive right subtree, continue to find the insertion position
    elif compare_value > 0:
      if node.right == None:
        node.right = Node(new_data, None, None)
      else:
        self.insert(node.right, new_data)
      
ttree = Binary_Tree()

ttree.insert(ttree.root, 60)
ttree.insert(ttree.root, 40)
ttree.insert(ttree.root, 20)
ttree.insert(ttree.root, 10)
ttree.insert(ttree.root, 30)
ttree.insert(ttree.root, 50)
ttree.insert(ttree.root, 80)
ttree.insert(ttree.root, 70)
ttree.insert(ttree.root, 90)

ttree.in_order(ttree.root)









    

    

