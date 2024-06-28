class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        maxArea = 0

        while left < right:
            currentArea = min(height[left],height[right]) * (right-left)

            # check if larger
            maxArea = max(currentArea,maxArea)

            if height[left] > height[right]:
                right -= 1
                continue
            elif height[left] < height[right]:
                left += 1
                continue
            else:
                left += 1
        return maxArea

'''
have a running max that we will return

2 pointers, now difficulty is determing how to increment and decrement our pointers

find area, which is we take the least between 2 lines and times by the indexes minus from each other

we increment left if the next is bigger, or the right if its bigger
 - otherwise just increment left

'''
