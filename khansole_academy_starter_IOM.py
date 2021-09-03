"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

# Count() is introduced to keep track of the number of times the user gets an answer correct in a row
count1 = 1
# Precondition for how many times the code will run until it exits
while count1 <= 3:
    # x represents the first random number generated
    x = random.randint(10, 99)
    # y represents the second random number generated
    y = random.randint(10, 99)
    # p represents the printout statement to the user
    p = print('What is ', x,'+' ,y  )
    # q represents the summation of the addition of x and y
    q = x + y
    # z represents the user's input
    z = int(input("Your answer: "))
   # condition: If the user's input is correct, then the program should keep count
    if z == q:
        print("Correct. You've gotten " + str(count1) + " correct in a row")
        count1 += 1
    # If the user's input is incorrect, the count is restarted.
    else:
        print('Incorrect. The expected answer is ' + str(q))
        count1 = 1
# If the user's input is correct three times in a row then the code exits.
print("Congratulations! You've mastered addition.")