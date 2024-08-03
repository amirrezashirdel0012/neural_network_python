import numpy as np

class NNTF:
    def __init__(self):
        pass

    def hardlim (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):
                if n[i][j] < 0:
                    a[i][j] = 0
                else:
                    a[i][j] = 1
        return a
        
    def hardlims (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):
                if n[i][j] < 0:
                    a[i][j] = -1
                else:
                    a[i][j] = 1
        return a
        
    def purelin (self, n):
        return n
    
    def satlin (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):
                if n[i][j] > 1:
                    a[i][j] = 1
                elif n[i][j] < 0:
                    a[i][j] = 0
                else:
                    a[i][j] = n[i][j]
        return a
        
    def satlins (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):
                if n[i][j] > 1:
                    a[i][j] = 1
                elif n[i][j] < -1:
                    a[i][j] = -1
                else:
                    a[i][j] = n[i][j]
        return a
        
    def logsig (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):  
                a[i][j] = 1 / (1+(np.exp**(-n[i][j])))            
        return a
    
    def tansig (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):  
                a[i][j] = (np.exp**(n[i][j]) - np.exp**(-n[i][j]))/(np.exp**(n[i][j]) + np.exp**(-n[i][j]))          
        return a
    
    def poslin (self, n):
        x, y = n.shape
        a = np.zeros([x, y])
        for i in range(x):
            for j in range(y):
                if n[i][j] >= 0:
                    a[i][j] = n[i][j]
                else:
                    a[i][j] = 0
        return a