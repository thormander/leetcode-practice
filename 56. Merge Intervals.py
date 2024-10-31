class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        # sort based on first value
        intervals.sort(key=lambda x: x[0])

        # start the merge logic
        for interval in intervals:
            # base case
            if not result:
                result.append(interval)
            else:
                # case where can merge
                if result[-1][1] >= interval[0]:
                    # we can update/merge
                    result[-1][1] = max(result[-1][1],interval[1])
                else:
                    # we cant merge
                    result.append(interval)

        return result
        
    '''
    sort it first (based on first value of the list)

    result list

    loop through interval logic for the merge:
        - base case --> allows us to look at previous (if result is empty)
        - case where we can merge
            - is the previous interval[1] >= current interval[0] --> if
            - update the previous interval[1] to whaterver the max is between current and previous
            - at postiion 1
        - case where we cant
            - just add to our result

    '''
