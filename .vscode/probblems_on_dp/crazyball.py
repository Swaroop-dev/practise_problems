# crazy ball bouncing.
# problem is to check wether ball can be stoped on the path i.e speed must be zero
# https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/


def canStoprecursive(runway, initialSpeed, startindex=0):
    if startindex >= len(runway) or startindex < 0 or runway[startindex] == False:
        return False
    if initialSpeed == 0:
        return True

    for adjustSpeed in [initialSpeed-1, initialSpeed, initialSpeed+1]:
        if canStoprecursive(runway, adjustSpeed, startindex+adjustSpeed):
            return True
    return False


# print(canStoprecursive(runway=[True,False,True,True,True,False,True,True,False,True,True],initialSpeed=4,startindex=00))

def canStoprecursive_with_memo(runway, initialSpeed, startindex=0, memo=None):
    print(initialSpeed, startindex)
    if memo == None:
        memo = [[]*100]*1000
    if memo[initialSpeed][startindex] in memo:
        return memo[initialSpeed][startindex]

    if startindex >= len(runway) or startindex < 0 or runway[startindex] == False:
        memo[initialSpeed][startindex] = False
        return False
    if initialSpeed == 0:
        memo[initialSpeed][startindex] = True
        return True

    for adjustSpeed in [initialSpeed-1, initialSpeed, initialSpeed+1]:
        if canStoprecursive_with_memo(runway, adjustSpeed, startindex+adjustSpeed, memo):
            memo[adjustSpeed][startindex] = True
            return True
    memo[initialSpeed][startindex] = False
    return False


# print(canStoprecursive_with_memo(runway=[
#       True, False, True, True, True, False, True, True, False, True, True], initialSpeed=4, startindex=0))
