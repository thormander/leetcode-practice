class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(current, pos, target):
            # base case
            if target == 0:
                result.append(current.copy())
            if target <= 0:
                return
        
            previous = -1
            for i in range(pos,len(candidates)):
                # check for duplicate numbers
                if previous == candidates[i]:
                    continue

                current.append(candidates[i])
                backtrack(current, i + 1, target - candidates[i])
                current.pop()

                previous = candidates[i]
            
        backtrack([],0,target)
        return result
            


