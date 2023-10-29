class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {} # course : [prereq]
        for i in range(numCourses):
            hashmap[i] = []

        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        
        # detect cycle
        hashset = set()

        def DFS(course):
            # base cases
            if course in hashset:
                return False
            if hashmap[course] == []:
                return True
            
            hashset.add(course)

            for prereq in hashmap[course]:
                if not DFS(prereq):
                    return False
            hashset.remove(course)
            hashmap[course] = [] # in case we run it again
            return True
        
        for course in range(numCourses):
            if not DFS(course):
                return False
        return True
 
        '''
        think of if there is a cycle then impossible. (use set for this)

        use a map to represent adjacency list

        return true if empty?
        '''
