
salario = float(input("Digite o salário do colaborador: R$ "))

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

inflacao = 3.8
aumento_real = aumento - (aumento * (inflacao / 100))

print("\nSalário antes do reajuste: R$ {:.2f}".format(salario))
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Novo salário após o aumento: R$ {:.2f}".format(novo_salario))
print("Valor do aumento real, descontado a inflação: R$ {:.2f}".format(aumento_real))
