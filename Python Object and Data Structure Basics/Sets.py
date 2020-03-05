# Sets - sets are unordered collection of unique elements

my_set = set()

#adding values to the set
my_set.add("1")
my_set.add("2")
my_set.add("3")
print("SET VALUES ARE : " + my_set.__str__())

my_set.add("3")
my_set.add("1")
print("SET VALUES ARE : " + my_set.__str__())    # Should print only 3 values (unordered) because sets are unique

my_set.add(1)
print("SET VALUES ARE : " + my_set.__str__())    # Should print only 4 values (unordered)
                                                 # because 1 and "1" are different from each other (1 - is int   but "1" - is string)


list1 = [1,1,1,2,2,2,3,3,3]
print("Printing list as a set: " + set(list1).__str__())  # Should print only 3 values (unordered)