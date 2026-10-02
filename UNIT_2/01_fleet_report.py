r1_battery = 8
if r1_battery < 15:
    print("Alpha: CRITICAL")
elif r1_battery < 30:
    print("Alpha: LOW")
else:
    print("Alpha: OK")

r2_battery = 22
if r2_battery < 15:
    print("Beta: CRITICAL")
elif r2_battery < 30:
    print("Beta: LOW")
else:
    print("Beta: OK")

r3_battery = 76
if r3_battery < 15:
    print("Gamma: CRITICAL")
elif r3_battery < 30:
    print("Gamma: LOW")
else:
    print("Gamma: OK")

def battery_band(pct, name="neev"):
    if pct < 15:
        print(f"{name}: CRITICAL")
    elif pct < 30:
         print(name,": LOW")
    else:
        print(f"{name}: OK")
battery_band(8, "Alpha")
battery_band(22,"Beta")
battery_band(76)

def battery_band(pct):
    if pct<15:
        return "critical"
    elif pct<30:
        return "low"
    return "OK"

fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76, "Delta": 41}
for name, pct in fleet.items():
    print(f"{name: <7} {pct: >3}% {battery_band(pct)}")

def area(r):
    print(3.14 * r * r)
total = area(2) + area(3)
print("total:", total)

def area(r):
    return 3.14 * r * r
total = area(2) + area(3)
print("total:", total)

def move_robot(x, y, speed = 1.0):
    print(f"moving to ({x}, {y}) at {speed} m/s")
move_robot(3, 4)
move_robot(3, 4, 0.5)
move_robot(y = 4, x = 3)
move_robot(3, speed = 2.0, y = 4)

def log(*values, **options):
    print("values:", values)
    print("options:", options)

log("start")
log("waypoint", 3, 4.5)
log("alert", level = "high", retries = 2)
log()

def add_waypoint(wp, route = []):
    route.append(wp)
    return route

r1 = add_waypoint((0, 0))
r2 = add_waypoint((5, 5))
print("r1 = ", r1)
print("r2 = ", r2)
print("same objects?", r1 is r2)  # this prints True. The default list route = [] is created only once, when the function is defined, so both calls add to the same list. That is why r1 and r2 both show [(0, 0), (5, 5)] even though each call was meant to start a fresh route. The fix is route = None, and then creating a new list inside the function when route is None
