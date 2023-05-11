hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)

middle_number = round(len(hat_list)/2)

def run():
    i = input("Replace "+ str(hat_list[middle_number])+" with? ").strip()
    if not i.isdigit():
        print("MUST BE DIGIT")
        return run()
    hat_list[middle_number] = int(i)
    hat_list.pop()
    print(len(hat_list), hat_list)
run()
