class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit=0;
        int minstock=prices[0];
        for(int i=0;i<prices.length;i++){
            int m=prices[i]-minstock;
            if(m>maxprofit){
                maxprofit=m;
            }
            if(minstock>prices[i]){
                minstock=prices[i];
            }
        }
        return maxprofit;
    }
}