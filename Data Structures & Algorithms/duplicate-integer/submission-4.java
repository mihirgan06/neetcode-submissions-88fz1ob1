class Solution {
    public boolean hasDuplicate(int[] nums) {
        //Given an integer array nums --> return true if any value appears more than once, otherwise false

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
            //Loop through the array
            //Add it to the hashmap and count the number of times it appears
            map.put(num, map.getOrDefault(num, 0) + 1);
            //count the number of times it appears in the map
        }
        for (int value : map.values()){
            if(value > 1) return true;
            }
        return false;
        
        }

        
    }
