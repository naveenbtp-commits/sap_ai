# def dynamic_function_call(func_name, *args, **kwargs):
#     if func_name == 'print':
#         print(*args, **kwargs)
#     elif func_name == 'sum':
#         print(sum(args))
#     elif func_name == 'len':
#         print(len(args[0]))
#     else:
#         print("Unknown function name")


# # dynamic_function_call('print', 'Hello, World!')
# dynamic_function_call('sum', 1, 2, 3, 4)
# dynamic_function_call('len', [1, 2, 3, 4])
# dynamic_function_call('unknown', 'This will print "Unknown function name"')


def dynamic_function_call(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for arg in args:
        print(f"Argument: {arg}")
dynamic_function_call(1, 2, 3, 4, name='Naveen', age=25, city='Hyderabad')
