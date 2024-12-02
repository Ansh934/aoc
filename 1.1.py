with open("input1.txt") as file:
    data = file.readlines()
    left, right = zip(*[(int(i.split("   ")[0]), int(i.split("   ")[1])) for i in data])
    sum_of_pairs = 0
    for i in range(len(left)):
        sum_of_pairs += abs(min(left) - min(right))
        left.remove(min(left))
        right.remove(min(right))

print(sum_of_pairs)
    