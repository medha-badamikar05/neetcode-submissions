class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        unordered_map<char, int> c1, c2;
        for (char c : s1) c1[c]++;

        int have = 0;
        int need = c1.size();
        int l = 0, k = s1.size();

        for (int r = 0; r < s2.size(); r++) {

            // INVALID CHARACTER → RESET WINDOW
            if (!c1.count(s2[r])) {
                c2.clear();
                have = 0;
                l = r + 1;
                continue;
            }

            c2[s2[r]]++;
            if (c2[s2[r]] == c1[s2[r]]) have++;

            if (r - l + 1 == k) {
                if (have == need) return true;

                if (c2[s2[l]] == c1[s2[l]]) have--;
                c2[s2[l]]--;
                l++;
            }
        }
        return false;
    }
};
