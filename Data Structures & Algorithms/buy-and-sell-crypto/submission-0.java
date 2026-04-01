class Solution {
    public int maxProfit(int[] prices) {

        int minPrice = Integer.MAX_VALUE; //start really high
        int maxProfit = 0; //no profit 
        for (int price : prices){
            if (price < minPrice){
                minPrice = price;
                }
            else if (price - minPrice > maxProfit){
                maxProfit = price - minPrice;
                }
            }
        return maxProfit;



            

        }
        
    }

