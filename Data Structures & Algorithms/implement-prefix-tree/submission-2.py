class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class PrefixTree:
    '''
        prefix tree = tree data structure used to efficiently store and retreive keys in a set of strings

        given a list of strings as input

        ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

        insert(word) --> inserts the string word into the prefix tree
        search(word) --> returns true if the string word is in the prefix tree

                        false otherwise
        
        startsWith(string prefix) --> true if there is a previously inserted string word
        that has the prefix prefix, false otherwise


        aim for o(n) for all operations

        node for every character
        we store each prefix once

        within our constructor we store 2 attributes
        - children as a hashmap
        - we map each character to a treenode
        c: treenode

        we store a boolean called endofWord: True if end of word False if not
        - useful because app is an end of word, but its also only part of the path for apple
        Each node stores children as a hashmap and endofWord


        Constructor: root is an new TrieNode

        insert start curr at root
        - iterate throught he characters in word, if the character is not in the hashmap we create a new node for ch
        - move curr to the ch
        - marke endof word as true once we iterate all the characters in word


        


        

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

        