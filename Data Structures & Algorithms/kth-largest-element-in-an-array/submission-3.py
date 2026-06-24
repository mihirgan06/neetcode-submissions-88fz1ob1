import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        #once we ue quickselect, the largest element iwll be the rightmost elemnt so subtract k from that for the kth largest element
        #find target somewhere inside nums[left, right + 1]
        def quickselect(left, right):
            #random pivot index
            pivot_idx = random.randint(left, right)
            #move the pivot to the end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            #store the pivot value
            pivot = nums[right]
            p = left
            #left...p - 1 = values <= pivot, p..i - 1 val > pivot, i... right - 1 = unknown
            
            for i in range(left, right):
                #if curr number < pivot its on the left side
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            #after this step everything left of pivot is less than or equal to pivot
            #nums[p...right] are > pivot
            #nums[right] is pivot
            #if the pivot is the target we return that element
            if p == target:
                return nums[p]
            
            elif p < target:
                return quickselect(p + 1, right)
            else:
                return quickselect(left, p - 1)

        return quickselect(0, len(nums) - 1)


        