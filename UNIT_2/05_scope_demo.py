count = 0
def tick():
    count = 0
    count += 1
    return count
print(tick(), tick(), count)

THRESHOLD = 70
def is_alert(value):
    return value > THRESHOLD
print(is_alert(85), is_alert(60))

count = 0
def tick():
    count += 1
    return count

print(tick())

count = 0
def tick():
    global count
    count += 1
    return count

print(tick(), tick(), tick())
print("global count is now:", count)

def tick(count):
    return count + 1
count = 0
count = tick(count)
count = tick(count)
print("count:", count)

lines = 0
def make_report():
    lines = ["header"]
    lines.append("body")
    return len(lines)
print(make_report())
print(make_report())
print("lines" in dir())  # this prints True. dir() at the top level lists the global names, and the global lines = 0 is one of them. The lines list inside make_report is a separate local variable that disappears when the function ends, so both calls print 2 and the global lines stays 0
