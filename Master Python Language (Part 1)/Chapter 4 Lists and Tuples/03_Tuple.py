b = (1,2,3,4,5,6)  # Tuple is immutable always....
print(type(b))

a = (1, 45, 342, 3424, False, 45, "Rohan")
print(a)
print(a.count(45)) # a.count(x) is used to count the number of element x in the tuple.....
print(a.index(45)) # a.index(x) is used to check the indexing no. of the element x present in the tuple.....
print(len(a))  # len() is used to check the length of tuple.....




c = ()
print(type(c))


tuple1 = (1, 2, 3)
a, b, c = tuple1  # Tuple can be unpacked into individual variables.....
print(a, b, c)


tuple2 = (1, 2, 5, 7, 8)
sliced = tuple2[1:3]  # Slicing of tuple can be done by this process.....
print(sliced)