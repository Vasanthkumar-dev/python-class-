# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
# p = Point(2, 3)
# print(p)
#----------------------------------------
# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# p = Point(2, 3)
# print(p)
# print(f"robot is at {p}")
#----------------------------------------
# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def status(self):
#         return f"{self.name} ready"
#
# r = Robot("Alpha")
# print(r.status())
#--------------------------------------------
# class Robot:
#     def __init__(self, name, battery = 100):
#         self.name = name
#         self.battery = battery
#
#     def band(self):
#         if self.battery < 15:
#             return "CRITICAL"
#         elif self.battery < 30:
#             return "LOW"
#         return "OK"
#
#     def needs_dock(self):
#         return self.band() != "OK"
#
#     def report(self):
#         flag = " -> DOCK NOW" if self.needs_dock() else ""
#         return f"{self.name}: {self.battery}% [{self.band()}]{flag}"
#
# for r in [
#     Robot("Alpha", 8),
#     Robot("Beta", 22),
#     Robot("Gamma", 76)
# ]:
#     print(r.report())
#------------------------------------------------------------------------
# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def dist_to(self, other):
#         return math.hypot(self.x - other.x, self.y - other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# robot = Point(2, 3)
# dock = Point(5, 7)
# print(f"robot {robot} -> dock {dock}")
# print("distance:", robot.dist_to(dock))