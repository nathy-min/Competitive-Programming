class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        output = []
        current_interval = intervals.pop(0)
        while intervals:
            next_interval = intervals.pop(0)
#             check if next two intervals overlap
            if current_interval[1] >= next_interval[0]:
                current_interval = [current_interval[0], max(
                    next_interval[1], current_interval[1])]

            else:
                output.append(current_interval)
                current_interval = next_interval
        output.append(current_interval)
        return output