# used def to call the function that has the formula to compute the values instead of manually typing it again or using a nested loop.
def calculate_ave(act1, act2, act3):
    total = act1 + act2 + act3
    ave = total / 3
    return ave


num_students = int(input("How many students? "))

print()

# used loop so it can repeat the program and ask for another set of scores from another student for the 3 activities that is to be 
# inputed by the user.
for student in range(1, num_students + 1):
    print(f"Student {student}")

    name = input("Enter Name: ")
    act1 = int(input("Activity 1: "))
    act2 = int(input("Activity 2: "))
    act3 = int(input("Activity 3: "))

    # called the function so it can calculate the inputed values.
    ave = calculate_ave(act1, act2, act3)

    # allows the program to choose the student's status by checking their grade average.
    if ave >= 90:
        stat = "Excellent"
    elif ave >= 80:
        stat = "Very Good"
    elif ave >= 75:
        stat = "Passed"
    else:
        stat = "Failed"

    print()
    print("Average: ", ave)
    print("Status: ", stat)
    print()