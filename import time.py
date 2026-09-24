import time

# 1. Start the stopwatch
start_time = time.time()

# --- Your algorithm goes here ---
my_list = [x**2 for x in range(1000000)]
# --------------------------------

# 2. Stop the stopwatch
end_time = time.time()

# 3. Calculate the difference
print(f"Algorithm finished in: {end_time - start_time} seconds")
