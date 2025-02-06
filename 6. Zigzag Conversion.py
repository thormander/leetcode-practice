class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # base case
        if numRows == 1:
            return s

        result = ""

        lengthS = len(s)
        lastRowI = numRows - 1

        for row in range(numRows):
            # first condition: top or bottom row
            if row == 0 or row == lastRowI:
                stepsReq = lastRowI * 2
                index = row
                while index < lengthS:
                    result += s[index]
                    index += stepsReq
            else:  # second condtion, handle middle rows
                stepsMiddle = lastRowI * 2  - 2 * row

                index = row
                while index < lengthS:
                    result += s[index]
                    index += stepsMiddle
                    if index < lengthS:
                        result += s[index]
                        index += 2 * row
                    
        return result

            

'''
P     I    N.  0
A   L S  I G.  1
Y A   H R.     2
P     I.       3

num rows 4

p --> i takes 6 steps
 - Only works for top or bottom
 - (num rows - 1) * 2
 - update index

handle any rows in middle
 - (num rows - 1) * 2 - 2(row we are on) # get us diagnol letters
 - update index to above line
 - then add the 2 (row we are on) back in to get back to usual spot and reset loop




'''
