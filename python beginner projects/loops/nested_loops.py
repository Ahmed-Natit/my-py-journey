for x in range(5):  # Outer loop
    for y in range(3):  # Inner loop
        if x == 1 and y == 1:
            continue
        if x == 2 and y == 0:
            break
        if x == 3 and y == 2:
            break
        if x == 4 and y == 1:
            break
        print(f"{x},{y}")
# This code prints pairs of numbers where x ranges from 0 to 4 and y ranges from 0 to 2.
# Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)

# In a nested loop, both loops start together — but the inner loop finishes all its cycles first.
# Only then does the outer loop move to the next value, and the inner loop repeats.
