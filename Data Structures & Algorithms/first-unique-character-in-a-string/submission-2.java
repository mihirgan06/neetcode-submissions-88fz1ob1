class Solution {
    public int firstUniqChar(String s) {
        //Given a string s, find first non-repeating character and return its index
        HashMap<Character, Integer> map = new HashMap<>();
        //count number of times character appears
        for (char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
            //we now have a hashmap that stores the number of times each character in a string appears
            //we want to return the first cahracter that deosnt repeat
            //We can iterate through the map and return the first character that doesn
        }
        for(int i = 0; i < s.length(); i++){
            if(map.get(s.charAt(i)) == 1){
                return i;

            }

            
        }
        return -1; 
        
    }
}