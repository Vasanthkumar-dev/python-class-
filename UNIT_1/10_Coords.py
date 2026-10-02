visited = {(0, 0), (0, 1)}
visited.add((1, 1))
visited.add((0, 0))
print(visited)
print("count:", len(visited))
print("(1, 1) visited?", (1, 1) in visited)
print("(9, 9) visited?", (9, 9) in visited)

codes = ["E2", "E7", "E2", "E1", "E7"]
print("raw: ", codes)
print("unique:", set(codes))
print("unique count:", len(set(codes)))

position = (4.2, 7.8)
print(position, type(position))
x, y = position
print("x =", x, "| y =", y)
single = (5,)
print(single, type(single))

c = set()
c.add((0, 0))
c.add((0, 1))
c.add((0, 2))
c.add((0, 3))
c.add((0, 2))
c.add((1, 2))
c.add((1, 1))
c.add((1, 0))
print(c)
print(len(c))
print((2, 2) in c)  # this prints False because (2, 2) was never added to the set. Also, only (0, 2) is repeated, so the 8 adds give 7 distinct cells, not 5 as the question needs for 3 repeats. A set has no fixed order, so print(c) can show the cells in any order
