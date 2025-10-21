# Write your MySQL query statement below
with dedup as (
    select *, 
    ROW_NUMBER() OVER 
    (PARTITION BY article_id, author_id, viewer_id
    ORDER BY view_date  )  as rn 
    FROM Views
)
SELECT DISTINCT(author_id) as id FROM dedup
where rn=1 and author_id = viewer_id
order by author_id asc;

