class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k #index we're looking for
        def quickSelect(l, r):
            #which portion of array we run quick select on
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    #pivot is just nums[r]
            nums[p], nums[r] = pivot, nums[p]
            
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)