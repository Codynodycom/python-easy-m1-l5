'''
Задача 1

Исправь ошибки в коде

У Бо совсем недавно сломалась зарядка для телефона, Бо решил заменить ее и купить новую. 
Он зашел на сайт где можно было их купить, но он заметил что на сайте сломались фильтры 
по поиску товара, поэтому Бо написал свой собственный, которы будет выводить товары 
подходящие под мощность которая больше 5 ватт, но меньше 10 ватт.
'''

charger_1 = "charger model 32XcP2: power_level: 12V"
charger_2 = "charger model 37FdJ8: power_level: 8V"
charger_3 = "charger model 3DkP90: power_level: 15V"

charger_1_power_level = charger_1[35:37]
charger_2_power_level = charger_2[35:36]
charger_3_power_level = charger_3[35:37]

charger_1_is_ok = 5 > charger_1_power_level < 10
charger_2_is_ok = 5 < charger_2_power_level < 10
charger_3_is_ok = 5 < charger_1_power_level < 10

print("Первая зарядка подходит:", charger_1_is_ok)
print("Вторая зарядка подходит:", charger_2_is_ok)
print("Третья зарядка подходит:", charger_3_is_ok)


