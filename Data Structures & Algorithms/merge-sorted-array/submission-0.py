class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Given:
        2 integer arrays, nums1, nums2 along with 2 integers m = number of valid elements in nums 1
        n = number of elements in nums2

        Your task is to merge the final array so its sorted in non-dec order


        you can have 2
        one for nums1
        one for nums2
        were merging into nums1
        Brute Force:
        start a new array
        start at beginning of each of array take the smaller element insert into new array
        and keep doing that till we finish our new array
        Problem is we need that temporary array


        we know theres empty space at the right side
        initalize a poiinter at the last value of nums[1]
        compare the two values between the last real number in nums1 and nums2






        """
        #last index of nums1

        last = m + n - 1
        #merge in reverse order

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


        


        

        