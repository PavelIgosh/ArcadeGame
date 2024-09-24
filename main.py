# Простая игра с РПГ аспектами
# integer (int)
# string (str)
# float - число с плавающей точкой 1.23432
# list - массив [1,2,3,4,5]
# boolean (bool) - True & False (1,0)
# dict - словарь {Key: Value}}
# set - множество {1,2,3,4,5}

# a = 10
# if a == 10:
#   print("hello")
# a = 12
# if a !="10":
#   print("world")

# Логические операторы
# > < >= <= == !=
# in работа со списками и строками
# in  -  if "1" in ["1", "2", "3"] - True
# for i in ["1", "2", "3"] -> "1" \n "2" \n "3"

# Карта 5х5
# Наш персонаж - Имя, Здоровье, Оружие, Выносливость, Броня, Моделька
# Враг - Здоровье, Оружие, Броня

import random

hero = {
    "Name": "",
    "Health": 100,
    "Inventory": {
        "Sword": 25,
        "Health_Flask": 30
    },
    "Armor": 25,
    "Model": "🐵",
    "base_damage": 40,
    "Luck": random.randint(0, 3),
    "Positon":[0, 0]
}


# print(hero["Health"])
# print(hero["Inventory"]["Sword"])

enemy = {
    "Health": 125,
    "Inventory": {
        "Sausage": 35,
        "Health_Flask": 30
    },
    "Armor": 10,
    "Model": "🍌",
    "base_damage": 25,
    "Position":[]
}

#print(hero["Luck"])

# Статы героев

hero["Name"] = input("Введите имя героя: ")
print(f"Добро пожаловать в игру, {hero['Name']}!")

# Старт игры

HEALTH_HERO = hero["Health"] + (hero["Armor"] * 0.25)
DAMAGE_HERO = hero["base_damage"] + hero["Inventory"]["Sword"]

HEALTH_ENEMY = enemy["Health"] + (enemy["Armor"] * 0.25)
DAMAGE_ENEMY = enemy["base_damage"] + enemy["Inventory"]["Sausage"]

# Вычисления урона и здоровья



model_health = "♥"

HEALTH_BAR_HERO = hero["Health"] // 10 * model_health
HEALTH_BAR_ENEMY = enemy["Health"] // 10 * model_health

# print(HEALTH_HERO)
# HEALTH_HERO = 15


# print(HEALTH_ENEMY)
# HEALTH_ENEMY = 15



# Боевка

map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

counter_hero = 0
counter_enemies = 0
while counter_hero != 1 and counter_enemies != 3:
  for y in range(5):
    for x in range(5):
      if random.randint(1, 50) in [10, 25, 50, 20, 30, 35]:
        if random.randint(0, 1) == 1:
          if counter_hero < 1:
            map[y][x] = hero["Model"]
            hero["Position"] = [y, x]
            counter_hero += 1
        else:
          if counter_enemies < 4:
            map[y][x] = enemy["Model"]
            enemy["Position"].append([y,x])
            counter_enemies += 1


while True:
    
  for i in map:
    print("\n")
    for j in i:
      print("".join(str(j)), end="\t")
  
  #Позиционириование    


  
  move = int(input("\n\nВыберите дейстиве\n1) Сходить налево\n2) Сходить направо\n3) Сходить вниз\n4) Сходить вверх\n--> "))
  if move == 1:
    temp = hero["Position"]
    if temp[1] > 0:
      map[temp[0]][temp[1]] = 0
      map[temp[0]][temp[1]-1] = hero["Model"]
      hero["Position"] = [temp[0],temp[1]-1]
  elif move == 2:
    temp = hero["Position"]
    if temp[1] < 4:
      map[temp[0]][temp[1]] = 0
      map[temp[0]][temp[1]+1] = hero["Model"]
      hero["Position"] = [temp[0],temp[1]+1]
  elif move == 3:
    temp = hero["Position"]
    if temp[0] < 4:
      map[temp[0]][temp[1]] = 0
      map[temp[0] + 1][temp[1]] = hero["Model"]
      hero["Position"] = [temp[0]+1,temp[1]]
  elif move == 4:
    temp = hero["Position"]
    if temp[0] > 0:
      map[temp[0]][temp[1]] = 0
      map[temp[0] -1][temp[1]] = hero["Model"]
      hero["Position"] = [temp[0]-1,temp[1]]
  # if (hero["Position"][0] - 1 in enemy["Position"]) or (hero["Position"][0] + 1 in enemy["Position"]) or (hero["Position"][1] - 1 in enemy["Position"]) or (hero["Position"][1] + 1 in enemy["Position"]):
  for p in range(len(enemy["Position"])):
    x = hero["Position"][1]
    y = hero["Position"][0]
    a = enemy["Position"][p][1]
    b = enemy["Position"][p][0]
    
    if ((a - x == -1) or (a - x == 0) or (a-x == 1)) and \
      ((b - y == -1) or (b - y == 0) or (b - y == 1)):
      while True:
        print("БАНАНЫ АТАКУЮТ 😲")
        if random.randint(1, 6) in [6, 1, 2]:
          print("Удача на вашей стороне!")
          HEALTH_ENEMY -= DAMAGE_HERO
          enemy["Health"] = HEALTH_ENEMY
          print("Вы нанесли врагу", DAMAGE_HERO, "урона")
          if enemy["Health"] <= 50:
            if "Health_Flask" in enemy["Inventory"]:
              print("Враг использовал зелье!")
              HEALTH_ENEMY += enemy["Inventory"]["Health_Flask"]
              del enemy["Inventory"]["Health_Flask"]
              print("У врага осталось", enemy["Inventory"])
              print(f"У врага осталось {HEALTH_BAR_ENEMY} здоровья")
            else:
              print("У врага нет зелья!")
          if enemy["Health"] <= 0:
            print("Враг повержен")
            break
          else:
            print("У врага", enemy["Health"], "здоровья")
          enemy["Armor"] = enemy["Armor"] - enemy["Armor"] * 0.25
          print("У врага", enemy["Armor"], "брони")
          if enemy["Health"] <= 0:
            print("Враг повержен!")
            break
        else:
          print("Удача не на вашей стороне!")
          HEALTH_HERO -= DAMAGE_ENEMY
          hero["Health"] = HEALTH_HERO
          print("Вам нанесли", DAMAGE_ENEMY, "урона")
          if hero["Health"] <= 50:
            print("У вас мало здоровья! Желаете использовать зелье?")
            s = input("(y/n): ")
            if s == "y":
              if "Health_Flask" in hero["Inventory"]:
                print("Вы использовали зелье!")
                HEALTH_HERO += hero["Inventory"]["Health_Flask"]
                del hero["Inventory"]["Health_Flask"]
                print("У вас осталось", hero["Inventory"])
                print(f"У вас осталось {HEALTH_BAR_HERO} здоровья")
              else:
                print("У вас нет зелья")
            else:
              print("Вы решили не использовать зелье")
          elif hero["Health"] <= 0:
            print("GAME OVER!")
            break
          else:
            print("У Вас", hero["Health"], "здоровья")
          hero["Armor"] = hero["Armor"] - hero["Armor"] * 0.25
          print("У Вас", hero["Armor"], "брони")
          
    

# Если гг стоит так, что рядом с вами враг, начинается бой
# Если победа - хп 100 + 10% за каждого убитого врага
# Если проиграете - вывод надписи бб
# * Вы можете добавлять предметы любые при убийстве в инвентарь
# Загрузить в "Знакомство с Python"
