import re

with open("input3.txt") as file:
    data = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
matches = re.findall(pattern, data)
do = True
dont = False
sum = 0
for match in matches:
    if match[2] == "do()":
        do = True
        dont = False
        continue
    elif match[3] == "don't()":
        do = False
        dont = True
        continue
    num1 = int(match[0])
    num2 = int(match[1])
    if do:
        sum += num1 * num2
print(sum)
