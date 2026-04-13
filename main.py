from db import LSMTree

db = LSMTree()

db.put("a", "1")
db.put("b", "2")
db.put("c", "3")
db.put("d", "4")
db.put("e", "5")  

print(db.get("a"))  # Hasilnya harus 1

db.delete("a")

print(db.get("a"))  # Hasilnya harus none