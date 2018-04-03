#!/usr/bin/python3
import re, bitarray
from time import sleep

pt = re.compile("[0-9]+,[0-9]+c")
tx = "<"
rx = ">"
st = "---"
sp = " \n\r"

bucket = [0]*1024
tmp = ""
error, total, index = 0, 0, 0
bArray = bitarray.bitarray()
with open('./result.txt') as f:
    #heading part
    tmp = f.readline().strip(sp)
    assert pt.match(tmp)

    while tmp!="":
        ci, co = [], ""

        #tx part
        tmp = f.readline().strip(sp)
        while tmp!=st and tmp!="":
            ci.append(f.readline())
            tmp = f.readline().strip(sp) #st part
            pass
        
        #rx part
        tmp = f.readline().strip(sp)
        while not pt.match(tmp) and tmp!="":
            co += f.readline()
            tmp = f.readline().strip(sp)
            pass
        pass

        if tmp=="": break

        assert len(ci)==2
        co = co[:co.index(ci[1])]
        ci = ci[0]
        # print(ci)
        # print(co)

        bArray = bitarray.bitarray()
        bArray.fromstring(ci)
        ci = bArray.to01()
        bArray = bitarray.bitarray()
        bArray.fromstring(co)
        co = bArray.to01()
        # print(ci)
        # print(co)
        out = [0 if x==y else 1 for x,y in zip(ci,co)]

        index = out.index(1)
        error += out.count(1)
        total += len(ci)
        bucket[index] += 1
        print('error:%d; total:%d; index:%d; BER:%.2f\r'%(error, total, index, error/total), end='')
        # sleep(1.0)
        pass
    print()
    for x in range(1024):
        if bucket[x]!=0:
            print("%d: %d"%(x, bucket[x]))
        pass
    pass