from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])   # sort the intervals by the first value in each interval
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = output[-1][1]

            if prev_end >= start:   # ex) [1,3], [2,6]
                output[-1][1] = max(prev_end, end)   # compare 3 and 6
            else:
                output.append([start, end])
        return output