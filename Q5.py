user1 = User("Alice", 25)
user2 = User("Bob", 30)
user3 = User("Charlie", 22)

users = [user1, user2, user3]
youngest_user = min(users, key=lambda user: user.age)
print(f"The youngest user is {youngest_user.name} with age {youngest_user.age}.")
