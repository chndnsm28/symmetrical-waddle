from idlelib.outwin import file_line_progs

l1 = ["chandan", "husky", "rekha"]

dict4 = dict(enumerate(l1))
print(dict4)

dict5 = {x:x*2 for x in range(1, 6)}
print(dict5)

dict6 = dict((x, x*3) for x in range(1,8))

l1 = [1,2,3]
l2 = ['a', 'b', 'c']
print("-------")

dict7 = dict((x,y) for x,y in zip(l1,l2))
print(dict7)

#------------or--------

dict8 = {x:y for x,y in zip(l1,l2)}
print(dict8)

dict9 = dict((x,y) for x,y in enumerate(l2))
print(dict9)

dict9 = {x:y for x,y in enumerate(l1)}
print(dict9)