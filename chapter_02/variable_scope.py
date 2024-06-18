# scope = The region that a variable is recognized in
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = 'alex__global'  # global scope (available inside & outside functions)


def display_name():
    # local variables are preferred
    # LEGB = Local -> Enclosing -> Global -> Builtins
    name = 'magma__localScoped'    # local scoped variable
    print(name)


display_name()
print(name)
