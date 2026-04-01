class TrieNode:
    #First step we need to create a Node object
    def __init__(self):
        self.children = {}
        self.endOfWord = False



class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        #initialize cur pointer at the root
        for char in word:
            #move char through the word and search for each character in the trie
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char] 
            #We have processed all characters, so we are now at the node representing the end of the word

        cur.endOfWord = True




    def search(self, word: str) -> bool:

        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        #does any word in the trie start with this prefix
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        #loops through whole prefix, if the loop finishes then we know that the prefix is valid
        return True