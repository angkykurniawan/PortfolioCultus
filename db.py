from memtable.memtable import MemTable
from sstable.writer import SSTableWriter
from sstable.reader import SSTableReader

class LSMTree:
    def __init__(self):
        self.memtable = MemTable()
        self.writer = SSTableWriter()
        self.reader = SSTableReader()
        self.sstables = []
        self.file_id = 0
        self.limit = 5 

    def put(self, key, value):
        self.memtable.put(key, value)

        if self.memtable.is_full(self.limit):
            self.flush()

    def get(self, key):
        # Cek Memtable
        val = self.memtable.get(key)
        if val:
            if val == "__TOMBSTONE__":
                return None
            return val

        # cek sstable terbaru ke lama
        for file in reversed(self.sstables):
            val = self.reader.get(file, key)
            if val:
                if val == "__TOMBSTONE__":
                    return None
                return val

        return None

    def delete(self, key):
        self.memtable.delete(key)

    def flush(self):
        data = self.memtable.flush()
        filename = self.writer.write(data, self.file_id)
        self.sstables.append(filename)
        self.file_id += 1