''' 
n cars travelling to the same destination on a one-lane highway

position[i] -> position of the ith car in miles
speed[i] -> speed of the ith car mph
destination at position target miles

cars cant pass each other. only catch upthen drive at the same speed as the car ahead

car fleet is non empty set of cars driving same position and speed

if a car catches up to a car fleet the moment the fleet reaches the dest -> it's considered part of the fleet.

return the number of different car fleets that will arrive at the dest. 

'''




class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        latest = 0
        for p, s in cars:
            time = (target - p) / s
            if time > latest:
                fleets += 1
                latest = time
        return fleets