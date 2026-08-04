class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            Given an array prerequisites, wehre prerequisites[i] = [a,b] indicates you must take course b first if you wanna take course a

            pair [0,1] indicates take course 1 before course 0

            total of numCourses courses

            numCourses = 2, prerequisites = [[0,1]]
            finish 1 then 0 easy true

            numCourses = 2, prerequisites = [[0,1],[1,0]]
            theres a cycle, so false
            to take course 0 you must take course 1, and to take course 0 you must taje course 1



            We need to dfs through, and see if theres a back edge if theres a back edge we return false



        '''
        adj_list = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)
        visited = set()


        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] ==[]:
                return True
            visited.add(course)

            for prerequite in adj_list[course]:
                if not dfs(prerequisite):
                    return False

            visited.remove(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            
                
            




