-- sample_data.sql

INSERT INTO users (username) VALUES 
  ('alice'), ('bob'), ('charlie'), ('diana'), ('eve');

INSERT INTO posts (user_id, content) VALUES 
  (1, 'Hello world!'), 
  (2, 'This is my first post!'),
  (1, 'Another day, another post.'),
  (3, 'Excited to join!'),
  (4, 'Good morning!');
