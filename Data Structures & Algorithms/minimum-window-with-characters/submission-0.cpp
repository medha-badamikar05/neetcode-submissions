class Solution {
public:
    string minWindow(string s, string t) {
        if(t.empty() || s.empty()){
            return "";
        }
        unordered_map<char, int> countWeHave;
        unordered_map<char, int> countWeNeed;

        for(int i=0;i<t.size();i++) {
            countWeNeed[t[i]]++;
        }
        int have = 0, need = countWeNeed.size();
        int res = INT_MAX;
        string substr = "";
        int subStart = 0, subEnd = 0;
        int l = 0;
        for(int r=0;r<s.size();r++) {
            if(countWeNeed.find(s[r]) != countWeNeed.end()){
                countWeHave[s[r]]++;
                if(countWeHave[s[r]] == countWeNeed[s[r]]) {
                    have += 1;
                }
            }
            
            while (have == need) {
                if((r - l + 1) < res) {
                    res = r - l + 1;
                    subStart = l;
                    subEnd = r;
                }
                if(countWeNeed.find(s[l]) != countWeNeed.end()){
                    countWeHave[s[l]]--;
                    if(countWeHave[s[l]] < countWeNeed[s[l]]) {
                        have -= 1;
                    } 
                }
                l++;
            }
        }
        return res == INT_MAX ? "" : s.substr(subStart, subEnd - subStart + 1);
     }
};
