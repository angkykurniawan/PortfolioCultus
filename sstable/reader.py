class SSTableReader:
    def get(self, filename, key):
        with open(filename, "r") as f:
            for line in f:
                k, v = line.strip().split(":", 1)
                if k == key:
                    return v
        return None