import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbers = new HashSet<>();
        for(int num : nums) {
            if(!numbers.add(num)) {
                return true;
            }
        }
        return false;
    }
}