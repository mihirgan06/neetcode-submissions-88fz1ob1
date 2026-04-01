class Solution {
    public boolean isAnagram(String s, String t) {
        //given 2 strings s and t, return true if the strings are naagrams

        //to be an anagram:
            //stirng contains same NUMBER of characters
            //String contains same characters

        //first check if the strings are the same length
        //first condition easily checked
        if(s.length() != t.length()){
            return false;
        }
        //we can count the number of characters in s first
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c : s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
            //counts the number of each letter in s
        }
        for(char ch : t.toCharArray()){
            map.put(ch, map.getOrDefault(ch, 0) - 1);
            //subtract the character counts from the map
        }
        for(int value : map.values()){
            if(value < 0 || value > 1){
                return false;
            }
        }
        return true;



    }
}
