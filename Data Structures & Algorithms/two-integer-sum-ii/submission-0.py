class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 pointer approach

        left = 0

        right = len(numbers) - 1

        while left < right:
            target_sum = numbers[left] + numbers[right]
            if target_sum == target:
                return [left + 1, right + 1]
            
            if target_sum < target:
                #SUM < target we need to increase sum
                #since its a non-dec integer array, moving left to the right would increase sun
                left += 1
                #move left forward
            
            if target_sum > target:
                right -= 1
        return [left + 1, right + 1]
        
        
            

        