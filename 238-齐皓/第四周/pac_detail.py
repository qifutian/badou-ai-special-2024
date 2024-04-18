
import numpy as np

class CPCA(object):
    def _init_(self,X,K):

        slef.X = X
        self.K = K
        self.centrX = []
        self.C = []
        self.U = []
        self.Z = []
        
        self.centrX = self._centralized()
        self.C = self._cov()
        self.U = self._U()
        self.Z = self._Z()

    def _centralized(self):
        print('样本矩阵x: \n', self.X)
        centrX = []
        # 样本集的特征均值
        mean = np.array([np.mean(attr) for attr in self.X.T])
        # 样本集中心化
        centrX = self.X - mean
        return centrX
    
    def _cov(self):
        # 样本集样例总数
        ns = np.shape(self.centrX)[0]
        # 矩阵的协方差矩阵C
        C =np.dot(self.centrX.T,self.centrX)/(ns-1)
        return C
    
    def _U(self):
        # 求X的协方差矩阵c的特征值特征向量
        a,b = np.linalg.eig(self.C)
        # 特征值降序的topK index
        ind = np.argsort(-1*a)
        # 降为转换矩阵U
        ut = [b[:ind[i]] for i in range(self.K)]
        u = np.transpose(ut)

        return u

    def _Z(self):
        Z = np.dot(self.X,self.U)
        print('X SHAPE',np.shape(self.X))
        print('U SHAPE',np.shape(self.U))
        print('Z SHAPE',np.shape(self.Z))
        return Z





X = np.array([
    [10,15,29],
    [15,46,13],
    [23,21,30],
    [11,9,35],
    [42,45,11],
    [9,48,5],
    [11,21,14],
    [8,5,15],
    [11,12,21],
    [21,20,25],
])

K = np.shape(X)[1]-1
print("样本集（10行3列，每样例3特征）:\n",X)
pca = CPCA(X,K)