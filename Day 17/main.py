class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

Player1 = User("jack" , "bob")
print(Player1.id)