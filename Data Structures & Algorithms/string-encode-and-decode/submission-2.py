class Solution:
    '''
        Design an alg to encode a list of strings to a string

        Decode back to the original list of strings
    '''

    def encode(self, strs: List[str]) -> str:
        #we take the list string and turn it to a single string
        result = []
        for i, word in enumerate(strs):
            result.append(str(len(word)) + "#" + word)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        #we want to loop through the list until we see the # delimiter
        
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result

            

