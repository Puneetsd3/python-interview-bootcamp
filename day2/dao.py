from models import User, Post
from db import get_connection

class UserDAO:
    def create(self, username, email)->User:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                            INSERT into users (username, email)
                            VALUES (%s, %s)
                            RETURNING id, username, email, created_at
                            """, (username, email))
                row = cur.fetchone()
                return User(*row)
    def get(self, user_id) -> User | None:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, username, email, created_at FROM users WHERE id = %s", (user_id,))
                row = cur.fetchone()
                return User(*row) if row else None

class PostDAO:
    def create(self, user_id, content)-> Post:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO posts (user_id, content)
                    VALUES (%s, %s)
                    RETURNING id, user_id, content, created_at
                            """, (user_id, content))
                row = cur.fetchone()
                return Post(*row)
        
    def list(self) -> list[Post]:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, user_id, content, created_at FROM posts")
                return [Post(*r) for r in cur.fetchall()]
            
                        
                