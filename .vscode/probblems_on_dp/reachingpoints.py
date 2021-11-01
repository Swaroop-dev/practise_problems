def reaching(w,x,y,z):
    # w,x are starting points 
    #, y,z are ending points 
    if w==y and x==z:
        return True
    if w>y or x>z:
        return False
    return (reaching(w+x,x,y,z) or reaching(w,w+x,y,z))

print(reaching(1,1,5,8))