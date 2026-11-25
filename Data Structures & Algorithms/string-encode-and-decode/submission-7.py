class Solution:
    '''
        Design an algorithm to encode a list of strings to a string
        encoded string is sent over network and decoded back to roginal list of strings
        encode takes the list of strings and converts it into a single string
        strs = ["Hello","World"]

        HelloWorld
        word then delimiter
        we need the ength of string incase and the delimiter we can do:
        length of string then delimiter then word itself

        for decode we just want the strings appended to an array
        we have 5#Hello
        we want to start right after the delimiter until the length variable which is right before the next delimiter


    '''

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word)) + '#' + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[i: i + length]
            res.append(word)
            i = i + length
        return res
        




        


