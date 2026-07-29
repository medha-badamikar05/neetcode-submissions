class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int l = 0;
        for(int r=0;r<prices.size();r++) {
            while(prices[l] > prices[r] && l < r) {
                l++;
            }
            int d = prices[r] - prices[l];
            profit = max(profit, d);
        }
        return profit;
    }
};
