""" Iterando a Tupla
As Tuplas são iteráveis (iterable), ou seja, capazes de retornar seus elementos um de cada vez. Para percorrermos as Tuplas, utilizaremos a mesma sintaxe das listas, como ocorre no exemplo a seguir: """
print("\n---------------------------\n")

tupla = ('a', 'b', [1, 2, 3], (1, 2, 3))
for elemento in tupla:
    print(elemento)

print("\n---------------------------\n")
