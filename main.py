from pprint import pprint


def edit_distance(src, target):
    m = len(src)
    n = len(target)
    distance = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(len(distance)):
        distance[i][0] = i
    for i in range(len(distance[0])):
        distance[0][i] = i
    for i in range(1, len(distance)):
        for j in range(1, len(distance[0])):
            delete = distance[i-1][j] + 1
            insert = distance[i][j-1] + 1
            if src[i-1] == target[j-1]:
                substitute = distance[i-1][j-1]
            else:
                substitute = distance[i-1][j-1] + 2
            distance[i][j] = min([insert, delete, substitute])
    pprint(distance)
    return distance[m][n]


print(edit_distance("intention", "extension"))
