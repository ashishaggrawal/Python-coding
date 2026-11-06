# This program gets four test scores and displays their average.
# It congrats the user if the average is high

#Set high score
HIGH_SCORE = 95

# Get test scores
test1= float(input("Enter the scores for the test 1: "))
test2= float(input("Enter the scores for the test 2: "))
test3= float(input("Enter the scores for the test 3: "))
test4= float(input("Enter the scores for the test 4: "))

# Calculate the average test scores

average = (test1+test2+test3+test4)/4

print(f"The average is: {average:.2f}")

if average > HIGH_SCORE:
    print("CONGRATS, you get high score.")
else:
    print("Good Job")