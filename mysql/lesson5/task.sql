-- 1) Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
update users set created_at = now();

-- 2) Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
update users set
	created_at = STR_TO_DATE(created_at, "%d.%m.%Y %H:%i"),
    updated_at = STR_TO_DATE(updated_at, "%d.%m.%Y %H:%i");

ALTER TABLE users CHANGE created_at created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE users_old CHANGE updated_at updated_at DATETIME on update CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP; 


-- 3) В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
select * from storehouses_products order by value = 0, value

--4) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')
select * from users where date_format(birthday_at, '%M') in ('may', 'august');

-- 5) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
SELECT * FROM catalogs WHERE id IN (5, 1, 2) ORDER BY FIELD(id, 5, 1, 2)


-- 1) Подсчитайте средний возраст пользователей в таблице users
select avg(floor((to_days(now()) - to_days(birthday_at))/365.25)) as avg_age from users

-- 2) Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
select count(id), DAYOFWEEK(STR_TO_DATE(concat(date_format(now(), '%Y'),date_format(birthday_at, '-%m-%d')),'%Y-%m-%d')) as dow
from users
group by dow
order by dow;