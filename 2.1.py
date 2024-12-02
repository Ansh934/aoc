with open("input2.txt") as file:
    data = [[int(num) for num in line.split(" ")] for line in file.readlines()]
    safe_counter = len(data)
for row in data:
    is_increasing = row[0] < row[1]
    is_decreasing = row[0] > row[1]
    if not is_increasing and not is_decreasing:
        safe_counter -= 1
        continue
    for i in range(len(row) - 1):
        num1 = row[i]
        num2 = row[i + 1]
        if is_increasing:
            diff = num2 - num1
        else:
            diff = num1 - num2
        if not diff in [1, 2, 3]:
            safe_counter -= 1
            break
print(safe_counter)
