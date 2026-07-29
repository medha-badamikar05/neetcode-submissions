class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 0;
        int prof = 0;
        while ( r < prices.length) {
            if (prices[r] > prices[l]) {
                prof = Math.max(prof, prices[r] - prices[l]);
            }
            else {
                l = r;
            }
            r++;
        }
        return prof;
    }
}
