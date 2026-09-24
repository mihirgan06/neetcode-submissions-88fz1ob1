class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class PrefixTree:
    '''
        Node class has a hashmap for children 
        - insert word into the prefix PrefixTree
        - search: returns true if the string word is in the prefix PrefixTree
        - startsWith(string prefix) true if there is prev inserted word with the prefix

    '''

    def __init__(self):
        self.root = TrieNode()


        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endofWord = True





    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.endofWord

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
        