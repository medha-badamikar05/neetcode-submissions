class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty()) return "";

        StringBuilder res = new StringBuilder();
        List<Integer> sizes = new ArrayList<>();

        for( String str: strs) {
            res.append(str.length());
            res.append("#");
            res.append(str);
        }

        return res.toString();
    }

    public List<String> decode(String str) {
        if (str.length() == 0) return new ArrayList<>();
        List<String> res = new ArrayList<>();
        int i=0;
        while(i<str.length()) {
            int delimiterIndex = str.indexOf('#', i);
            int size = Integer.valueOf(str.substring(i, delimiterIndex));

            int begin = delimiterIndex + 1;
            int end = begin + size;
            
            res.add(str.substring(begin, end));
            i = end;
        }
        return res;
    }
}
