import sys
import pytest
from typing import List
import bisect
import itertools


#If no points found, return None instread of string "None"
def findNearestCities(
    numOfPoints: int,
    points: List[str],
    xCoordinates: List[int],
    yCoordinates: List[int],
    numOfQueriedPoints: int,
    queriedPoints: List[str]) -> List[str]:
    d = {}
    rows = {}
    cols = {}
    for p, x, y in zip(points, xCoordinates, yCoordinates):
        d[p] = (x, y)
        rows.setdefault(x, []).append(p)
        cols.setdefault(y, []).append(p)
    for arr in rows.values():
        arr.sort(key=lambda p: d[p][1])
    for arr in cols.values():
        arr.sort(key=lambda p: d[p][0])

    def find_closest(points, point, xy):
        v = point[xy]
        values = [d[p][xy] for p in points]
        i = bisect.bisect_left(values, v)
        mp, mn = None, float('inf')
        if i > 0:
            p = points[i-1]
            v = abs(v-values[i-1])
            if v < mn:
                mn = v
                mp = p
        if i < len(points)-1:
            p = points[i+1]
            v = abs(v-values[i+1])
            if v < mn:
                mn = v
                mp = p
        return mp, mn

    ret = []
    for q in queriedPoints:
        x, y  = d[q]
        mp, mn = find_closest(rows.get(x, set()), d[q], xy=1)
        p, v = find_closest(cols.get(y, set()), d[q], xy=0)
        if v < mn:
            mn = v
            mp = p
        ret.append(mp)
    return ret


@pytest.mark.parametrize(('args'), [
    ((3,
      ["p1","p2","p3"],
      [30, 20, 10],
      [30, 20, 30],
      3,
      ["p3", "p2", "p1"],
      ["p1", None, "p3"])),
    ((5,
      ["p1", "p2","p3", "p4", "p5"],
      [10, 20, 30, 40, 50],
      [10, 20, 30, 40, 50],
      5,
      ["p1", "p2", "p3", "p4", "p5"],
      [None, None, None, None, None])),
])
def test(args):
    assert args[-1] == findNearestCities(*args[:-1])


def main():
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))


if __name__ == '__main__':
    main()
