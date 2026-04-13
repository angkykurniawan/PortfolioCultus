def merge(file1, file2, output):
    data = {}

    for f in [file1, file2]:
        with open(f, "r") as file:
            for line in file:
                k, v = line.strip().split(":", 1)
                data[k] = v  # overwrite dengan yang terbaru

    sorted_data = sorted(data.items())

    with open(output, "w") as f:
        for k, v in sorted_data:
            if v != "__TOMBSTONE__":
                f.write(f"{k}:{v}\n")