robot_name = "Alpha"
battery_pct = 78.5
is_docked = True
waypoints = 12
print("---")
print(type(robot_name))

battery = 100
print("start: ", battery)
battery = battery - 15
print("after: ", battery)
battery -= 15
print("later: ", battery)

battery = 45
if battery < 50:
    print("Charging recommended")
    print("Docking now...")
print("Status check done")

robot_name = "Beta"
Battery_pct = 45
docked = False
points = 17
print(robot_name, battery_pct, docked, points)

if battery < 50:
    print("BATTERY IS LOW")  # prints a low battery warning because battery is 45, which is below 50. Also, Battery_pct is spelled with a capital B, so the print above still shows the old 78.5
