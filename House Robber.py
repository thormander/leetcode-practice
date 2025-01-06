class Solution:
    def rob(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0

        for house in nums:
            most_money = max(p1 + house,p2)
            p1 = p2
            p2 = most_money
        
        return p2



'''
[1,2,3,1]
 | |

[p1, p2, n (current house we are on) , n+1, n+2, ...]

'''
