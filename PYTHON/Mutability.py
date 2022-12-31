#integer is immutable, a new instance will be generated after an assignment.
number = 1
print(f'number location: {id(number)}')
number = 2
print(f'number location: {id(number)}')

#list is mutable, the value inside an object can change
lst = [1]
print(f'list location: {id(lst)}')
lst.append(2)
print(f'list location: {id(lst)}')

# In Python, objects are passed-by-assignment. That is:
# 1. If an object is mutable, the same object instance will be passed.
# 2. If an object type is immutable, a new object instance will be created inside the called function.

#As integer is immutable, passing an interger to a function will not alter its value outside the function scope.
print(f'Before addOne: {number}')
def addOne(num):
    num += 1
addOne(number)
print(f'After addOne: {number}')

#As list is mutable, passing an interger to a function will not alter its value outside the function scope.
print(f'Before appendOne: {lst}')
def appendOne(alist):
    alist.append(1)
appendOne(lst)
print(f'After appendOne: {lst}')    

# Output:
# number location: 4432740592
# number location: 4432740624
# list location: 4434111488
# list location: 4434111488
# Before addOne: 2
# After addOne: 2
# Before appendOne: [1, 2]
# After appendOne: [1, 2, 1]