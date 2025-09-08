from itertools import combinations

def jaccard(a, b):

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



def jaccard_matrix(dic):

    jaccard_dic = {}

    for query in dic.keys():
        n = len(dic[query])
        jaccard_matrix = [[1.0]*n for _ in range(n)]
        res_list = []
        for loc, result in dic[query].items():
            
            res_list.append(result)

        for (i, list_i), (j, list_j) in combinations(enumerate(res_list),2):

            res = jaccard(list_i,list_j)

            jaccard_matrix[i][j] = res
            jaccard_matrix[j][i] = res
        
        jaccard_dic[query] = jaccard_matrix

    return jaccard_dic
