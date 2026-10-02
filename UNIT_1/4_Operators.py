heading = 359
turn = 5
print("Wrong:", heading + turn)
print("right:", (heading + turn)%360)
print("negative:", (-30)%360)

distance = 8.0
limit = 10
print(distance < limit)
print(distance == limit)
print(0 <= distance < limit)
battery = 45
print(distance>5 and battery > 20)
print(distance>5 or battery > 90)
print(distance>5)

distance = 35
battery = 50
docked = True
print(distance>10 and battery>20 and docked)  # this prints True only when all three conditions are true, but docked is used without "not", so it prints True even though the robot is docked. For the robot to be safe to move it should be "not docked"
