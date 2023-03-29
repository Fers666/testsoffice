import random


def get_random_user(user_type: str):
    return random.choice(users_tree[user_type])


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class UserType:
    LOGISTIC = "0"
    ADMIN = "1"
    SAMMBTK = "2"
    TK = "3"


user_types = [UserType.LOGISTIC, UserType.ADMIN, UserType.SAMMBTK, UserType.TK]
users_tree = {
    UserType.LOGISTIC: [
        User("autologistrand@tests.ru", "72sHHYVK3u")
    ],
    UserType.ADMIN: [
        User("autoadmin@tests.ru", "72sHHYVK3u")
    ],
    UserType.SAMMBTK: [
        User("autotcsammb@tests.ru", "72sHHYVK3u")
    ],
    UserType.TK: [
        User("autotcrand@tests.ru", "72sHHYVK3u")
    ]
}
