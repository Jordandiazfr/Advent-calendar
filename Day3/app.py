import os 
import string
file = os.path.join(os.path.dirname(__file__),"input.txt")

with open(file, "r") as f:
    input_data = f.readlines()
    f.close()

example = ["vJrwpWtwJgWrkhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]

class Rucksack:
    def __init__(self, sack:str) -> None:
        self.data = sack
        self.len = len(sack)
    
    def shared_letter(self) -> str:
        i = self.len//2
        pocket_1 = set(self.data[:i])
        pocket_2 = set(self.data[i:])
        l = pocket_1.intersection(pocket_2)
        return ''.join(l)

    def prioritize(self, letter:str) -> int:
        if letter == None:
            return 0

        priority = { letter:index 
        for index, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase, 1)
        }

        return priority[letter]

def main():
    total = []
    for data in input_data:
        sack = Rucksack(data.strip())
        letter = sack.shared_letter()
        value = sack.prioritize(letter)
        total.append(value)
    
    print(sum(total))


if __name__ == "__main__":
    main()