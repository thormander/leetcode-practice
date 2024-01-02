class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        result = 0

        while left < right:
            # current area
            area = (right - left) * min(height[left],height[right])
            result = max(area,result)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return result

        

        '''
        area = (right index - left index) * min(height Left,height Right)

        2 pointers = start at ends where maximize length
            - how do we move our pointers?
            - move the pointer whose height is less

        keep a running variable for max height
        '''
