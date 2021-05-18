#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("input n")
n=input()
#nを代入

print("input W")
W=input()
#Wを代入

if W.isdecimal():
   W=int(W)
#Wを数字化

import math

if n.isdecimal():
   n=int(n)
i=0
weight=[0]*n
#空リスト作成
value=[0]*n
while i<=n-1:
    print("input weight",i)
    #iというintは使えなくてstrしかprintの()の中には入れられない。
    weight[i]=input()
#数列weight[i]に数字を代入
    if weight[i].isdecimal():
       weight[i]=int(weight[i])
    print("input value",i)
    value[i]=input()
    if value[i].isdecimal():
       value[i]=int(value[i])

    i +=1

else:
       pass

wlist=[]
vlist=[]
#空リスト作成

k=0
while k<=n-1:
   wlist.append(weight[k])
   vlist.append(value[k])
#####数列weight[n]をリストとして一つにまとめる

   k +=1
else:
   pass

from itertools import permutations
wper=permutations(wlist,n)
vper=permutations(vlist,n)
#wlistの全順列=wnの全順列のリスト化 リストの要素の数はn!で要素の一つ一つはn個の数列

wpl =list(wper)
#wperのリスト化
vpl =list(vper)
#vperのリスト化
tlist=[0]*math.factorial(n)
#tを特定、記録するためのリストを作成



s=0
t=0
wsum=[0]*math.factorial(n)
#wsum=[0,0,0,,,,,0] 要素がn!個のリスト

while wsum[s]<W and t<=n-1 and s<=math.factorial(n)-1 :

    wsum[s]=wsum[s]+wpl[s][t]
    if wsum[s]>W:
        tlist[s]=t-1

       
    elif wsum[s]==W:
        tlist[s]=t
       
    else:
        t +=1

#Wにギリギリまで近づいた時のtを記録　wperの要素の数列w1に対するWに最も近づいた時のtを記録
    t=0
#tの初期化
    s +=1
    break
#ここでsum[s]の最後のwpl[s][t]のtを特定する関数、行tlistを書く→書いた。さらにvperからそれぞれの数列に対する和vsum[s]を出した後、その中での最大値を答えとする。例えばvperの要素の数列、というかリストのvper[0]のvper[0][0]からvper[0][tlist[0]]までの和を出す。得られた数値を全て記録してリスト化してそのリストの最大値が求めるもの。

vsum=[0]*math.factorial(n)
#vsum=[0,0,0,0,0,,,,0]とn!個のリスト。valueの和を出すために作られた。

h=0
d=0
while h<=math.factorial(n)-1 and d<=tlist[h]:

    vsum[h]=vsum[h]+vpl[h][d]
    d +=1


else:
    h +=1
    d=0
#vsumの作成


klist=[]
#空リスト作成
p=0
while p<=math.factorial(n)-1:
    klist.append(vsum[p])
    p +=1
else:
   pass

print(max(klist))

