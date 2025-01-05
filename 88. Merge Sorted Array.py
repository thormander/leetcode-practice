class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = m + n - 1
        c = n - 1

        while c >= 0:
            if a >= 0 and nums2[c] <= nums1[a]:
               nums1[b] = nums1[a]
               a -= 1
               b -= 1
            else:
                nums1[b] = nums2[c]
                c -= 1
                b -= 1
                    




'''
3 pointers

[1,2,3,0,5,6]
     | |
[2,5,6]
 |


if no more a,
just assign b with c

if c > a:
    value at b == value at c
    c--
    b--
if a <= c:
    valuse at b == value at a
    a --
    b --



'''
