class Solution {
public:
    int trap(vector<int>& height) {
        int lheight = 0, rheight = 0;
        int maxWaterTrapped = 0;
        int n = height.size();
        // Just traverse array and determine highest and lowest left and right pointers
        vector<int> maxLeft(height.size(), 0);
        vector<int> maxRight(height.size(), 0);
    
        for(int i=1;i<height.size();i++) {
            maxLeft[i] = max(maxLeft[i-1], height[i-1]);
        }
        for(int i=n-2;i>=0;i--) {
            maxRight[i] = max(maxRight[i+1], height[i+1]);
        }

        for(int i=0;i<n;i++) {
            cout<<"MAX LEFT: "<<maxLeft[i]<<endl;
        }
        for(int i=0;i<height.size();i++) {
            int trapped = min(maxLeft[i], maxRight[i]) - height[i];
            if(trapped < 0) {
                trapped = 0;
            }
            maxWaterTrapped += trapped;
        }
        return maxWaterTrapped;
    }
};
