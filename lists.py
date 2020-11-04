demo_list=[1, "hello ", 1.34, True,[1, 2, 3]]
colors=["green","red", "blue"]

numers_list=list((1, 2, 3, 4))
print(numers_list)

r=list(range(1, 100))
print(r)
print(len(demo_list))
print(colors[-2])

print(colors)
suma=numers_list[1]+numers_list[2]+numers_list[3]+numers_list[0]
print(suma)

print(dir(colors))

colors.append("violet") #añadir elemento a lista
colors.extend(("yellow", "violet"))
colors.extend(("pink", "black"))

colors.insert(-1, "violet")
colors.insert(len(colors),"violet ")
print(colors)

colors.sort(reverse=True)
colors.sort()

print(colors.index("blue"))
