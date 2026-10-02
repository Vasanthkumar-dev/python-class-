battery = int(input("Enter battery pct: "))
print(battery+10)

name = "Alpha"
battery = 78.456
print("Robot", name, "at", battery, "%")
print(f"Robot {name} at {battery}%")
print(f"Robot {name} at {battery:.1f}%")
print(f"{name: <10} | {battery: >3.2f}|")

battery_capacity = eval(input("Enter battery capacity(mAh): "))
current_drawn = eval(input("Enter the current drawn by the robot(mAh): "))
runtime = battery_capacity/current_drawn
print(f"Estimated runtime: {runtime:.2f} hours")  # runtime is capacity (mAh) divided by current (mA), which gives hours, and :.2f rounds it to 2 decimal places when printing
