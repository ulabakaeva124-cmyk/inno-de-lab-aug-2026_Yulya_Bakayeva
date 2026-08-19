CREATE TABLE dim_date
(
Date_id SERIAL PRIMARY KEY,
Purchase_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE area 
(
Area_id SERIAL PRIMARY KEY,
Area_address VARCHAR (150) NOT NULL UNIQUE,
Area_name VARCHAR (150) NOT NULL,
Limit_visitors INTEGER 
);

CREATE TABLE event
(
Event_id SERIAL PRIMARY KEY,
Event_name VARCHAR (50) NOT NULL,
Area_id INTEGER NOT NULL,
Price DECIMAL (10, 2) NOT NULL CHECK (Price >= 0),
Event_date TIMESTAMP NOT NULL,
FOREIGN KEY (Area_id) REFERENCES area(Area_id)
);

CREATE TABLE visitor
(
Visitor_id  SERIAL PRIMARY KEY,
Name VARCHAR (50) NOT NULL,
Surname VARCHAR (50) NOT NULL,
Email VARCHAR (255) UNIQUE NOT NULL
);

CREATE TABLE status
(
Status_id  SERIAL PRIMARY KEY,
Status_name VARCHAR(50) NOT NULL
);

CREATE TABLE dim_order
(
Order_id  SERIAL PRIMARY KEY,
Status_id INTEGER NOT NULL,
FOREIGN KEY (Status_id) REFERENCES status(Status_id)
);

CREATE TABLE fact_sales
(
Sales_id SERIAL PRIMARY KEY,
Event_id INTEGER NOT NULL,
Visitor_id INTEGER NOT NULL,
Date_id INTEGER NOT NULL,
Order_id INTEGER NOT NULL,
Purchase_price DECIMAL (10, 2) NOT NULL CHECK (Purchase_price >= 0), 
Service_price DECIMAL (10, 2) NOT NULL,
FOREIGN KEY (Event_id) REFERENCES event(Event_id),
FOREIGN KEY (Visitor_id) REFERENCES visitor(Visitor_id),
FOREIGN KEY(Date_id) REFERENCES dim_date(Date_id),
FOREIGN KEY(Order_id) REFERENCES dim_order(Order_id)
);

--Generated data for queries:
INSERT INTO status (status_name) VALUES 
('Оплачено'),
('Возврат'),
('Отменено');

INSERT INTO dim_order (status_id) VALUES 
(1), (1), (1), (2), (1);

INSERT INTO dim_date (purchase_date) VALUES 
('2026-06-01 10:30:00'),
('2026-06-02 14:15:00'),
('2026-06-05 18:40:00'),
('2026-06-10 09:20:00'),
('2026-06-15 12:00:00');

INSERT INTO area (area_address, area_name, limit_visitors) VALUES 
('ул. Ленина, 10', 'Концертный зал "Минск"', 1500),
('пр. Победителей, 4', 'Дворец Спорта', 4500),
('ул. Октябрьская, 16', 'Клуб "Брудершафт"', 300);

INSERT INTO event (event_name, area_id, price, event_date) VALUES 
('Рок-концерт "Лето"', 1, 45.00, '2026-07-01 19:00:00'),
('Стендап Вечер', 3, 25.00, '2026-07-05 20:00:00'),
('Симфоническое шоу', 2, 70.00, '2026-07-10 18:30:00');

INSERT INTO visitor (name, surname, email) VALUES 
('Анна', 'Иванова', 'anna.ivanova@test.com'),
('Иван', 'Петров', 'ivan.petrov@test.com'),
('Елена', 'Смирнова', 'elena.smirnova@test.com'),
('Дмитрий', 'Ковалев', 'dmitry.kovalev@test.com');

INSERT INTO fact_sales (event_id, visitor_id, date_id, order_id, purchase_price, service_price) VALUES 
(1, 1, 1, 1, 45.00, 4.50),
(1, 2, 2, 2, 45.00, 4.50),
(2, 3, 3, 3, 25.00, 2.50),
(3, 4, 4, 4, 70.00, 7.00),
(2, 1, 5, 5, 25.00, 2.50);

