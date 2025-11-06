# Write your MySQL query statement below


with temp_cte as (
SELECT recordDate, temperature, id, 
LAG(temperature) OVER(ORDER BY recordDate) as previous_temp,
LAG(recordDate) OVER(ORDER BY recordDate) as previous_date
FROM  WEATHER
)
SELECT id  FROM temp_cte
where temperature > previous_temp
and DATEDIFF(recordDate, previous_date) = 1;
