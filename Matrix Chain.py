def chain(p):
    n = len(p) - 1
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i<j:
                c = [m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1] for k in range(i, j)]
                s[i][j], m[i][j] = min(enumerate(c), key = lambda x:x[1])
                s[i][j] += i+1
    return m,s

def display(s, i, j):
    if i == j:
        print('A',i+1, end=' ')
    else:
        print('(', end=' ')
        display(s, i, s[i][j] - 1)
        display(s, s[i][j], j)
        print(')', end=' ')

order = [ 10,20,50,1,100 ]
m,s = chain(order)
display(s,0, len(s)-1)
print()