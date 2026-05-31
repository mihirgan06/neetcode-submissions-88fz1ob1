class TreeNode:
    def __init__(self):
        self.children = {}
        #map to use to find next node quick
        self.isWord = False #initialize boolean for the word existing as false
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        #initialize root
        

    def addWord(self, word: str) -> None:
        #if the word isnt in the map add word
        #if the word is already in map just return nothing
        curr = self.root
        for ch in word:
            
            if ch not in curr.children:
                curr.children[ch] = TreeNode()
            curr = curr.children[ch]

    
        curr.isWord = True

    def search(self, word: str) -> bool:
        #follow path
        #if we hit a . it can be any letter
        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):
                ch = word[i]

                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]

            return curr.isWord

        return dfs(0, self.root)

        
