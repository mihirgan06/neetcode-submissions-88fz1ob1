class Solution {
    /**
    given an array of strings, group all anagrams into sublists
    Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    */
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String, List<String>> map = new HashMap<>();
        //key = the sorted word (String) 
        //Value = the list of all original words that match (List<String>)
        for(String word : strs){
            //iterate through array of strings
            //create a new char array of chars where we convert the word into a character array
            char[] chars = word.toCharArray();
            Arrays.sort(chars); //sort the chars alphabetically
            String key = new String(chars); //sorted version

            //if the key is not in the map --> create an empty list
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(word);
            //adds the original word to the hashmap




        }
        return new ArrayList<>(map.values());
        
        
    }
}
