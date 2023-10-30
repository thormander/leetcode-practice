class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(len(edges)+1): # we go to n
            parent.append(i)
        
        rank = [1] * (len(edges)+1)

        def find(node):
            p = parent[node]

            while p != parent[p]:
                parent[p] = parent[parent[p]] # ie. grandparent
                p = parent[p]
            return p

        def union(node1,node2):
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return False # when it causes cycle
            
            # union by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True # successful union
        
        for l,r in edges:
            # we want to find when union encounters False (ie. the edge we want to remove)
            if union(l,r) == False:
                return [l,r]
        


        '''
        union find; use of ranks
        '''
