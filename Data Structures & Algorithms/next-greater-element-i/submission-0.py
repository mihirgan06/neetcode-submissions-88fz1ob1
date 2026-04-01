class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #first element greater than x to the right of x
        #given 2 0-indexed integer arrays: nums1 and nums22
            #nums1 is a subset of nums2
        
        nextGreater = {num : i for i, num in enumerate(nums1)}
        stack = [] #this will hold values
        result = [-1] * len(nums1)


        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nextGreater[val]
                result[idx] = cur
            if cur in nextGreater:
                stack.append(cur)
        
        return result



