class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            given an unsorted array of integers nums and integer k findKthLargest
            by kth largest element we mean the kth largest leement int he sorted order not the kth distinct element
            nums = [2,3,1,5,4], k = 2
            push into a heap

            then return the top of the array


            Quickselect approach:
            
        '''
        k = len(nums) - k
        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
            nums[p], nums[r] = nums[r], nums[p]
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                #found a Solution
                return nums[p]
        return quickSelect(0, len(nums) - 1)

        
            
        






        