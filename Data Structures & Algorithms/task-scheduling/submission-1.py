from collections import defaultdict
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            Given an array of tasks, where tasks[i] is an uppercase letter from A-Z
            Also given integer n
            each CPU cycle allows the completion of a single task, tasks can be compelted in any order

            however identical tasks must be sperated by at lest n CPU cycles


            tasks = [X, X, Y, Y] n = 2
            cycle 1: X
            cycle 2: cannoy do X again do Y
            cyele 3: nothing
            cycle 4: X
            cycle 5: Y

            tasks = ["A","A","A","B","C"], n = 3

            1: A
            2: B
            3: c
            4, idle
            5. A
            6. idle
            7. idle
            8, idle
            9. A
        
        How do we use a heap here?
        - Greedy strategy, always execute the task w the highest remaining frequency
        - Repeatedly get the max --> max heap

    '''
    #start with empty heap

        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        #atp we have a count for each tasks
        maxHeap = [- cnt for cnt in task_count.values()]
        time = 0
        heapq.heapify(maxHeap)
        q = deque()
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        