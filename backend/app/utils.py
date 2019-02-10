
from functools import reduce
from itertools import groupby
from operator import add, itemgetter


def merge_records_by(key, combine):
    return lambda first, second: {
        k: first[k] if k == key else combine(first[k], second[k])
        for k in first
    }


def merge_list_of_records_by(key, combine):
    keyprop = itemgetter(key)
    return lambda lst: [
        reduce(merge_records_by(key, combine), records)
        for _, records in groupby(sorted(lst, key=keyprop), keyprop)
    ]
