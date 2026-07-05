def test_func(*args):
    print(args)

test_func(1,2,3,4)


def test_func_1(name , *args):
    print(f"my name is: {name}")
    print(args)


test_func_1("gab",1,2,3)


def test_func_2(name , *args):
    print(f"my name is: {name}")
    if args:
        print(f"the other names : {args}")

test_func_2("gab","alex","tom")  


def test_func_3(name , *args):
    print(f"my name is : {name}")

    i = 1
    for n in args:
        print(f"name{i} : {n}")
        i=+1

test_func_3("gab","alex","tom")



def test_func_4(name,**kwargs):
    print(f"my name is : {name}")
    for n in kwargs.values():
        print(n)

test_func_4("gab",name1="alex",name2="tom")