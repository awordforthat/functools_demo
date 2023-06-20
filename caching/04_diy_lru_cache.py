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
            self.move_to_end(node)
            return node

    def put(self, node):
        # A better implementation would check for a naming clash here
        if len(self.nodes) >= self.max_size:
            del self.nodes[self.first.key]
            self.first = self.first.next
            self.first.prev = None
            assert len(self.nodes) <= self.max_size

        if len(self.nodes) == 0:
            self.first = node
            self.last = node

        else:
            assert self.last is not None
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.nodes[node.key] = node

    def move_to_end(self, node):
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
    def inner_lru(func):
        lru = LRUCache(maxsize)
        cache_info = {"hits": 0, "misses": 0}

        def wrapper(*args):
            cached_result = lru.get(args)
            if cached_result is not None:
                cache_info["hits"] += 1
                print(cache_info)
                return cached_result
            computed_result = func(*args)
            cache_info["misses"] += 1
            print(cache_info)

            lru.put(Node(computed_result, args))
            return computed_result

        return wrapper

    return inner_lru


@lru_cache(2)
def add(a, b):
    return a + b


add(1, 2)
add(1, 2)
add(1, 2)
add(3, 4)
add(1, 4)
