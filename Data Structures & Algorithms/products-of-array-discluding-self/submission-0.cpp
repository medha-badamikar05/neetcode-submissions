class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1;
        int n = nums.size();
        vector<int> result;
        for(int i = 0; i < n; i++) {
            if(i != 0) {
                int temp = nums[0];
                nums[0] = nums[i];
                nums[i] = temp;
            }
            for(int j = 1; j < n; j++){
                prod *= nums[j];
            }
            result.push_back(prod);
            prod=1;
        }
        return result;
    }
};
