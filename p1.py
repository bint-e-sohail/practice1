marks = [88, 45, 92, 67, 30, 75]
PASS_MARK = 50 #min marks
#count passed students, condition
passed = sum(1 for m in marks if m >= PASS_MARK) 
average = sum(marks) / len(marks)
# f= formated str
print(f"Passed: {passed}")
print(f"Average: {average:.1f}") #avg 1 decimal
print(f"Highest: {max(marks)} Lowest: {min(marks)}")

