from prettytable import PrettyTable
table = PrettyTable()
#table is object which is created from a class called PrettyTable

#table is object and add coloumn is methods(another name - function)

table.add_column("POKEMON NAME",["PIKACHU","SQUIRTLE","RAICHU"])
table.add_column("TYPE",["ELECTRIC","WATER","ELECTRIC"])

print(table)

#object attributes can also be changed for eg table style..
#how to change table attribute given below.
#this time insted of method we tap into field(we can see that in pycharm)

print(table.align)#line attributeis set to c which is centered (run code and see)

#if we want to shift that to left aligned
table.align = 'l'
print(table.align)