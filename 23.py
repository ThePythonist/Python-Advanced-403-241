import random

comments = {}


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.active = True

    def leave_comment(self, text, id):
        if self.active:
            comments.setdefault(id, {self.username: text})
            print(f"Posted comment : {text}")
        else:
            print("You are not permitted to leave any comment")


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)
        self.permissions = ["Get Report", "Ban User", "Create Article"]

    def remove_comment(self, id):
        comments.pop(id)
        print(f"Deleted comment {id}")

    def ban_user(self, user):
        user.active = False
        print(f"Deactivated user {user}")


karbar1 = User("Ahmad", "123", "example@gmail.com")
karbar2 = User("Arshia", "123", "example@gmail.com")
karbar3 = Admin("Rostam", "123", "example@gmail.com")

# karbar3.ban_user(karbar1)
karbar1.leave_comment("nice", 2001)
karbar2.leave_comment("awesome", 2002)
karbar3.remove_comment(2001)
print(comments)
