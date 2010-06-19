from time import time

from django.utils.datastructures import MultiValueDict
import django.utils.copycompat as copy

case = {'a': ['a'], 'b': ['a','b'], 'c':['a','b','c']}
update = {'a': ['a'], 'b': ['a','b'], 'c':['a','b','c']}

def benchmark_multi():
    #instantiate a new MultiValueDict and call key method (i.e. that do something diff than dict)
    caseDict = MultiValueDict(case)

    caseDict['a']
    caseDict['b']
    caseDict['c']
    
    caseDict.update(update)
    copy.copy(caseDict)
    copy.deepcopy(caseDict)
    
    caseDict.items()
    caseDict.lists()
    for i in caseDict:
        i

    caseDict['a'] = 'A'
    caseDict['b'] = 'B'
    caseDict['c'] = 'C'

def benchmark_dict():
    #instantiate a new dict and call same methods as above - to be fair, get unlistify in this method where required
    caseDict = dict(case)
    
    caseDict['a'][0]
    caseDict['b'][1]
    caseDict['c'][2]
    
    caseDict.items()
    caseDict.values()
    for i in caseDict:
        i
    
    caseDict.update(update)
    copy.copy(caseDict)
    copy.deepcopy(caseDict)
    
    caseDict['a'] = ['A']
    caseDict['b'] = ['B']
    caseDict['c'] = ['C']

diff = 0.0
for x in range(200):
    multi_time_start = time()
    benchmark_multi()
    multi_time_diff = time() - multi_time_start
    dict_time_start = time()
    benchmark_dict()
    dict_time_diff = time() - dict_time_start
    diff = diff + multi_time_diff - dict_time_diff
print diff  


