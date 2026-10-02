temp = 45.0
if temp > 40:
    print("Cooling on")
print("Check complete")

temp = float(input("Enclosure temperature: "))
if temp < 40:
    mode = "heater on"
elif temp <= 40:
    mode = "normal"
elif temp <= 60:
    mode = "cooling"
else:
    print("Shut down")
print("Operating mode:", mode)

marks = 95
if marks >= 40:
    grade = "PASS"
elif marks >= 90:
    grade = "DISTINCTION"
else:
    grade = "FAIL"
print(grade)  # this prints PASS for 95 marks because the first condition (marks >= 40) is already true, so the DISTINCTION check is never reached. The order of the conditions should be flipped to check for 90 first
