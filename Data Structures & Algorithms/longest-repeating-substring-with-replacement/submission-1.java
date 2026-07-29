class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        int l = 0;
        for (int r=0;r<s.length();r++) {
            HashMap<Character, Integer> count = new HashMap<>();
            int maxFreq = 0;
            for(int x=r;x<s.length();x++) {
                count.put(s.charAt(x), count.getOrDefault(s.charAt(x), 0) + 1);

                maxFreq = Math.max(maxFreq, count.get(s.charAt(x)));
                if ((x - r + 1) - maxFreq <= k) {
                    res = Math.max(res, (x - r + 1));
                }
            }
        }
        return res;
    }
}
