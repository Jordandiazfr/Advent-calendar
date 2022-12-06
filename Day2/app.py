import score
# Get and parse data
p1 = []
elf = []

with open("input.txt", "r") as f:
    input_data = f.readlines()
    for data in input_data:
        x = data.strip().split()
        p1.append(x[0])
        elf.append(x[1])
    f.close()

print(p1)

# Game and Score calcul
mygame = score.Play()
for p, e in zip(p1, elf):
    outcome = mygame.game(p, e)
    mygame.score(p, outcome)

print(mygame.total_score)
