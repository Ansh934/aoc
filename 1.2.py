with open("input1.txt") as file:
    data = file.readlines()
    left, right = zip(*[(int(i.split("   ")[0]), int(i.split("   ")[1])) for i in data])

sim_score = 0
for i in left:
    c =right.count(i)
    t = i * c
    sim_score+=t
        
print(sim_score)

