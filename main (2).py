#Binary search tree insertion and searching,preorder,inorder ,postorder traversal respectively
class BST:
  def __init__(self,key):
    self.key = key
    self.lchild = None
    self.rchild = None
  # Insertion 
  def insert(self,data):
    if self.key is None:
      self.key = data
      return
    if self.key == data:
      return
    if self.key > data:
      if self.lchild:
        self.lchild.insert(data)
      else:
        self.lchild = BST(data)
    else:
      if self.rchild:
        self.rchild.insert(data)
      else:
        self.rchild = BST(data)
  # searching in tree
  def search(self,data):
    if self.key==data:
      print("node found")
      return 
    if self.key > data:
      if self.lchild:
        self.lchild.search(data)
      else:
        print("node is not present")
    else:
      if self.rchild:
        self.rchild.search(data)
      else:
        print("node is not present ")
  # Preorder traversal
  def preorder(self):
    print(self.key,end=' ')
    if self.lchild:
      self.lchild.preorder()
    if self.rchild:
      self.rchild.preorder()
  #Inorder traversal
  def Inorder(self):
    if self.lchild:
      self.lchild.Inorder()
    print(self.key,end=' ')
    if self.rchild:
      self.rchild.Inorder()

  def Postorder(self):
    if self.lchild:
      self.lchild.Postorder()
    if self.rchild:
      self.rchild.Postorder()
    print(self.key,end=' ')
    

root = BST(10)
list1 = [20,4,30,4,1,5,6]
for i in list1:
  root.insert(i)

root.search(5)

print("preorder traversal is ;")
root.preorder()
print("\nInorder traversal is ;")
root.Inorder()
print("\nPostorder traversal is ;")
root.Postorder()


        
    
    


