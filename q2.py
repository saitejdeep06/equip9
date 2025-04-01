import heapq
from collections import defaultdict

def match_requests_to_sellers(requests, sellers):
    # Group sellers by equipment type and store their prices in a min-heap
    equipment_heap = defaultdict(list)
    
    for equipment_type, price in sellers:
        heapq.heappush(equipment_heap[equipment_type], price)
    
    result = []
    
    for equipment_type, max_price in requests:
        # If there are sellers for the requested equipment type
        if equipment_type in equipment_heap:
            # Check the lowest price in the heap
            if equipment_heap[equipment_type] and equipment_heap[equipment_type][0] <= max_price:
                result.append(heapq.heappop(equipment_heap[equipment_type]))  # Pick the best match
            else:
                result.append(None)
        else:
            result.append(None)
    
    return result

# Example Input
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

# Function call
result = match_requests_to_sellers(requests, sellers)

# Output the result
print(result)