#!/usr/bin/env python3
# *-* coding:utf-8 *-*

class BinTreeNode():
    
    """
       Constructor with value to insert in tree which assigns
       the left child and right child with default None
    """

    def __init__(self, value = 5):
        
        self.value = value    
        self.left = None
        self.right = None
    """
      If the data to be inserted is  already present in tree,
      it wont be added again to avoid duplication of values
      """
        
    def insert(self, value):
                 
        """
      If the data to be inserted is less than value
      of current node,then data will  insert into the left node
        """
        
        """
             If the data to be inserted is greater than value of current node,
                    then data will  insert into the Right node
        """
        
        if value < self.value:
            if self.left is None:
                self.left = BinTreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None :
                self.right = BinTreeNode(value)
            else:
                self.right.insert(value)
        else:
            pass  #node already exist
        
       
    def search(self, value):
        """if current node equal to data we are finding,return true"""
        """if current node is lesser than data we are finding,we have search in left child node"""
        """if current node is greater than  data we are finding,
         we have search in right child node"""
         
        if self.value == value:
            return self        
        elif value < self.value and self.left is not None:
           return self.left.search(value)           
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        else:
            pass
            
            
    def __show__(self):
        return "[ {} ] == {} == [ {} ]".format(self.left,self.value,self.right)
    

class BinTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinTreeNode(value)
        else:
            self.root.insert(value)

    def search(self, value):
        if self.root is not None:
            return self.root.search(value)
        else:
            return None

    def __show__(self):
        return "BinTree(root={})".format(self.root)
    
if __name__ == "__main__":
    pass

