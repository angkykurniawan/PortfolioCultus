class MemTable:
    def __init__(self):
        self.table = {}

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        self.table[key] = "__TOMBSTONE__"

    def is_full(self, limit):
        return len(self.table) >= limit

    def flush(self):
        items = list(self.table.items())
        items.sort(key=lambda x: x[0])
        self.table.clear()
        return items