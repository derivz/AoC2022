import re

with open('./input.txt') as f:
    lines = f.read().strip().split('\n')

sensor_beacons = []
for line in lines:
    # extract the sensor and beacon from the line
    sensor = tuple(map(int, re.findall(r'x=(-?\d+), y=(-?\d+)', line)[0]))
    beacon = tuple(map(int, re.findall(r'x=(-?\d+), y=(-?\d+)', line)[1]))
    sensor_beacons.append((sensor, beacon))

# list all x from the sensors and beacons
all_x = [x for sensor, beacon in sensor_beacons for x in sensor + beacon]
min_x = min(all_x)
max_x = max(all_x)
start_x = min_x - (max_x - min_x) // 2
end_x = max_x + (max_x - min_x) // 2


def dst(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


y = 2000000
count = 0
for x in range(start_x, end_x):
    if any((x, y) == beacon for sensor, beacon in sensor_beacons):
        continue
    for sensor, beacon in sensor_beacons:
        if dst((x, y), sensor) <= dst(sensor, beacon):
            count += 1
            break
print("Part 1:", count)

lim = 4_000_000
result = None
for y in range(lim + 1):
    ranges = []
    for sensor, beacon in sensor_beacons:
        d = dst(sensor, beacon)
        yd = abs(sensor[1] - y)
        xd = d - yd
        if xd > 0:
            from_x = sensor[0] - xd
            to_x = sensor[0] + xd
            ranges.append((from_x, to_x))

    ranges.sort()
    mx = 0
    for i in range(1, len(ranges)):
        mx = max(ranges[i-1][1], mx)
        if ranges[i][0] > mx + 1 and ranges[i][0] > 0 and ranges[i-1][1] < lim:
            result = (ranges[i][0]-1, y)
            break
    if result:
        break

print("Part 2:", result, result[0]*4_000_000 + result[1])
