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
        curr = self.root
        for ch in word:
            if ch not in curr.children and ch != '.':
                return False
                #we automatically reject this bc its clearly not a word in our trie
            
            elif ch in curr.children or ch == '.':
                return True
        return curr.isWord

        
