"""
This exercise is to check your understanding of how Least Recently Used caches work. 
There's not much implementation to be done (just one line) - rather, your job is to
make the assertions pass. Note that each block builds on the last, so don't comment 
any blocks out or clear the cache. The idea is to figure out the state of the cache at 
each step, and for each new call to `factorial`, predict how many hits and misses the 
cache will report. 

So first, add the lru_cache decorator to the `factorial` function. Give the cache 
a maximum size of 5. (don't get this number wrong! The tests depend on it.)

Next, work through each of the assertion blocks. In the first block, replace 'None'
on each line with the number of cache hits and misses you expect to see. 

Uncomment each of the next blocks, one at a time. For each block, try to predict the
state of the cache. Fill in the appropriate number of hits and misses. 

Once you've filled in the right numbers, running the script should complete with no 
assertion errors.
"""

import functools


def factorial(n):
    return n * factorial(n - 1) if n else 1


factorial(5)
assert factorial.cache_info().hits == None
assert factorial.cache_info().misses == None


# factorial(5)
# assert factorial.cache_info().hits == None
# assert factorial.cache_info().misses == None

# factorial(0)
# assert factorial.cache_info().hits == None
# assert factorial.cache_info().misses == None

# factorial(7)
# assert factorial.cache_info().hits == None
# assert factorial.cache_info().misses == None
