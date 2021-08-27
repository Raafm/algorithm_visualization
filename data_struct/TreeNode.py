class TreeNode:
    def __init__(self,DATA):
        self.data   = DATA
        self.parent = None
        self.left   = None
        self.right  = None

    
    def link(self,childNode, right_child):
        if right_child:
            self.right = childNode
        else: self.left = childNode

        if childNode is not None: childNode.parent = self
    
    