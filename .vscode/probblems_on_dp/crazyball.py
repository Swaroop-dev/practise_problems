# crazy ball bouncing.
# problem is to check wether ball can be stoped on the path i.e speed must be zero
# https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/


# def canStoprecursive(runway, initialSpeed, startindex=0):
#     if startindex >= len(runway) or startindex < 0 or runway[startindex] == False:
#         return False
#     if initialSpeed == 0:
#         return True

#     for adjustSpeed in [initialSpeed-1, initialSpeed, initialSpeed+1]:
#         if canStoprecursive(runway, adjustSpeed, startindex+adjustSpeed):
#             return True
#     return False


# # print(canStoprecursive(runway=[True,False,True,True,True,False,True,True,False,True,True],initialSpeed=4,startindex=00))

# def canStoprecursive_with_memo(runway, initialSpeed, startindex=0, memo=None):
#     print(initialSpeed, startindex)
#     if memo == None:
#         memo = [[]*100]*1000
#     if memo[initialSpeed][startindex] in memo:
#         return memo[initialSpeed][startindex]

#     if startindex >= len(runway) or startindex < 0 or runway[startindex] == False:
#         memo[initialSpeed][startindex] = False
#         return False
#     if initialSpeed == 0:
#         memo[initialSpeed][startindex] = True
#         return True

#     for adjustSpeed in [initialSpeed-1, initialSpeed, initialSpeed+1]:
#         if canStoprecursive_with_memo(runway, adjustSpeed, startindex+adjustSpeed, memo):
#             memo[adjustSpeed][startindex] = True
#             return True
#     memo[initialSpeed][startindex] = False
#     return False


# # print(canStoprecursive_with_memo(runway=[
# #       True, False, True, True, True, False, True, True, False, True, True], initialSpeed=4, startindex=0))

# def checkForAnagrams(word, arr):
#     # Checking if the word has an anagram in the sliced array.
#     for x in arr:
#         if (sorted(word) == sorted(x)):
#             return True
#     return False
            
# def funWithAnagrams(text):
#     limit = len(text)
#     text.reverse()
#     # Creating a copy of the list which will be modified,
#     # and will not affect the array slicing during the loop.
#     final_text = list(text)

#     # Looping through the list in reverse since we're eliminating
#     # the second anagram we find from the original list order.
#     count = 0
#     for i in range(0, limit):
#         if text[i+1:] and checkForAnagrams(text[i], text[i+1:]):
#             final_text.pop(i - count)
#             count += 1

#     return sorted(final_text)

# print(funWithAnagrams(['code','eodc','farmer','farm']))



s="acdeabc"
s=s.lower()
n=len(s)
max1=-10000
for i in range(n):
    asi=int(ascii(s[i]))
    cnt=1
    for j in range(i,n):
        if int(ascii(s[j]))==asi+1:
            asi=asi+1
            cnt=cnt+1
        else:
            break
        
        if cnt>max1:
            max1=cnt
print(max1)

             
