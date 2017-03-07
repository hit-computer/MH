# Metropolis-Hastings Algorithm
Metropolis-Hasting算法是对MCMC方法中的一种改良，利用了马尔科夫链的收敛性，即马氏链的收敛定理（如果一个非周期马氏链具有转移概率矩阵P，且它的任何两个状态是联通的，那么 lim n->无穷 Pij的n次方 存在且与i无关，而这个值就是状态j的平稳概率。）详细内容可以参见我的博客 [马尔科夫链，mh，gibbs采样，以及mcmc](http://glacier.iego.net/%E9%A9%AC%E5%B0%94%E7%A7%91%E5%A4%AB%E9%93%BE%EF%BC%8Cmh%EF%BC%8Cgibbs%E9%87%87%E6%A0%B7%EF%BC%8C%E4%BB%A5%E5%8F%8Amcmc/)<br>
关于MH算法的几点说明与建议：

1. 初始概率尽可能接近平稳概率，这样可以减少迭代次数。
2. 转移概率可以选用Independence（独立），即q(i,j)=g(j)，g(j)为一个概率密度函数，同时尽可能选用和p(x)分布接近的概率分布(此时初始值无意义)。
3. 该算法解决的问题为，给定一个概率分布函数，生成符合这一概率分布的样本。
4. 算法关键在于选定适当的初始值和马氏链的转移函数。
