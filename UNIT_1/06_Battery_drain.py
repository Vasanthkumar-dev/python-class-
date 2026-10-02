battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
print(f"Low battery alert {minutes} minutes ({battery})%")

battery = 100
minutes = 0
while battery > 20:
    battery -= 7
    minutes += 1
    print(f"minute {minutes:2d} -> battery {battery}%")
print("Alert")

while True:
    test = input("Enter battery %(0 - 100): ")
    value = float(test)
    if 0 <= value <= 100:
        break
    print("Out of range, try again")
print("accepted: ", value)

value = 10
while True:
    print(value)
    value -= 1
    if value == 0:
        break
print("Take off")

value = 10
while value >= 1:
    print(value)
    value -= 1
print("Take off")

j = 0
i = 1
while True:
    j = j+1
    i += 1
    if i == 100:
        break
print(j)  # this prints 99, not the sum. j only goes up by 1 each time instead of adding i, so it counts the loops, and the loop stops when i reaches 100 so 100 is never included. It should be j = j + i, and the loop should run until i passes 100, which would give 5050
