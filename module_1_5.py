immutable_tuple_ = ("Карнаухов", 1998, True)
print(immutable_tuple_)

# immutable_tuple_ [0] = "Григорий"  # Кортеж не поддерживает общение по элементам

mutable_list = ["Григорий", 25, True]
print(mutable_list)
mutable_list[0] = "Сергеевич"
mutable_list[1] = 52
mutable_list[2] = False
print(mutable_list)