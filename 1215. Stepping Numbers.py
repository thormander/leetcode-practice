class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        result = []

        # base case of 0
        if low == 0:
            result.append(0)

        queue = deque([1,2,3,4,5,6,7,8,9])

        while queue:
            num = queue.popleft()
            # case when we finish, ie. we start getting numbers greater than high
            if num > high:
                return result

            # include numbers from low --> high inclusive
            if num >= low:
                result.append(num)
            
            prev_ones_place = num % 10
            # now add another place, and add +- 1 to that new ones place
            # make sure they append in order
            if prev_ones_place > 0:
                queue.append(num * 10 + prev_ones_place - 1)
            if prev_ones_place < 9:
                queue.append(num * 10 + prev_ones_place + 1)

        

'''
we can use BFS

think of tree like decisions

 1
|  \
10  12

15
|   \
154  156

start with a queue of 1 - 9

we generate numbers and if its between low and high, append result

10
|   \
x   101

9
|  \
98    x

'''
