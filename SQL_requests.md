# Autotest_and_SQL_diplom
# Задание 1. SQL-запрос на вывод логина курьера и количества заказов в доставке

scooter_rent=# SELECT c.login, COUNT(ord.track) FROM "Couriers" AS c JOIN "Orders" AS ord ON c.id = ord."courierId" WHERE "inDelivery" = true GROUP BY login;
 
# Задание 2. SQL-запрос на вывод трека заказа и его статуса

scooter_rent=# SELECT track, CASE WHEN finished IS true THEN 2 WHEN cancelled IS true THEN -1 WHEN "inDelivery" IS true THEN 1 ELSE 0 END FROM "Orders";
