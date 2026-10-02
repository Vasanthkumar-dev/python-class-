THRESHOLD = 70.0

def is_alert(value):
    return value > THRESHOLD

def average(values):
    return sum(values)/len(values)
if __name__ == '__main__':
    print("self-test:", is_alert(85), average([10, 20, 30]))  # this prints "self-test: True 20.0". 85 is above the threshold of 70, so is_alert gives True, and the average of 10, 20 and 30 is 20.0. The if __name__ == '__main__' check makes this test run only when the file is run directly, so nothing is printed when another file imports these functions
