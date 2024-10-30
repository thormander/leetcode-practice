class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        result = []

        nums.sort()

        # make precomputed sums list
        # precomput[i] = sum from 0,1,2,3...i-1
        # it will be sum of everything before the i'th index
        # if i = 0, sum should be 0 so we need extra space
        precompute = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            precompute[i+1] = precompute[i] + nums[i]


        # go through query
        for query in queries:
            # find midpoint (binary search)
            mid = bisect_left(nums,query)

            numsLeft = mid
            numsRight = len(nums) - mid

            # case 1: operations where we need to increment (left)
            leftSum = precompute[numsLeft] # sum up to the midpoint
            leftOperations = numsLeft * query - leftSum # opposite of decrement

            # case 2: operations where we need to decrement (right) OR total sum - left side
            rightSum = precompute[-1] - leftSum # sum after the midpoint
            rightOperations = rightSum - numsRight * query 

            totalOps = rightOperations + leftOperations
            result.append(totalOps)

        return result





'''
to do this faster,
sort first

have a list of precomputed sums:
    where precompute[i] = sum of all nums up to i

loop through the queries:
    find the midpoint
    everything to left wil use logic for incrementing
    everythign to right will use logic for decrementing

    sum up the totals

'''
