class Solution {
    public int addMinimum(String word) {
        int i = 0, res = 0;
        while (i < word.length()) {
            if (i >= word.length() || word.charAt(i) != 'a') {
                res++;
            } else {
                i++;
            }
            if (i >= word.length() || word.charAt(i) != 'b') {
                res++;
            } else {
                i++;
            }
            if (i >= word.length() || word.charAt(i) != 'c') {
                res++;
            } else {
                i++;
            }
        }
        return res;
    }
}