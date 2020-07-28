from pprint import pprint

'''
Dynamic programming algorithm for minimum edit distance
subproblem: to reach target[0...n] from src[0...m] optimally,
we should reach target[0...j] from src[0...i] optimally
'''
def edit_distance(src, target):
    m = len(src)
    n = len(target)
    # initializing the distance matrix of size m+1 x n+1
    distance = [[0 for j in range(n+1)] for i in range(m+1)]
    # initializing the action matrix for tracing back steps for minimum edit
    action = [["" for j in range(n+1)] for i in range(m+1)]
    # initializing trivial cases:

    # where target is empty string
    for i in range(len(distance)):
        distance[i][0] = i
        if i > 0:
            action[i][0] = "delete {}".format(src[i-1])

    # where src is empty string
    for i in range(len(distance[0])):
        distance[0][i] = i
        if i > 0:
            action[0][i] = "insert {}".format(target[i - 1])
    # pprint(action)
    '''
    Levenstien distance is used to calculate distance which defines edit distances as follows:
    cost of insertion/deletion = 1 unit
    cost of substituting asimilar letters = cost of insertion + cost of deletion = 2 units
    cost of substituting similar letters = 0
    '''
    for i in range(1, len(distance)):
        for j in range(1, len(distance[0])):
            # to get target[0...j] from src[0...i]

            # what if we delete src[i] from src[0..i]
            delete = distance[i-1][j] + 1

            # what if we insert target[j] into src[0...i]
            insert = distance[i][j-1] + 1

            # what if we substitute src[i] with target[j] in src[0...i]
            if src[i-1] == target[j-1]:
                substitute = distance[i-1][j-1]
            else:
                substitute = distance[i-1][j-1] + 2

            # optimal edit distance to get target[0...j] from src[0...i]
            distance[i][j] = min([insert, delete, substitute])
            # noting the optimal steps
            if distance[i][j] == substitute:
                action[i][j] = "substitute {} with {}".format(src[i-1],target[j-1])
            elif distance[i][j] == delete:
                action[i][j] = "delete {}".format(src[i - 1])
            else:
                action[i][j] = "insert {}".format(target[j - 1])
    pprint(distance)
    return distance[m][n],action

'''
follow the optimal path for minimum edit distance
'''
def traceback(movement):
    steps = []
    i = len(movement) - 1
    j = len(movement[0]) - 1
    while i > 0 or j > 0:
        if movement[i][j].__contains__("delete") or j == 0:
            i -= 1
        elif movement[i][j].__contains__("insert") or i == 0:
            j -= 1
        else:
            j -= 1
            i -= 1
        steps.append(movement[i][j])
    steps.reverse()
    pprint(steps)

dist, move = edit_distance("intention", "execution")
traceback(move)
print(dist)
