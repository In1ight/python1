import random
print("\t\t\tПриветствую тебя в игре от 1 до 100")
print("\t\t\tТебе нужно отгадать число, которое я загадал за меньшее число попыток")
userNumber = int(input("Введи число "))
randomNumber = random.randint(1, 100)
tries = 1
while userNumber != randomNumber:
    if userNumber > randomNumber:
        print('Меньше ')
    else:
        print("Больше")
    userNumber = int(input("Введи число "))
    tries += 1

print("Поздравляю! Это было число: ", randomNumber)
print("Тебе понадобилось", tries, "попыток")
input('Нажми')