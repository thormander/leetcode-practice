class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # check mid
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[left]: # left sorted section
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1  
            else: # right sorted section
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1






'''
find index of our target; otherwiser return -1 if its not there

logN -> binary search

 l           r
[4,5,6,7,0,1,2]   
       

figure out sections: left sorted section and right sorted section

if nums[mid] >= nums[l] --> left sorted section
else --> right sorted section
 

'''
