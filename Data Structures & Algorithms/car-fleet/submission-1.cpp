class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> pairs;
        vector<double> st;
        for(int i=0;i<position.size();i++) {
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.rbegin(), pairs.rend());
        for(auto &p : pairs) {
            st.push_back((double)(target - p.first)/p.second);
            if(st.size() >= 2 && st[st.size() - 1] <= st[st.size() - 2]) {
                st.pop_back();
            }
        }
        return st.size();
    }
};
