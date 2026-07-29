class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
         vector<int> twoSum;
        int first = 0;
        int last = numbers.size() - 1;
        while(first < last) {
            int sum = numbers[first] + numbers[last];
            if(sum == target) {
                twoSum.push_back(first+1);
                twoSum.push_back(last+1);
                return twoSum;
            }
            if(sum < target) {
                first++;
            }
            if(sum > target) {
                last--;
            }
        }
        return twoSum;
    }
};
