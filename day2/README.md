# Day 2: Python OOP + Mapping Classes to SQL

## Key Concepts
- Dataclasses reduce boilerplate (compare to manual init)
- We created lightweight DAOs to interact with Postgres directly
- No ORM like SQLAlchemy or Django — everything manual via psycopg2
- Used raw SQL and converted DB rows → Python objects

## Usage

- Use `UserDAO.create()` to insert a user
- Use `UserDAO.get(id)` to fetch a user
- Post operations via `PostDAO`

## Flow: SQL Row → Class

1. Run a query
2. Fetch raw `row` from DB cursor
3. Unpack into a Python `@dataclass`

