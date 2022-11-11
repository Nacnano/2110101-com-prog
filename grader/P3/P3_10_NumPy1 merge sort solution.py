import numpy as np


def eq(A, B, p):
    return np.sum(A == B) / np.prod(A.shape) >= p / 100


def closest_point_indexes(points, p):
    dis = (points[:][0] - p[0])**2 + (points[:][1]-p[1])**2
    return np.arange(dis.shape[0])[dis == np.max(dis)]


def merge_count_inversion(lst):
    lst = list(lst)
    if len(lst) <= 1:
        return lst, 0
    middle = int(len(lst) / 2)
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)


def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count


def number_of_inversions(A):
    lst, count = merge_count_inversion(A)
    return count
# FENWICK TREE SOLUTION
# def count_inversions(a):
#   res = 0
#   counts = [0]*(len(a)+1)
#   rank = { v : i+1 for i, v in enumerate(sorted(a)) }
#   for x in reversed(a):
# i = rank[x] - 1
# while i:
#   res += counts[i]
#   i -= i & -i
# i = rank[x]
# while i <= len(a):
#   counts[i] += 1
#   i += i & -i
#   return res


exec(input().strip())
