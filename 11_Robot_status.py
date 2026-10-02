robot = {"name": "Alpha", "battery": 78, "mode": "auto"}
print(robot)
print(robot["name"])
robot["battery"] -= 5
robot["speed"] = 0.4
print(robot)
print("keys :", list(robot.keys()))
print("values:", list(robot.values()))

robot = {"name": "Alpha", "battery": 78}
print(robot.get("speed"))
print(robot.get("speed", 0.0))
print("speed" in robot)

log = ["E2", "E7", "E2", "E1", "E7", "E2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)
for code in sorted(freq, key = freq.get, reverse = False):
    print(f"{code} occurred {freq[code]} time(s")
print(freq)

name = "shubham"
freq = {}
for i in range(len(name)):
    freq[name[i]] = freq.get(i, name.count(name[i]))
print(freq)
for i in sorted(freq, key = freq.get, reverse = True):
    print(f"{i} occurred {freq[i]} times")  # this prints each letter with its count, sorted from highest to lowest, so h (2 times) comes first. The counts are right only by luck: freq.get(i, ...) looks up the index number i, which is never a key (the keys are letters), so it always falls back to name.count(). It should be freq.get(name[i], 0) + 1. Also, the question asks to print the most frequent letter, but the program never prints it separately, it only shows up first in the sorted list
