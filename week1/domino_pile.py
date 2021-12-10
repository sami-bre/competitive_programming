dim_string = input()
# m,n= list(map(int,input().spli))
d1, d2 = dim_string.split(" ")
d1 = int(d1)
d2 = int(d2)

def dominos_if_even_side(even, other):
    n = even/2
    return n*other

def dominos_if_both_odd(odd1, odd2):
    return dominos_if_even_side(odd1-1, odd2) + (odd2-1)/2

if(d1%2 == 0):
    print(int(dominos_if_even_side(d1, d2)))
elif(d2%2 == 0):
    print(int(dominos_if_even_side(d2, d1)))
else:
    print(int(dominos_if_both_odd(d1, d2)))