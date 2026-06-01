# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        '''
            merge sort:
                Split in half everytime
                impleemnnt a seperate two pointer merge function
        '''
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    def mergeSortHelper(self, pairs, s, e):

        if (e - s + 1 <= 1):
            return pairs
            

        m = (s + e ) //  2 #round down with the division

        self.mergeSortHelper(pairs, s, m)

        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(s, m, e)
        return pairs
        

    def merge(self, s, m, e):
            #two pointers
            #first split arrays into left and right halves

        L = pairs[s: m + 1] #start to mid inclusive
        R = pairs[m + 1: e + 1] #mid + 1 to end inclusive

        i = 0 #pointer for the first array
        j = 0 #pointer for the second array
        k = s #ppinter for our main array post merge

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                    #alwasys move the left half first to keep it stabke
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1 #move our main pointer no matter waht bc we always move the main pointer

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1





        
        
