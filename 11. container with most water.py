class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        most_water = 0

        while left < right:
            # calc amountof water b/t pointers
            heightContainer = min(height[left],height[right])
            lengthContainer = right - left

            area = heightContainer * lengthContainer

            # compare with running max
            most_water = max(most_water,area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
        
        return most_water


'''
2 pointers

running max area

[1,8,6,2,5,4,8,3,7]
   |             | 

increment left if smaller than right height
otheriwse decrement right
'''
