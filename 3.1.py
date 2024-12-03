import re

with open("input3.txt") as file:
    data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, data)
sum = 0
for match in matches:
    num1 = int(match[0])
    num2 = int(match[1])
    sum += num1 * num2
print(sum)