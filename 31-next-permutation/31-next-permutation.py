class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = n - 2
        while k >= 0:
            if arr[k] < arr[k + 1]:
                break
            k -= 1
        if k < 0:
            print(1)
            arr = arr.reverse()
        else:
            for l in range(n - 1, k, -1):
                if arr[l] > arr[k]:
                    break    
            arr[l], arr[k] = arr[k], arr[l]
            arr[k + 1:] = reversed(arr[k + 1:])
            
            
            
#         t=int("".join(map(str,nums)))
#         print(t)
#         n=len(nums)
#         k=n-2
#         while k>=0:
#             if nums[k]<nums[k+1]:
#                 break
#             k-=1
#         if k<0:
#             nums=nums[::-1]
#         else:
#             for l in range(n - 1, k, -1):
#                 if nums[l] > nums[k]:
#                     break
 
#         # swap the elements at arr[k] and arr[l     
#             nums[l], nums[k] = nums[k], nums[l]
        
#             nums[k+1:]=reversed(nums[k+1:])