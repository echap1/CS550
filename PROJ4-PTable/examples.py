from prettytable import PrettyTable


# ------------------------------ Example 1 (Basics) ------------------------------ #

table = PrettyTable()  # Initialize the table

table.field_names = ["this", "is", "a", "pretty", "table"]  # Set the titles for each column

# Add the values for each row
table.add_row([12345, 756765, 134234, 4, 3434543543])
table.add_row(["abcdefg", "fdsf", "cool stuff", "fun", "pretty tables"])
table.add_row(["dfds", "dfgdfgdfg", "ddfgffg", "dfgfdgfdgfd", "dgfdgfdgfdgf"])

print(table)

# Output:
#
# +---------+-----------+------------+-------------+---------------+
# |   this  |     is    |     a      |    pretty   |     table     |
# +---------+-----------+------------+-------------+---------------+
# |  12345  |   756765  |   134234   |      4      |   3434543543  |
# | abcdefg |    fdsf   | cool stuff |     fun     | pretty tables |
# |   dfds  | dfgdfgdfg |  ddfgffg   | dfgfdgfdgfd |  dgfdgfdgfdgf |
# +---------+-----------+------------+-------------+---------------+


# ------------------------------ Example 2 (Adding columns) ------------------------------ #

table = PrettyTable()  # Initialize the table

table.field_names = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]  # Set the titles for each column

# Add 5 rows to the tables
table.add_row(["Adding rows", "to table", "is", "very", "cool"])
table.add_row(["Adding rows", "to table", "is", "very", "cool"])
table.add_row(["Adding rows", "to table", "is", "very", "cool"])
table.add_row(["Adding rows", "to table", "is", "very", "cool"])
table.add_row(["Adding rows", "to table", "is", "very", "cool"])

# Add a column to the table (column length must equal the number of rows in the table (currently 5)
table.add_column("Cool Column", ["You", "Can", "Also", "Add", "Columns"])

print(table)

# Output:
#
# +-------------+----------+----------+----------+----------+-------------+
# |   Column 1  | Column 2 | Column 3 | Column 4 | Column 5 | Cool Column |
# +-------------+----------+----------+----------+----------+-------------+
# | Adding rows | to table |    is    |   very   |   cool   |     You     |
# | Adding rows | to table |    is    |   very   |   cool   |     Can     |
# | Adding rows | to table |    is    |   very   |   cool   |     Also    |
# | Adding rows | to table |    is    |   very   |   cool   |     Add     |
# | Adding rows | to table |    is    |   very   |   cool   |   Columns   |
# +-------------+----------+----------+----------+----------+-------------+


# ------------------------------ Example 3 (CSV File) ------------------------------ #

from prettytable import from_csv

file = open("example.csv", "r")  # Open the csv file

table = from_csv(file)  # Load the csv into the table

print(table)

# Output:
#
# +------+-----+-----+-------------+--------------+
# | Name | Sex | Age | Height (in) | Weight (lbs) |
# +------+-----+-----+-------------+--------------+
# | Alex |  M  |  41 |      74     |     170      |
# | Bert |  M  |  42 |      68     |     166      |
# | Carl |  M  |  32 |      70     |     155      |
# | Dave |  M  |  39 |      72     |     167      |
# | Elly |  F  |  30 |      66     |     124      |
# | Fran |  F  |  33 |      66     |     115      |
# | Gwen |  F  |  26 |      64     |     121      |
# | Hank |  M  |  30 |      71     |     158      |
# | Ivan |  M  |  53 |      72     |     175      |
# | Jake |  M  |  32 |      69     |     143      |
# | Kate |  F  |  47 |      69     |     139      |
# | Luke |  M  |  34 |      72     |     163      |
# | Myra |  F  |  23 |      62     |      98      |
# | Neil |  M  |  36 |      75     |     160      |
# | Omar |  M  |  38 |      70     |     145      |
# | Page |  F  |  31 |      67     |     135      |
# | Quin |  M  |  29 |      71     |     176      |
# | Ruth |  F  |  28 |      65     |     131      |
# +------+-----+-----+-------------+--------------+


# ------------------------------ Example 4 (Slicing) ------------------------------ #

table = PrettyTable()

table.add_row("This is the row 0".split(" "))
table.add_row("This is the row 1".split(" "))
table.add_row("This is the row 2".split(" "))
table.add_row("This is the row 3".split(" "))
table.add_row("This is the row 4".split(" "))
table.add_row("This is the row 5".split(" "))
table.add_row("This is the row 6".split(" "))
table.add_row("This is the row 7".split(" "))
table.add_row("This is the row 8".split(" "))
table.add_row("This is the row 9".split(" "))
table.add_row("This is the row 10".split(" "))
table.add_row("This is the row 11".split(" "))
table.add_row("This is the row 12".split(" "))

print(table[5:10], "\n")

table = table[2:4]

print(table)

# Output:
#
# +---------+---------+---------+---------+---------+
# | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 |
# +---------+---------+---------+---------+---------+
# |   This  |    is   |   the   |   row   |    5    |
# |   This  |    is   |   the   |   row   |    6    |
# |   This  |    is   |   the   |   row   |    7    |
# |   This  |    is   |   the   |   row   |    8    |
# |   This  |    is   |   the   |   row   |    9    |
# +---------+---------+---------+---------+---------+
#
# +---------+---------+---------+---------+---------+
# | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 |
# +---------+---------+---------+---------+---------+
# |   This  |    is   |   the   |   row   |    2    |
# |   This  |    is   |   the   |   row   |    3    |
# +---------+---------+---------+---------+---------+


# ------------------------------ Example 5 (Built-in styles) ------------------------------ #

from prettytable.prettytable import DEFAULT, MSWORD_FRIENDLY, PLAIN_COLUMNS

table = PrettyTable()

table.add_row("This is the row 0".split(" "))
table.add_row("This is the row 1".split(" "))
table.add_row("This is the row 2".split(" "))
table.add_row("This is the row 3".split(" "))
table.add_row("This is the row 4".split(" "))
table.add_row("This is the row 5".split(" "))

table.set_style(DEFAULT)
print(table, "\n")
table.set_style(MSWORD_FRIENDLY)
print(table, "\n")
table.set_style(PLAIN_COLUMNS)
print(table)

# Output:
#
# +---------+---------+---------+---------+---------+
# | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 |
# +---------+---------+---------+---------+---------+
# |   This  |    is   |   the   |   row   |    0    |
# |   This  |    is   |   the   |   row   |    1    |
# |   This  |    is   |   the   |   row   |    2    |
# |   This  |    is   |   the   |   row   |    3    |
# |   This  |    is   |   the   |   row   |    4    |
# |   This  |    is   |   the   |   row   |    5    |
# +---------+---------+---------+---------+---------+
#
# | Field 1 | Field 2 | Field 3 | Field 4 | Field 5 |
# |   This  |    is   |   the   |   row   |    0    |
# |   This  |    is   |   the   |   row   |    1    |
# |   This  |    is   |   the   |   row   |    2    |
# |   This  |    is   |   the   |   row   |    3    |
# |   This  |    is   |   the   |   row   |    4    |
# |   This  |    is   |   the   |   row   |    5    |
#
# Field 1        Field 2        Field 3        Field 4        Field 5
#   This            is            the            row             0
#   This            is            the            row             1
#   This            is            the            row             2
#   This            is            the            row             3
#   This            is            the            row             4
#   This            is            the            row             5


# ------------------------------ Example 6 (Custom styles) ------------------------------ #

import prettytable

table = PrettyTable()

table.vertical_char = "!"
table.horizontal_char = "~"
table.junction_char = "#"

table.padding_width = 1

table.hrules = prettytable.ALL
table.vrules = prettytable.ALL

table.border = True
table.header = False

table.add_row("This is the row 0".split(" "))
table.add_row("This is the row 1".split(" "))
table.add_row("This is the row 2".split(" "))
table.add_row("This is the row 3".split(" "))
table.add_row("This is the row 4".split(" "))
table.add_row("This is the row 5".split(" "))

print(table)

# Output:
#
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 0 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 1 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 2 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 3 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 4 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#
# ! This ! is ! the ! row ! 5 !
# #~~~~~~#~~~~#~~~~~#~~~~~#~~~#