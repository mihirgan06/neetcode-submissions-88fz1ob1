class Solution {
    /**
    Two strings s and t are isomorphic if the characters in s can be replaced to get t
    basically mapping one letter to another 
    Conditions:
    Need to have same amount of characters in s and t
    also have to have same counts for each letter in s and t


    Two Strings s and t are isomorphic if:
        Each char in s consistently maps to exactly one char in t
        AND every character in t maps back to exactly one char in s
        Mapping must be bijective 
        Lengths must match

    
    */
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()) return false;
        //Ensuring the lengths match
        HashMap<Character, Character> mapST = new HashMap<>();
        //MapST maps characters of s --> t
        HashMap<Character, Character> mapTS = new HashMap<>();
        //mapTS maps characters of t to s


        for(int i = 0; i < s.length(); i++){
            //use index to check pairs at matching positions
            char c1 = s.charAt(i);//current char from s
            char c2 = t.charAt(i); //from t
            //If we have seen c1 before:
            //c1 already mapped to something elsse
            //it would need to map the exact same character so returns false
            if (mapST.containsKey(c1)){
                if(mapST.get(c1) != c2){
                    return false;
                }
            }
            //new mapping is created
            else{
                mapST.put(c1, c2);
            }
            //check if weve seen c2 before in mapTS
            if (mapTS.containsKey(c2)) {
                if (mapTS.get(c2) != c1) {
                    return false;
                }
            }
            else{
                mapTS.put(c2, c1);
            }


        }
        return true;
        
        
    }
}
/*
Why two maps are necessary:
ensures no two s-chars map to exact same t-char
no two t-chars map to same s-char
*/