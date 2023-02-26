class Solution {
    public String interpret(String c) {
        while(c.contains("(")==true){
            c=c.replace("()","o");
            c=c.replace("(al)","al");
            
        }
        return c;
        
    }
}