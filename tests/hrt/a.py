#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyright © 2022 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are aggregating data from k IOT devices. Each source sends pairs of timestamp (in minutes) and temperature. As an example, the data may look like
Stream 0: (9:31, 70), (9:32, 72), (9:33, 74), ...
Stream 1: (9:31, 90), (9:32, 92), (9:33, 94), ...

Each stream is guaranteed to be ordered, but messages will be received one at a time with no guarantee on ordering among streams.  Streams might not report data for every minute.

Implement the code below to output the average temperature across devices for each minute. Your code should output data as soon as it can be known. In the example above, we should produce

931 80.0 (logged by record 2)
932 82.0 (logged by record 4)
933 84.0 (logged by record 6)
"""
from heapq import heappush, heappop
from collections import deque


class Aggregator:
    def __init__(self, num_streams):
        self.counter = 0
        self.deques = [deque() for _ in range(num_streams)]
        self.latest_timestamps = [0]*num_streams

    def _output(self, minute: int, avg_temp: float):
        print(f"{minute} {avg_temp:.1f} (logged by record {self.counter})")

    def record(self, stream_no: int, minute: int, temp: float):
        """
        TC: O(k)
        """
        self.counter += 1
        self.deques[stream_no].append((minute, temp))
        self.latest_timestamps[stream_no] = minute

        while True:
            min_stream_timestamp = float('inf')
            for latest_timestamp, d in zip(self.latest_timestamps, self.deques):
                data_timestamp = d[0][0] if d else float('inf')
                stream_timestamp = min(latest_timestamp, data_timestamp)
                min_stream_timestamp = min(min_stream_timestamp, stream_timestamp)

            temp_sum = 0
            data_cnt = 0
            for d in self.deques:
                if d and d[0][0] == min_stream_timestamp:
                    temp_sum += d.popleft()[1]
                    data_cnt += 1

            if data_cnt > 0:
                self._output(min_stream_timestamp, temp_sum/data_cnt)
            else:
                break

    def close(self):
        self.counter += 1
        def consume(i):
            d = self.deques[i]
            if d:
                # minute, temp, stream_id
                heappush(heap, (*d.popleft(), i))

        heap = []
        for i in range(len(self.deques)):
            consume(i)

        while heap:
            m, t, i = heappop(heap)
            cnt = 1
            consume(i)
            while heap and heap[0][0] == m:
                _, another_t, another_i = heappop(heap)
                t += another_t
                cnt += 1
                consume(another_i)
            self._output(m, t/cnt)

class Aggregator:
    def __init__(self, num_streams):
        self.counter = 0
        self.deques = [deque() for _ in range(num_streams)]
        self.empty_streams = set(list(range(num_streams)))
        self.heap = []

    def _output(self, minute: int, avg_temp: float):
        print(f"{minute} {avg_temp:.1f} (logged by record {self.counter})")

    def record(self, stream_no: int, minute: int, temp: float):
        self.counter += 1
        self.deques[stream_no].append((minute, temp))
        if len(self.deques[stream_no]) == 1:
            heappush(self.heap, (minute, temp, stream_no))
            self.empty_streams.remove(stream_no)
        self._consume()

    def _pop(self):
        m, t, i = heappop(self.heap)
        self.deques[i].popleft()  # the same as element poped from the heap
        if self.deques[i]:
            heappush(self.heap, (*self.deques[i][0], i))
        else:
            self.empty_streams.add(i)
        return m, t, i

    def _consume(self):
        while not self.empty_streams and self.heap:
            cnt = 1
            m, t, i = self._pop()
            while (not self.empty_streams or self.empty_streams=={i})\
                    and self.heap and self.heap[0][0] == m:
                t += self._pop()[1]
                cnt += 1
            self._output(m, t/cnt)

    def close(self):
        self.counter += 1
        while self.heap:
            cnt = 1
            m, t, i = self._pop()
            while self.heap and self.heap[0][0] == m:
                t += self._pop()[1]
                cnt += 1
            self._output(m, t/cnt)


def test1():
    agg = Aggregator(2)
    agg.record(0, 931, 70.0)
    agg.record(1, 931, 90.0)
    agg.record(0, 932, 72.0)
    agg.record(1, 932, 92.0)
    agg.record(0, 933, 74.0)
    agg.record(1, 933, 94.0)
    agg.close()


def test2():
    agg = Aggregator(2)
    agg.record(0, 931, 70.0)
    agg.record(1, 931, 90.0)
    agg.record(0, 932, 72.0)
    agg.record(0, 933, 74.0)
    agg.record(1, 933, 94.0)
    agg.close()


def test3():
    agg = Aggregator(2)
    agg.record(0, 931, 70.0)
    agg.record(1, 931, 90.0)
    agg.record(0, 932, 72.0)
    agg.record(0, 933, 74.0)
    agg.close()


def test4():
    agg = Aggregator(1)
    agg.record(0, 931, 70.0)
    agg.record(0, 932, 72.0)
    agg.record(0, 933, 74.0)
    agg.close()


def test5():
    agg = Aggregator(2)
    agg.record(0, 931, 70.0)
    agg.record(0, 932, 72.0)
    agg.record(0, 933, 74.0)
    agg.record(1, 931, 90.0)
    agg.record(1, 932, 92.0)
    agg.record(1, 933, 94.0)
    agg.close()


def test6():
    agg = Aggregator(2)
    agg.record(1, 935, 70.0)
    agg.record(1, 936, 72.0)
    agg.record(0, 931, 90.0)
    agg.record(0, 932, 92.0)
    agg.close()


def main():
    test1()
    print('\n')
    test2()
    print('\n')
    test3()
    print('\n')
    test4()
    print('\n')
    test5()
    print('\n')
    test6()




if __name__ == "__main__":
    main()

