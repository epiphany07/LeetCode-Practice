class Solution {
    public int minimizeArrayValue(int[] nums) {
        if(nums.length==2){
            if(nums[0]>nums[1]){
                return nums[0];
            }else{
                return (nums[0]+nums[1]+1)/2;
            }
        }
        long s=0,ps=0;
        for(int i=0;i<nums.length;i++){
            ps+=nums[i];
            s=Math.max(s,(ps+i)/(i+1));
        }
        return (int)s;
        
    }
}