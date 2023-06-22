import functools

PENNIES = "pennies"
NICKELS = "nickels"
DIMES = "dimes"
QUARTERS = "quarters"

bank = {PENNIES: 0, NICKELS: 0, DIMES: 0, QUARTERS: 0}


@functools.singledispatch
def count_coins(coins):
    raise NotImplementedError(f"Data type {type(coins)} is not supported :(")


@count_coins.register(float)
def _(coins):
    key = None
    match coins:
        case 0.01:
            key = PENNIES
        case 0.05:
            key = NICKELS
        case 0.10:
            key = DIMES
        case 0.25:
            key = QUARTERS
    bank[key] += 1


@count_coins.register(str)
def _(coins):
    converted = float(coins)
    count_coins(converted)


@count_coins.register(list)
def _(coins):
    for coin in coins:
        count_coins(coin)


@count_coins.register(dict)
def _(coins):
    for value in coins.values():
        count_coins(value)


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
