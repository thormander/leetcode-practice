class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = set()

        for trip in triplets:
            # check if its greater
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            
            for index, num in enumerate(trip):
                if num == target[index]:
                    result.add(index)

        return len(result) == 3
