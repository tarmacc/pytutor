from collections import Counter
def sorting(array):
    counts = Counter(array)
    print(counts)
    result = sorted([[key] * value for key, value in counts.items()])
    return result
print(sorting([1,5,3,3,1,1,7,2,4,5,5,]))
