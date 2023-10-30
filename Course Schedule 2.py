class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        # set our adjacency list up
        hashmap = defaultdict(list) # course : prereqs

        # fill list
        for course,prereq in prerequisites:
            hashmap[course].append(prereq)

        cycle = set()
        visited = set()

        def DFS(course):
            # base cases
            if course in cycle:
                return False 
            if course in visited:
                return True # do not need to do DFS on course already visited
            
            cycle.add(course) # current path we are on

            for prereq in hashmap[course]:
                if DFS(prereq) == False:
                    return False # there was a cycle
            
            visited.add(course)
            result.append(course)
            cycle.remove(course) # verified prereqs do not result in cycle
            return True # no issues occured

        for i in range(numCourses):
            # handle case of cycle
            if DFS(i) == False:
                return []
        
        return result


        '''
        hashset for cycle and visited

        map for storing adjacency list
        '''C
