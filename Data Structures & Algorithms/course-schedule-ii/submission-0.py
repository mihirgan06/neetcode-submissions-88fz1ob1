class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            for prerequites[i] = [a,b] --> must take course b to take course a
            numCourses to take (0, numcourses - 1)

            return a valid ordering of courses you can take to finish all courses:

            numCourses = 3, prereqs = [[1,0]]
            must take course 0 then 1, then we can append any additional course to get to coruse numebr


            [0,1, 2]

            numCourses = 3, prerequisites = [[0,1], [1,2], [2,0]]

            - must take course 0 before 2, must take course 2 before 1, but you must take 1 before 0 so not possible

            Cycle detection first
        '''

        adjList = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        #current DFS path
        visiting = set()

        #fully completed set
        visited = set()
        res = []

        def dfs(course):
            #2 base cases: if the course is in visited --> []], if the course has no prereqs return course
            #we are guaranteed to have >= 1 numCourses
            if course in visiting:
                return False
            #we alreadyu added the course to our final res so return true
            if course in visited:
                return True
            #add to path
            visiting.add(course)
            #empty list of prereqs
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            #course is completed
            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res










        