# Устройство состоит из трех деталей. 
# Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: 
# а). все детали = произведение вероятностей 1, 2 и 3 деталей
# б). только две детали = сумма всех событий из (2 вероятностей * на 3-ю противоположную вероятность)
# в). хотя бы одна деталь = противоположное событию "из строя не выйдет ни одной детали"
# г). от одной до двух деталей = сумме вероятностей событий "из строя выйдет 1 деталь" и "из строя выйдут 2 детали"

# а) Вероятность того, что "вышли из строя все детали"
P3=0.1*0.2*0.25
print(f'Вероятность того, что из строя выйдут все детали Р(3) = {P3:.3f}') # 0.005


# б) Вероятность того, что "вышли из строя 2 детали"
P2=0.1*0.2*0.75+0.1*0.25*0.8+0.2*0.25*0.9
print(f'Вероятность того, что из строя выйдут только 2 детали Р(2) = {P2:.3f}') # 0.080


# в) Вероятность того, что  "выйдет из строя хотя бы одна деталь" (1м=1-0.1=0.9, 2м=1-0.2=0.8, 3м=1-0.25=0.75)
P0=0.9*0.8*0.75
print(f'Вероятность того, что из строя не выйдет ни одной детали Р(0) = {P0:.3f}') # 0.540
P4=1-P0
print(f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(>=1) = {P4:.3f}') # 0.460


# г) Вероятность того, что  "из строя выйдут от одной до двух деталей" 
P1=0.1*0.8*0.75+0.2*0.9*0.75+0.25*0.9*0.8 # из строя вышла 1 деталь (сумма каждой из вероятностей * на 2 противоположных вероятности)
print(f'Вероятность того, что выйдет из строя от одной до двух деталей Р(1,2) = {P1+P2:.3f}') # 0.455