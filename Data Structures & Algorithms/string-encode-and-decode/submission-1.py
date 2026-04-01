class Solution:

    def encode(self, strs: List[str]) -> str:
        #take in a list of strings
        #return an encoded string
        #we also have to account for special characters, or if the string is empty
        parts = []
        for s in strs:
            
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        
        return "".join(parts)

        

            

    def decode(self, s: str) -> List[str]:
        #receives one LONG encoded string 
        #read length till #, this is the digits so the length
        #then move i after the # and read from i to i + L (to account for full length of the string)
        #append this string to the result array
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
            

            
