class Solution {
    public boolean hasDuplicate(int[] nums) {
        //given integer array nums
        //return true if any value appears more than once
        //otherwise false
        if(nums == null || nums.length == 0){
            return false;
        //edge case: empty array
        }
        int counter = 0;
        for (int i = 0; i < nums.length; i++){
            for(int j = 0; j < i; j++){
                if(nums[j] == nums[i]){
                    counter++;
                }
        
            }
        if (counter >= 1){
            return true;

        }

            
        }
        return false;
        
        
    }
}