class ProfileManager:
    def __init__(self):
        self.users = {}  # hash table

    def add_user(self, user_id, name, interests):
        self.users[user_id] = {
            "name": name,
            "interests": set(interests)
        }

    def get_profile(self, user_id):
        return self.users.get(user_id, None)

    def update_profile(self, user_id, name=None, interests=None):
        if user_id in self.users:
            if name:
                self.users[user_id]["name"] = name
            if interests:
                self.users[user_id]["interests"] = set(interests)

    def display_profile(self, user_id):
        user = self.get_profile(user_id)
        if user:
            return f"{user_id}: {user['name']} | Interests: {list(user['interests'])}"
        return "User not found"