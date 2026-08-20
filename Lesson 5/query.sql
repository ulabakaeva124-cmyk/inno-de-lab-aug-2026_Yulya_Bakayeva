SELECT event_name, COUNT(DISTINCT visitor_id) AS visitors --Number of visitors per event
FROM
	event
	LEFT JOIN fact_sales USING(event_id)
GROUP BY event_name
ORDER BY visitors DESC;

SELECT Month, --Revenue by month
    SUM(Service_price) AS total
FROM fact_sales
	INNER JOIN dim_date USING(date_id)
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY Month
ORDER BY Month;

SELECT visitor_id, COUNT(sales_id) AS amount --Repeat visitors
FROM fact_sales
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY visitor_id
HAVING COUNT(sales_id) > 1;

SELECT event_id, Year, --Annual revenue per event
	SUM(Purchase_price) AS total
FROM fact_sales
	INNER JOIN event USING(event_id)
	INNER JOIN dim_date USING(date_id)
	INNER JOIN dim_order USING(order_id)
	INNER JOIN status USING(status_id)
WHERE status_name = 'Оплачено'
GROUP BY event_id, Year
ORDER BY event_id, Year;
