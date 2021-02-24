from math import gcd
def solution(w,h):
    # if w==h:
    #     return w*h
    
    
    return w*h-(w+h-gcd(w,h))