class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
            Ok cars can become a fleet even if that happens at 10
            Fleet = just any group of cars even if one car\

            car cant pass another car ahead of it, only catch up and then move at the sam esppeed as the car in front or as the fleet it merges into

            O(N log N)
            - Monotonic stack
            - we definitely have to sort i assume the position and the speed


            - the way we mapped this out was using the car diagram
            - track the displacement of each car from position and speed to see when the cars merge

            We sort the positions, we need to process the car closest to the target first

            We want to zip together position and speed into a new list
            THis is exactly what the cars are

        '''
        cars = list(zip(position, speed))
        cars.sort(reverse=True) #the last index would have the greatest position so we need to prioritize that first
        stack = []
        fleets = 0
        #sort the position first and speed if needed thats how sorting utuples works
        for pos, speed in cars:
            #we can create a stack of arrival times fo rht efleets ahead of us
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                #the time is greater than the top of stack so this just adds an additional car to the stack
                fleets += 1
                stack.append(time)
            else:
                #fleets wills tay the same 
                #so the car merges into the stack
                continue
            
        return fleets

                


        











            
        