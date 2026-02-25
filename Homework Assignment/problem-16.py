def merge_intervals(intervals):
    intervals.sort()
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result


n = int(input("Enter number of intervals: "))
intervals = []
for i in range(n):
    start, end = map(int, input("Enter start and end: ").split())
    intervals.append([start, end])
print("Merged intervals:", merge_intervals(intervals))
