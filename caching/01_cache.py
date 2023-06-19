"""
This exercise is to check your understanding of how caches work. There's not much 
implementation to be done (just one line) - rather, your job is to make the assertions
pass.

So first, add the cache decorator to the `factorial` function. The `functools` module
has been imported for you already.

Next, work through each of the assertion blocks. In the first block, fill in how many
hits and misses you expect to see after the first call to `factorial`.

Now uncomment the next block. In this block, `factorial` has been called with a value 
that doesn't match the assertions. Fill in the correct value.

Finally, uncomment the last block. The cache has been cleared. Just as you did with the first
block, fill in the number of hits and misses so that the assertions pass.
"""

import functools


def factorial(n):
    return n * factorial(n - 1) if n else 1


factorial(10)
assert factorial.cache_info().hits == None
assert factorial.cache_info().misses == None

# factorial(1)
# assert factorial.cache_info().hits == 1
# assert factorial.cache_info().misses == 18

# factorial.cache_clear()
# factorial(5)
# assert factorial.cache_info().hits == None
# assert factorial.cache_info().misses == None
