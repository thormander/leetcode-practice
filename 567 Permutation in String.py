class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 reference map
        mapS1 = {}
        for char in s1:
            if char not in mapS1:
                mapS1[char] = 1
            else:
                mapS1[char] += 1

        # s2 check map
        mapS2 = {}
        targetSize = len(s1)


        left = 0

        for right in range(len(s2)):
            # populate mapS2
            if s2[right] not in mapS2:
                mapS2[s2[right]] = 1
            else:
                mapS2[s2[right]] += 1
            
            # shifting left
            while (right - left + 1) > targetSize:
                # decrement AND remove if needed (if its 0) -- save on memory
                if mapS2[s2[left]] > 0:
                   mapS2[s2[left]] -= 1

                if mapS2[s2[left]] == 0:
                    del mapS2[s2[left]]

                
                left += 1
            
            if (right - left + 1) == targetSize and mapS1 == mapS2:
                return True

        return False






'''
char occurances for both s1 and s2
 - where s1 is our reference

substring that has exact occurances as s1
    return true

first, get our hashmap for s1 and fill it out (reference)

second, go through s2 using pionts
 - shift both if no similarities
 - keep left in position only when we are in s1
'''
