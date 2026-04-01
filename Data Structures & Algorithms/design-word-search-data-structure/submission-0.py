class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    #insert and search


    def __init__(self):
        self.root = Node()
        

        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.endOfWord = True

        

    def search(self, word: str) -> bool:
        #Whenever we hit a dot we need to recurse in all directions --> DFS
        #j is the index, root is the node, we start dfs at the root
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                #ourcharacter as a . means there are 26 different paths
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)