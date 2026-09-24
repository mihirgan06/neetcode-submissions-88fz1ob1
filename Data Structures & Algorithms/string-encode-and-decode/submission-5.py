class Solution:
    '''
        Design an algorithm to encode a list of strings into single strings
        the encoded string is then sent over the network and decoded back to orginal list of strings

        encode: 
        - iterate over lsit of strings and create a single string
        strs = ["Hello","World"]
        - "5#hello5#World"
        the delimiter serves as a seperator between the length and the actual word

        say our string is 12World
        how would we knwo diff between 5 and 12 we need the # between them
        decode:
        - iterate through the string
        - go until the delimiter and append to the array
        - skip forward past the length until the next delimiter

    '''

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #until the end of the string
        while i < len(s):
            #start j at i
            j = i
            while s[j] != "#":
                #move j forward until we hit a hashtag

                j += 1
            length = int(s[i:j]) #say length = 5 we move 5 characters forward
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res



            



