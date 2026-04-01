class Solution {
    /**
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j such that
    nums[i] == nums[j] and abs(i - j) <=k */
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                int prevIndex = map.get(nums[i]);
                if (i - prevIndex <= k) return true;
            }
            map.put(nums[i], i);



        }
        return false;

        
    }
}
/** Logic Breakdown
Is there a number that appears twice within distance k in an array
Loop through array with index i (index needed due to distance)
if weve seen nums[i] before --> true get prev index 
*/