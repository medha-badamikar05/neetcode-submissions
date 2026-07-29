class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int longest = 0;
        set<char> eliminate;

        for(int r=0;r<s.length();r++) {
            while(eliminate.find(s[r]) != eliminate.end()) {
                eliminate.erase(s[l]);
                l++;
            }
            eliminate.insert(s[r]);
            longest = max(longest, r-l+1);
        }
        return longest;
    }
};
