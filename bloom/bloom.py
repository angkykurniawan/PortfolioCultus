class BloomFilter:
    def __init__(self, size=1000):
        self.size = size
        self.bit_array = [0] * size

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        return (hash(key) * 7) % self.size

    def add(self, key):
        self.bit_array[self._hash1(key)] = 1
        self.bit_array[self._hash2(key)] = 1

    def might_contain(self, key):
        return (
            self.bit_array[self._hash1(key)] == 1 and
            self.bit_array[self._hash2(key)] == 1
        )