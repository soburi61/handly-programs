"""
Created on Sun Jun 11 20:32:33 2023
coding: utf-8

"""

import numpy as np
 
names =\
[
[u'北口',   u'南口'],
[u'橋１',    u'橋２'],
[u'信号１',  u'信号２'],
[u'ローソン', u'セブンイレブン']
]
 
times =\
[
[[3],[5]],
[[4,1],[5,4]],
[[3,2],[4,3]],
[[7,5],[3,3]]
]
 
 
bfr_pnt  = [[0,0],[0,0],[0,0],[0,0]]  # 直前のポイント
accum_tm = [[0,0],[0,0],[0,0],[0,0]]  # 累積時間
 
for i in range(len(accum_tm)):
    if i == 0:
        accum_tm[i][0] = times[i][0][0]
        accum_tm[i][1] = times[i][1][0]
    else:
        #
        # 橋１、信号１、ローソン
        #
 
        # 「２つの直前ポイントまでの時間 ＋ そこからの時間」 を比較
        cmp_0 = [accum_tm[i-1][0] + times[i][0][0],  accum_tm[i-1][1] + times[i][0][1]]
        min_0 = np.argmin(cmp_0)       # 短いほう 0 or 1
        accum_tm[i][0] = cmp_0[min_0]  # 短いほうの時間
        bfr_pnt[i][0] = min_0          # 直前のポイント
 
 
        #
        # 橋２、信号２、セブンイレブン
        #
 
        # 「２つの直前ポイントまでの時間 ＋ そこからの時間」 を比較
        cmp_1 = [accum_tm[i-1][0] + times[i][1][0],  accum_tm[i-1][1] + times[i][1][1]]
        min_1 = np.argmin(cmp_1)       # 短いほう 0 or 1
        accum_tm[i][1] = cmp_1[min_1]  # 短いほうの時間
        bfr_pnt[i][1] = min_1          # 直前のポイント
 
shortest = np.argmin(accum_tm[3])
print(u'%s\t%d分' % (names[3][shortest], accum_tm[3][shortest]))
 
for i in reversed(range(1,len(bfr_pnt))):
    shortest = bfr_pnt[i][shortest]
    print(u'%s\t%d分' % (names[i-1][shortest], accum_tm[i-1][shortest]))