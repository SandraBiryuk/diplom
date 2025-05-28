# Отчёт по выполнению дипломных заданий
# Бирюкова Александра, 30-я когорта

# 1. SQL-запрос: курьеры и количество заказов в статусе inDelivery = true
print("Задание 1: Количество заказов в статусе 'inDelivery = true' у каждого курьера")

sql_1 = """
SELECT c.login, COUNT(o.id) AS deliveryCount
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;
"""
print(sql_1)

# Результат:
print("Результат:\nromashka | 0\nivan     | 4\n")

# 2. SQL-запрос: все трекеры заказов и их статусы
print("\nЗадание 2: Статусы заказов")

sql_2 = """
SELECT "track",
    CASE
        WHEN "finished" = true THEN 2
        WHEN "cancelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders";
"""
print(sql_2)

# Результат:
print("Результат:\n751685 | 1\n829196 | 1\n...")

# 3. API-тест: создание заказа, получение по треку, принятие заказа
print("\nЗадание 3: API-тесты")

# Создание курьера
courier = {
    "login": "romasha",
    "password": "4477",
    "firstName": "romanov"
}
print("Создание курьера:", courier)

# Авторизация курьера
courier_login = {
    "login": "romasha",
    "password": "4477"
}
print("Авторизация курьера:", courier_login)

# ID курьера
print("ID курьера: 3")

# Создание заказа
order_data = {
    "firstName": "Петя",
    "LastName": "Петров",
    "adress": "Центральный проезд Хорошеевского Серебрянского Бора 2",
    "metroStation": 153,
    "phone": "+79273262226",
    "rentTime": 5,
    "deliveryDate": "2025-05-22",
    "commet": "Спасибо"
}
print("Создание заказа:", order_data)

# Получен track:
print("Track заказа: 434420")

# Получение заказа по треку
print("GET /api/v1/orders/track?t=434420 — код ответа 200")

# Принятие заказа
print("Принятие заказа: /api/v1/orders/accept/19?courierId=3 — ответ: {'ok': true}")