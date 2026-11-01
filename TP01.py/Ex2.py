# ---------------------------------------------------------------------------
# Problem 2 (Easy) · Time converter
# ---------------------------------------------------------------------------
total_seconds = 9875

hours = total_seconds // 3600              # whole hours
minutes = (total_seconds % 3600) // 60     # what is left, in whole minutes
seconds = total_seconds % 60               # the remainder after whole minutes
print(f"\n{total_seconds} seconds = {hours} h {minutes} min {seconds} s")

# Check: rebuild the total from the three parts
print("Check:", hours * 3600 + minutes * 60 + seconds == total_seconds)
