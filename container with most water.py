class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        left = 0
        right = len(height) - 1

        while left < right:
            currentArea = (right-left) * min(height[right],height[left])

            answer = max(currentArea,answer)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return answer


        '''
        2 pointers, left and right on both ends
        maxArea variable

        while l<r:
            currentArea = (r-l) * min(of their heights)
            increment left if height[left] smaller than height[right]
            decrement right if its height is smaller 
            if equal, just increment one or the other

        return maxArea
        '''
        
