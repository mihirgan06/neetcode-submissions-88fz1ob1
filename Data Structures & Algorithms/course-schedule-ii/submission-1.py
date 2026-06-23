from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            Topological Sort:
                Indegree = how mmay arrows point into me

                A --> B
                indegree of A = 0, indegree of B = 1

                indegree[course] = number of prerequisites that a course needs
                indegree[3] = 2 --> 2 prerequisites prior to completion of course 3

                Courses with an indegree of 0 are courses that can be taken NOW
                Once we complete the prerequisite we can decrement the indegree of a course

            1. Build graph: prereq --> course
            2. Count the number of indegrees for each course
            3. Put all courses with an indegree of 0 into a queue
            4. while q is not empty
                pop a course
                add to result
                for every course it unlocks
                    Reduce that course's indegree by 1
                    if that course's indegree becomes 0:
                        add to queue
            5. if the result has ll the courses return result
            6. Otherwise there's a cycle so return []
        '''

        adj = [[] for i in range(numCourses)]
        #create adjacency list

        #begin with an indegree of 0 for all courses
        indegree = [0] * numCourses

        #wire the prerequisites to the courses
        #increment the indegree for courses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        res = []

        while q:
            course = q.popleft()
            res.append(course)

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1
                
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)
        
        if len(res) == numCourses:
            return res
        return []
        