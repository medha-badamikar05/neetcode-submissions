class Solution {
public:
    int maxArea(vector<int>& heights) {
        int start = 0;
        int end = heights.size() - 1;
        int maxArea = -1;
        while(start < end) {
            int area = calcArea((end-start), min(heights[start], heights[end]));
            maxArea = max(area, maxArea);
            int wall = min(heights[start], heights[end]);
            while(heights[start] <=  wall && start < end) {
                start++;
            }
            area = calcArea((end-start), min(heights[start], heights[end]));
            maxArea = max(area, maxArea);
            while(heights[end] <=  wall && end > start) {
                end--;
            }
            
        }
        return maxArea;
    }
private:
    int calcArea(int ln, int br) {
        return ln*br;
    }
};
