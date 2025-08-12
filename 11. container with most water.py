class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        result = -1

        while left < right:
            # get current area
            area = (min(height[left],height[right])) * (right - left)

            result = max(result,area)            
            # move the pointers
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1


        return result

'''
[1,8,6,2,5,4,8,3,7]
   |            
                 |

1. area of 8
2. area of 49
...


calc the current area
    - (take the lowest height of the 2) * (right - left pointer)

how to move pointers?
    - take the smaller height of the 2, and shift that one

compare to the result, and check if current area we have is bigger
'''
