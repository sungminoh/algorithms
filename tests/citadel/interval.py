# A ContentsInterval is triple of the following type: (date, date, Set[int])
# It encodes the presence of some set of integers between the two dates (inclusive on both sides of the interval)
# For example
#   (2020-01-02, 2020-01-04, {1,2,3}) indicates that the values 1, 2, 3 are present on dates 2020-01-02, 2020-01-03, 2020-01-04
# A List[ContentsInterval] encodes the presence of various sets of integers in different date regions
# For example:
import itertools
from heapq import heappop, heappush
from collections import Counter
from datetime import date, timedelta
from typing import Set, Any, List, Tuple, Iterator, Dict, Mapping
example_intervals = [
   (date(2020, 1, 1), date(2020, 1, 2), {1,2}),
   (date(2020, 1, 5), date(2020, 1, 6), {5}),
   (date(2020, 1, 2), date(2020, 1, 3), {1,2,3}),
   (date(2020, 1, 2), date(2020, 1, 2), {4}),
]
# Visually:
#    |   01   |   02   |   03   |   04   |   05   |   06   |   07   |   08   | (date axis)
#    [       1,2       ]
#                                        [        5        ]
#             [      1,2,3      ]
#             [    4   ]

class Interval:
    def __init__(self, start: date, end: date, contents: Set[Any]):
        self.start = start
        self.end = end
        self.contents = contents


def iter_dates(intervals):
    seen = set()
    ends = []
    for s, e in intervals:
        while ends[0] < s:
            closed_e = heappop(ends)
            if closed_e not in seen:
                seen.add(closed_e)
                yield closed_e
        if s not in seen:
            seen.add(s)
            yield s
        heappush(ends, e)


def iterate_over_counts(
    example_intervals: List[Tuple[date, date, Set[Any]]]
    ) -> Iterator[Tuple[date, Mapping[Any, int]]]:  # nlogn
    intervals: List[Interval] = [Interval(*args) for args in example_intervals]
    intervals.sort(key=lambda x: x.start) # nlogn
    dates: List[date] = sorted(list(set(itertools.chain(*[
        [interval.start, interval.end + timedelta(days=1)] for interval in intervals
        ]))))  # nlogn
    h: List[Interval] = []
    i = 0
    counter = Counter()
    # O(nlogn + nk)
    for d in dates:  # O(n)
        while i < len(intervals) and intervals[i].start <= d:
            interval = intervals[i]
            for n in interval.contents:   # k
                counter[n] += 1
            heappush(h, (interval.end, i))  # log(n)
            i += 1

        if h:
            end, interval_idx = h[0]
            while h and end < d:
                end, interval_idx = heappop(h)  # log(n)
                for n in intervals[interval_idx].contents:  # k
                    counter[n] -= 1
        yield d, dict(counter)


# - Write a function `iterate_over_counts` which allows users to iterate over any *changes* in the counts of integers across time.
# - The count of any integer is equal to the number of intervals that contain the integer on some date.
# - The function should return some iterable containing the date of change and a mapping of each value to its count.
# For example:
for date, counts in iterate_over_counts(example_intervals):
    print(f"Count changes on {date}")
    for value, count in counts.items():
        print(f"{value} -> {count}")
# The above program should print:
# Count changes on 2020-01-01
# 1 -> 1
# 2 -> 1
# Count changes on 2020-01-02
# 1 -> 2
# 2 -> 2
# 3 -> 1
# 4 -> 1
# ... and so on



#    |   01   |   02   |   03   |   04   |   05   |   06   |  (date axis)
#    [   1    ]
#    [        2        ]
#    [        3                 ]
#              [         1, 2, 3, 4      ]





#    |   01   |   02   |   03   |   04   |   05   |   06   |  (date axis)
#    [   1             ]
#    [        2        ]
#                      [         1, 2,   ]
"""
itervals.sort()
i = 0
for d in sort(set(chain(*[d for d in inervals]))):
    while intervals[i][0] <= d:
        # add count
        i += 1
    while heap[0].enddate < d:
        interval = heappop(heap)
        # deduct

"""


