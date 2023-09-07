class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


    


        '''
        cycles --> slow,fast pointer

        node value point at its own value/index: will give us a cycle we can detect

        start of the cycle (ie where both the duplicate values point at), is the num/index we       return:
            determine start by re running another slow pointer at the head, and start up the other

            then where slow1 = slow2 is the answer

        Why does nums[slow] work?
            think of it as a linked list...essentially pointing to the node/value of the index
    
        '''
