class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        /*
        build an adjacency list
        course -> prereqs
        dfs through each course
        have a visting path for each course
        if there is a cycle return false
        */
        const adjList = {};
        for(let i = 0; i < numCourses; i++) {
            adjList[i] = [];
        }
        for(const course of prerequisites) {
            const curr = course[0];
            const pre = course[1];
            adjList[curr].push(pre);
        }
        const visited = new Set();
        const visiting = new Set();
        function dfs(node) {
            if(visiting.has(node)) {
                return false;
            }
            if(visited.has(node)) {
                return true;
            }
            visiting.add(node);
            for(const n of adjList[node]) {
                if(dfs(n) === false) {
                    return false;
                }
            }
            visiting.delete(node);
            visited.add(node);
            return true;
        }
        for(let i = 0; i < numCourses; i++) {
            if(dfs(i) === false) {
                return false;
            }
        }
        return true;
    }
}
