#どうしてmax()関数はいくでも引数を受け取ることができるのだろう
print(max(1,3))
print(max(1,3,5,7))
print(max(1,3,5,7,9,11))

#*args
def get_args(*args):
    print(args)
    print(type(args))

get_args(1)
get_args(1,2)
get_args(1,2,3)

# **kwargs
def get_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))

get_kwargs(name="Caroline", age=18)
get_kwargs(name="Caroline", age=18, hobby="embroidery")

def various_args(name, age, *friends_name, **work_history):
    print(name)

    print(friends_name)
    print(type(friends_name))

    print(work_history)
    print(type(work_history))

various_args("Caroline", 38,"John","Terry",programmer=5,engineer=7)