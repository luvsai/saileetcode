# Last updated: 18/12/2025, 20:17:39
class Solution:
#     Sort cars by starting position descending (closest to target first). For each car compute its time to reach the target:
# t = (target - position) / speed.
# Traverse from the car nearest the target to the farthest; maintain max_time_so_far.

# If a car’s time > max_time_so_far, it forms a new fleet and update max_time_so_far = time.

# Otherwise its time ≤ max_time_so_far → it catches up and becomes part of the fleet counted earlier.

# This gives an O(n log n) solution (due to sorting), O(n) extra time for the scan.
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetcount = 0
        currentfleettime = -1
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key= lambda x : x[0], reverse= True)

        for car in cars:
            timetotarget = (target- car[0])/car[1]
            if timetotarget > currentfleettime :
                fleetcount +=1
                currentfleettime = timetotarget
        return fleetcount
        