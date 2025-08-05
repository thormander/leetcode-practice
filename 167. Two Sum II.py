class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                # need to decrease sum
                right -= 1
            elif current_sum < target:
                # need to increase sum
                left += 1
            else:
                return [left+1,right+1] 

'''
2 pointers
    - one at both ends

[2,7,11,15], target = 9
 |
   |

sum @ the 2 pointers
    if sum > target
        decrease the right pointer (this shrinks our sum)
    if sum < target
        increase left pointer (this will incresase our suim)
    we get teh answer
'''
