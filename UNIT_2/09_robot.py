# # The Unit-1 way: parallel data, and, every function needs
# r1 = {"name":"Alpha", "battery": 100}
# r2 = {"name":"Beta", "battery": 60}
#
# def drain(robot, amount):
#     robot["battery"] = max(0, robot["battery"] - amount)
#
# def status(robot):
#     return f'{robot["name"]}: {robot["battery"]}%'
#
# drain(r1, 35)
# print(status(r1))
# print(status(r2))

# class Robot:
#     """A mobile robot with a battery."""
#
#     def __init__(self, name, battery = 100):
#         self.name = name
#         self.battery = battery
#
#     def drain(self, amount):
#         self.battery = max(0, self.battery - amount)
#
#     def status(self):
#         return f"{self.name}: {self.battery}%"
#
# r1 = Robot("Alpha")
# r2 = Robot("Beta", 60)
# r1.drain(35)
# print(r1.status())
# print(r2.status())

# class Robot:
#     """A mobile robot with a battery."""
#
#     def __init__(self, name, battery = 100):
#         self.name = name
#         self.battery = battery
#
#     def drain(self, amount):
#         self.battery = max(0, self.battery - amount)
#
#     def status(self):
#         return f"{self.name}: {self.battery}%"
#
# fleet = [Robot("Alpha"), Robot("Beta", 60), Robot("Gamma", 25)]
# for r in fleet:
#     r.drain(20)
# for r in fleet:
#     print(r.status())
# print("Objects created: ", len(fleet))

'''
    CREATE A CLASS WITH THE NAME STUDENT, WHICH HAS 2 INSTANCE ATTRIBUTES NAME AND SRN AND A DISPLAY
    METHOD. THEN CREATE 3 OBJECTS, AND PRINT ALL 3.
'''
from tkinter.font import names


# class Student:
#     def __init__(self, name, srn):
#         self.name = name
#         self.srn = srn
#     def display(self):
#         print(f"Name: {self.name}, SRN: {self.srn}")
# s1 = Student("Ravi", "R25EV029")
# s2 = Student("Rahul", "R25EV053")
# s3 = Student("Abhi", "R25EV058")
# s1.display()
# s2.display()
# s3.display()

# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def status(self):
#         return f"{self.name} ready"
#
# r = Robot("Alpha")
# print(r.status())
# print(Robot.status(r))

# class Robot:
#     def __init__(self, name, battery = 100, speed = 0.5):
#         self.name = name
#         self.battery = battery
#         self.speed = speed
#
#     def status(self):
#         return f"{self.name}: {self.battery}% at {self.speed}"
#
# print(Robot("Alpha").status())
# print(Robot("Beta", 60).status())
# print(Robot("Gamma", 25, 1.2).status())

# class Robot:
#     wheels = 4
#     fleet_size = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.fleet_size += 1
#
# a = Robot("Alpha")
# b = Robot("Beta")
# print("names: ", a.name, b.name)
# print("wheels: ", a.wheels, b.wheels)
# print("fleet :", Robot.fleet_size)
#
# Robot.wheels = 6
# print("after change: ", a.wheels, b.wheels)

# class Robot:
#     log = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def record(self, event):
#         self.log.append(event)
#
# a = Robot("Alpha")
# b = Robot("Beta")
# a.record("Alpha started")
# b.record("Beta started")
# print("Alpha log: ", a.log)
# print("Beta log: ", b.log)

class Robot:
    log = []

    def __init__(self, name):
        self.name = name
        self.log = []

    def record(self, event):
        self.log.append(event)

a = Robot("Alpha")
b = Robot("Beta")
a.record("Alpha started")
b.record("Beta started")
print("Alpha log: ", a.log)
print("Beta log: ", b.log)