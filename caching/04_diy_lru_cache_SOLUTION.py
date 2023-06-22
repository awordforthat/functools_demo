class Node:
    """
    A Node wraps a key/value pair, and stores a reference to the Node ahead of it
    and the Node behind it.

    Keys should be hashable, although this is not enforced.
    """

    def __init__(self, value, key):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key

    def __str__(self):
        return f"{self.key}: {self.value}"


class LRUCache:
    """
    The LRUCache stores Nodes such that the list never grows beyond a given size, and the
    least-used values are the first to leave the cache as nodes are dropped.
    """

    def __init__(self, max_size):
        self.max_size = max_size
        self.first = None
        self.last = None
        self.nodes = {}

    def get(self, key):
        """
        If a value exists for the given key, returns it. Otherwise, returns None.

        A node that is accessed via this method is "used" and moves to the end of the list.
        """
        if key in self.nodes:
            node = self.nodes[key]
            self._move_to_end(node)
            return node

    def put(self, node):
        """
        Adds a node to the end of the list.
        """
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
        """
        Prints the contents of the cache.
        """
        next_node = self.first
        result = []
        while next_node:
            result.append((next_node.key, next_node.value))
            next_node = next_node.next
        print(result)


def lru_cache(maxsize):
    def inner_lru(func):
        lru = LRUCache(maxsize)
        cache_info = {"hits": 0, "misses": 0}

        def wrapper(*args):
            cached_result = lru.get(args)
            if cached_result is not None:
                cache_info["hits"] += 1
                return cached_result
            computed_result = func(*args)
            cache_info["misses"] += 1
            lru.put(Node(computed_result, args))
            return computed_result

        return wrapper

    return inner_lru


@lru_cache(2)
def add(a, b):
    return a + b
