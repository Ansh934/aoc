with open("input2.txt") as file:
    data = [[int(num) for num in line.split(" ")] for line in file.readlines()]

def check_row(row):
    is_increasing = row[0] < row[1]
    is_decreasing = row[0] > row[1]
    if not is_increasing and not is_decreasing:
        return (False,0)
    for i in range(len(row) - 1):
        num1 = row[i]
        num2 = row[i + 1]
        if is_increasing:
            diff = num2 - num1
        else:
            diff = num1 - num2
        if diff not in [1, 2, 3]:
            return (False,i)
    return (True,-1)

def dampen_and_check_row(row,index):
    lower_bound = max(0,index-1)
    upper_bound = min(len(row),index+2)
    for i in range(lower_bound,upper_bound):
        temp = row.pop(i)
        is_safe = check_row(row)[0]
        if is_safe:
            return True
        else:
            row.insert(i,temp)
    return False

safe_counter = 0
for row in data:
    is_safe,index = check_row(row)
    if is_safe:
        safe_counter += 1
    else:
        if dampen_and_check_row(row,index):
            safe_counter += 1

print(safe_counter)