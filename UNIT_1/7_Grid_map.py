waypoints = [(0,0), (2, 3), (5, 1)]
for wp in waypoints:
    print("Heading to", wp)

for i in range(3):
    print("scan", i)
print("---")

for i in range (1, 6):
    print(i, end = " " )
    
for i in range(10, 0, -2):
    print(i, end = " ")
print()

readings = [22.5, 23.1, 21.8, 24.0, 22.9]
total = 0
for r in readings:
    total += r
print(f"sum :{total:.2f}")
print("count :", len(readings))
print(f"mean : {total/len(readings):.2f}")

obstacles = [(1,2), (3, 3), (0, 4)]
for row in range(5):
    for col in range(5):
        if(row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end = "")
    print()

obstacles = [(2, 3), (1, 7), (5,5)]
for i in range(8):
    for j in range(8):
        if (i,j) in obstacles:
            print("X", end = " ")
        else:
            if (i,j) == (0, 0):
                print("S", end = " ")
            elif (i, j) == (7, 7):
                print("G")
            else:
                print(".", end = " ") 
    print()

readings = [12, -1, 34, 78, 15]
for r in readings:
    if r<0:
        continue
    if r>70:
        print("Danger at", r)
        break
    else:
        print("all readings safe")  # the else belongs to the r>70 check, so it prints "all readings safe" for every normal reading (12 and 34) instead of once at the end. -1 is skipped by continue, and the loop stops at 78 with "Danger at 78", so 15 is never checked. To print it only once, the else should be attached to the for loop
