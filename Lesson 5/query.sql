SELECT event_name, COUNT(visitor_id) AS visitors --Number of visitors per event
FROM
	fact_sales
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
	INNER JOIN event USING(event_id)
WHERE status_name = 'Оплачено'
GROUP BY event_name
ORDER BY visitors DESC;

SELECT date_part('month', Purchase_date) AS month, --Revenue by month
    SUM(Service_price) AS total
FROM fact_sales
	INNER JOIN dim_date USING(date_id)
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY date_part('month', Purchase_date)
ORDER BY month;

SELECT event_id, visitor_id, COUNT(sales_id) AS amount --Repeat visitors per event
FROM fact_sales
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY event_id, visitor_id
HAVING COUNT(sales_id) > 1;

SELECT event_id, date_part('year', Event_date) AS date_year, --Annual revenue per event
	SUM(Purchase_price) AS total
FROM fact_sales
	INNER JOIN event USING(event_id)
	INNER JOIN dim_date USING(date_id)
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY event_id, date_part('year', Event_date)
ORDER BY event_id, date_year;
