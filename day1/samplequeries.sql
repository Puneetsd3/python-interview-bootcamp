-- sample_queries.sql

-- All posts
SELECT * FROM posts;

-- Posts by username
SELECT p.*
  FROM posts p
  JOIN users u ON p.user_id = u.id
  WHERE u.username = 'alice';

-- Count likes per post
SELECT p.id, p.content, COUNT(l.id) AS like_count
  FROM posts p
  LEFT JOIN likes l ON p.id = l.post_id
  GROUP BY p.id;
