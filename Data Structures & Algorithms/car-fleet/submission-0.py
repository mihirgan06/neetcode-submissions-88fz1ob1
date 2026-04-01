class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        n cars traveling to same destination

        position = array of the positions of each car
        Spped = speed of each car

        Destination = position target miles

        car cannot pass another car only catch up and travel at same speed

        car fleet is a non-empty set of cars driving at same position and speed
        Single car can be a car fleet

        if a car catches up to a car fleet the moment the fleet reaches destination, car is part of fleet
        Return number of different car fleets

        we want to know how many GROUPS of cars reach the targe

        For example 1:
        the car traveling at speed 3 catches up the car at speed 2 from position 4 --> makes a fleet


        Track:
        car 1             car 2.             

        traveling at 3    traveling at 2
        position 1 ---> position 4 -------> destination
        the car behind will catch up before dest -> fleet

        For example 2:
        Starting Position:
        car 1: position 4 -> position 6 -> position 8 -> pos 10 MEETS CAR 4
        car 2: position 1 -> position 3 -> 5 -> 7 (group 2)
        car 3: position 0 -> position 1 -> pos 2 -> 3 (group 3)
        car 4: position 7 -> position 8 -> pos 9 -> pos 10 MEETS car 4

        Total: 3 Fleets
        The car is affected by the car ahead of it
        if a car is going faster than a car infront of it, its forced to


        time = (dest - initial pos)/speed
        the cars behind with a smaller time to get to dest will collide but SLOW DOWN to speed ahead


        Sort the pairs of cars
        We add the cars ot stack
        Compare the new car with the car adjacent to it on the stack
        Remove the car that's on the top of the stack
        Add next car, if we pop the other one
        what we end up returning is the number of car fleets
        '''
        stack = []
        #we need to merge speed and position
        cars = [[p, s] for p, s in zip(position, speed)]

        #each tupple is its own car
        for p, s in sorted(cars)[::-1]: #loop through in reverse sorted order
            time = (target - p ) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)    

        


        










