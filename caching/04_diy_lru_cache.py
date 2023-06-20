"""
In this example, you'll implement your own LRU cache, mimicking the behavior of `functools.lru_cache`. 

You can do either part 1 and part 2 here, or you can go straight to part 2 (do this if you're short on time).

The first option is to write your own LRU cache, as well as the decorator. In this case, delete the Node class
as well as the LRUCache class.
The solution provided uses a doubly-linked list, but 
there are many other options. As a reminder, your LRU cache should: 
    - take in a max size parameter
    - accept new values, and add them to the end of the cache
    - if accepting a new value will make the size of the cache exceed the maximum, 
        you should remove the oldest value
    - identify values by a unique key
    - allow looking up values by key
    - if a value is accessed by key, it is now "most recently used" and should be moved to the end
        of the cache
Once you've done that, move on to the second part.

The second option/part is to use the provided implementation of a LRU cache and just write the decorator
that wraps a function and uses the cache to keep track of which values have been accessed.
A stub function called `lru_cache` has been provided. Your solution should:
    - keep track of cache hits and misses
    - try to look up a value in the cache based on the provided arguments (your choice whether to pay attention to types or not!)
    - if the value is found, return it immediately, and increment cache hits by 1
    - if the value is not found, add it to the cache, using the provided arguments as a key. Increment cache misses by 1

Note: a solution that accepts a `maxsize` parameter will require you to write a doubly-nested 
decorator. If you want, you can start by hard-coding the max size and checking that the caching logic
works first. That simplifies the problem a bit, and you can add the maxsize parameter in later.
"""


class Node:
    def __init__(self, value, key):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key

    def __str__(self):
        return f"{self.key}: {self.value}"


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.first = None
        self.last = None
        self.nodes = {}

    def get(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            self._move_to_end(node)
            return node

    def put(self, node):
        # A better implementation would check for a naming clash here
        if len(self.nodes) >= self.max_size:
            del self.nodes[self.first.key]
            self.first = self.first.next
            self.first.prev = None

        if len(self.nodes) == 0:
            self.first = node
            self.last = node

        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.nodes[node.key] = node

    def _move_to_end(self, node):
        if self.last is node:
            return

        if self.first is node:
            self.first = node.next
            if node.next:
                node.next.prev = None
        else:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

        self.last.next = node
        node.prev = self.last
        node.next = None
        self.last = node

    def print_cache(self):
        next_node = self.first
        result = []
        while next_node:
            result.append((next_node.key, next_node.value))
            next_node = next_node.next
        print(result)


def lru_cache(maxsize):
    # write your decorator here
    pass


@lru_cache(2)
def add(a, b):
    return a + b
