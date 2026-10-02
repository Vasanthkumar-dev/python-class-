def add_waypoint(wp, route = None):
    if route is None:
        route = []
    route.append(wp)
    return route
r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("r1 =", r1)
print("r2 =", r2)
print("same object?", r1 is r2)  # this prints r1 = [(0, 0)], r2 = [(5, 5)] and then False. Because route = None, a brand new list is made inside the function on every call, so each route starts fresh and the two lists are separate objects. This is the fix for the earlier version where route = [] made both calls share one list
