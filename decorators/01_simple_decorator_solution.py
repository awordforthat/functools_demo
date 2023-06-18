global_sum = 0  # Don't use mutable global variables 🙃


def call_twice(func):
    """
    This function returns a wrapper function that executes the original twice.
    """

    def wrapper():
        func()
        func()

    return wrapper


@call_twice
def increment():
    """This is a function that should always be invoked twice"""
    global global_sum
    global_sum += 1


increment()


print(global_sum)
assert global_sum == 2
