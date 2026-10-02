errors = ["E2", "E7"]
print(errors)

errors.append("E2")
print("after append: ", errors)

errors.insert(0, "E1")
print("after insert: ", errors)

errors.remove("E7")
print("after remove:", errors)

a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print("a = ", a)
print("b = ", b)
print("c = ", c)

print("b is a:", b is a, "| c is a:", c is a)

readings = [10, -1, -1, 20, 30]
for r in readings:
    if r == -1:
        readings.remove(r)
print(readings)

readings = [12, 45, 7, 61, 33]
doubled = [r *2 for r in readings]
big = [r for r in readings if r > 30]
print(doubled)
print(big)  # this prints [45, 61, 33] because the list comprehension keeps only the readings greater than 30. doubled works the same way but multiplies every reading by 2, giving [24, 90, 14, 122, 66]. Both build new lists, so readings itself does not change
