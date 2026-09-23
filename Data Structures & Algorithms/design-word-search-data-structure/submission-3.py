class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class WordDictionary:
    '''
        design a data structure that supports adding new words
        and searchign for existing words
        addWord --> adds word to the data structure
        search(word) --> tru if any string that matches word false otehrwise

        the variation 
        '.' means any character

        so basically, we would folloow the path similarly, but the . is variable to be anything that works
    '''

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endofWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.endofWord
            ch = word[i]
            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(i + 1, node.children[ch])
        return dfs(0, self.root)


        
        
