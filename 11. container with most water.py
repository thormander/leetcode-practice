class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        result = 0

        while left < right:
            # find area
            area = (right-left) * min(height[left],height[right])
            result = max(area,result)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return result



'''
find max water

2 poitners, start and end
    - maximize potential area


increment/decremetn the smaller bar
'''
