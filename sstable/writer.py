import os

class SSTableWriter:
    def __init__(self, directory="data"):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def write(self, data, file_id):
        filename = os.path.join(self.directory, f"sst_{file_id}.txt")

        with open(filename, "w") as f:
            for key, value in data:
                f.write(f"{key}:{value}\n")

        return filename