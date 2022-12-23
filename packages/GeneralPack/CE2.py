import math

class program:
    def dataset_split(self,data,arc,val):
        newData=[]
        for rec in data:
            if rec[arc]==val:
                reducedSet=list(rec[:arc])
                reducedSet.extend(rec[arc+1:])
                newData.append(reducedSet)
        return newData
        
    def calc_entropy(self,data):
        entries = len(data)
        labels = {}
        for rec in data:
            label = rec[-1]
            if label not in labels.keys():
                labels[label] = 0
            labels[label] += 1
        entropy = 0.0
        for key in labels:
            prob = float(labels[key])/entries
            entropy -= prob * math.log(prob, 2)
        return entropy

    def attribute_selection(self,data):
        features=len(data[0])-1
        baseEntropy=self.calc_entropy(data)
        maxInfoGain=0.0
        bestAttr=-1
        for i in range(features):
            AttrList=[rec[i]for rec in data]
            uniqueVals=set(AttrList)
            newEntropy=0.0
            attrEntropy=0.0
            for value in uniqueVals:
                newData = self.dataset_split(data, i, value)
                prob = len(newData)/float(len(data))
                newEntropy = prob * self.calc_entropy(newData)
                attrEntropy += newEntropy
            infoGain=baseEntropy-attrEntropy
            if infoGain>maxInfoGain:
                maxInfoGain=infoGain
                bestAttr=i
        return bestAttr

    def decision_tree(self,data,labels):
        classList=[rec[-1]for rec in data]
        if classList.count(classList[0])==len(classList):
            return classList[0]
        maxGainNode=self.attribute_selection(data)
        treelabel=labels[maxGainNode]
        theTree={treelabel:{}}
        del(labels[maxGainNode])
        nodeValues=[rec[maxGainNode]for rec in data]
        uniqueValues=set(nodeValues)
        for value in uniqueValues:
            sublabels=labels[:]
            theTree[treelabel][value]=self.decision_tree(self.dataset_split(data,maxGainNode,value),sublabels)
        return theTree
        
    def print_tree(self,tree,level=1):
        if tree=="yes"or tree=="no":
            print(" "*level,"d=",tree)
            return
        for key,value in tree.items():
            print(" "*level,key)
            self.print_tree(value,level*2)