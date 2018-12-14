''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables mentioned in the description are declared and initialized; however, feel free to use additional variable as necessary (please avoid extra variables, though; don't use them unless you must to store a required value or simplify your code.) Write your solution below the commented description.
'''

''' 1. 
   Write a for loop that will print out all the integers from 0-4 in ascending order. 
'''

[print(i) for i in range(4)]

''' 2. 
   Write a for loop that will print out all the integers from 0-4 in descending order.
'''

[print(i) for i in range(4, -1, -1)]

''' 3. 
   Write a for loop that will print out all the integers from 5-15 in descending order.
'''

[print(i) for i in range(15, 4, -1)]

''' 4. 
   Write a for loop that will print out all the integers from -5 to 5 in ascending order.
'''

[print(i) for i in range(-5, 6)]

''' 5. 
   Write two for loops that will both print out odd numbers from 25 to 49. The loops themselves must be different, but they will have the same output.
'''

[print(i) for i in range(25, 50, 2)]

''' 6. 
   Write a for loop that prints out the squares of the numbers from 1 to 10. ie 1, 4, 9, 16, ... 100
'''

[print(i ** 2) for i in range(1, 11)]

''' 7. 
   Write while loops that do the same thing as numbers 1-6.
'''
# 1

i = 0
while i <= 4:
    print(i)
    i += 1

# 2

i = 4
while i >= 0:
    print(i)
    i -= 1

# 3

i = 15
while i >= 5:
    print(i)
    i -= 1

# 4

i = -5
while i <= 5:
    print(i)
    i += 1
 
# 5

i = 25
while i <= 49:
    print(i)
    i += 2

# 6

i = 0
while i <= 10:
    print(i ** 2)
    i += 1

''' 8. 
   A number starts at 4 and increases by one every day after the day it was created. Write a loop and use the variable days (int) that will print out how many days it will take for number to reach 57. 
'''

days = 0
n = 4

while n < 57:
    days += 1
    n += 1

print(days)

''' 9. 
   A girl in your class has jellybeans in a jar. The number of jellybeans is stored in int beans. Every day she shares one jellybean with every student in the class, and she herself takes two. The number of students in the class is held in variable students (int). Write a loop that determines how many days it will take for her to run out of jellybeans. You can store the result in variable numDays (int).
'''

beans = 1000
students = 25

numDays = 0

while beans > 0:
    numDays += 1
    beans -= 2 + students

''' 10. 
   Today is the 14th of December. Vacation starts on firstDayOfVacation (int). Assuming your vacation starts in December, write a loop that will count down the number of days until your vacation starts. It's output should be something like: "10 days until vacation!" "9 days until vacation!" ... "1 day until vacation!" "Vacation has arrived!"
'''

today = 14
vacation = 20

while vacation > today:
    print(f"{vacation - today} days until vacation")
    vacation -= 1

print("vacation is here")


''' 11. 
   Write a loop that will calculate n factorial. The sum should be stored in result (int).
'''

n = 5
result = 1

for i in range(2, n + 1):
    result *= i

''' 12. 
   A flying car can travel an average of 96mph. Write a loop that will determine how long it will take you (to the nearest quarter hour) to get to your destination if you were to travel by flying car. The distance to your destination is stored in distance (int).
'''

distance = 1000

print(f"{distance / 96} miles")


''' 13.  
   Write a loop that, given a number, n, will determine the value of n to the power of b. Store the result in variable exponent (int). 
'''

n = 2
b = 5

exponent = 1

for _ in range(b):
    exponent *= n


''' 14. 
   Write a loop that will print out all the letters of the alphabet.
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

for l in alphabet:
    print(l)

''' 15. 
   Now write a loop that will print out "A is a vowel." "B is a consonant." "C is a consonant." and so on. 
'''

vowels = "aeiou"

for l in alphabet:
    print(l + " is a " + ("vowel" if l in vowels else "consonant") + ".")

''' 16. 
   Write code that will produce the following output: 
   122333444455555666666777777788888888999999999
'''

print("122333444455555666666777777788888888999999999")

''' 17. 
   Write a loop that will print out the decimal equivalents of 1/2, 1/3, 1/4, 1/5, 1/6, ... 1/20. The output for each iteration should look like:
   "1/2 = .5" "1/3 = .666666666667" etc.
'''

for i in range(2, 21):
    print("1/" + str(i) + " = " + str(1/float(i)))

''' 18. 
   Write a loop that determines the sum of all the numbers from 1-100, as well as the average. Store the sum in variable total (int) and the average in variable avg (double).
'''

sum = 0
n = 0

for i in range(1, 101):
    sum += i
    n += 1

avg = sum / n

''' 19. 
   A friend tells you that PI can be computed with the following equation:
   PI = 4 + (1-1/3+1/5-1/7+1/9-1/11+1/13-1/15...)
   Write a loop that will calculate this output for n-iterations of the pattern (n being an int), that could help you determine if your friend is right or wrong.
'''

n = 1000
pi = 4

for i in range(n):
    x = 2 * i + 1

    if i % 2 == 0:
        x *= -1

    pi += 1 / x



''' 20. 
   A mother rabbit can have a litter of rabbits every month. In the litter, the number of rabbits can vary from 1 to 14 babies per litter, half of which are females. Rabbits can start reproducing at 6 months, so let's add all the new rabbits from the year to the reproductive pool at the end of each year (when their average age is 6 months). Write a simulation that will show how many rabbits will exist at the end of 5 years, starting with just one mother rabbit. 
'''

import random

last_born = 0
reproductive_pool = 1
time = 0

for i in range(time):
    reproductive_pool += last_born

    for j in range(reproductive_pool):
        last_born += random.randint(1, 7)

population = last_born + reproductive_pool

''' 21. 
   Write some code that will run the rabbit simulation above 1000 times, to help determine what we can expect on average.
'''

populationSum = 0
populationN = 0

for x in range(1000):
    last_born = 0
    reproductive_pool = 1
    time = 10

    for i in range(time):
        reproductive_pool += last_born

        for j in range(reproductive_pool):
            last_born += random.randint(1, 7)

    population = last_born + reproductive_pool

    populationN += 1
    populationSum += population

populationAvg = populationSum / populationN



''' 22. 
   Write a loop which prints the numbers 1 to 110, 11 numbers per line. The program shall print "Coza" in place of the numbers which are multiples of 3, "Loza" for multiples of 5, "Woza" for multiples of 7, "CozaLoza" for multiples of 3 and 5, and so on. Sample output:
   1 2 Coza 4 Loza Coza Woza 8 Coza Loza 11 
   Coza 13 Woza CozaLoza 16 17 Coza 19 Loza CozaWoza 22 
   23 Coza Loza 26 Coza Woza 29 CozaLoza 31 32 Coza
   ......
'''

n = 0

while n <= 110:
    p_str = ""

    for _ in range(11):
        n += 1

        if n % 3 == 0: p_str += "Coza"
        if n % 5 == 0: p_str += "Loza"
        if n % 7 == 0: p_str += "Woza"

        if (n % 3) * (n % 5) * (n % 7) != 0: p_str += str(n)

        p_str += " "

    print(p_str)


''' 23.
   Write code that will print out a times-table for practice and reference. It should look like this:
    * |  1  2  3  4  5  6  7  8  9
    -------------------------------
    1 |  1  2  3  4  5  6  7  8  9
    2 |  2  4  6  8 10 12 14 16 18
    3 |  3  6  9 12 15 18 21 24 27
    4 |  4  8 12 16 20 24 28 32 36
    5 |  5 10 15 20 25 30 35 40 45
    6 |  6 12 18 24 30 36 42 48 54
    7 |  7 14 21 28 35 42 49 56 63
    8 |  8 16 24 32 40 48 56 64 72
    9 |  9 18 27 36 45 54 63 72 81
'''

print('''* |  1  2  3  4  5  6  7  8  9
-------------------------------
1 |  1  2  3  4  5  6  7  8  9
2 |  2  4  6  8 10 12 14 16 18
3 |  3  6  9 12 15 18 21 24 27
4 |  4  8 12 16 20 24 28 32 36
5 |  5 10 15 20 25 30 35 40 45
6 |  6 12 18 24 30 36 42 48 54
7 |  7 14 21 28 35 42 49 56 63
8 |  8 16 24 32 40 48 56 64 72
9 |  9 18 27 36 45 54 63 72 81''')

''' 24. 
   Write code that will produce each of these visual outputs:
   # # # # # # #    # # # # # # #    # # # # # # #
   #           #      #       #      # #       # #
   #           #        #   #        #   #   #   #
   #           #          #          #     #     #
   #           #        #   #        #   #   #   #
   #           #      #       #      # #       # #
   # # # # # # #    # # # # # # #    # # # # # # #
'''

print('''# # # # # # #    # # # # # # #    # # # # # # #
#           #      #       #      # #       # #
#           #        #   #        #   #   #   #
#           #          #          #     #     #
#           #        #   #        #   #   #   #
#           #      #       #      # #       # #
# # # # # # #    # # # # # # #    # # # # # # #''')

''' 25. 
   Write code that will extract each digit from an int, in the reverse order. For example, if the int is 15423, the output shall be "3 2 4 5 1", with a space separating the digits.
   Hint: Use n % 10 to extract the least-significant digit; and n = n / 10 to discard the least-significant digit.
'''

n = 1234

s_n = str(n)
p_str = ""

while len(s_n) > 0:
    p_str += s_n[-1] + " "
    s_n = s_n[:-1]

print(p_str)


''' Sources
   http://www.bowdoin.edu/~ltoma/teaching/cs107/fall05/Lectures-Handouts/for.pdf
   http://www.ntu.edu.sg/home/ehchua/programming/java/j2a_basicsexercises.html
'''