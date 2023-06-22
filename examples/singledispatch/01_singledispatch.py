"""
In this exercise, you'll write a set of singledispatch functions to count up 
the number of each type of coin represented in the data. The coins are listed
for you in constants at the top, and there is also a `bank` dictionary where
you can record the number of coins you find.

To solve this exercise, complete these steps:


1. The first function (count_coins) has been provided for you. Add the decorator from functools
that will turn it into a singledispatch generic function.

2. Next, register an overload implementation function for floats. This should take in one parameter, 
and based on its value, increment the values in `bank` - e.g, if you see the value 0.01, add one to 
PENNIES, if you see 0.05, add one to NICKELS, etc.

3. Now register an overload for strings. It should do the same thing as the float handler, but it 
should handle strings gracefully.

4. Register an overload for lists. It should iterate over the list and count each entry as described above.

5. Finally, register an overload for dictionaries. You will only be processing the values here, ignoring the
keys. Assume each value is a single coin, and count it accordingly.

At the bottom of the file, there is a small test suite and a set of assertions. Your solution is correct
if you run the script (`python 01_singledispatch.py`) and there are no assertion errors.

"""

import functools

PENNIES = "pennies"  # 0.01
NICKELS = "nickels"  # 0.05
DIMES = "dimes"  # 0.10
QUARTERS = "quarters"  # 0.25

bank = {PENNIES: 0, NICKELS: 0, DIMES: 0, QUARTERS: 0}


# decorate this function
def count_coins(coins):
    raise NotImplementedError(f"Data type {type(coins)} is not supported :(")


# put your overload implemenations here

loose_change = [0.05, "0.25", 0.01, 0.01, 0.05, "0.10", "0.01", 0.25, 0.25]
purchases = {
    "gumball": 0.10,
    "pencil": "0.25",
    "gum": 0.01,
    "keychain": "0.05",
    "candy": [0.01, "0.25", 0.10, 0.25, 0.10, "0.25"],
}

count_coins(loose_change)
count_coins(purchases)

print(bank)

assert bank[PENNIES] == 5
assert bank[NICKELS] == 3
assert bank[DIMES] == 4
assert bank[QUARTERS] == 7
