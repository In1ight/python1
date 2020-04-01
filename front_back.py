import random
score = int(random.randint(1, 2))
front = 0
back = 0
count = 0
while count != 10:
    count += 1
    if score == 1:
        front += 1
        print("Решка")
    else:
        back += 1
        print("Орел")
    score = int(random.randint(1, 2))
print("Решка выпала ", front, " раз")
print("Орел выпал ", back, " раз")
input("Нажми чтобы выйти")