class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            Quickselect algorithm for kth largest elem in array


            given an unsorted array of integers nums, and an integer k return the kth largest elemnet in array

        '''
        #k elements fromt je largest elemnt
        target = len(nums) - k

        l = 0
        r = len(nums) - 1
        while True:
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]

            if i == target:
                return nums[i]
            elif i < target:
                l = i + 1
            else:
                r = i - 1
        