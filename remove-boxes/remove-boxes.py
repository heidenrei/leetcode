class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        Interval = namedtuple("Interval", ["color", "length"])
        intervals = [Interval(color, len(list(group))) for color, group in groupby(boxes)]
        color_indexes = defaultdict(list)
        for index, interval in enumerate(intervals):
            color_indexes[interval.color].append(index)

        @cache
        def max_points(left, right, k):
            if left > right:
                return 0

            interval = intervals[left]
            if left != right and interval.color == intervals[right].color:
                return max_points(left, right - 1, k + intervals[right].length)

            k += interval.length
            best = k ** 2 + max_points(left + 1, right, 0)
            indexes = color_indexes[interval.color]
            for mid in islice(indexes, bisect_left(indexes, left) + 1, bisect_left(indexes, right)):
                best = max(best, max_points(left + 1, mid - 1, 0) + max_points(mid, right, k))
            return best

        return max_points(0, len(intervals) - 1, 0)
            