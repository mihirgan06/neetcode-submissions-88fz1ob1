class Solution:
    '''
    encode list of strings into strings
    decode back to the list of strings

    when we encode the list of strings into a string,
    We need to have the length of the strign because we could have random symbols
    We n eed a delimiter
    the delimiter might not be unique, so we go till the NUMBER because thats the len(string)


    '''

    def encode(self, strs: List[str]) -> str:

        res = ''
        delimiter = ','
        for word in strs:
            res += str(len(word)) + ',' + word
        #string will look like 5hello,5world,
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        #s = 5,hello5,world
        i = 0
        while i < len(s):
            j = i
            while s[j] != ",":
                j += 1
            #move j forward
            length = int(s[i:j])
            i = j + 1
            
            word = s[i:i+length]   
            
            res.append(word)
            i = i + length
        return res


