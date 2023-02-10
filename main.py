import pymorphy3

morph = pymorphy3.MorphAnalyzer()



a = morph.parse("Матвеев")[0]
print(a.inflect({'gen2'}).word)
