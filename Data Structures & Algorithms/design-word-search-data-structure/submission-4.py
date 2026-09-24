class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False
class WordDictionary:

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
        '''
            we cant do traditional iterative search due to the period condition

        '''
        def dfs(i, node):
            if i == len(word):
                return node.endofWord
            

            ch = word[i]


            if ch != "." and ch not in node.children:
                return False
            
            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            return dfs(i + 1, node.children[ch])
        return dfs(0, self.root)




        


        
