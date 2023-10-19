class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        minS = 1
        maxS = 1

        for num in nums:
            # edge case for '0'
            if num == 0:
                minS = 1
                maxS = 1
                continue
            
            temp = maxS
            maxS = max(num, num * maxS, num * minS)
            minS = min(num, num * temp, num * minS)

            result = max(result,minS,maxS)
        
        return result


                
        '''
        as we go through subarrays, keep a running track of min and max (to account for when we have to multiply negatives)
            - handle case of '0', whwere we just set our trackers to 1 as 0 will mess up the tracker
        '''
