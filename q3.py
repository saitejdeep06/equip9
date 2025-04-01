from collections import defaultdict
import bisect

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def process_maintenance_logs(maintenance_logs, queries):
    # Step 1: Create a sorted list of unique dates
    all_dates = sorted(set(log[1] for log in maintenance_logs) | set(query[0] for query in queries) | set(query[1] for query in queries))
    
    # Step 2: Map each date to an index
    date_to_index = {date: idx + 1 for idx, date in enumerate(all_dates)}  # 1-based index
    
    # Step 3: Create a Fenwick Tree
    fenwick = FenwickTree(len(all_dates))
    
    # Step 4: Update the Fenwick Tree with maintenance logs
    for equipment_id, date, cost in maintenance_logs:
        idx = date_to_index[date]
        fenwick.update(idx, cost)
    
    # Step 5: Process the queries
    result = []
    for start_date, end_date in queries:
        start_idx = date_to_index[start_date]
        end_idx = date_to_index[end_date]
        result.append(fenwick.range_query(start_idx, end_idx))
    
    return result

# Example Input
maintenance_logs = [(101, "2024-01-01", 500), (102, "2024-01-10", 300), (101, "2024-01-15", 700)]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

# Function call
result = process_maintenance_logs(maintenance_logs, queries)

# Output the result
print(result)
