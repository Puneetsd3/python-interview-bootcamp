# -*- coding: utf-8 -*-
print("Hello, world! 你好，世界！")

def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
# Output: [[1, 2, 3], [4, 5, 6], [7]]

'''
i=0 , n=3, i+n=3 lst[0:3] -> [1,2,3]
i=3 , n=3, i+n=6 lst[3:6] -> [4,5,6]
i=6 , n=3, i+n=9 lst[6:9] -> [7]
i=9 -> end of list
'''

def flatten_one_level(lst):
    return [item for sublist in lst for item in sublist]
nested = [[1,2], [3,4], [5]]
print(flatten_one_level(nested))

def safe_get(d, key, default_callable):
    return d[key] if key in d else default_callable()
mydict = {'a': 1}
print(safe_get(mydict, 'b', lambda: 'not found'))


from collections import Counter
def freq_counter(lst): 
    return dict(Counter(lst))
def freq_manual(lst):
    freq = {}
    for item in lst:
        freq[item]= freq.get(item, 0) + 1
    return freq

print(freq_counter(['a','b','a']))
print(freq_manual(['a','b','a']))
