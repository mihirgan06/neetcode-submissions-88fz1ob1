class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            given an array prerequisites
            prerequisites[i] = [a,b] means finish b first to take a
            [0, 1] --> means you must take course 1 before course 0
            TOTAL = numCourses to take (0 - numCourses - 1)
            true if possible to finish all course else false


            so for 2 courses, prereqs = [[0,1]]
            finish course 1 then 0 2 courses so good

            numCourses 2, prerequisites = [[0,1],[1,0]]
            Fails bc, to take course 0 you must take course 1 but you must also take course 0 to take course 1

            SO if we detect a cycle the code should return false

        '''
        #start by creating an empty adj list
        adjList = [[] for i in range(numCourses)]
        #populate the list where each course has a subarray of prerequisites

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        visited = set()
        
        def dfs(course):
            #we already visited course --> false
            if course in visited:
                return False
            
            if adjList[course] == []:
                return True
                #no prerequites

            #dfs through the prerequisites for a course
            visited.add(course)



            for prereq in adjList[course]:
                
                if not dfs(prereq):
                    return False
            visited.remove(course)

            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        



        
        