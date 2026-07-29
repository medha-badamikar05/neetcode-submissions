#include<algorithm>
class Solution {
public:
    int findMaxFreq(map<char, int> freq) {
        auto it = max_element(freq.begin(), freq.end(), [](const auto& a, const auto& b) {return a.second < b.second;});
        return it->second;
    }
    int characterReplacement(string s, int k) {
        map<char, int> freq;
        int maxLength = 0;

        int l=0, r=0;
        while(l <= r && r < s.size()) {
            freq[s[r]]++;
            int maxFreq = findMaxFreq(freq);
            int subStringLen = r - l + 1;
            if(subStringLen - maxFreq > k) {
                freq[s[l]]--;
                l++;
            }
            maxLength = max(maxLength, (r - l + 1));
            r++;
        }

        return maxLength;
    }
};
