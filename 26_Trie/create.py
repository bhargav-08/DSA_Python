
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofString=False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertString(self,word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node==None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofString = True
        print('Successfully inserted!!')

    def searchString(self,word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node==None:
                return False
            current = node

        # if current.endofString:
        #     return True
        # else:
        #     return False
        return True if current.endofString else False


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endofString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endofString == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


t = Trie()
t.insertString("APP")
t.insertString("APPLE")
deleteString(t.root, "APP", 0)
print(t.searchString("APP"))