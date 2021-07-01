l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista initiala: ", l);

sorted_list = l.copy()
sorted_list.sort()
print("Lista sortata: ", sorted_list)

sorted_list2 = l.copy()
sorted_list2.sort()
sorted_list2 = sorted_list2[::-1]
print("Lista sortata descrescator: ", sorted_list2)

print("Numerele pare din lista: ", sorted_list[1::2])

print("Numerele impare din lista: ", sorted_list[::2])

print("Multiplii lui 3 din lista: ", sorted_list[2::3])
