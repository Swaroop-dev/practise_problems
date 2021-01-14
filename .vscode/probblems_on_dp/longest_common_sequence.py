# longest common palindrome
# rodcutting problem
# longest common sequence and subsequence
# longest common increasing sequence
# deletions required to convert string into palindrom
# coin change problem


def longest_common_sequence(X, Y):
    if X is None or Y is None:
        return None
    m = len(X)
    n = len(Y)
    t = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                t[i][j] = t[i-1][j-1]+1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n]

# print(longest_common_sequence(X="XMJYAUZ",
#     Y = "MZJAWXU"))


def rod_cutting_problem(p, n):
    t = [0 for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            t[i] = max(t[i], p[j-1]+t[i-j])
    return t[-1]


def longest_increasing_subsequence(S):

    n = len(S)
    output = [0 for i in range(n)]
    output[0] = 1
    for i in range(1, n):
        for j in range(0, i):
            if S[j] < S[i] and output[i] < output[j]:
                output[i] = output[j]
        output[i] = output[i]+1
    print(max(output))

# longest_increasing_subsequence(S=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])


def deletions_required(S):
    n = len(S)
    if n == 0:
        return 0
    S1 = S[::-1]
    o1 = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S1[j-1]:
                o1[i][j] = o1[i-1][j-1]+1

            else:
                o1[i][j] = max(o1[i-1][j], o1[i][j-1])
    return n-o1[-1][-1]
# print(deletions_required(S="ACBCDBAA"))


def shortest_path():
    cost = [
        [0, 25, 20, 10, 105],
        [20, 0, 15, 80, 80],
        [30, 15, 0, 70, 90],
        [10, 10, 50, 0, 100],
        [40, 50, 5, 10, 0]
    ]
    for i in range(len(cost)):
        return min()


def coinchange_recursive(A, s):
    if s == 0:
        return 0
    if s < 0:
        return float('inf')
    coins = float('inf')

    for i in A:
        res = coinchange_recursive(A, s-i)
        if res != float('inf'):
            coins = min(coins, res+1)
    return coins

# print(coinchange_recursive(A=[1,3,5,7],s=15))


def coinchange_optimized(A, s, T=None):
    if T == None:
        T = [None]*(s+1)
    if s == 0:
        T[s] = 0
        return 0
    if s < 0:
        return float('inf')

    if T[s]:
        return T[s]

    coins = float('inf')

    for i in A:
        if T[s-i] and (s-i) >= 0:
            res = T[s-i]
        elif (s-i) < 0:
            res = float('inf')
        else:
            res = coinchange_optimized(A, s-i, T)

        if res != float('inf'):
            coins = min(coins, res+1)
    T[s] = coins
    return coins


# print(coinchange_optimized(A=[1, 3, 5, 7], s=24))


def coinchange_iterative(A,s):
    T=[0]*(s+1)
    
    for i in range(1,s+1):
        T[i]=float('inf')
        for j in A:
            if i-j>=0:
                res=T[i-j]
                if res!=float('inf'):
                    T[i]=min(T[i],res+1)
    return T[-1]           

print(coinchange_iterative([1,3,5,7],18))
