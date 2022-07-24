a = float(input("Preço $ :"))
b = float(input("Desconto % :")) 
e = a - (a * (b/100))
print(f" preço----------{a}$\nDesconto----------{(a*(b/100))}%\npreço final----------{e}$")