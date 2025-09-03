class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 1

        if len(nums) < 2:
            return nums[-1]

        while left < len(nums):
            if nums[left-1] > nums[left]:
                return nums[left]
            
            left += 1

        return nums[0]


'''
figure out where its no longer ascending --> pivot

logn --> binary search 

How do we know if its the start of a sorted section?


-inf [3,4,5,1,2]
            |

[4,5,6,7,0,1,2]
         |

[11,13,15,17]
              |
    - there is no pivot

2 cases
    - we have pivot
    - no pivot
'''
