class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        result = float('inf')

        while left <= right:
            if nums[left] < nums[right]:
                # if section sorted ( no pivot in section)
                result = min(nums[left],result)
                break

            mid = (right+left) // 2
            result = min(nums[mid],result)

            if nums[mid] >= nums[left]:
                # inside left sorted section
                left = mid + 1
            else:
                # inside right sorted section
                right = mid - 1
        
        return result


'''
figure out where its no longer ascending --> pivot

logn --> binary search 

How do we know if its the start of a sorted section?
    - we dont need to know if we are at teh start of a sorted section


    [3,4,5,1,2]
     |
             |

result = 5 (just compare and take smaller)
mid = 5


if middle >= left:
    middle is inside the left sorted section
    want to search the section to the right

    push left pointer to middle++

else:
    search left section
    



'''
