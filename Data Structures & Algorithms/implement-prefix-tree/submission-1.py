class TrieNode:
    def __init__(self):
        self.children = {} #use a hashmap for ease of access with the next node
        ''' 
            If we wanna insert cat, first check for c, if c doesnt exist create it
            then a then t
            after the final letter we can change isWord to be true
        '''
        self.isWord = False
        #start this at false so we can change to true if we do end up finding the word
        
class PrefixTree:


    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True
        


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

        
        