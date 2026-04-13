### Project Explanation
This project implements a very simple simplified Log-Structured Merge Tree (LSM Tree) storage engine. 
The goal of this project is to simulate how modern NoSQL databases handle write-heavy workload with efficiently.

Insted of writing data directly to the disk, all write operations are first stored into a memory structure called MemTable.
One the MemTable reaches size threshold, the data is flushed to disk as an immutable Sorted String Table (SSTable)

This design improves write performance by converting random disk writes into sequential writes process. 
The system also supports logical deletion using tombstones and includes a basic compaction mechanism to merge SSTables and remove data.

### Approach
This system is designed by dividing the LSM Tree into several modular components:
1) MemTable (In-Memory Layer)
   - Stores key-value pairs temporarily in RAM
   - Supports inserts, read, and delete operation
   - Deletion is handled using a tombstone marker insted of immediate removal

2. SSTable (Disk Layer)
   - When the MemTable reaches its size limit, data is sorted and flushed to disk.
   - Each flush creates a new immutable SSTable file.
   - Files are stored sequentially to optimize disk I/O.

3. Read Path Strategy
   - The system first checks the MemTable for the requested key.
   - If not found, it searches SSTables from the most recent to the oldest.
   - This ensures that the latest version of the data is always returned.

4. Bloom Filter (Optimization)
   - A Bloom Filter is used to quickly determine whether a key might exist in an SSTable.
   - This reduces unnecessary disk reads and improves query performance.

5. Compaction
   - Multiple SSTables are merged into a single file.
   - Duplicate keys are resolved by keeping the latest value.
   - Tombstones are removed during the process to reclaim storage space.

### File Sequence
1. main.py --> Starting Point
2. db.py --> Core Engine
3. memtable.py --> Temporaly Storage (RAM)
4. db.py --> Trigger Flush
5. writer.py --> Write to Disk
6. Data Folder --> Physical Storage
7. Reader.py --> Reading from Disk
8. bloom.py --> Avoid reading unnecessary files
9. compaction.py --> Cleaning and tidying up data

### Limitations
- The current implementation uses a simplified file format without advanced indexing.
- SSTable reads are performed using linear scanning, which can be optimized further.
- Compaction strategy is basic and does not implement multi-level optimization.

### Conclusion
This project demonstrates the fundamental concepts behind LSM Tree-based storage systems, 
highlighting the balance between write efficiency and read complexity. It provides a strong 
foundation for understanding modern database storage engines such as LevelDB.
