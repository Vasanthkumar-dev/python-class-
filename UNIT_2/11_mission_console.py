# class Robot:
#     def __init__(self, name):
#         self.name = name
#         self.speed = 0.4
#
# r = Robot("Alpha")
# print("attributes:", r.__dict__)
# del r.speed
# print("after del: ", r.__dict__)

class Probe:
    def __init__(self, pid):
        self.pid = pid
        print("created", self.pid)

    def __del__(self):
        print("destroyed", self.pid)

p = Probe(1)
q = p
del p
print("q still works: ", q.pid)
del q
print("end of demo")