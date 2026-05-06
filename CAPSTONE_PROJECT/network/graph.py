class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user_id):
        if user_id not in self.graph:
            self.graph[user_id] = set()

    def add_connection(self, u, v):
        self.add_user(u)
        self.add_user(v)
        self.graph[u].add(v)
        self.graph[v].add(u)

    def remove_connection(self, u, v):
        self.graph[u].discard(v)
        self.graph[v].discard(u)

    def get_friends(self, user_id):
        return list(self.graph.get(user_id, []))