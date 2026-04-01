class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //Two parts
        //First check whetehr two strings within the list (given) is an anagram
            //Same amount of letters
            //Same letters

        //Create a hashmap for characters and frequency
        HashMap<String, List<String>> map = new HashMap<>();
        
        for(int i = 0; i < strs.length; i++){
            int[] count = new int[26];
            
            for(char ch : strs[i].toCharArray()){
                count[ch - 'a']++; //convert the entire string into ascii
                
            }
            String key = Arrays.toString(count);
            // map.put(.f.hh.)
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(strs[i]);
        }
        return new ArrayList<>(map.values());
        

        
        
    }
}
