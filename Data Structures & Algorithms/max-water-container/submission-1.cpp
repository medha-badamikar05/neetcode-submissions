class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int l = 0, r = n-1;
        int maxArea = 0;
        while(l < r) {
            int area = (r-l) * min(heights[l], heights[r]);
            cout<<"Area: "<<area<<endl;
            maxArea = max(maxArea, area);
            if(heights[l] < heights[r]){
                l++;
            }
            else {
                r--;
            }
        }
        return maxArea;
    }
};
