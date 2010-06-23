from time import time

import django.utils.copycompat as copy
from django.utils.datastructures import MultiValueDict

from djangobench.utils import run_comparison_benchmark

case = {'a': ['a'], 'b': ['a','b'], 'c':['a','b','c']}
update = {'a': ['a'], 'b': ['a','b'], 'c':['a','b','c']}

def benchmark_multi():
    # Instantiate a new MultiValueDict and call key method (i.e. that do
    # something diff than dict)
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
    # Instantiate a new dict and call same methods as above - to be fair,
    # get unlistify in this method where required
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

run_comparison_benchmark(
    benchmark_multi,
    benchmark_dict,
    syncdb = False,
    meta = {
        'description': 'Overhead of a MultiValueDict compared to a builtin dict.',
    }
)