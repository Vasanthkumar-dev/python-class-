raw = "Alpha Rover"
print(f"[{raw}]")
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace(" ", "_"))
print("Rover" in raw)

packet = "T:25;H:60;B:78"
fields = packet.split(";")
print(fields)
key, value = 0, 0
for field in fields:
    key, value = field.split(":")
    print(key, "->", float(value))
print(key, value)

details = "gps_coordinates:12, 45, 80; motor currents:0.5"
details = details.split(";")
for i in details:
    key, value = i.split(":")
    print(details)
    print(key, "->", int(value))  # this crashes with a ValueError on the first loop because int() can't convert "12, 45, 80" (it has commas and spaces). int() would also fail on "0.5" since it is a decimal, so float() is needed for the motor current. The gps value should be split on "," first. Also, print(details) prints the whole list every time, it should print i instead
