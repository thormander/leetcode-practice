class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        # find the pairs
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1

        # handle impossible case
        if (xy+yx) % 2 != 0:
            return -1
        
        # handle counts

        # case of ex1, only have 1 swap per pair
        swapsXY = xy // 2
        swapsYX = yx // 2

        # case of ex2, where we have an xy/yx pair
        temp = 0
        if xy % 2 == 1 and yx % 2 == 1:
            temp = 2
        
        return swapsXY + swapsYX + temp





'''
we need to find how many pairs of
xy or yx we have

s1 = "xy" 
s2 = "yx"

if s1[0] = x then s2[0] is y --> pair

for yx same but opposite

IT MUST BE AT LEAST EVEN

when its impossible, we know the pairs will add up to being odd


'''
