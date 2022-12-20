from packages.AIML_ACHARYA_SAHIL.CE import program
import csv

obj=program()

def candidate_elimination(obj,examples):
    domains = obj.get_domains(examples)[:-1]
    
    G = set([obj.g_0(len(domains))])
    S = set([obj.s_0(len(domains))])
    i=0
    print("\n G[{0}]:".format(i),G)
    print("\n S[{0}]:".format(i),S)
    for xcx in examples:
        i=i+1
        x, cx = xcx[:-1], xcx[-1]
        if cx=='yes':
            G = {g for g in G if obj.fulfills(x, g)}
            S = obj.generalize_S(x, G, S)
        else:
            S = {s for s in S if not obj.fulfills(x, s)}
            G = obj.specialize_G(x, domains, G, S)
        print("\n G[{0}]:".format(i),G)
        print("\n S[{0}]:".format(i),S)
    return

examples=[]
with open(r'D:\Programs\CLG\AIML\notebook\csv\sprts.csv') as csvFile:
    examples = [tuple(line) for line in csv.reader(csvFile)]
obj.get_domains(examples)
candidate_elimination(obj,examples)