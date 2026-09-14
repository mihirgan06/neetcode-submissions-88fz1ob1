class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            given array prerequisites where prerequisites[i] = [a, b] --> must take course b first to take course a


            pair [0, 1] means take course 1 before course 0


            numCourses courses from 0 to numCourses - 1

            Topological sort

            we must detect a cycle using DFS


            - if we detect a cycle then its not possible to complete and we must return false

            0 --> 1
            1 --> 0
            not possible

            0 = haven't visited
            1 = currently exploring this course
            2 = completely finished exploring it



        '''

        adj_list = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
                adj_list[prerequisite].append(course)


        visited = set()
        state = [0] * numCourses




        def dfs(course):
            #if we detect a cycle we want to return false

            if state[course] == 1:
                return False
            

            if state[course] == 2:
                return True
            state[course] = 1


            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            #finished exploring

            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



            
            






        