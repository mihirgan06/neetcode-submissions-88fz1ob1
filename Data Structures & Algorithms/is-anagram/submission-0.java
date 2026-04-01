class Solution {
    public boolean isAnagram(String s, String t) {
        //given two strings s and t return true if two strings are anagrams otherwise false
        //anagram means two words use exactly the same letters just rearranged
        if(s.length() != t.length()){
            return false;
        }
        
        HashMap<Character, Integer> map = new HashMap<>();
        //stores how many times each character appears
        //count characters in s

        for(char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
            //tries to get the current value for key c
            // if c does NOT exist yet, it returns the default value 0
            //Adds 1 to the existing (or default) count
            //map.put updates or creates the entry for that cahracter in the map wiht a new value

        }
        for (char c : t.toCharArray()){
            if (!map.containsKey(c)){
                return false; //char in t not in s
            }
            map.put(c, map.get(c) - 1);
            if (map.get(c) < 0){
                return false; //more occurences in t than in s
            }
        }
        return true;






    }
}
