def findLength(ar,sum,res,r,i):
    if sum<0:
        return
    if sum == 0:
        res.append(tuple(r))
        return
    while(i<len(ar) and sum-ar[i]>=0):
        r.append(ar[i])
        findLength(ar, sum - ar[i], res, r, i)
        i += 1
        r.pop()

def rod(ar, sum):
    ar.sort()
    r = []
    res = []
    findLength(ar, sum, res, r, 0)
    return (res)

q = {1:3,2:5,3:8,4:9,5:10,6:17,7:17,8:20}
arr = list(q.keys())
di = {}
sol = rod(arr,8)

for keys in di:
    if di[keys] == max(di.values()):
        print(keys, di[keys])
