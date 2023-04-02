class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int i=0,j=0;
        int ar[]=new int[spells.length];
        
        int p=potions.length;
        
        Arrays.sort(potions);
        
        for(i=0;i<spells.length;i++){
            
               
           
            
            long min = (long) Math.ceil((1.0 * success) / spells[i]);
            // System.out.print(min);
             if(min>potions[p-1]){
                ar[i]=0;
                continue;
            }
            
            int lo=0,hi=p;
            
            while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (potions[mid] < (int)min) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
            // System.out.println(lo);

            // for(j=0;j<potions.length;j++){
            //     // potions[j]=spells[i];
            //     int x=potions[j]*spells[i];
            //     if(x>=success){
            //         c=j;
            //         break;
            //     }  
            // }
           
            ar[i]=p-lo;
        }
        return ar;
        
    }
}