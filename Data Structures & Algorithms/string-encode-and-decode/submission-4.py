class Solution:
    '''
        design an alg to encode a list of strings to a string
        encoded string iss ent over the network and is decoded back to original list
        strs = ["Hello","World"]
        ["Hello","World"]

        use a delimiter
        lenstring then delimiter then len string 

        len(string) say is 4 then take the next 4 letters for encode

        5hello#4butt#
    '''

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))
            encoded_string += '#'
            encoded_string += word
            

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[j + 1: j+1 + length]
            res.append(word)
            i = i + length
        return res
            
                
        
            
