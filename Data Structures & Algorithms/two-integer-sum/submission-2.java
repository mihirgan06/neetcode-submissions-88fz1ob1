class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        //we create a hashmap with the integer within nums and its index
        for(int i = 0; i < nums.length; i++){
            //we are looking at nums[i] and we know there is a number that must be added to it to get to target
            //That number is complement
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int[]{map.get(complement), i}; //return the two indices (complement, and the index)
            }
            map.put(nums[i], i);
        }
        return new int[]{};
        
    }
}
