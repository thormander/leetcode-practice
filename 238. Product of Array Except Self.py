class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        result = [1] * len(nums)

        # first pass
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]

        # second pass (reverse)
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]

        return result

'''
1 [1,2,4,6]
     |

[1,1,2,8]

hold = 48

now in reverse

hold = 24

[48,24,12,8]
    |
'''
