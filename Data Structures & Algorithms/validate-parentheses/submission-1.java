class Solution {
    public boolean isValid(String s) {
        /*
        given a string s consisting of different parentheses
        input string s is only valud if each open bracket is closed by same type of close bracket
        String s contains 3 pairs of parentheses
        
        
        
        We cannot start with a CLOSING parentheses
        We must start with an open parentheses of any kind
        After this, we can add as many as we want as long as we eventually close them */

        
        Stack<Character> stack = new Stack<>();
        for(char ch: s.toCharArray()){
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
        } 
        else{
            if (stack.isEmpty()){
                return false;
            }
            if (ch == ')' || ch == ']' || ch == '}') {
                char top = stack.pop();
                if ((ch == ')' && top != '(') ||
                    (ch == ']' && top != '[') ||
                    (ch == '}' && top != '{')) {
                    return false;
                }
            }

        } 
        }
        return stack.isEmpty();
}
}