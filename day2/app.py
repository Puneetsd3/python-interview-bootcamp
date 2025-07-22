def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")
greet("Alice", msg="Welcome")

def add_user(user, users=[]):
    users.append(user)
    return users

print(add_user("alice"))
print(add_user("bob"))

def add_user_safe(user, users=None):
    if users is None:
        users = []
    users.append(user)
    return users

def flexible(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

flexible(1,2,3,name="Alice", age=30)

def make_multiplier(n):
    def inner(x):
        return x*n
    return inner

double = make_multiplier(2)
print(double(5))

from dao import UserDAO, PostDAO

user_dao = UserDAO()
post_dao = PostDAO()

new_user = user_dao.create("frank", "frank@example.com")
print(f"New User: {new_user}")

user = user_dao.get(new_user.id)
print(f"Fetched User: {user}")

new_post = post_dao.create(user.id, "This is a post by Frank")
print(f"New Post: {new_post}")


print("All posts:")
for post in post_dao.list():
    print(post)