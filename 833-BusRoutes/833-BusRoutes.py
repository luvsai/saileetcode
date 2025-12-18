# Last updated: 18/12/2025, 20:17:44
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        S, T = source, target
        if S == T :
            return 0
        stop_to_routes = defaultdict(list)
        #Build stop -> routes mapping
        for i , route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        
        # BFS Q of (route, buses_taken_so_far)
        q = deque()
        visited_routes = set()
        visited_stops = set()
        visited_stops.add(S)

        #since we start with stop S we can start with any of the routes that 
        #stop S starts from.

        for route in stop_to_routes[S]:
            q.append((route,1))
            visited_routes.add(route)
        
        while q:
            route ,buses = q.popleft()

            # if this route contains T -reached
            if T in routes[route]:
                return buses
            
            #explore all the stops in the route
            for stop in routes[route]:
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)
                #From this stop we can go to other routes

                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        q.append((next_route, buses + 1))
        return -1