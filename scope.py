'''Scope in python'''

# The order is LEGB
# L == Local
# E == Enclosing
# G == Global
# B == Built in



# Local scope

def test():
    '''Local scope'''
    x = "local scope"
    print(x)

test()


# Enclosing scope === Nested functions == function in a function


x = "global x"
def outer():
    x = "outer x"

    def inner():

        x = "inner x"
        print(x)

    inner()
    print(x)

outer()
print(x)


def num():
    x = "number 1"
    print(x)

    def num2():
        x = "number 2"
        print(x)

    num2()
num()




# Global scope

x = 'global x'
def sim():
    '''scope'''
    y = 'local y'
    print(y)

sim()
print(x)


# x = 'global x'
# def sim():
#     '''scope'''
#     global x
#     x = 'local x'
#     print(x)

sim()
# print(x)


# Built-in

m = min([5, 2, 1, 3, 4])
print(m)

import builtins
print(dir(builtins))



# def text():
#     '''built in'''

#     pass

# m = min([5, 2, 3, 1, 6])
# print(m)
