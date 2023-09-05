# greet関数の定義
def greet(name):
    return(f"Hello {name}!")

print(greet("Jim"))

#関数はFirst-class Objectだから変数に代入できる
hello = greet   
print(hello("jim"))


#関数はFirst-class Objectだから、listに入れることができる
def first_char2upper(name):
    return(name.capitalize())
def char2upper(name):
    return(name.upper())
def char2lower(name):
    return(name.lower())

fu = first_char2upper
up = char2upper
lo = char2lower
#listに入れることができる
func_lst = [fu,up,lo]
for func in func_lst:
    print(func("caroline"))

#関数はFirst-class Objectだから他の関数に渡すことができる
def greet2(func,name):
    return(f"Hello {func(name)}!")

for func in func_lst:
    print(greet2(func,"lucy"))