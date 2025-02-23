class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0 # s
        p2 = 0 # t

        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        if p1 >= len(s):
            return True
        else:
            return False
'''
pointers

one one s and t
increment t until s == t,
    if it is, then increment s and check next char
'''
