"""
CS550 Homework: Random Walk
Due January 11, 2019

@author: Ethan Chapman

Part A: What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?
    This is a harder question than it seems. You can't just do random walks of length n, and calculate the percent
    that they are of distance 4 from the origin. This is because the walks are random, and the percents vary from
    run to run, unless you account for every walk of length n, of which there are 4 ** n, and that number is way
    to high to compute in a reasonable amount of time. So, we need to think of another method.

    My method to do this is start out with a grid that contains the amount of ways that each point can be reached when
    n=0, which would be

        00000
        00000
        00100
        00000
        00000

    with the center representing the origin. To calculate the grid for n=1, for a given point (a, b), we calculate the
    sum of the values around that point, and that is it's new value. It would be

        00000
        00100
        01010
        00100
        00000

    and for n=2

        00100
        02020
        10401
        02020
        00100

    and so on. To find out the percent of walks that are within 4 steps, we just take the sum of squares that are within
    4 steps of the origin and divide it by the sum of the grid.

    Conclusion:
        The largest value is n=22, with a percent of 50.93980588580962

Part B: imagine you are throwing darts at a square dartboard, which has a circle perfectly inscribed in the square.
    Let's say the location of the center of the dartboard is 0,0, and the side length of the square is 2, giving the
    circle a radius of 1. Keep track of the number of times that your dart lands within the circle in 100 tries. Now,
    multiply that number by 4, and divide by the number of darts you threw. What value do you get? Repeat the
    simulation, but with 1000 darts... and 10,000 darts... and 100,000 darts. What do you notice about the output?

    The number approaches pi. this is because the area of the square is 4, and the area of the circle is pi. So, the
    probability of a dart landing in the circle is pi / 4. Multiplying that by 4 gives pi.
"""


# Part A ---------------------------------------------------------------------------------------------------------------


def increase_dimensions(x, k=1):  # Makes a list bigger by adding zeros to all sides k times
    l = [[0] * (len(x[0]) + (2 * k)) for _ in range(k)]
    return l + [([0] * k) + i + ([0] * k) for i in x] + l


def decrease_dimensions(x, k=1):  # Makes a list smaller by removing the edges k times
    return [i[k:-k] for i in x[k:-k]]


def get_grid(n, n_minus_one=None):  # Gets the grid given n steps
    if n == 0: return [[1]]  # Return the grid for n=0 if n=0

    # If we don't already have the previous grid, calculate it
    if n_minus_one is None:
        n_minus_one = get_grid(n - 1)

    # Resize n_minus_one and create the new grid (dimensions increased twice to avoid edge cases in below for loop
    n_minus_one = increase_dimensions(n_minus_one, 2)
    new_list = [i.copy() for i in n_minus_one]

    l = len(new_list[0]) - 2  # The size of the actual grid we will return

    # Loop through all non-edge points and calculate their value based on the old grid
    for x in range(1, l + 1):
        for y in range(1, l + 1):
            new_list[x][y] = sum([n_minus_one[x][y + 1],
                                  n_minus_one[x][y - 1],
                                  n_minus_one[x + 1][y],
                                  n_minus_one[x - 1][y],])

    return decrease_dimensions(new_list)  # Return the properly sized grid


def num_in_range(grid, steps):  # Calculate how many routes are within <steps> steps of the origin
    res = 0  # The result

    n = len(grid[0])  # The size of the grid
    c = int((n - 1) / 2)  # The center of the grid (the origin, x and y are both c)

    for x in range(n):  # Loop through all points
        for y in range(n):
            if abs(x - c) + abs(y - c) <= steps:  # If the current point is within <steps> steps of the origin
                res += grid[x][y]  # Add it's number of routes to the result

    return res


print("Part A:")

n = 0  # The current number of steps
allowedSteps = 4  # The allowed number of steps for calculating the percent
prev_grid = None  # The grid from the previous calculation (currently none)
percent = 1  # The percent of walkable routes (currently 1)

percents = []

for n in range(100):
    # Get the grid for this iteration (using the previous grid if there is one)
    if prev_grid is None:
        grid = get_grid(n)
    else:
        grid = get_grid(n, prev_grid)

    grid_sum = sum(map(sum, grid))  # Find the sum of the 2d grid (just sum(grid) doesn't work)

    percent = num_in_range(grid, allowedSteps) / grid_sum  # Find the percent walkable by dividing the walkable num by the sum

    print(f"    n={n}, {percent * 100} walkable, {'OK' if percent > .5 else 'FAIL'}")

    percents += [percent]

    prev_grid = grid  # Update the previous grid

for n in range(len(percents) - 1, -1, -1):
    if percents[n] > 0.5:
        print(f"\n    Largest Solution: n={n}, {percents[n] * 100}% walkable\n")
        break


# Part B ---------------------------------------------------------------------------------------------------------------


import random


print("Part B:")


def darts(tries):  # Calculates the number of darts that land inside of the circle for a given number of throws
    in_circle = 0

    for i in range(tries):
        num = complex(random.uniform(-1, 1), random.uniform(-1, 1))  # Generate a random point from ((-1, -1) to (1,1))

        if abs(num) <= 1:  # If the point is in the circle
            in_circle += 1  # Add one to the number

    return in_circle


for tries in [100, 1000, 10000]:  # Loop through all of the numbers of darts
    in_circle = darts(tries)  # Calculate the number that landed in the circle
    print(f"    {tries} tries, {in_circle} in the circle, n={in_circle * 4 / tries}")  # Print the number and other info
