import score
import os.path
# Get and parse data
p1 = []
elf = []
file = os.path.join(os.path.dirname(__file__),"input.txt")

with open(file, "r") as f:
    input_data = f.readlines()
    print(input_data)
    for data in input_data:
        x = data.strip().split()
        p1.append(x[1])
        elf.append(x[0])
    f.close()


# Game and Score calcul
mygame = score.Play()
for p, e in zip(p1, elf):
 #   outcome = mygame.game(p, e) 
 #   mygame.score(p, outcome)
    mygame.strategy(p,e)


print(mygame.total_score)
