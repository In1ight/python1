import random
userScore = int(input("Введи свое число "))
systemScore = random.randint(1, 100)
systemScoreMax = 100
systemScoreMin = 1
tries = 1
while userScore != systemScore:

    if userScore > systemScore:
        if systemScoreMin < systemScore:
            systemScoreMin = systemScore
        print("больше ", systemScoreMin, ' до ', systemScoreMax)
    else:
        if systemScoreMax > systemScore:
            systemScoreMax = systemScore
        print("меньше ", systemScoreMin, ' до ', systemScoreMax)
    systemScore = random.randint(systemScoreMin, systemScoreMax)
    tries += 1

print('Я угадал это число ', systemScore, "с ", tries, " попытки!")
input("Нажмите")