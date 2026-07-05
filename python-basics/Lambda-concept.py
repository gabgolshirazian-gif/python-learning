
#Lambda concepts:
a = (lambda a : a+2)(2)
print(a)


x = (lambda a,b : a+b)
print(x(a=2,b=4))
print(x(2,4))


my_full_name = lambda first,last: f'my name is {first} {last}'
print(my_full_name("gab","gol"))



#using lambda in functions:
def power_n(n):
    return lambda a : a**n


power_2 = power_n(2)
power_3 = power_n(3)
power_4 = power_n(4)

print(power_2(2))
print(power_3(4))
print(power_4(6))



MAX = lambda a,b : a if a>b  else b
print(MAX(10,5))