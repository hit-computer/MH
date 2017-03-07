import numpy
import matplotlib.pylab as plt
import random
import collections

P = [0.15,0.1,0.2,0.3,0.25] #需要采样的P(x)分布函数
x0 = 2 #初始值

G = [0.13,0.12,0.18,0.31,0.26] #independence方法中的g(x)
G1 = [0.22,0.66,0.02,0.02,0.08]
translate = [[0.4,0.05,0.2,0.28,0.07],[0.4,0.22,0.1,0.1,0.18],[0.1,0.66,0.02,0.02,0.2],[0.41,0.02,0.08,0.03,0.46],[0.35,0.1,0.15,0.1,0.3]] #转移概率矩阵

def sample(pro):
	NewP = pro[:]
	for i in range(1,len(NewP)):
		NewP[i] += NewP[i-1]
		#print pro[i]
	u = random.uniform(0.0,1.0)
	#print u,pro
	t = 0
	for i in range(len(NewP)):
		if NewP[i] > u:
			t = i
			break
			
	return t

#--------------------Independence----------------------#
iter = 10000 #迭代次数
res_seq = []
x = x0
#print sample(G)
for i in range(iter):
	y = sample(G)
	u = random.uniform(0.0,1.0)
	if u < min(P[y]*G[x]/(P[x]*G[y]),1):
		x = y
	if i > 2000: #因为马尔科夫链需要转移一定次数才能收敛，所以也需要转移一定次数后才保留结果
		#print x
		res_seq.append(x)
#------------------------------------------------------#

#--------------------独立----------------------#
iter = 10000 #迭代次数
res_seq1 = []
x = x0
#print sample(G)
for i in range(iter):
	y = sample(G1)
	u = random.uniform(0.0,1.0)
	if u < min(P[y]*G1[x]/(P[x]*G1[y]),1):
		x = y
	if i > 2000:
		#print x
		res_seq1.append(x)
#------------------------------------------------------#


"""
#--------------------非独立，使用转移矩阵--------------#
iter = 10000 #迭代次数
res_seq = []
x = x0
#print sample(G)
for i in range(iter):
	y = sample(translate[x])
	u = random.uniform(0.0,1.0)
	if u < min(P[y]*translate[y][x]/(P[x]*translate[x][y]),1):
		x = y
	if i > 2000:
		#print x
		res_seq.append(x)
#-------------------------------------------------------#
"""

stat = collections.Counter(res_seq)
for key in stat:
	print key,float(stat[key])/len(res_seq)

print "转移概率分布函数与原分布不接近："
stat = collections.Counter(res_seq1)
for key in stat:
	print key,float(stat[key])/len(res_seq1)

plt.figure(1)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)	

res_seq = res_seq[-1000:]
res_seq1 = res_seq1[-1000:]

plt.sca(ax1)
plt.plot(range(len(res_seq)),res_seq,'-')
plt.ylim(0.0,5.0)

plt.sca(ax2)
plt.plot(range(len(res_seq1)),res_seq1,'-r')
plt.ylim(0.0,5.0)

plt.show()
