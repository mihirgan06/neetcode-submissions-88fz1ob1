class Solution {
    //Binary search
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while(low <= high){ //stop when low and high MEET
            int mid = (low + high) / 2; //we have the middle 
            if(target < nums[mid]){
                high = mid - 1; //it HAS to be in left half
            }
            else if(target > nums[mid]){
                low = mid + 1; //has to be in right half

            }
            else{
                return mid;
            }

        }
        return -1;
        
    }
}
