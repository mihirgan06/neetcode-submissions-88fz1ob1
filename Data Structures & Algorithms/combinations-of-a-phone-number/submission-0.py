class     Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
            Given string digits made up of 2-9 inclusive
            Possible digits = 2,3,4,5,6,7,8,9
            eacgh digit is mapped to sereis of characters
            - create manually mapping of digits to letters  
            - recurse on the map to create all possible mappings

            '''
        if not digits:
            return []
            
        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        path = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for ch in digitsToLetters[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
