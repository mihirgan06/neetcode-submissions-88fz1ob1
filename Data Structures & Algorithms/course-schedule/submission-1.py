class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            Given an array prerequisites where prerequisites[i] = [a, b] indicates you ust take course b THEN course a
            ex: [0, 1] means you must take 1 before takint 0

            ex; numCourses = 2, prerequisites = [[0,1], [1,0]]

            - not possible: to take course 0 finish course 1, to take course 1, finish course 0 --> impossible


            prerequisites:
                [[a, b], [b, a]] --> fails if numCourses = 2
                [[a, b]] --> should succeed if numCourses = 2

                each array of prerequisites is length of 2, so 2 elements do b then a

            for ex: [[0, 1]]

            1 --> 0
            prereq -> course

            the reason why example.2 fails
            0 --> 1, 0
            1 --> 0, 1

            oh if we detect a cycle return False
        
        First build an adjacency list check for a cycle if no cycle return true, else false

        '''
        #make each course map to a prerequite

        preMap = {i: [] for i in range(numCourses)}
        #creates an empty list for each course
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            #append the prerequites for each course to every courses mapped list
        path = set()
        visited = set()
        def dfs(course):
            if course in path:
                return False 
            if course in visited:
                return True
            path.add(course)
            for prereq in preMap[course]:
                if dfs(prereq) == False:
                    return False
            path.remove(course)
            visited.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True