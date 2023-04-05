class Solution {
    public int partitionString(String s) {
        int c=1,i=0;
        Set d = new HashSet();
        for(i =0;i<s.length();i++){
            if(d.contains(s.charAt(i))){
                c++;
                d.clear();
            }
            d.add(s.charAt(i));
        } 
        return c;       
    }
}