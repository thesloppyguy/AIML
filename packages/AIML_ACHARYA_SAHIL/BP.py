import numpy as np




class program:

    def __init__(self,X,y,epoch,lr,inp,hid,out):
        self.X = X
        self.y = y
        self.X = self.X/np.amax(self.X,axis=0) 
        self.y = self.y/100
        self.epoch=epoch           
        self.lr=lr                    
        self.inputlayer_neurons = inp   
        self.hiddenlayer_neurons = hid  
        self.output_neurons = out
        self.wh=np.random.uniform(size=(self.inputlayer_neurons,self.hiddenlayer_neurons))
        self.bh=np.random.uniform(size=(1,self.hiddenlayer_neurons))
        self.wout=np.random.uniform(size=(self.hiddenlayer_neurons,self.output_neurons))
        self.bout=np.random.uniform(size=(1,self.output_neurons))       


    def sigmoid (self,x):
        return 1/(1 + np.exp(-x))

    def derivatives_sigmoid(self,x):
        return x * (1 - x)




    def solve(self):
        for i in range(self.epoch):
            hinp1=np.dot(self.X,self.wh)
            hinp=hinp1 + self.bh
            hlayer_act = self.sigmoid(hinp)
            outinp1=np.dot(hlayer_act,self.wout)
            outinp= outinp1+ self.bout
            output = self.sigmoid(outinp)
            

            EO = self.y-output
            outgrad = self.derivatives_sigmoid(output)
            d_output = EO* outgrad
            EH = d_output.dot(self.wout.T)


            hiddengrad = self.derivatives_sigmoid(hlayer_act)
            d_hiddenlayer = EH * hiddengrad
            self.wout += hlayer_act.T.dot(d_output) *self.lr
            self.wh += self.X.T.dot(d_hiddenlayer) *self.lr
            
        
        print("Input: \n" + str(self.X))
        print("Actual Output: \n" + str(self.y))
        print("Predicted Output: \n" ,output)