class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0

        left = 0
        right = 0

        while right < len(nums) - 1:
            largest = 0
            # greedy
            for i in range(left,right+1):
                largest = max(largest,i + nums[i])
            
            # update pointers
            left = right + 1
            right = largest

            result += 1 # up one layer
        
        return result

        '''
        greedy, 'layer-like' - BFS (track where we can jump to almost like a sliding window)
        2 pointers
        largest variable -> track farthest we can jump within layer (current index + the value)
            - set our right pointer to this
        '''
