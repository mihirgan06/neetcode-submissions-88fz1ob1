class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            Given array of integers nums, and an integer k
            Sliding window of size k --> Fixed
            starts at left edge, slides one position right until it reaches the right edge

            EX:
                nums = [1,2,1,0,4,2,6] k = 3
                First window: [1,2,1] --> max = 2 --> append to res
                second window [2,1,0] --> max = 2 --> append to res
                third window [1,0,4] --> max = 4 --> append to res
                fourth window [0,4,2] --> max = 4 --> append ot res
                fifth window [4,2,6] --> max = 6 --> append to res


                Final window --> terminate loop and return res
            O(Nlogn)

            Brute Force Intuition O(N^2) --> each index you compute a max:
                Start a window of fixed size k at the leftmost index
                Get max 
                Move that fixed iwndow forward by 1 
                get max 
                append to res
                return res
            '''
        res = []
        #bug 1: its working for every window except the initial

        for l in range(len(nums) - k + 1):
                #iterate through while a valid window can be started
                #create a cur max at the first index well reset this later
            real_max = nums[l]
            for i in range(l, l + k):
                 #max from the window
                real_max = max(real_max, nums[i])
            res.append(real_max)
        return res

            

        