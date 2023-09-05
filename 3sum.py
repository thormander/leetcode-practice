class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue # skipping if same
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[left] + nums[right]

                if currentSum + num < 0:
                    left += 1
                elif currentSum + num > 0:
                    right -= 1
                else:
                    answer.append([num,nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
        
        return answer





        '''
        sort the array nlogn

        break this down to where on i, we solve j and k like 2 sum
            - where (j + k) + i == 0
        loop through numsSorted:
            get our i value
            skip if same as previous

            l,r pointers
            while l < r:
                increment if currentSum+i less than 0
                decrement if currentSum+i more than 0
                if == 0:
                    append to answer
                
        
        return answer

        '''
