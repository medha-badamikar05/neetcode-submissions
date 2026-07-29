class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> closeToOpen;
        closeToOpen.insert(pair<char, char>(')','('));
        closeToOpen.insert(pair<char, char>('}','{'));
        closeToOpen.insert(pair<char, char>(']','['));
        for(auto c:s) {
            if(closeToOpen.find(c) != closeToOpen.end()) {
                if(!stk.empty() && stk.top() == closeToOpen[c]) {
                    stk.pop();
                }
                else {
                    return false;
                }
            }
            else {
                stk.push(c);
            }
        }
        if(stk.empty()) {
            return true;
        }
        return false;
    }
};
