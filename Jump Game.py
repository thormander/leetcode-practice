class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach_end = len(nums) - 1

        # iterate in reverse
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= can_reach_end:
                # we know it is reachable
                can_reach_end = i
        
        return can_reach_end == 0

'''
greedy approach

take steps needed to reach the next biggest index
 - within current range

But if we do in reverse,

[2,3,1,1,4]
 |

pointer is what we want reach

lets iterate in reverse:
    can we reach the pointer from our index?

    if i reaches index 0, we know the end is reachable --> return True
'''
