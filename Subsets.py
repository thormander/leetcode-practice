class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        lastIndex = len(nums) - 1

        def DFS(index):
            # base case
            if index > lastIndex:
                result.append(subset.copy())
                return
            
            # left (dec. to add)
            subset.append(nums[index])
            DFS(index+1)

            # right (dec. to not add)
            subset.pop()
            DFS(index+1)
        
        DFS(0)
        return result

'''
result =[]
subset = []

decision tree problem
[1,2,3]
X
|     \
1      []
|   \.  |. \
1,2  1.  2.  []

to do this --> DFS(index that we are on)

recursion:
    base case - if our index is out of range (more than 2 for the ex)
    return nothing, but we should have a valid subset to add to result

    go left (decision to add the number)

    go right (decision to not add number)


DFS on index 0
return our result
'''
