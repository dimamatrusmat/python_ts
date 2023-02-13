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

