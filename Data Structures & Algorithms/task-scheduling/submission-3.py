from collections import deque
from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            Given an array of CPU tasks, (tasks), where tasks[i] = uppercase englush char from A-Z

            Also you are given an integer n
            Each cpu cycle allows the completion of a single task
            tasks may be completed in any order



            Identical tasks must be seperated by at least n CPU cycles


            tasks = ["X", "X", "Y", "Y"], n = 2

            cycle 1: X
            cycle 2: y
            cycle 3: idle
            cycle 4: X
            cycle 5: Y

            use a max heap for priority of tasks to minimize number of cycles
            Hashmap (defaultdict) to count the number of appearances of each tasks
            We should heapify the values so we prioroitize the highest appearance tasks first
            queue for cooldown 
        '''
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        #atp we have a count for all the tasks stored in counts.values
        maxHeap = [-cnt for cnt in counts.values()]
        time = 0
        heapq.heapify(maxHeap)
        q = deque()
        
        while q or maxHeap:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1 #increment bc count is neg
                if cnt != 0:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time   

            
        