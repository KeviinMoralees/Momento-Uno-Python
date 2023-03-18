import random

cuentas = {}

for i in range(1, 11):
    num_cuenta =  (f"64703225498{i}") 
    saldo = float(input(f"Digite el saldo de la cuenta {num_cuenta}: "))
    cuentas[f"Cuenta {num_cuenta}"] = saldo

cuentas_ordenadas = dict(sorted(cuentas.items(), key=lambda x: x[1], reverse=True))

print("Cuentas y sus saldos ordenados de mayor a menor:")
for cuenta, saldo in cuentas_ordenadas.items():
    print(f"{cuenta}: ${saldo}")
