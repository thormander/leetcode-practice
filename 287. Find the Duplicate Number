class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. find the cycle
        slow = 0
        fast = 0

        while True:
            slow = nums[slow] # move 1 step
            fast = nums[nums[fast]] # move 2 steps

            if slow == fast:
                break
        
        # 2. find the start
        newSlow = 0

        while True:
            newSlow = nums[newSlow] # move 1
            slow = nums[slow] # move 1

            if slow == newSlow:
                break
        
        return newSlow


    
'''
O(1) space, no hashset

do sorting + binary search = O(nlogn) --> but we cant sort no modfiying

we want linear --> use a linked list
 - think of values in nums are where the node at index points at
 - so give nums = [1,3,4,2,2] nums[0] = node and 1 is what it points too

it can NEVER point at node 0 due to constraints

# 1. use slow and fast pointer to find cycle
    - we will later need the slow pointer location

# 2. intilize another slow pointer, and increment them both up until they intersect
    - this will be our result
'''
