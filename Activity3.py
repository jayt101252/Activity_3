# Jason Thomas
# ISQA 3900 9/07/23
# Grade Calculator - Creates letter grade and numeric score based
# on score inputted by user
def display_main():
    display_title()
def display_title():
    print("Welcome to the Grade Calculator")


def get_total_points(points):

    total = points / 1000 * 100

    return round(total,2)


def get_letter_grade(total):

    if 100 > total > 92:
        grade = 'A'

    if 91.99 > total > 88:
        grade = 'B+'

    if 87.99 > total > 81:
        grade = 'B'

    if 81.99 > total > 78:
        grade = 'C+'

    if 77.99 > total > 69:
        grade = 'C'

    if 69.99 > total > 59:
        grade = 'D'

    if total < 60:
        grade = 'F'
    return grade


repeat = str('y')


display_main()

while repeat =="y":

    if repeat!="y":
            break

    print('\nEnter the total score!\n')

    points = int(input())


    total = points / 1000 * 100

    while points > 1000 or points < 0:
        print('Please enter number between 0 and 1000!')

        points = (input())

    print("\nYou earned an average of", get_total_points(points), "%. Letter grade earned:", get_letter_grade(total),)
    print("\nDo you want to repeat?\n")
    repeat = input()

print("\nThank You!")
