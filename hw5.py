# продолжение классной работы с 29.10
#2 написать декоратор, аналогичный декоратору functools.cache, но позволяющий использовать в качестве аргументов функции нехэшируемые типы - список, множество, словарь

'''@mynewcache
def method(1: List):
    return sum(1) ''' 

from functools import wraps

def mynewcache(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        def make_hashable(item):
            if isinstance(item, (list, tuple)):
                return tuple(make_hashable(e) for e in item)
            elif isinstance(item, set):
                return tuple(sorted(make_hashable(e) for e in item))
            elif isinstance(item, dict):
                return tuple(sorted((make_hashable(k), make_hashable(v)) 
                                  for k, v in item.items()))
            return item
        
        key = (make_hashable(args), make_hashable(kwargs))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

@mynewcache
def method(lst):
    return sum(lst)

print(method([1, 2, 3]))
print(method([1, 2, 3]))  #из кэша
print(method([4, 5, 6]))
print(method([4, 5, 6]))  #из кэша


print('множества')
@mynewcache
def process_set(s):
    return len(s)

print(process_set({1, 2, 3}))
print(process_set({1, 2, 3}))  #из кэша
print(process_set({3, 2, 1}))  #из кэша


print('словари')
@mynewcache
def process_dict(d):
    return sum(d.values())

print(process_dict({'a': 1, 'b': 2}))
print(process_dict({'a': 1, 'b': 2}))
print(process_dict({'b': 2, 'a': 1}))
