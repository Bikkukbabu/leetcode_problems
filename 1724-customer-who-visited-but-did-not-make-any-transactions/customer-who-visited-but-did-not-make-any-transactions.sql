# Write your MySQL query statement below
SELECT visits.customer_id , count(*)  as count_no_trans FROM Visits visits
LEFT join Transactions transactions
on visits.visit_id = transactions.visit_id
where transactions.visit_id is null
group by visits.customer_id;