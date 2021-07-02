# def powerfu1(N):
#     o=2**N
#     rem=0
#     while o>0 or rem>9:
#         if o<=0 and rem>9:
#             o=rem
#             rem=0
#         else:
#             rem=rem+o%10
#             o=o//10            
#     return rem        
# print(powerfu1(11))

#pyramid printing
# def pyramidPrint(N):
#     arr=[[0]*(i+1) for i in range(N)]
#     for i in range(N):
#         x=i+1
#         y=N-1
#         for j in range(len(arr[i])):
#             arr[i][j]=x
#             x=x+y
#             y=y-1
#     for i in range(N):
#         for j in range(len(arr[i])):
#             print(arr[i][j],end="\t")
#         print("\n")    
# pyramidPrint(3)    


