from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    username: str
    email: str
    created_at: datetime

@dataclass
class Post:
    id: int
    user_id: int
    content: str
    created_at:datetime

def from_row(cls, description, row):
    columns= [desc[0] for desc in description]
    data = dict(zip(columns, row))
    return cls(**data)