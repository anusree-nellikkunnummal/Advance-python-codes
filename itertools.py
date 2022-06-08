import itertools
import statistics
# count()
counter = itertools.count(5, step=5)# counter will count from 0 to 5
lst = [100,200,300,400,500]
zipped = list(zip(counter,lst)) # count will cut after the shortest iterable exhausted
print(zipped)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter)) # will execute the next count value each time print
# zip longest()
ziped = list(itertools.zip_longest(range(10),lst))
print(ziped) # it takes none value after shortest iterable exhausted

'''cycle() This method prints all the values that are given as an argument to this method. 
And again it starts from the beginning when it reaches the end. To terminate this we need to keep a 
termination condition'''
counter = itertools.cycle(('on','off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# repeat() will repeat the data infinite time and we can set time by 'times= '

counts = list(itertools.repeat(5, times= 6))
sqr = list(map(pow, range(10), itertools.repeat(2)))
print(sqr)
print(counts)

# starmap takes tuple values

squares = itertools.starmap(pow,[(0,2), (1,2), (2,2), (3,2)])
print(list(squares))

# combinations

letters = ['a','b','c','d','e']
numbers =[1,2,3,4]
names = ['anu', 'first']
result = itertools.combinations(letters, 2)
for item in result:
    print(item)
result1 = itertools.permutations(letters,2)
for item in result1:
    print(item)
result2 = itertools.product(numbers, repeat=4)
for item in result2:
    print(item)
    result3 = itertools.combinations_with_replacement(numbers, 4)
    for item in result3:
        print(item)