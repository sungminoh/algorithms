import heapq
from typing import Tuple
from typing import Any
from typing import List

def k_shortest(edges: List[Tuple[Any, Any, Any]], s, e, k):
    g = {}
    for a, b, w in edges:
        g.setdefault(a, {}).setdefault(b, w)
        g.setdefault(b, {}).setdefault(a, w)

    heap = [(0, s)]
    count = {}
    i = 0
    while heap:
        d, u = heapq.heappop(heap)
        if count[u] >= k: break

        count[u] += 1
        if u == e:
            if count[u] == k:
                return d

        for v, w in g[u].items():
            heapq.heappush(heap, (d+w, v))

    return None















