class Solution {
    /*
    Given two strings s and t, return true if the two strings are anagrams, false otherwise
    To be an anagram:
        String contains same nu
    */
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap<Character, Integer> map = new HashMap<>();
        //Counts number of occurences of each character
        for(char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
            //Tries to get the current value for key c
            //If c does not exist yet, it returns the default value
            //Adds 1 to the existing or default value
            //map.put updates or creates the entry for the character with a new value

        }
        for(char c : t.toCharArray()){
            if(!map.containsKey(c)){
                return false;
            }
            map.put(c, map.get(c) - 1);
            if(map.get(c) < 0){
                return false;
            }
        }
        return true;


    }
}
