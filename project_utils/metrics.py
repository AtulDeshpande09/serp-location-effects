

def jaccard_similarity(a, b):

    a = set(a)
    b = set(b)

    intersection = len(a.intersection(b))
    union = len(a.union(b))

    if union==0:
        return 1.0
    else:
        return intersection/union




def overlap(a, b):

    a = set(a)
    b = set(b)

    return len(a.intersection(b))



