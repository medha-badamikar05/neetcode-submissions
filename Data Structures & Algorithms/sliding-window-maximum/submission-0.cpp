class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        int l = 0;
        deque<int> q;

        for(int r=0;r<nums.size();r++) {
            while(!q.empty() && nums[q.back()] <= nums[r]) {
                q.pop_back();
            }
            q.push_back(r);
            if(!q.empty() && q.front() <= r - k) {
                q.pop_front();
            }
            
            if((r - l + 1) == k) {
                res.push_back(nums[q.front()]);
                l++;
            }
        }
        return res;
    }
};
