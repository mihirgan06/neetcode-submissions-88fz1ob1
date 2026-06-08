# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quicksortrec(pairs, 0, len(pairs) - 1)
        return pairs

    def quicksortrec(self, arr: List[Pair], s: int, e: int):
            # s and e = start and end
        if (e - s + 1 <= 1):
            return
        pivot = arr[e]
            #left pointer for left side

        left = s
        for i in range(s, e):
                #only perform swap with the left side if less than pivot
            if arr[i].key < pivot.key:

                temp = arr[left]
                    #reassign the left val
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        arr[e] = arr[left]
        arr[left] = pivot

        self.quicksortrec(arr, s, left - 1)
        self.quicksortrec(arr, left + 1, e)

                

        