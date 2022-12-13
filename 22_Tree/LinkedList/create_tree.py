class TreeNode:
    def __init__(self,data,children=[]) -> None:
        self.data = data
        self.children = children
        
    def __str__(self,level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self,child):
        self.children.append(child)
        
drinks = TreeNode("Drinks",[])
hot = TreeNode("Hot",[])
cold = TreeNode("Cold",[])
tea = TreeNode("Tea",[])
coffee = TreeNode("Coffee",[])
soda = TreeNode("Soda",[])
fanta = TreeNode("Fanta",[])
drinks.addChild(hot)
drinks.addChild(cold)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(fanta)
cold.addChild(soda)
print(drinks)
