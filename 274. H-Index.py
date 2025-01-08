class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # initilize our count list
        count_papers = [0] * (len(citations) + 1)

        # fill the list
        for cites in citations:
            count_papers[min(len(citations),cites)] += 1
        
        
        # check count_papers in reverse
        paper_tracker = 0
        for i in range(len(count_papers)-1,-1,-1):
            paper_tracker += count_papers[i]
            if paper_tracker >= i:
                return i
            




'''
h is some number where we take max h citations in a paper >= at least h papers with more than h citations


[3,0,6,1,5]

List that stores counts of papers with that many citations(index)
[0,0,0,0,0,0] --> count of papers
 0 1 2 3 4 5  --> # of citations

       2
[1,1,0,1,0,2] --> count of papers
 0 1 2 3 4 5 --> # of citations

given an h, is there at least h papers, cited at least h times

go through the filled out count list: (in reverse)
    at what point is the value at the index > than the index
    add whatever the value was to a running variable tracking papers

return the first one that passes immedeatly

'''
