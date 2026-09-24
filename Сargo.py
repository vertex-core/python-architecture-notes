from collections import deque

# 1. Initialize a single unified queue of cargo trucks (FIFO structure)
port_queue = deque(
    [
        {
            "id": "105AA",
            "destination": "Washington",
            "weight": 100,  # Stored as a number for calculations
            "distance": 200,  # Stored as a number for calculations
            "fuel": 50,
        },
        {
            "id": "105BB",
            "destination": "New York",
            "weight": 200,
            "distance": 400,
            "fuel": 60,
        },
    ]
)

COST_PER_KM_TON = 0.5


# 2. Pure function to calculate trip cost
def calculate_trip_cost(weight, distance):
    return weight * distance * COST_PER_KM_TON


# 3. Processing the queue simulation loop
print("=== PORT LOGISTICS PROCESSING START ===\n")

while port_queue:
    # Pop from the front of the queue instantly (O(1) time complexity)
    current_truck = port_queue.popleft()

    truck_id = current_truck["id"]
    dest = current_truck["destination"]
    weight = current_truck["weight"]
    distance = current_truck["distance"]
    fuel = current_truck["fuel"]

    # Calculate cost using our function
    total_cost = calculate_trip_cost(weight, distance)

    print(f"Processing Truck ID: {truck_id}")
    print(f"  Destination: {dest} | Fuel Required: {fuel}L")
    print(f"  Load: {weight} tons | Distance: {distance} km")
    print(f"  Calculated Transport Cost: ${total_cost:.2f}\n")

print("=== ALL TRUCKS CLEARED ===")
