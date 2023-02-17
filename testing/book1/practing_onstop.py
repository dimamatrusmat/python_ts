# def apply_discount(product, discount):
#     price = int(product['цена'] * (1.0-discount))
#     assert 0 <= price <= product['цена']
#
#     return price
#
# shoes = {'имя': 'Модные туфли', 'цена': 14900}
#
# print(apply_discount(shoes, 2.0))

# ##################################
# # This is False example
# names = ['Apa', "Yra", "Kate"]
#
# # This is True example
# names = [
#     'Apa',
#     'Yra',
#     'Kate',
# ]
#
#
# ##################################
# class ManagedFile:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         self.file = open(self.name, 'w')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#
#
# with ManagedFile("hello.txt") as f:
#     f.write("Hello wordl1!\n")
#     f.write("By Word")
#
# ######################
# from contextlib import contextmanager
# @contextmanager
# def manager_file(name):
#     try:
#         f = open(name, 'w')
#         yield f
#     finally:
#         f.close()
#
#
# with manager_file('privet.txt') as f:
#     f.write('hhelo wpld')
#     f.write('\ndsadd')
#
# #########################
# class Test:
#     def __init__(self):
#         self.foo = 11
#         self._bar = 23
#         self.__baz = 23
#
#
# class ExtendedTest(Test):
#     def __init__(self):
#         super().__init__()
#         self.foo = 'переопределено'
#         self._bar = 'переопределено'
#         self.__baz = 'переопределено'
#
#
# t = Test()
# t2 = ExtendedTest()
#
# print(dir(t2))
# t._Test__baz = 1
# print(t._Test__baz)

##########################

# errno = 50159747054
# name = "Bob"
# print("Hello %s, это ошибка 0x%x" % (name, errno))
# print("Hello %(name)s!, это ошибка 0x%(errno)x!" % {"name": name, 'errno': errno})
# print(f"Hi, {name}! This is error 0x{errno:x}!".format(name=name, errno=errno))

###################

# def bak(text):
#     return text.upper() + "!"
#
# print(bak("tetetete"))
#
# park = bak
#
# print(park("fffff"))

#######################

# class Faible:
#
#     def __init__(self, doc, gil):
#         self.seil = doc
#         self.gil = gil
#


#######################

# add = lambda x, y: x + y
#
# print(add(4, 5))

# def make_adder(n):
#     return lambda x: x + n
#
# plus_3 = make_adder(3)
# plus_5 = make_adder(5)
# x = plus_3(4)
# print(x)
# w = plus_5(4)
# print(w)
##############################
# def null_decorator(func):
#     return func
#
#
# def greet():
#     return 'Hello!'
#
#
# greet = null_decorator(greet)
#
#
# print(greet())

#########################

# def null_decorator(func):
#     return func
#
# @null_decorator
# def greet():
#     return "hello"
#
# a = greet()
# print(a)

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modifield_result = original_result.upper()
#
#         return modifield_result
#
#     return wrapper
#
#
# @uppercase
# def greet():
#     return "hello"
#
#
# print(greet())


# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#
#     return wrapper
#
#
# def body(func):
#     def wrapper():
#         return '<' + "body" + '>' + func() + '</' + "body" + '>'
#
#     return wrapper
#
# @body
# @strong
# def start():
#     return "Staing"
#



#
# print(start())
#############################
# import functools
#
#
# def proxy(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def trace(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Trassirovka: call {func.__name__}() '
#               f'c {args}, {kwargs}')
#
#         original_result = func(*args, **kwargs)
#
#         print(f'Trassirovka: {func.__name__}() '
#               f'return {original_result!r}')
#
#         return original_result
#
#     return wrapper
#
#
# @trace
# def say(name, line):
#     """Return Say"""
#     return f'{name}: {line}'
#
#
# print(say("Jeny", "Hello"))
# print(say.__name__)
#
#################






