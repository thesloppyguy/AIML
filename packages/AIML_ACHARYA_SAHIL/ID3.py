import pandas as pd
import math


class program:
    def base_entropy(self,dataset):
        p = 0
        n = 0
        target = dataset.iloc[:, -1]
        targets = list(set(target))
        for i in target:
            if i == targets[0]:
                p = p + 1
            else:
                n = n + 1
        if p == 0 or n == 0:
            return 0
        elif p == n:
            return 1
        else:
            entropy = 0 - (
                ((p / (p + n)) * (math.log2(p / (p + n))) + (n / (p + n)) * (math.log2(n/ (p + n)))))
            return entropy

    def entropy(self,dataset, feature, attribute):
        p = 0
        n = 0
        target = dataset.iloc[:, -1]
        targets = list(set(target))
        for i, j in zip(feature, target):
            if i == attribute and j == targets[0]:
                p = p + 1
            elif i == attribute and j == targets[1]:
                n = n + 1
            if p == 0 or n == 0:
                return 0
            elif p == n:
                return 1
            else:
                entropy = 0 - (
                    ((p / (p + n)) * (math.log2(p / (p + n))) + (n / (p + n)) * (math.log2(n/ (p + n)))))
                return entropy

    def counter(self,target, attribute, i):
        p = 0
        n = 0
        targets = list(set(target))
        for j, k in zip(target, attribute):
            if j == targets[0] and k == i:
                p = p + 1
            elif j == targets[1] and k == i:
                n = n + 1
        return p, n

    def Information_Gain(self,dataset, feature):
        Distinct = list(set(feature))
        Info_Gain = 0
        for i in Distinct:
            Info_Gain = Info_Gain + feature.count(i) / len(feature) * self.entropy(dataset,feature, i)
            Info_Gain = self.base_entropy(dataset) - Info_Gain
        return Info_Gain


    def generate_childs(self,dataset, attribute_index):
        distinct = list(dataset.iloc[:, attribute_index])
        childs = dict()
        for i in distinct:
            childs[i] = self.counter(dataset.iloc[:, -1], dataset.iloc[:, attribute_index], i)
        return childs

    def modify_data_set(self,dataset,index, feature, impurity):
        size = len(dataset)
        subdata = dataset[dataset[feature] == impurity]
        del (subdata[subdata.columns[index]])
        return subdata

    def greatest_information_gain(self,dataset):
        max = -1
        attribute_index = 0
        size = len(dataset.columns) - 1
        for i in range(0, size):
            feature = list(dataset.iloc[:, i])
            i_g = self.Information_Gain(dataset, feature)
            if max < i_g:
                max = i_g
                attribute_index = i
        return attribute_index

    def construct_tree(self,dataset, tree):
        target = dataset.iloc[:, -1]
        impure_childs = []
        attribute_index = self.greatest_information_gain(dataset)
        childs = self.generate_childs(dataset, attribute_index)
        tree[dataset.columns[attribute_index]] = childs
        targets = list(set(dataset.iloc[:, -1]))
        for k, v in childs.items():
            if v[0] == 0:
                tree[k] = targets[1]
            elif v[1] == 0:
                tree[k] = targets[0]
            elif v[0] != 0 or v[1] != 0:
                impure_childs.append(k)
        for i in impure_childs:
            sub = self.modify_data_set(dataset,attribute_index,
            dataset.columns[attribute_index], i)
            tree = self.construct_tree(sub, tree)
        return tree