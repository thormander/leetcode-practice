class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        while k > 0:
            num_rotated = nums.pop()
            nums.insert(0,num_rotated)
            k -= 1



'''
pop from end, and insert at beggining up to k times

we dont need additonal array

O(1) space adhered ; in place
'''
