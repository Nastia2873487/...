sitost = 0
happy = 0
level = 1
class pet(sitost, happy):
    while True:
        print("Выберите действие:Покормить или Поиграть")
        task = input()
        if task == "Покормить":
            sitost += 5
            print("Сытость:", sitost,"Счастье:", happy, "Уровень:", level)
        elif task == "Поиграть":
            happy += 5
            print("Сытость:", sitost, "Счастье:", happy, "Уровень:", level)
        if sitost >= 5 and sitost <= 15 and happy >= 5 and happy <= 15:
            level = 2
        if sitost > 15 and sitost <= 25 and happy > 15 and happy <= 25:
            level = 3
        if sitost > 25 and sitost <= 35 and happy >= 25 and happy <= 35:
            level = 4
        if sitost > 35 and sitost <= 45 and happy > 35 and happy <= 45:
            level = 5
        if sitost > 45 and sitost <= 55 and happy > 45 and happy <= 55:
            level = 6
        if sitost > 55 and sitost <= 65 and happy > 55 and happy <= 65:
            level = 7
        if sitost > 65 and sitost <= 75 and happy > 65 and happy <= 75:
            level = 8
        if sitost > 75 and sitost <= 85 and happy > 75 and happy <= 85:
            level = 9
        if sitost > 85 and sitost <= 100 and happy > 85 and happy <= 100:
            level = 10

