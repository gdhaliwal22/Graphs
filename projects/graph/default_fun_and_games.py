def foo(list_to_set, the_set=set()):
    for item in list_to_set:
        the_set.add(item)

    print(the_set)


foo([1, 2, 3])
foo([4, 5, 6])
