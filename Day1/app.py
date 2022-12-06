class Elf:
    def __init__(self) -> None:
        self.calories: list[int]= []
        self.total_calories_list: list[int] = []
        self.most_cal = 0
    def add(self,num: int):
        try:
            n = int(num, base=10)
            self.calories.append(n)
        except TypeError:
            print(TypeError())
    def biggest(self):
        max_num = self.total_calories_list[0]
        for cal in self.total_calories_list:
            if cal > max_num:
                max_num = cal
        return max_num
    def sort(self):
        if self.total_calories_list != []:
            n = len(self.total_calories_list)
            for i in range (n):
                already_sorted = True
                for j in range (n - i - 1):
                    if self.total_calories_list[j] > self.total_calories_list[j+1]:
                        self.total_calories_list[j], self.total_calories_list[j + 1] = self.total_calories_list[j + 1], self.total_calories_list[j]
                        already_sorted= False
                if already_sorted:
                    break
        else:
            raise ValueError("The total calorie list is empty")

elf = Elf()
with open(file="input.txt",mode= "r", newline="\n") as file:
    data_list = file.readlines()
    file.close()
    
for data in data_list:
    if data != '' and data != '\n':
        data = data.strip()
        elf.add(data)
    elif data == '\n':
        elf.total_calories_list.append(sum(elf.calories))
        elf.calories = []

elf.most_cal = elf.biggest()
elf.sort()
total_last_3 = elf.total_calories_list[-2] +elf.total_calories_list[-3] + elf.total_calories_list[-1] 
print(total_last_3)
