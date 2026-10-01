counter = 0

while True:
    counter += 1

    # If the counter is 3, we want to skip this iteration
    if counter == 3:
        print("Skipping iteration number 3!")
        continue  # Skips the print below and goes back to the top of the loop

    print(f"Current counter value: {counter}")

    # Break out of the infinite loop once we reach 5
    if counter >= 5:
        break