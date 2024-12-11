class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def DFS(index,combos,total):
            # base cases
            if total == target:
                result.append(combos.copy())
                return
            
            if total > target or index > (len(candidates) - 1):
                return
            
            # go left (add current number)
            combos.append(candidates[index])
            DFS(index,combos,total + candidates[index])

            # go right (skip current number, and increment)
            combos.pop() # return back to original state (ie. skip)
            DFS(index+1,combos,total)
        
        DFS(0,[],0)

        return result


'''
need a pointer on the list, we increment it anytime we go right

decision tree:
    if we go left --> add number on current index
    if we go right --> increment index, b/c we cannot have duplicates

X
|     \ +1 the index
2.    []
|.   \ +1 index
2,2.  2
      |. \
     2,3. 2

use a DFS(index, combos, total):
    base cases:
        is the total = target?
        is total > target or is the index valid?

    we go left --> keep index same

    we go right --> do not add the current index, increment index

'''
