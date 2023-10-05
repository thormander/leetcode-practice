class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def DFS(pointer, current, cur_sum): # current is a list
            # base cases
            if cur_sum == target:
                result.append(current.copy())
                return
            if (pointer >= len(candidates)) or (cur_sum > target):
                return

            # left side where we do not ignore and take pointer value
            current.append(candidates[pointer])
            DFS(pointer,current,cur_sum + candidates[pointer])  
            current.pop()

            # right side where we ignore whatever pointer was on
            DFS(pointer + 1,current,cur_sum)
        
        DFS(0,[],0)
        return result


        '''
        decision tree
            - have to ignore when looking at different values
            - such as when we pick 2, ignore it for the right side
            - left side will have 2 and we can restart the idea
        '''
