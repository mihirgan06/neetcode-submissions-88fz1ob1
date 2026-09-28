class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            quickselect --> O(n) on average
            kth largest = index len(nums) - k in ascending order
        '''
        target = len(nums) - k


        def quickSelect(l, r):
            #start pivot at the right most element of the array
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)
        return quickSelect(0, len(nums) - 1)