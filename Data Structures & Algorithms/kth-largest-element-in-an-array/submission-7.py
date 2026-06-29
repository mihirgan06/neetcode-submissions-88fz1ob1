class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
            Parition:
                nums = [7,2,5,1,9,4]
                say pivot = last leemnt = 4
                everything <= 4 | 4 | everything > 4
                following partition --> everything <= pivot is left,e verything right of pivot is > pivot
        '''
        target = len(nums) - k
        def partition(left, right):
            #p represents the first place where a numebr greater than the pivot currently lives

            pivot = nums[right]

            p = left
            for i in range(left, right):
                if nums[i] > pivot: 
                    continue
                elif nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            return p
        
        def quickselect(left, right):
            pivot_index = partition(left, right)
            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                #search right side
                return quickselect(pivot_index + 1, right)
            else:
                #search left side
                return quickselect(left, pivot_index - 1)
        return quickselect(0, len(nums) - 1)
            
            




        
        