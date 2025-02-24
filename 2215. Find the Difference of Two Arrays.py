class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashset1 = set() # store distinct nums in 1
        hashset2 = set() # store distinct nums in 2

        # fill hashsets
        for num in nums1:
            if num not in hashset1:
                hashset1.add(num)
        

        for num in nums2:
            if num not in hashset2:
                hashset2.add(num) 

        result = [[],[]]

        def helper(nums,hashset,i):
            hashset_ans = set()
            for num in nums:
                if num not in hashset_ans and num not in hashset:
                    result[i].append(num)
                    hashset_ans.add(num)
        
        # left result
        helper(nums1,hashset2,0)

        #right result
        helper(nums2,hashset1,1)
        
        return result



'''
like a left + right join

set for both 1 and 2

check 2 against 1, and vice versa
'''
