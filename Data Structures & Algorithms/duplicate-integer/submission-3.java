class Solution {
    /**
    Given an array nums return true if any value appears more than once in the array
    Otherwise return false
    */
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                return true;
            }
            map.put(nums[i], true);
        }
        return false;
        
    }
}