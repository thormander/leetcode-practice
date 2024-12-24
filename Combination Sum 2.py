class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []

        def backtrack(index, combo, total):
            # base cases
            if target == total:
                result.append(combo.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            # go left (add current number)
            combo.append(candidates[index])
            backtrack(index+1,combo,total+candidates[index])

            # go right (skip current number)
            combo.pop()
            # handle number skipping
            while index+1 < len(candidates) and candidates[index+1] == candidates[index]:
                index += 1
            backtrack(index+1,combo,total)
        
        backtrack(0,[],0)

        return result



'''
backtracking
    - sort original list

decision tree
    - left is we choose the current number
    - right is we skip the current number 
        *BUT, there could me multiples of these, so we need to skip any numbers that are same

backtrack (index, combo list, running total):
    - base cases
        if we reach target, add to result list
        if index is out of bounds
        if running total is > than target, we do not need to go down that path
    
    go left --> choose number on our current index
    go right --> skip number on our current index (also handle skipping any numbers of same value)
'''
        
