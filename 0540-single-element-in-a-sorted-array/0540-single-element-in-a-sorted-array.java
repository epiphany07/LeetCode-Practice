class Solution {
    public int singleNonDuplicate(int[] nums) {
        int i=0;
        for( i=1;i<nums.length;i=i+2){
            if (nums[i]!=nums[i-1]){
                break;
            }
        }
        return nums[i-1];
    }
}