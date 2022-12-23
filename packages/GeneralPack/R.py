import numpy as np
import matplotlib.pyplot as plt

class program:
    def __init__(self,X,Y,domain):
        self.X=X
        self.Y=Y
        self.domain=domain
        
    def local_regression(self,x0, X, Y, tau):
        x0 = [1, x0]   
        X = [[1, i] for i in X]
        X = np.asarray(X)
        xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
        beta = np.linalg.pinv(xw @ X) @ xw @ Y @ x0  
        return beta    
        
    def draw(self,tau):
        prediction = [self.local_regression(x0, self.X, self.Y, tau) for x0 in self.domain]
        plt.plot(self.X, self.Y, 'o', color='black')
        plt.plot(self.domain, prediction, color='red')
        plt.show()