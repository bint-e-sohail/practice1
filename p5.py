numbers = [4, 8, 15, 16, 23, 42]

def stats(nums):
    mn = min(nums)
    mx = max(nums)
    avg = sum(nums) / len(nums)
    return mn, mx, avg  #  returns tuple (4, 42, 18.0)

def grade(marks, passing=50):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"

# Main execution

# Unpack tuple from stats()
lo, hi, avg = stats(numbers)
print(lo, hi, avg)

# Call grade as required
result1 = grade(55)  # uses default passing=50
result2 = grade(55, passing=60)  # overrides to 60

print(result1, result2)



#Advance one
"""from typing import List, Tuple

numbers: List[int] = [4, 8, 15, 16, 23, 42]

def stats(nums: List[int]) -> Tuple[int, int, float]:
    #Returns (min, max, average) in one tuple.
    if not nums:
        raise ValueError("List is empty")
    return min(nums), max(nums), sum(nums) / len(nums)

def grade(marks: int, passing: int = 50) -> str:
    #Return Pass/Fail with customizable passing threshold.
    return "Pass" if marks >= passing else "Fail"

# Unpacking with * (tuple unpacking)
lo, hi, avg = stats(numbers)
print(f"{lo} {hi} {avg}")

# Using default vs keyword argument
print(f"{grade(55)} {grade(55, passing=60)}")

# --- Advance concepts demo ---

# 1. You can also unpack like this:
data = stats(numbers)
print(f"Stats tuple: {data}")

# 2. Using lambda version (one-liner for grade)
grade_lambda = lambda m, p=50: "Pass" if m >= p else "Fail"
print(grade_lambda(55), grade_lambda(55, 60))

# 3. Works for any list
print(stats([1, 2, 3])) # -> (1, 3, 2.0)"""