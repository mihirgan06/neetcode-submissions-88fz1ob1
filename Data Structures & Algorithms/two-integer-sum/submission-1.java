class Solution {
    public int[] twoSum(int[] nums, int target) {
        //given an array of integers nums and integer target, return the indices i and j thaat nums[i] and nums[j] == target

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(map.containsKey(complement)){
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i],i);

        }
        return new int[]{};

        
    }
}
