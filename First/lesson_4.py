def my_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function(n):
        result = function_to_decorate(n)
        if 100 % result == 0:
            print("We are OK")
        else:
            print("Bad news guys, we got{}")

    return the_wrapper_around_the_original_function


@my_new_decorator
def function_to_decorate(n):
    return n


function_to_decorate(1)


####


def first_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function(b):
        if type(b) is int:
            print('int is allowed')
            function_to_decorate(b)
        else:
            raise TypeError("Only integers are allowed")

    return the_wrapper_around_the_original_function


@first_decorator
def function_to_decorate(b):
    return b


function_to_decorate('34')


