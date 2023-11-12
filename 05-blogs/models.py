
class User:
    def __init__(self, uid, username, password, role) -> None:
        self.id = uid
        self.username = username
        self.password = password
        self.role = role

    
class Post:
    def __init__(self, pid, title, uid) -> None:
        self.id = pid
        self.title = title
        self.users_id = uid