from collections import deque
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            Given an array of CPU tasks
            tasks[i] = uppercase english character from A - Z,
            given an integer n
            Each cpu cycle allows the completion of a single task, tasks can be completed in any order
            once you complete a task A for ex, there is  a cooldown of n before you can do the next A

            tasks = ["X","X","Y","Y"], n = 2

            1. X
            2. Y
            3. Idle
            4. X
            5. Y

            youll need a queuee for the cooldown
            we need the counts of each task
            and then a max heap to minimiuze time as we should do the taskjs with highest count first

        '''
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        #have a count for each task in tasks
        #next we shpuld convert the counts into a max heap so we optimally do tasks
        maxHeap = [- cnt for cnt in task_count.values()]
        time = 0
        heapq.heapify(maxHeap)
        q = deque()

        while maxHeap or q:
            time += 1 #increment itme
            if maxHeap:
                #add one bc the counts are in negatives
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                    
             


        



        
        