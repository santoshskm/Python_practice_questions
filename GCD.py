#method=1
def fun(m,n):
    fm = [] #factors of m
    fn = [] #factors of n
    cf = [] #common factors of m and n
    for i in range(1, m+1):
        if m %i ==0:
            fm.append(i)
    for j in range(1, n+1):
        if n % j ==0:
            fn.append(j)
    for k in fm:
        if k in fn:
            cf.append(k)
    return max(cf)
print(fun(8,10))



#method=2
#check from 1 to min(m,n) which one is highest common factor.
def fun(m, n):
    for i in range(1,min(m, n)+1):
        if (m%i) ==0 and n%i ==0:
            gcd = i
    return gcd

print(fun(8, 10))

#method=3
#check from top value to 1, which devides both m and n is the highest common factor of m and n.
def fun(m,n):
    for i in range(min(m,n),0,-1):
        if m%i == 0 and n%i == 0:
            return i
print(fun(10,12))

#method=4
#same as method=2 but using "while" loop

def fun(m,n):
    i=min(m, n)
    while  i>0:
        if (m%i == 0) and (n%i == 0):
            return i
        else:
            i = i-1
print(fun(8,24))



#GCD by Euclid algorithm
def gcd_fun(m,n):
    #assume m > n
    if m < n:
        m,n =n,m
    if (m % n == 0):
        return n
    else:
        diff = m-n
        #diff > n
        return gcd_fun(max(n, diff), min(n,diff))

print(gcd_fun(20,12))

